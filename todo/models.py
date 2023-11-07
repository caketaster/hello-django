from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) 
    # ^ name cannot be blank, so blank=False
    done = models.BooleanField(null=False, blank=False, default=False)

    # to change the default name...
    def __str__(self):
        return self.name

