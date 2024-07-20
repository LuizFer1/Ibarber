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