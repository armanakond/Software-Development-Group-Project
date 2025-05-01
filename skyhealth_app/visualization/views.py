#Author: Arman

from django.shortcuts import render
from django.db.models import Q, Count
from voting.models import HealthVote

def trends_view(request):
    return render(request, 'visualization/trends.html')

# presents the summaries and trend charts
def teamsummary_view(request):
    vote_counts = HealthVote.objects.aggregate(
        red_count=Count('id', filter=Q(q1_vote='red') | Q(q2_vote='red') | Q(q3_vote='red') |
                                  Q(q4_vote='red') | Q(q5_vote='red') | Q(q6_vote='red')),
        amber_count=Count('id', filter=Q(q1_vote='amber') | Q(q2_vote='amber') | Q(q3_vote='amber') |
                                    Q(q4_vote='amber') | Q(q5_vote='amber') | Q(q6_vote='amber')),
        green_count=Count('id', filter=Q(q1_vote='green') | Q(q2_vote='green') | Q(q3_vote='green') |
                                    Q(q4_vote='green') | Q(q5_vote='green') | Q(q6_vote='green'))
    )

    return render(request, 'visualization/teamsummary.html', {'vote_counts': vote_counts})
