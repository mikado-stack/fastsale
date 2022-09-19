from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views 
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)



app_name = 'core'

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
     
 	path('logout/', LogoutView.as_view(next_page='collections'), name='logout'),
    
    path('', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    
    path('search', views.search, name="search"),
    path('comment', views.comment, name="comment"),
    path('contact', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    
    
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    
    path('payment/<payment_option>/', PaymentView.as_view(), name='bankTransfer'),
    
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
