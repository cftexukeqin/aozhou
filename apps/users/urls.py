from django.urls import path
from . import views
app_name = 'users'


urlpatterns = [
    path("login/",views.my_login,name='login'),
    path("regist/",views.regist,name='regist'),
    path("logout/",views.my_logout,name='logout'),
]