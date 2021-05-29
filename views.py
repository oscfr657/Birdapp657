

from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.search.models import Query


def bird_page_403(request, exception=None, template_name='bird_403.html'):
    context = {'error': '403 Permission denied'}
    return render(request, 'bird_403.html', context, status=403)


def bird_page_404(request, exception=None, template_name='bird_404.html'):
    context = {'error': '404 Page not found'}
    return render(request, 'bird_404.html', context, status=404)


def bird_page_500(request, exception=None, template_name='bird_500.html'):
    context = {'error': '500 Server error'}
    return render(request, 'bird_500.html', context, status=500)


def search(request):
    search_query = request.GET.get('search_query', None)
    if search_query:
        search_results = Page.objects.live(
                    ).public().exclude(
                        show_in_menus=True).order_by(
                            '-first_published_at').search(
                                search_query, order_by_relevance=False)
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()
    return render(request, 'birdapp657/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
