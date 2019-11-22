from django.contrib import admin

# Register your models here.

from .models import BrandingSettings, SoloBirdPage, SearchBirdPage, FormBirdPage, SoloBirdPageTag, FormField


admin.site.register(BrandingSettings)

admin.site.register(SoloBirdPage)

admin.site.register(SearchBirdPage)

admin.site.register(FormBirdPage)

admin.site.register(SoloBirdPageTag)

admin.site.register(FormField)
