from django.urls import path

from . import views

urlpatterns = [
    #Leave as empty string for base url
    path('', views.home, name="Home"),
	path('sign-up/', views.sign_up, name="Sign Up"),
    path('coffee-bags/', views.products, name="Coffee Bags"),
    path('coffee-bags/checkout/<str:id>/', views.checkout, name='checkout'),
    path('order/', views.addorder, name='order'),
    #Product manager views
    path('productmanager/',views.productmanager, name="Manage_Products"),
    path('productmanager/insertproduct/',views.addproduct, name="Insert Product"),
    path('productmanager/delete/<str:id>', views.delete, name='delete'),
    path('productmanager/update/<str:id>', views.update, name='update'),
    path('productmanager/update/updateproduct/<str:id>', views.productupdate, name='updaterecord'),

]