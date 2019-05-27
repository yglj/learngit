from django.db import models

# Create your models here.


class Book(models.Model):
     bname = models.CharField(max_length=20)
     pub_date = models.DateField()

     def __str__(self):
          return self.bname
     
     
class Role(models.Model):
    rname = models.CharField(max_length=20)
    render = models.BooleanField(default=False)
    comment = models.CharField(max_length=128)
    rbook = models.ForeignKey('book')

    def __str__(self):
        return self.rname
