from django.urls import path
from . import views

urlpatterns=[
    path('dish_manage/',views.dish_manage,name="dish_manage"),
    path('new_dish/',views.new_dish,name="new_dish"),
    path('edit_dish/<int:id>',views.edit_dish,name="edit_dish"),
    path('delete_dish/<int:id>',views.delete_dish,name="delete_dish"),
    path('category_manage/',views.category_manage,name="category_manage"),
    path('add_category/',views.new_category,name="new_category"),
    path('edit_category/<int:id>',views.edit_category,name="edit_category"),
    path('delete_category/<int:id>',views.delete_category,name="delete_category")
]