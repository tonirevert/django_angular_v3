from rest_framework import viewsets
from retail.models import Chain, Store, Employee
from retail.serializers import ChainSerializer, StoreSerializer,EmployeeSerializer


class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet per visualitzar i editar objectes Chain """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet per visualitzar i editar objectes Store """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet per visualitzar i editar objectes Employee """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer