# from django.db import models
# from django.contrib import admin
# from .forms import *
#
#
# class notificationAdmin(admin.ModelAdmin):
#     subject = models.CharField(max_length=100)
#     message = models.TextField()
#
# def change_view(self, request, object_id, extra_context=None):
#         if not request.user.is_superuser:
#             extra_context = extra_context or {}
#             extra_context['readonly'] = True
#
#         return super(notificationAdmin, self).change_view(request, object_id, extra_context=extra_context)
#
# class notification(models.Model):
#     subject = models.CharField(max_length=100)
#     message = models.TextField()
