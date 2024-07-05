from warnings import filters
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from appcaixa.api import serializers
from appcaixa import models
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.empresa.objects.all()


class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializer
    queryset = models.clientes.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id_cliente','nm_cliente','cpf_cnpj','telefone','email']
    search_fields = ['id_cliente','nm_cliente','cpf_cnpj','telefone','email']

    

class tp_movimentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.tipo_movimentoSerializer
    queryset = models.tipo_movimento.objects.all()


class formas_pgtosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.formas_pgtoSerializer
    queryset = models.forma_pgtos.objects.all()

class bancosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.bancos_Serializer
    queryset = models.bancos.objects.all()



# filtros de pesquisa de movimento
class MetricFilter(filters.FilterSet):
    dt_lancamento= filters.DateFromToRangeFilter()
    search_fields =['id_movimento','dt_lancamento', 'dt_caixa','id_cliente','nm_cliente','descricao','nm_tp_movimento','status']

    class Meta:
        model = models.movimento
        fields =['id_movimento','dt_lancamento', 'dt_caixa','id_cliente','nm_cliente','descricao','nm_tp_movimento','status']


class MovimentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovimentoSerializer
    queryset = models.movimento.objects.all()
   # authentication_classes=[TokenAuthentication]
   # permission_classes=[IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricFilter


# filtros folha pgto
class MetricFilterFolha(filters.FilterSet):
    dt_lancamento = filters.DateFromToRangeFilter()
    search_fields =['id_folha','id_cliente', 'nm_cliente','status','forma_pgto','dt_lancamento']

    class Meta:
        model = models.folhapgto
        fields =['id_folha','id_cliente', 'nm_cliente','status','forma_pgto','dt_lancamento']


class FolhaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.folhapgtoSerializer
    queryset = models.folhapgto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricFilterFolha



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','is_staff']



