from django.shortcuts import render

def trends_view(request):
    return render(request, 'visualization/trends.html')
# presents the summaries and trend charts
def teamsummary_view(request):
    return render(request, 'visualization/teamsummary.html')