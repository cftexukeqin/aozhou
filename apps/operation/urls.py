from django.urls import path

from .views import userfav,fav_list,del_fav
app_name = 'operation'

urlpatterns =[
    path('userfav/',userfav,name='usefav'),
    path('favs/',fav_list,name='fav_list'),
    path('delfav/',del_fav,name='delfav'),
]