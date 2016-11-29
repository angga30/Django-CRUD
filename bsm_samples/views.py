from watson import search as watson

from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_input', None)

        search_results = watson.search(search_query)

        return render(request, 'base.html', context={"SEARCH_RESULTS": search_results})
