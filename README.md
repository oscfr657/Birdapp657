
# Birdapp 657 #

A small Wagtail app

## Compatible ##

### Tested with ###

``` Python
Django == 3.1.6
Wagtail == 2.12
Wagtailmedia == 0.7.0
```

## Installation ###
  
### Pip requirements ###

> pip install -r requirements.txt

### Django settings ###

To your settings file,

add to the INSTALLED_APPS

``` Python

    'django.contrib.sites',  # extra
    'django.contrib.sitemaps',  # extra

    # wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',  # extra
    'wagtail.contrib.search_promotions',  # extra
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

add to the MIDDLEWARE settings

``` python
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',  # wagtail
```

add to the TEMPLATES settings

``` python
    TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors': [
                    'wagtail.contrib.settings.context_processors.settings',  # Extra
            },
        },
    ]
```

#### Optionaly set ####

the admin title

``` python
WAGTAIL_SITE_NAME = 'Birdapp657'
```

the password required template

``` python
PASSWORD_REQUIRED_TEMPLATE = 'birdapp657_password_required.html'
```

#### I recommend ####

the use of the postgres_search.backend, set the search backend settings

``` python
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
    },
}
```

and set the WAGTAILIMAGES_FORMAT_CONVERSIONS setting

``` python
WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    'bmp': 'webp',
    'jpeg': 'webp',
    'jpg': 'webp',
    'JPG': 'webp',
    'webp': 'webp',
    'png': 'webp',
}
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

from wagtail.contrib.sitemaps.views import sitemap
```

and

``` python
urlpatterns = [
    re_path('sitemap.xml', sitemap),
    #  Wagtail
    re_path(r'^birdapp/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
  ]
```

```python
handler403 = 'birdapp657.views.bird_page_403'
handler404 = 'birdapp657.views.bird_page_404'
handler500 = 'birdapp657.views.bird_page_500'
```

### Collectstatic ###

> python manage.py collectstatic

### [Management commands](https://docs.wagtail.io/en/stable/reference/management_commands.html) ###

Some commands is good to have in cron to run once every hour.

> crontab -e

> 0 * * * * /path/to/env/bin/python /path/to/project/manage.py publish_scheduled_pages

> 0 * * * * /path/to/env/bin/python /path/to/project/manage.py search_garbage_collect

> crontab -l

## For development ##

> pip install pylint

To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To the Django project url.py add

``` python
from django.conf import settings
from django.conf.urls.static import static
```

and at the bottom of the file add

``` python

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
