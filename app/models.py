from django.db import models

# Create your models here.



class user(models.Model):

    user = models.CharField(max_length=100)
    age = models.IntegerField()



    def __str__(self):
        return self.user



 
