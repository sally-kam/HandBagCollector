from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('items_detail', kwargs={'pk': self.id})

class Handbag(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    # Add the M:M relationship
    # related manager named toys
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name
    
      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    

class Worn(models.Model):
    date = models.DateField('Date used:')
    occasion = models.CharField(max_length=100)
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
     # Create a handbag_id FK
    handbag = models.ForeignKey(Handbag, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"Worn on {self.date} in the {self.get_time_display()} for {self.occasion}"
    
    class Meta:
        ordering = ['-date']