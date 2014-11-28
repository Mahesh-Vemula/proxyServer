from django.contrib import admin
from .models import cacheData

# Register your models here.
class cacheDataAdmin(admin.ModelAdmin):
	"""cache in admin page"""
	class meta:
		model = cacheData
	list_display = ('ip_address','present_slide','updated')
	search_fields = ['ip_address']
		


admin.site.register(cacheData,cacheDataAdmin)