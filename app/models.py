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

class Doctor(models.Model):
	dUid = models.IntegerField(primary_key=True)
	dName = models.CharField(max_length=20, help_text= "name")
	dPractice = models.CharField(max_length=20, help_text="practice")

	# def get_absolute_url(self):
	# 	"""
     #    Returns the url to access a particular instance of the model.
     #    """
	# 	return reverse('model-detail-view', args=[str(self.id)])