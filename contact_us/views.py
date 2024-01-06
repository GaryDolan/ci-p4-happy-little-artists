from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm

class ContactUsView(View):
    form_class = ContactUsForm
    

    def get (self, request):
        current_page = 'contact_us'
        # declare dictionary to hold initial values 
        initial = {}
        # populate any details we already have for a logged in user 
        if request.user.is_authenticated:
            # set up the name key value pair
            initial['name'] = f"{request.user.first_name} {request.user.last_name}"
        else:
            initial = {}
        
        form = self.form_class(initial=initial)
        
        return render(request, 'contact_us.html', {'current_page': current_page, 'form':form})