from django.db import models

# Create your models here.

choices = (
    ('online','online'),
    ('cod','cod'),
)

class Record(models.Model):
    email           = models.EmailField(null=True)
    name            = models.CharField(max_length=70)
    track           = models.CharField(max_length=70)
    book            = models.CharField(max_length=70)
    pincode         = models.IntegerField()
    village         = models.CharField(max_length=70)
    date            = models.DateField(null=True)
    payment         = models.CharField(choices=choices,max_length=70)
    total           = models.IntegerField()
    phone           = models.IntegerField()