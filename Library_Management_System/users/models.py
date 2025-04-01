from django.db import models

# Create your models here.
class User(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    username=models.IntegerField(max_length=15, unique=True)
    Email=models.EmailField(unique=True)
    Date_of_membership=models.DateTimeField.auto_now
    Active_Status=models.BooleanField

    def __str__(self):
        return f"{self.Users}"
    class Meta:
        ordering = ['Date_of_membership' ]
