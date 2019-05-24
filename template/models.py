from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField("Nome", max_length=255)
    month = models.CharField("Mês", max_length=255)
    day = models.CharField("Dia", max_length=255)
    link = models.CharField("Link", max_length=255)
    code = models.CharField("Código", max_length=255)
    short_description = models.TextField("Descrição Curta", null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    image = models.ImageField("Imagem", upload_to='eventimage/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name