from django.db import models
import uuid

# Create your models here.

class Proprietario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    telefone = models.IntegerField()
    cpf = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Barbearia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=40)
    cnpj = models.CharField(max_length=14)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Despesa(models.Model):
    descricao_despesa = models.CharField(max_length=30)
    valor_despesa = models.DecimalField(max_digits=5, decimal_places=2)
    data_despesa = models.DateField()
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao_despesa  
    
class Receita(models.Model):
    descricao_receita = models.CharField(max_length=30)
    valor_receita = models.DecimalField(max_digits=6, decimal_places=2)
    data_receita = models.DateField()
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao_receita

class Funcionario(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.IntegerField()
    email = models.CharField(max_length=120)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

class Contrato(models.Model):
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    data_contrato = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contrato {self.id} - {self.valor_total}"

class Servicos(models.Model):
    descricao_servico = models.CharField(max_length=30)
    valor_servico = models.DecimalField(max_digits=6, decimal_places=2)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao_servico

class BarbeariaCliente(models.Model):
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.barbearia} - {self.cliente}"

class ServicosContrato(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servico} - {self.contrato}" 