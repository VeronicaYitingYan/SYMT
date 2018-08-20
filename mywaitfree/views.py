from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SignupForm
from .models import Guest
from django.utils import timezone

# Create your views here.
 
def signupform(request):
 #if form is submitted
    if request.method == 'POST':
 #will handle the request later,record fill in information
        form = SignupForm(request.POST)
 
 #checking the form is valid or not 
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone']
            group = form.cleaned_data['group']
            g = Guest(guest_name=name, phone_number=number, group_size=int(group), register_time=timezone.now())
            g.save()
            rank = len(Guest.objects.all()) 
 #if valid rendering new view with values
 #the form values contains in cleaned_data dictionary render呈现
            return render(request, 'submit.html', {
                   'name': name,
                   'phone': number,
                   'group': group,
                   'rank': rank,
                  })
    else: #create new form
        form = SignupForm()
 
 #returning form 
    return render(request, 'signupform.html', {'form':form});
 
def results(request):
    waiting_list = Guest.objects.order_by('register_time')
    template = loader.get_template('results.html')
    context = {
        'waiting_list' : waiting_list,
     }
    return HttpResponse(template.render(context, request))