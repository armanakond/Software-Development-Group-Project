from django.shortcuts import render, redirect

def session_view(request):
    return render(request, 'voting/session.html')


def voting_view(request):
    if request.method == "POST":

        return redirect('dashboard')

    return render(request, 'voting/voting.html')

