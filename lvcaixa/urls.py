"""
URL configuration for lvcaixa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from appcaixa.api import viewsets as appcaixaviewsets
from rest_framework.authtoken.views import obtain_auth_token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'empresa', appcaixaviewsets.EmpresaViewSet)
router.register(r'tipo_movimento', appcaixaviewsets.tp_movimentoViewSet)
router.register(r'clientes', appcaixaviewsets.ClientesViewSet)
router.register(r'movimento', appcaixaviewsets.MovimentoViewSet)
router.register(r'folha', appcaixaviewsets.FolhaViewSet)
router.register(r'formas_pgtos', appcaixaviewsets.formas_pgtosViewSet)
router.register(r'bancos', appcaixaviewsets.bancosViewSet)
router.register(r'habilitacoes', appcaixaviewsets.HabilitacoesViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('rest_authtoken.urls')),
]
