from django.shortcuts import render

# Create your views here.

# home page
def home_page_view(request):

    return render(request, 'main/index.html')

# about page
def about_page_view(request):

    return render(request, 'main/about.html')

# contact page
def contact_page_view(request):

    return render(request, 'main/contact.html')

# service page
def service_page_view(request):

    return render(request, 'main/service.html')
