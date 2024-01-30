from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(verbose_name='Заверешено', default=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'ToDo list'
        verbose_name_plural = 'ToDo lists'