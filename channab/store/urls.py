from django.urls import path

from . import views

app_name = 'store'


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    # path('<int:product_id>/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('order_complete/', views.order_complete, name='order_complete'),
]