from django.db import models

# Create your models here.

class Page(models.Model):
    title= models.CharField(verbose_name='Titulo', max_length=100)
    content= models.TextField(verbose_name='contenido', blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated= models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']

    def __str__(self):
        return self.title
