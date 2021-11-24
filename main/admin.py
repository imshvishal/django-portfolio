from django.contrib import admin
from .models import (
                    ContactFormData,
                    WebData,
                    SocialMedia,
                    Skill,
                    Config
                    )

# Register your models here.
admin.site.register(ContactFormData)
admin.site.register(WebData)
admin.site.register(Skill)
admin.site.register(SocialMedia)
admin.site.register(Config)