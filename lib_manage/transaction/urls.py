from django.urls import path
from . import views

urlpatterns = [
    path("viewtransactions/", views.view_transaction, name="viewtransactions"),
    path("downloadtransactions/", views.download_transaction, name="downloadtransactions"),
    path("issuebook/<id>", views.issue_book, name="issuebook"),
    path("returnbook/<id>", views.return_book, name="returnbook"),
]
