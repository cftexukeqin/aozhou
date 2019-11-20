function Lists() {

}

Lists.prototype.ListenSearchBtn = function(){
    var searchBtn = $("#search-btn");
    var searchInput = $('input[name="search"]');
    searchBtn.click(function (event) {
        event.preventDefault();
        kw = searchInput.val();
        console.log("******************");
        console.log(kw);
        xfzajax.post({
            'url':'/search/',
            'data':{
                'kw':kw
            },
            'success':function (result) {
                console.log(result)
            }
        })
    })
};



Lists.prototype.run = function () {
    this.ListenSearchBtn();
};

$(function () {
   var lists = new Lists();
   lists.run()
});