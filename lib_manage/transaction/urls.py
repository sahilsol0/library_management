from django.urls import path
from . import views

urlpatterns = [
    path("viewtransactions/", views.view_transaction, name="viewtransactions"),
    path("issuebook/", views.issue_book, name="issuebook"),
    path("returnbook/", views.return_book, name="returnbook"),
]
