from django.db import models
from Account.models import Account
from django.shortcuts import get_object_or_404

class Trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    id_obj = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True) 
    image = models.ImageField(upload_to='.images/', null=True, blank=True)


    @classmethod
    def deleteEachTrainee(cls, id):
        try:
            trainee = cls.objects.get(pk=id)

            trainee.delete()
            return True
        except cls.DoesNotExist:
            return False
        
    @classmethod
    def get_trainee_details(cls, id):
        
        return get_object_or_404(cls, pk=id)
    