from django.shortcuts import render

def session_view(request):
    return render(request, 'voting/session.html')