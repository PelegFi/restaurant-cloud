from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.signup,name="signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_screen/',views.user_screen,name="user_screen"),
    path('edit_managers/',views.edit_managers,name="edit_managers"),
    path('edit_user/',views.edit_user,name="edit_user"),
    path('logout_user/',views.logout_user,name="logout_user")
]