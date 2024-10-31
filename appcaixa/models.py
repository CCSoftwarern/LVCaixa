import datetime
from django.db import models
from uuid import uuid4

# Create your models here

class empresa(models.Model):
    id_empresa = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    nome_fantasia = models.CharField(max_length=150, null=False)
    razao_social = models.CharField(max_length=150, null=False)
    cnpj = models.CharField(max_length=22,null=False)
    status = models.CharField(max_length=30,null=True) 
    cnae_principal_descricao = models.CharField(max_length=150,null=True, blank=True)
    cnae_principal_codigo = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=11,null=True, blank=True)
    data_abertura = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)


class tipo_movimento(models.Model):
    id_tp_movimento = models.AutoField(primary_key=True, editable=False)
    nm_tp_movimento = models.CharField(max_length=100, null=False, blank=False)

class clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True, editable=False)
    nm_cliente = models.CharField(max_length=100, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=22,null=False, unique=True) 
    cep = models.CharField(max_length=11,null=True, blank=True)
    data_abertura = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    tipo_cliente = models.IntegerField(default=0, null=False, blank=False) # 0= cliente comum, 1=instrutor
    id_usuario = models.IntegerField(default=0, null=True)
    nm_usuario = models.CharField(max_length=150, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)

class movimento(models.Model):
    id_movimento = models.AutoField(primary_key=True, editable=False)
    dt_lancamento = models.DateField(auto_now_add=True)
    horario = models.TimeField(auto_now_add=True)
    dt_caixa = models.DateField(auto_now_add=True)
    nm_tp_movimento = models.CharField(max_length=100, null=False, blank=False)
    id_cliente = models.IntegerField(default=0)
    nm_cliente = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=300, null=False, blank=False)
    status = models.IntegerField(default=0)
    vr_movimento = models.DecimalField(max_digits=15, decimal_places=2)
    id_usuario = models.IntegerField(default=0, null=True)
    nm_usuario = models.CharField(max_length=150, null=True)
    vr_entrada = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vr_parcelado = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cod_forma_entrada= models.IntegerField(default=0, null=True)
    cod_forma_parcelado= models.IntegerField(default=0, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)
    #incluido apartir daqui
    ACC = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_A = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_B = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_C = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_D = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status =  models.IntegerField(default=0, null= True) # 0=aberto, 1=liquidado, 2=Cancelado
    forma_pgto = models.CharField(max_length=30, null=True, blank=True)
    data_pgto = models.DateField(null=True)
    idusuario_folhapgto = models.IntegerField(default=0, null=True)
    nm_usuario_folhapgto = models.CharField(max_length=150, null=True)
    dt_atualizacao_folhapgto = models.DateTimeField(auto_now=True)
    idinstrutor_catA = models.IntegerField(default=0) #instrutor
    nm_instrutor_catA = models.CharField(max_length=150, null=True, default=0)
    idinstrutor_catB = models.IntegerField(default=0)
    nm_instrutor_catB = models.CharField(max_length=150, null=True, default=0)
    idmovimento = models.IntegerField(default=0, null=False)
    idforma_pgtos = models.IntegerField(default=0,null=False)# forma de pgto
    codigo_pe = models.CharField(max_length=50,default=0, null=True)
    nm_categoria = models.CharField(default=0, max_length=50, null=False)
    valor_b = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status_pgto_a =  models.IntegerField(default=0, null= True) # 0=aberto, 1=liquidado, 2=Cancelado
    status_pgto_b=  models.IntegerField(default=0, null= True) # 0=aberto, 1=liquidado, 2=Cancelado
    id_habilitacoes = models.IntegerField(default=0, null=False, blank=False)
    dt_pgto = models.DateField(auto_now_add=True, null=True)
    hora_pgto = models.TimeField(auto_now_add=True, null=True)
    tem_na_folha = models.BooleanField(default=False)



class folhapgto(models.Model):
    id_folha = models.AutoField(primary_key=True, editable=False)
    dt_lancamento = models.DateField(auto_now_add=True)
    hora_lancamento = models.TimeField(auto_now_add=True)
    id_cliente = models.IntegerField(default=0)
    nm_cliente = models.CharField(max_length=100, null=True, blank=True)
    ACC = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_A = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_B = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_C = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    Categoria_D = models.IntegerField(default=0, null= True) # 0=não pretedido, 1=falta pgto, 2= pronto para pgto, 3=pago
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    status =  models.IntegerField(default=0, null= True) # 0=aberto, 1=liquidado, 2=Cancelado
    forma_pgto = models.CharField(max_length=30, null=True, blank=True)
    data_pgto = models.DateField(null=True)
    id_usuario = models.IntegerField(default=0, null=True)
    nm_usuario = models.CharField(max_length=150, null=True)
    valor_b = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    dt_atualizacao = models.DateTimeField(auto_now=True)
    id_instrutor = models.IntegerField(default=0)
    nm_instrutor = models.CharField(max_length=150, null=True)
    id_movimento = models.IntegerField(default=0, null=False)
    id_forma_pgtos = models.IntegerField(default=0,null=False)
    codigo_pe = models.CharField(max_length=50,default=0, null=True)
    nm_categoria = models.CharField(default=0, max_length=50, null=False)




class forma_pgtos(models.Model):
    id_forma_pgtos = models.AutoField(primary_key=True, editable=False)
    descricao = models.CharField(max_length=150, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)


class bancos(models.Model):
    id_banco = models.AutoField(primary_key=True, editable=False)
    descricao = models.CharField(max_length=150, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)

class habilitacoes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_cliente = models.IntegerField(default=0, null=False, blank=False)
    cod_pe = models.CharField(max_length=50,default=0, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    dt_cadastro = models.DateField(auto_now_add=True)
    hora_cadastro = models.TimeField(auto_now_add=True)
    status = models.IntegerField(default=0) #0 = aberto, 1= Concluido, 2 = cancelado
    id_usuario = models.IntegerField(default=0)










