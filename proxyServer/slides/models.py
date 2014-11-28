from django.db import models

# Create your models here.
class cacheData(models.Model):
	"""stores cacheData"""
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	present_slide = models.IntegerField()
	def __unicode__(self):
		return self.ip_address
		