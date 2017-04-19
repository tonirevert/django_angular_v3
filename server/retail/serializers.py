from rest_framework import serializers
from retail.models import Chain, Store, Employee


class ChainSerializer(serializers.ModelSerializer):
    """ Serializer per representar el model Chain """
    class Meta:
        model = Chain
        fields = ("name", "description", "slogan", "founded_date", "website")


class StoreSerializer(serializers.ModelSerializer):
    """ Serializer per representar el model Store """
    class Meta:
        model = Store
        fields = (
            "chain", "number", "address", "opening_date",
            "business_hours_start", "business_hours_end"
        )


class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer per representar el model Employee """
    class Meta:
        model = Employee
        fields = ("store", "number", "first_name", "last_name", "hired_date")