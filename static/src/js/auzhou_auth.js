function Auth() {

}
Auth.prototype.LoginClick = function(){
    var self = this;
    var loginBtn = $("#login");
    var telephoneInput = $("input[name='telephone']");
    var pwdInput = $('input[name="pwd"]');
    var next = window.location.search;
    console.log("&*******************");
    console.log(next);
    loginBtn.click(function () {
        telephone = telephoneInput.val();
        pwd = pwdInput.val();
        console.log("Login",telephone);
        console.log("pwd",pwd);
        xfzajax.post({
            'url':'/user/login/',
            'data':{
                'telephone':telephone,
                'pwd':pwd,
                'next':next
            },
            'success':function (result) {
                if(result['code'] === 200){
                    next_url = result['data']['next_url'];
                    if (next_url){
                        var pattern = RegExp('operation');
                        var fav_url = pattern.test(next_url);
                        console.log("&****************************");
                        console.log(fav_url);
                        if(fav_url){
                            window.location.href = "http://" + window.location.host + next_url;
                        }else {
                            window.location.href ='/'+ next_url
                        }

                    } else{
                        window.location.href = '/'
                    }
                }else {
                    console.log(result['message'])
                }
            },
            "fail":function (err) {
                console.log(err)
            }
        })
    })

};
Auth.prototype.ListenRegistClick = function(){
  var self = this;
  var registButton = $("#regist");
  var telephoneInput = $("input[name='telephone']");
  var pwd1Input = $('input[name="pwd1"]');
  var pwd2Input = $('input[name="pwd2"]');


  registButton.click(function () {
      telephone = telephoneInput.val();
      pwd1 = pwd1Input.val();
      pwd2 = pwd2Input.val();
      xfzajax.post({
          'url':'/user/regist/',
          'data':{
              'telephone':telephone,
              'pwd1':pwd1,
              'pwd2':pwd2
          },
          'success':function (result) {
              if(result['code']===200){
                  window.location.href ='/user/login/';
              }
          },
          "fail":function (err) {
              console.log(err)
          }
      })

  })
};


Auth.prototype.run = function () {
    this.ListenRegistClick();
    this.LoginClick();
};
$(function () {
    var auth = new Auth();
    auth.run()
});