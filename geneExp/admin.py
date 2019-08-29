from django.contrib import admin
from geneExp.models import SampleInf


# Register your models here.
class SampleAdmin(admin.ModelAdmin):
    list_display = ('sample_id', 'tissue')

    search_fields = ['sample_id', 'tissue']


admin.site.register(SampleInf, SampleAdmin)
