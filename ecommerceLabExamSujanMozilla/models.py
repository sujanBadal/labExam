class labexam(models.Model): exam_date = models.DateTimeField() exam_name = models.CharField(max_length=300) exam_description = models.TextField(max_length=500) total_marks = models.FloatField() pass_marks = models.FloatField() exam_status = models.BooleanField() is_active = models.BooleanField()

INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'exam_module' ]

from django.contrib import admin from .models import labexam admin.site.register(labexam)