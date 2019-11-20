function Fav() {

}

Fav.prototype.ListenRemoveFavEvent =function(){
  var removeBtn = $('.remove');
  removeBtn.click(function (event) {
      event.preventDefault();
      var self = $(this);
      var td = self.parent();
      xfzajax.post({
          'url':'/operation/delfav/',
          'data':{
              'id':td.attr('data-id')
          },
          'success':function (result) {
              if (result['code'] === 200){
                  window.location.reload()
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



Fav.prototype.run = function () {
    this.ListenRemoveFavEvent();
};

$(function () {
    var fav = new Fav();
    fav.run();
    span_text_change = function () {
        var goods_nums = $('input[name="number"]').val();
        var priceTag = $('.goods-price');
        var spanTag = $('.per-goods-amount');
        var goods_amount = goods_nums * priceTag.attr('data-price');
        spanTag.text('￥' + goods_amount.toFixed(1));
    }
})