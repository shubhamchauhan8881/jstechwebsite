from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserQuery)
admin.site.register(models.Blogs)
admin.site.register(models.Testimonial)
admin.site.register(models.Feedback)
admin.site.register(models.Team)
admin.site.register(models.Projects)
admin.site.register(models.TelegramClients)