from django.db import models
class Account(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    
    @classmethod
    def getall(cls):
      
        return [(acc.id,acc.name) for acc in cls.objects.all()]
    def __str__(self):
        return self.name