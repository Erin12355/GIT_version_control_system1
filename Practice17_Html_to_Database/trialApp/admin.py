from django.contrib import admin
from trialApp.models import Trial 

# Register your models here.

class TrialAdmin(admin.ModelAdmin):
    list=['fname','lname','sdate','edate','course']

admin.site.register(Trial,TrialAdmin)