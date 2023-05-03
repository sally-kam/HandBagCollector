from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Handbag(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    

class Worn(models.Model):
    date = models.DateField()
    occasion = models.CharField()
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
