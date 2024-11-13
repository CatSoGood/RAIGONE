from django.db import models

# Create your models here.
class orders(models.Model) :
    site = models.CharField(max_length=10)
    rule = models.CharField(max_length=60)
    name = models.CharField(max_length=255, default="Default Name")
    user = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.rule +"__"+ self.name