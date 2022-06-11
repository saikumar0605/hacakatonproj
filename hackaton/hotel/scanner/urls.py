
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('menupage/', views.menupage, name='menupage'),
    path('tableselect/', views.tableselect, name='tableselect'),
    path('login/tableselect', views.tableselect, name='tableselect'),
    path('login/index', views.index, name='index'),
    path('login/signup', views.signup, name='signup'),
    path('login/menupage', views.menupage, name='menupage'),
    path('signup/index', views.index, name='index'),
    path('signup/login', views.login, name='login'),
    path('signup/menupage', views.menupage, name='menupage'),
    path('signup/signup', views.signup, name='signup'),
    path('login/signup/index', views.index, name='index'),
    path('login/login', views.login, name='login'),
    path('menupage/login', views.login, name='login'),
    path('menupage/index', views.index, name='index'),
    path('menupage/signup', views.signup, name='signup'),
    path('menupage/menupage', views.menupage, name='menupage'),
    path('qrcode/', views.qrcode, name='qrcode'),
    path('login/qrcode', views.qrcode, name='qrcode'),
    path('menupage/pay', views.pay, name='pay'),
    path('pay/index', views.index, name='index'),
    path('menupage/tableselect', views.tableselect, name='tableselect'),
    path('sucess/', views.sucess, name='success'),
    path('menupage/sucess', views.sucess, name='success'),
    path('login/pay', views.pay, name='pay'),
    path('login/sucess', views.sucess, name='success'),


]
