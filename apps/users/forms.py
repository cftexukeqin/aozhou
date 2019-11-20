from django import forms
from apps.forms import FormMixin
# from utils import dxcache
from django.core import validators
from django.contrib.auth import get_user_model
import hashlib
User = get_user_model()

class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,error_messages={'max_length':'请输入11位的手机号','min_length':'请输入11位的手机号'})
    pwd = forms.CharField(max_length=20,min_length=6,error_messages={'max_length':'密码不能超过20个字符','min_length':'密码不得少于6个字符'})
    next = forms.CharField(max_length=100,required=False)
    # remember = forms.IntegerField(required=False)

class SignupForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,min_length=11,validators=[validators.RegexValidator(r'1[3578]\d{9}')],error_messages={'max_length': '请输入11位的手机号', 'min_length': '请输入11位的手机号'})
    pwd1 = forms.CharField(max_length=20, min_length=6,error_messages={'max_length': '密码不能超过20个字符', 'min_length': '密码不得少于6个字符'})
    pwd2 = forms.CharField(max_length=20, min_length=6,error_messages={'max_length': '密码不能超过20个字符', 'min_length': '密码不得少于6个字符'})
    # sms_captcha = forms.CharField(max_length=6,min_length=6)
    # img_captcha = forms.CharField(max_length=4,min_length=4)
    # username = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        telephone = cleaned_data.get('telephone')
        exists = User.objects.filter(mobile=telephone).exists()
        if exists:
            raise forms.ValidationError('此手机号已被注册')
        password1 = cleaned_data.get('pwd1')
        password2 = cleaned_data.get('pwd2')
        if password1 != password2:
            raise forms.ValidationError('两次输入的密码不一致')
        #
        # sms_captcha = cleaned_data.get('sms_captcha')
        # sms_captcha_mem = dxcache.get(telephone)
        # if not sms_captcha_mem or sms_captcha != sms_captcha_mem:
        #     raise forms.ValidationError('短信验证码错误')
        #
        # img_captcha = cleaned_data.get('img_captcha')
        # img_captcha_mem = dxcache.get(img_captcha)
        # if not img_captcha_mem or img_captcha!= img_captcha_mem:
        #     raise forms.ValidationError('图形验证码错误')
        return cleaned_data