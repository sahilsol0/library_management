from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name = 'home'),
    path('about/',views.about_page, name = 'about'),
    path('', include('user_auth.urls')),
    path('dashboard/',views.dashboard_view, name = "dashboard"),
    path('', include('book.urls')),
    path('', include('transaction.urls')),
]