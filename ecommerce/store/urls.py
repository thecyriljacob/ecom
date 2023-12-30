from django.urls import path
from . import views

urlpatterns = [
    # empty string path works as the base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")

]
