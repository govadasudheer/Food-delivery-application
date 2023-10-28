from django.urls import path
from . import views

urlpatterns=[
    path('forder/', views.homepage, name='homeurl'),
    path('login/', views.loginRecord, name='loginurl'),
    path('signup/', views.signupRecord, name='signupurl'),
    path('logout/',views.userlogout, name='logouturl'),
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('mycart/',views.mycart, name='mycarturl'),
    path('add_to_order/<int:item_id>/', views.add_to_order, name='add_to_order'),
    path('myorder/',views.myorders, name='myorderurl'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]