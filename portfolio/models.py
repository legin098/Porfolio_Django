from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200, verbose_name='Título')
  description = models.TextField(verbose_name='Descripción')
  image = models.ImageField(verbose_name='Imagen', upload_to='projects')
  link = models.URLField(verbose_name='Enlace', null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Proyecto'
    verbose_name_plural = 'Proyectos'
    ordering = ['-created'] # -created organiza del mas nuevo al mas antiguo

  def __str__(self):
    return self.title # muestra el titulo del proyecto en el administrador