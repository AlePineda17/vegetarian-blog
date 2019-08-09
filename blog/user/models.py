from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    picture = models.ImageField(upload_to='images')
    about = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
