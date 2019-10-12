from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search, sorting
import json

#renders the search page.
def search_view(request):
    return render(request, 'searchapp/search.html', {})

#Returns the autocomplete results while the user types in a letter.
# This is used to show dropdown of matching word
# called by ui end point
def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sorting(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)

# Returns a jsonresponse having the search results(25 words) containing the searched word
# this is used, to return json reponse containing 25 matching words.
# Will be called once search button clicked.
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term') # for example: query = 'hello'
        if query:
            # search and sort result
            searchResult = sorting(search(query.lower()), query.lower())
            # No matching word
            if len(searchResult) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchResult})
        else:
            return redirect('/')
