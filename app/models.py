from django.db import models

# Create your models here.

class Hospital(models.Model):
	hUid = models.IntegerField()
	hName = models.IntegerField()
	hCapacity = models.IntegerField()
	hStreetAddress = models.IntegerField()
	hCapacity = models.IntegerField()
	hZipcode = models.IntegerField()
	hStateCode = models.IntegerField()
