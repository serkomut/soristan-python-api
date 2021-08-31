from django.db import models

class User(models.Model):
    name=models.CharField(max_length=60)
    surname=models.CharField(max_length=60)
    username=models.CharField(100)
    email=models.CharField(100)
    password=models.CharField(512)

    def __str___(self):
        return '%s %s' %(self.name, self.surname)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'