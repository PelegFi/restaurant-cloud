from django.urls import path
from . import views

urlpatterns=[
    path('cart/',views.cart,name="cart"),
    path('active_orders/',views.active_orders,name="active_orders"),
    path('order_by_category/<int:category_id>/<int:cart_id>',views.order_by_category,name="order_by_category"),
    path('order/<int:cart_id>',views.order,name="order"),
    path('delivery/<int:cart_id>',views.delivery,name="delivery"),
    path('order_history/',views.order_history,name="order_history"),
    path('order_management/',views.order_management,name="order_management")
]