from django.contrib import admin

# Register your models here.

from .models import BirdAppSettings, SoloBirdPage, SearchBirdPage, FormBirdPage, SoloBirdPageTag, FormField


admin.site.register(BirdAppSettings)

admin.site.register(SoloBirdPage)

admin.site.register(SearchBirdPage)

admin.site.register(FormBirdPage)

admin.site.register(SoloBirdPageTag)

admin.site.register(FormField)
