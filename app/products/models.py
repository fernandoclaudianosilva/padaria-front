from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    is_available = models.BooleanField(default=True, verbose_name="Disponível")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name