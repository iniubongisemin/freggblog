from django.urls import path
from .views import home_page_view, about_page_view, contact_page_view, service_page_view

urlpatterns = [
    path('', home_page_view, name = 'home'),
    path('about/', about_page_view, name = 'about'),
    path('contact/', contact_page_view, name = 'contact'),
    path('service/', service_page_view, name = 'service'),
]