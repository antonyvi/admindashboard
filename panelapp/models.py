from django.db import models



class ClientsContactInformation(models.Model):

    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    are_details_as_per_id=models.CharField(max_length=100)


class CareGiversContactInformation(models.Model):
      

    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    Realtionshipwithclient=models.CharField(max_length=100)
    are_details_as_per_id=models.CharField(max_length=100)