from watson import search as watson

from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        return render(
            request,
            'base.html',
            context={"ON_HOMEPAGE": True})


def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_input', None)
        search_results = watson.search(search_query)

        results = []

        for result in search_results:
            results.append(
                {
                    "title": result.title,
                    "url": result.url,
                    "pk": result.meta["pk"]
                }
            )
        return render(
            request,
            'base.html',
            context={
                "SEARCH_RESULTS": results, "SEARCH_QUERY": search_query
            }
        )
