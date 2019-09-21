
# Birdapp 657 #

A small Django Wagtail app

## Installation ###
  
### Pip requirements ###

> pip install wagtail

> pip install wagtailmedia

### Django settings ###

To your settings file,

add to the INSTALLED_APPS

``` Python
    # extra
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',

    # custom
    'birdapp657',
    # birdapp657 media file block
    'wagtailmedia',
    # birdapp657 default search backend
    'wagtail.contrib.postgres_search',

```

add to the  MIDDLEWARE settings

``` python
    'wagtail.core.middleware.SiteMiddleware',  # wagtail
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',  # wagtail
```

add the search backend settings

``` python
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
    },
}
```

set the admin title

``` python
WAGTAIL_SITE_NAME = 'Birdapp657'
```

### Database configuration ###

> python manage.py migrate

### Search Index setup ###
> python manage.py update_index

### Django url ###

To the django projects' url.py add

``` python
from django.urls import path, re_path
from django.conf.urls import include

# Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from wagtail.contrib.sitemaps.sitemap_generator import Sitemap
from wagtail.contrib.sitemaps.views import sitemap
```
and
``` python
SITEMAPS = {
    'wagtail': Sitemap,
}
```
and
``` python
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}),
    #  Wagtail
    re_path(r'^birdapp/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
  ]
```

### Collectstatic ###

> python manage.py collectstatic

### [Management commands](https://docs.wagtail.io/en/stable/reference/management_commands.html) ###

This commands can be good to have in a cron script to run once every hour.

> python manage.py publish_scheduled_pages

> python manage.py search_garbage_collect

## For development ##

> pip install pylint

To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To the Django project url.py add

``` python
from django.conf.urls.static import static
```

and at the bottom of the file add

``` python

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
