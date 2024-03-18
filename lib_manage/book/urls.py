from django.urls import path
from . import views

urlpatterns = [
    path("viewbook/", views.view_book_all, name="viewbook"),
    path("viewbook/<id>/", views.view_book, name="detailviewbook"),
    path("addbook/", views.add_book_view, name="addbook"),
    path("viewbook/<id>/deletebook/", views.delete_book, name="deletebook"),
    path("viewbook/<id>/updatebook/", views.update_book, name="updatebook"),
]