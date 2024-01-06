from django.shortcuts import render
from django.views import View

class AboutUsView(View):
    def get(self, request):
        current_page = 'about_us'
        return render(request, 'about_us.html',{'current_page': current_page})

