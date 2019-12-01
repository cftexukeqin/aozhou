function Index() {
    var self = this;
    self.page = 2
}

Index.prototype.ListenCategory = function(){
    var productItems = $(".product-item");
    $.each(productItems,function (index,element) {
        var catTag = element.dataset.category;
        if (catTag=== "1"){
            element.className += " special"
        }else if (catTag === "2"){
            element.className += ' cosmetic'
        }else if (catTag === "3"){
            element.className += " milk"
        }else if (catTag === "4"){
            element.className += " love"
        }else if (catTag === "5"){
            element.className += " normal"
        }else if (catTag === "6"){
            element.className += " cat"
        }else if (catTag === "7"){
            element.className += " care"
        }
    })
};
Index.prototype.ListenLoadMoreBtnEvent = function(){
    var self = this;
    var loadBtn = $('#load-more-btn');
    //点击按钮获取数据，前端显示出来
    loadBtn.click(function (event) {
        event.preventDefault();
        xfzajax.get({
            'url': '/goods_lists/',
            'data': {
                'p': self.page
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    var goodses = result['data'];
                    if(goodses.length>0){
                        var listGroup = $('.product-grid');
                        var html = template('goodslist', {'goodses': goodses});
                        listGroup.append(html);
                        self.page += 1;
                    }else{
                        loadBtn.hide();
                    }
                }
            }
        })
    })
};

Index.prototype.ListenUserFavClick = function(){
    var userfavBtn = $('.user-fav');
    // var goods_id = $('#user-fav').data('goods');
    userfavBtn.click(function (event) {
        var id = userfavBtn.attr('data-goods-id');
        xfzajax.get({
            'url':'/operation/userfav/',
            "data":{
                'goods_id':id
            },
            'success':function (result) {
                if (result['code']=== 200){
                    console.log(result)
                } else {
                    console.log(result['message'])
                }
            },
            'fail':function (err) {
                console.log(err)
            }
        })
    })

};

Index.prototype.run = function () {
    this.ListenCategory();
    this.ListenLoadMoreBtnEvent();
    this.ListenUserFavClick();
};

$(function () {
  var index = new Index();
  index.run()
});