from django.urls import path

from banks_api.views import BankAPIViewSet, BranchAPIViewSet

app_name = "banks_api"

urlpatterns = [
    path(
        "bank/",
        BankAPIViewSet.as_view({"get": "list", "post": "create"}),
        name="bank-list-create"
    ),
    path(
        "bank/<id>/",
        BankAPIViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="bank-retrieve-delete"
    ),
    path(
        "bank/<bank_id>/branch/",
        BranchAPIViewSet.as_view({"get": "list", "post": "create"}),
        name="branch-list-create"
    ),
    path(
        "bank/<bank_id>/branch/<ifsc>/",
        BranchAPIViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="branch-retrieve-delete"
    ),
]
