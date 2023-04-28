from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('delivery.urls')),
    path('',include('Dishes.urls')),
    path('',include('users.urls')),
    path('home_page',views.home_page,name='home_page')
]
