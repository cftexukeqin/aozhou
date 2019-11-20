function Operation() {
    var self = this;

}

Operation.prototype.ListenUserFavClick = function(){
    var userfavBtn = $('#user-fav');
    // var goods_id = $('#user-fav').data('goods');
    userfavBtn.click(function (event) {
        event.preventDefault();
        var goods_id = userfavBtn.attr('data-goods-id');
        xfzajax.get({
            'url':'/operation/userfav/',
            "data":{
                'goods_id':goods_id
            },
            'success':function (result) {
                if (result['code']=== 200){
                    xfzalert.alertSuccessToast("收藏成功！")
                } else if (result['code'] === 401){
                    window.location.href = "/user/login/"+"?next=goods/"+goods_id
                }else {
                    xfzalert.alertInfoToast("您已收藏该商品！")
                }
            },
            'fail':function (err) {
                console.log(err)
            }
        })
    })

};

Operation.prototype.run = function () {
    this.ListenUserFavClick();
};

$(function () {
  var operation = new Operation();
  operation.run()
});