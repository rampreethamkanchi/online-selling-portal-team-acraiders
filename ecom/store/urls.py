from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
    path('search/',views.search,name='search'),
    path('sell/',views.sell,name='sell'),
    path('buy/',views.buy,name='buy'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('product_upload/<int:pk>',views.product_upload,name='product_upload'),
    path('orders/',views.orders,name='orders'),
    path('order_expanded/<int:pk>',views.order_expanded,name='order_expanded'),
    path('my_requests/',views.my_requests,name='my_requests'),
    path('success_requests_expanded/<int:pk>',views.success_requests_expanded,name='success_requests_expanded'),
    path('user_requests/',views.user_requests,name='user_requests'),
    path('seller_accepted_expanded/<int:pk>',views.seller_accepted_expanded,name='seller_accepted_expanded'),
    path('deliveries/',views.deliveries,name='deliveries'),
    path('deliveries_expanded/<int:pk>',views.deliveries_expanded,name='deliveries_expanded'),
    path('products/',views.products,name='products'),
    path('buySuccess/',views.buySuccess,name='buySuccess'),
    path('buyFailure/',views.buyFailure,name='buyFailure'),
    path('request/',views.request,name='request'),
    path('accept_request/',views.accept_request, name='accept_request'),
    path('reject_request/', views.reject_request, name='reject_request'),
    path('change_password/',views.change_password,name='change_password'),
    path('issue/',views.issue,name='issue'),
    path('add_chat_buyer/',views.add_chat_buyer,name='add_chat_buyer'),
    path('add_chat_seller/',views.add_chat_seller,name='add_chat_seller'),
    # path('accept_request/',views.accept_request, name='accept_request'),
    # path('reject_request/', views.reject_request, name='reject_request'),
    path('negotiate_expanded/<int:pk>',views.negotiate_expanded,name='negotiate_expanded'),
] 