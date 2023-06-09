from django.db import models
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(null=False, blank=False,
                   verbose_name=u'Fecha de creación',auto_now_add=True)
        
    def __str__(self):
        return "{} : {}".format(self.title, self.date)
