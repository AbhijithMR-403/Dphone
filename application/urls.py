
from django.urls import path
from application import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reg/',views.register,name='register'),
    path('logout/',views.signout,name='signup'),
    path('home/',views.home,name='home'),
    path('feature/',views.feature,name='feature'),
    path('price/',views.price,name='price'),
    path('adminlogin/',views.adminPage,name='adminPage'),
    path('adminhome/',views.adminHome,name='adminhome'),

]