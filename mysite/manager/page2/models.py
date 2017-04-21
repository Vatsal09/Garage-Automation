from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
	license_id = models.IntegerField
	name = models.CharField(max_length=200)
	
class Spot(models.Model):
	spot_id = models.IntegerField
	price = models.DecimalField(max_digits=6,decimal_places=2)
	
class Transaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	trans_id = models.IntegerField
	trans_date = models.DateTimeField('date of transaction')
	pm = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	
