

from django.shortcuts import render


def bird_page_403(request, exception=None, template_name='bird_403.html'):
    context = {'error': '403 Permission denied'}
    return render(request, 'bird_403.html', context)


def bird_page_404(request, exception=None, template_name='bird_404.html'):
    context = {'error': '404 Page not found'}
    return render(request, 'bird_404.html', context)


def bird_page_500(request, exception=None, template_name='bird_500.html'):
    context = {'error': '500 Server error'}
    return render(request, 'bird_500.html', context)
