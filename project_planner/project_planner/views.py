from django.shortcuts import render
from django.views.generic import TemplateView

#class view for 'index' page of backend-api 
class HomePageView(TemplateView):
    template_name="homepage.html"


"""
def homePage(request):
    return render(request,'homepage.html')
"""