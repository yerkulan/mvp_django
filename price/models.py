from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_description

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    pc_title = models.CharField(max_length=200, verbose_name='Услуга')
    pc_old_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Старая цена')
    pc_new_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Новая цена')

    def __str__(self):
        return self.pc_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
