#Author: MD


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def accountdetails_view(request):
    user = request.user

    if request.method == 'POST':
        # fields for updating 
        user.first_name = request.POST.get('first_name', '').strip() # strip helps to remove and trails and unnecessary whitespace
        user.username   = request.POST.get('username', '').strip()
        user.email      = request.POST.get('email', '').strip()

        # this only updates password if the user decides to set it
        new_pw = request.POST.get('password', '')
        if new_pw:
            user.set_password(new_pw)

        # redirects to the same page, which is the same as refreshing it
        user.save()
        return redirect('accountdetails')

    # simple site render
    return render(request, 
                  'account_details/accountdetails.html', 
                  { 'user': user }) # allows the html to access the user object and display its attributes which are the email and user info

