from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('shop/', views.AllProducts.as_view(), name='shop'),
    path('shop/<slug:slug>/', views.product_detail, name='product'),
    
    path('about/',views.about, name='about'),
    path('contact/',views.about, name='contact'),

]
