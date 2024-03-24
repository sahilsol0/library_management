from django.urls import path
from . import views

urlpatterns = [
    path("viewbook/", views.view_book_all, name="viewbook"),
    path("viewbook/<id>/", views.view_book, name="detailviewbook"),
    path("addbook/", views.add_book_view, name="addbook"),
    path("viewbook/<id>/deletebook/", views.delete_book, name="deletebook"),
    path("viewbook/<id>/updatebook/", views.update_book, name="updatebook"),
    path("viewauthor/", views.view_author_all, name="viewauthor"),
    path("viewauthor/<id>/deleteauthor/", views.delete_author, name="deleteauthor"),
    path("viewauthor/<id>/updateauthor/", views.update_author, name="updateauthor"),
    path("viewcategory/", views.view_category_all, name="viewcategory"),
    path("viewcategory/<id>/deletecategory/", views.delete_category, name="deletecategory"),
    path("viewcategory/<id>/updatecategory/", views.update_category, name="updatecategory"),
    path("viewpublisher/", views.view_publisher_all, name="viewpublisher"),
    path("viewpublisher/<id>/deletepublisher/", views.delete_publisher, name="deletepublisher"),
    path("viewpublisher/<id>/updatepublisher/", views.update_publisher, name="updatepublisher"),
    path("downloads/",views.downloads,name="downloads"),
]