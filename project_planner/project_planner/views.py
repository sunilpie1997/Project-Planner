from django.shortcuts import render

#class view for 'index' page of backend-api 
def homePage(request):
    return render(request,'homepage.html')
