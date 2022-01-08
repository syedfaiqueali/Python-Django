from django.contrib import admin
from profiles_api import models


# Enable models for admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
