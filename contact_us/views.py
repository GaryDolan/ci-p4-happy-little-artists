from smtplib import SMTPException
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactUsForm

class ContactUsView(View):
    form_class = ContactUsForm
    template_name = 'contact_us.html'
    

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
        
        return render(request, self.template_name, {'current_page': current_page, 'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Retrieve the sender details
            from_name = self.request.POST.get('name')
            from_email = self.request.POST.get('email')
            enquiry = self.request.POST.get('message')

            try:
                # Send email using form details
                send_mail(
                    subject='Happy little artists enquiry',
                    # using html message instead
                    message='',
                    html_message=f'<p>{enquiry}</p>\n\n<p><strong>Sent by {from_name}</strong> ({from_email})</p>',
                    from_email=None, 
                    recipient_list=['happylittleartistsartclub@gmail.com'],
                )

                # Redirect the user home and display a success message
                messages.success(request, 'We have received you message and will be in touch soon.')
                return redirect('home')
            except SMTPException as e:
                # Catch any SMTP-related exceptions
                messages.error(request, 'An error occurred while sending the email. Please try again later.')
                return redirect('home')
        
        # form was not valid, return to form page and display message 
        messages.warning(request, 'Form invalid please try again')
        return render(request, self.template_name, {'form': form})