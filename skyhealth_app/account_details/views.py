from django.shortcuts import render

# Create your views here.
def accountdetails_view(request):
    return render(request, 'account_details/accountdetails.html') #returns requested page 