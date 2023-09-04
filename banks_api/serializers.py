from rest_framework import serializers
from banks_api.models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = (
            "id",
            "name",
        )


class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = Branch
        fields = (
            "id",
            "ifsc",
            "bank",
            "branch",
            "address",
            "city",
            "district",
            "state"
        )

        read_only_fields = ("id", "bank")

    def create(self, validated_data):
        return Branch.objects.create(**validated_data)

