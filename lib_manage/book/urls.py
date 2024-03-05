from django.urls import path
from . import views

urlpatterns = [
    path("viewbooks/", views.view_books, name="viewbooks"),
]