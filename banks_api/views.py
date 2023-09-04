from django.core.exceptions import ValidationError
from rest_framework import viewsets
from banks_api.serializers import BankSerializer, BranchSerializer
from banks_api.models import Bank, Branch


class BankAPIViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    authentication_classes = []
    serializer_class = BankSerializer
    permission_classes = []
    pagination_class = None

    def get_queryset(self):
        bank_list = Bank.objects.all()
        return bank_list


class BranchAPIViewSet(viewsets.ModelViewSet):
    lookup_field = "ifsc"
    authentication_classes = []
    serializer_class = BranchSerializer
    permission_classes = []
    pagination_class = None

    def get_queryset(self):
        branch_list = Branch.objects.filter(bank__id=self.kwargs.get("bank_id"))
        return branch_list

    def perform_create(self, serializer):
        try:
            bank = Bank.objects.get(id=self.kwargs.get("bank_id"))
        except Exception as e:
            raise ValidationError("bank does not exist")

        serializer.save(bank=bank)
