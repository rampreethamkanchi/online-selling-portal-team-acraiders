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
    path('product_upload/<int:pk>',views.product_upload,name='product_upload'),
    path('orders/',views.orders,name='orders'),
    path('deliveries/',views.deliveries,name='deliveries'),
    path('deliveries_expanded/<int:pk>',views.deliveries_expanded,name='deliveries_expanded'),
    path('products/',views.products,name='products'),
    path('buySuccess/',views.buySuccess,name='buySuccess'),
    path('buyFailure/',views.buyFailure,name='buyFailure'),
]
