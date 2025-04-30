from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SurveySubmission, SurveyAnswer

def session_view(request):
    return render(request, 'voting/session.html')


def voting_view(request):
    if request.method == "POST":

        return redirect('dashboard')

    return render(request, 'voting/voting.html')

