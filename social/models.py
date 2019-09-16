from django.db import models

# Create your models here.
class link(models.Model):
    key=models.SlugField(verbose_name='nombre clave', max_length=100, unique=True)
    name= models.CharField(verbose_name='Red social', max_length=100)
    url= models.URLField(verbose_name='Enlace', max_length=200,blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated= models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name
