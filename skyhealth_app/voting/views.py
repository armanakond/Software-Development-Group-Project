from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthVote

def session_view(request):
    return render(request, 'voting/session.html')


#All the inputs in views.py for healthvote
@login_required
def voting_view(request):
    if request.method == "POST":
        HealthVote.objects.create(
            user=request.user,
            session_name=request.POST.get('session_name'),
            session_date=request.POST.get('session_date'),
            team_name=request.POST.get('team_name'),

            q1_vote=request.POST.get('q1_vote'),
            q1_feedback=request.POST.get('q1_feedback'),
            q1_team_actions=request.POST.get('q1_team_actions'),
            q1_org_solutions=request.POST.get('q1_org_solutions'),

            q2_vote=request.POST.get('q2_vote'),
            q2_feedback=request.POST.get('q2_feedback'),
            q2_team_actions=request.POST.get('q2_team_actions'),
            q2_org_solutions=request.POST.get('q2_org_solutions'),

            q3_vote=request.POST.get('q3_vote'),
            q3_feedback=request.POST.get('q3_feedback'),
            q3_team_actions=request.POST.get('q3_team_actions'),
            q3_org_solutions=request.POST.get('q3_org_solutions'),

            q4_vote=request.POST.get('q4_vote'),
            q4_feedback=request.POST.get('q4_feedback'),
            q4_team_actions=request.POST.get('q4_team_actions'),
            q4_org_solutions=request.POST.get('q4_org_solutions'),

            q5_vote=request.POST.get('q5_vote'),
            q5_feedback=request.POST.get('q5_feedback'),
            q5_team_actions=request.POST.get('q5_team_actions'),
            q5_org_solutions=request.POST.get('q5_org_solutions'),

            q6_vote=request.POST.get('q6_vote'),
            q6_feedback=request.POST.get('q6_feedback'),
            q6_team_actions=request.POST.get('q6_team_actions'),
            q6_org_solutions=request.POST.get('q6_org_solutions')
        )
        return redirect('dashboard')


#Session inputs for healthvote
    session_names = ["Sprint 1", "Sprint 2"]
    session_dates = ["2025-05-01", "2025-05-15"]
    team_names = ["Team A", "Team B"]

    return render(request, 'voting/voting.html', {
        'session_names': session_names,
        'session_dates': session_dates,
        'team_names': team_names
    })
