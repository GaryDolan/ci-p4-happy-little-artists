"""
Views for the about_us app.
"""
from django.shortcuts import render
from django.views import View


class AboutUsView(View):
    """
    A class based view for displaying the about us page.
    """
    def get(self, request):
        """
        Handles the get request for the about us page. Sets the current page
        and renders the about us page via the about_us.html template.
        """
        current_page = 'about_us'
        return render(request, 'about_us.html', {'current_page': current_page})
