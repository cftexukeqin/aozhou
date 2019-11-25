function Fav() {

}

Fav.prototype.ListenRemoveFavEvent =function(){
  var removeBtn = $('.remove');
  removeBtn.click(function (event) {
      event.preventDefault();
      var self = $(this);
      var ptag = self.parent();
      xfzajax.post({
          'url':'/operation/delfav/',
          'data':{
              'id':ptag.attr('data-id')
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
});