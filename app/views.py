from django.shortcuts import render
import requests

# Create your views here.
# def index(request):
#     a = requests.get("https://restcountries.com/v2/all")  #pip install requests (Connecting two projects only works when server is on for both the projects)
#     data = a.json()
#     return render(request,'index.html',{'data':data})

def index(request):
    # Fetch data from the API
    response = requests.get("https://restcountries.com/v2/all")
    if response.status_code == 200:
        data = response.json()
    else:
        data = []

    # Handle search query
    query = request.GET.get('search', '')  # Get 'search' parameter from request
    if query: 
        # Filter countries by name (case-insensitive)
        query = query.lower()
        data = [country for country in data if query in country.get('name', '').lower()]


    return render(request, 'index.html', {'data': data, 'query': query})
