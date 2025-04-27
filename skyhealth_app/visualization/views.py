from django.shortcuts import render

def trends_view(request):
    return render(request, 'visualization/trends.html')

def teamsummary_view(request):
    return render(request, 'visualization/teamsummary.html')