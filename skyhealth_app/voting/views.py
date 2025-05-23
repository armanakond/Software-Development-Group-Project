#Author - Junayed Ahmed
#Co Author - Md Hoque
#Co Author - Sikandar Ali

#All required imports for methods and code to run in views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthVote
from .models import Session, Team

#Login required makes it to where the individual can't access url without being logged in
@login_required
def session_view(request):
    votes = HealthVote.objects.filter(user=request.user)

    return render(request, 'voting/session.html', {
        'votes': votes
    })



#All the inputs in views.py for healthvote
@login_required #Login required makes it to where the individual can't access url without being logged in
def voting_view(request): #Function defined for voting view
    #If statement checking if POST has been ran for the form
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
        
        #Redirects to dashboard after form is submitted
        return redirect('dashboard')


#Session inputs for healthvote
    sessions = Session.objects.all()
    teams    = Team.objects.all()

    session_names = [s.name for s in sessions] #Used for dynamically creating session names from admin dashboard
    session_dates = [s.date.isoformat() for s in sessions] #Used for dynamically creating session names from admin dashboard
    team_names    = [t.name for t in teams] #Used for dynamically creating team names from admin dashboard

    return render(request, 'voting/voting.html', {
        'session_names': session_names,
        'session_dates': session_dates,
        'team_names': team_names,
    })


#Login required makes it to where the individual can't access url without being logged in
@login_required
def change_vote_view(request, pk): #Function created for changing voting
    vote = get_object_or_404(HealthVote, pk=pk, user=request.user) #Gets details and stores into vote

    #If statement checking if POST has been ran for the form
    if request.method == "POST": 
        vote.q1_vote = request.POST.get('q1_vote', vote.q1_vote)
        vote.q1_feedback = request.POST.get('q1_feedback', vote.q1_feedback)
        vote.q1_team_actions = request.POST.get('q1_team_actions', vote.q1_team_actions)
        vote.q1_org_solutions = request.POST.get('q1_org_solutions', vote.q1_org_solutions)

        vote.q2_vote = request.POST.get('q2_vote', vote.q2_vote)
        vote.q2_feedback = request.POST.get('q2_feedback', vote.q2_feedback)
        vote.q2_team_actions = request.POST.get('q2_team_actions', vote.q2_team_actions)
        vote.q2_org_solutions = request.POST.get('q2_org_solutions', vote.q2_org_solutions)

        vote.q3_vote = request.POST.get('q3_vote', vote.q3_vote)
        vote.q3_feedback = request.POST.get('q3_feedback', vote.q3_feedback)
        vote.q3_team_actions = request.POST.get('q3_team_actions', vote.q3_team_actions)
        vote.q3_org_solutions = request.POST.get('q3_org_solutions', vote.q3_org_solutions)

        vote.q4_vote = request.POST.get('q4_vote', vote.q4_vote)
        vote.q4_feedback = request.POST.get('q4_feedback', vote.q4_feedback)
        vote.q4_team_actions = request.POST.get('q4_team_actions', vote.q4_team_actions)
        vote.q4_org_solutions = request.POST.get('q4_org_solutions', vote.q4_org_solutions)

        vote.q5_vote = request.POST.get('q5_vote', vote.q5_vote)
        vote.q5_feedback = request.POST.get('q5_feedback', vote.q5_feedback)
        vote.q5_team_actions = request.POST.get('q5_team_actions', vote.q5_team_actions)
        vote.q5_org_solutions = request.POST.get('q5_org_solutions', vote.q5_org_solutions)

        vote.q6_vote = request.POST.get('q6_vote', vote.q6_vote)
        vote.q6_feedback = request.POST.get('q6_feedback', vote.q6_feedback)
        vote.q6_team_actions = request.POST.get('q6_team_actions', vote.q6_team_actions)
        vote.q6_org_solutions = request.POST.get('q6_org_solutions', vote.q6_org_solutions)

        #Saves vote data onto the SQLite database
        vote.save()
        #Redirects to dashboard after form is submitted
        return redirect('dashboard')

    #Keeps user on change vote if nothing is done
    return render(request, 'voting/change_vote.html', {'vote': vote})

