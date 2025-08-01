from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('about', views.aboutView, name='about'),
    path('contact', views.contactView, name='contact'),
    path('services', views.serviceView, name='services'),
    path('services/research', views.service_researchView, name='service_research'),
    path('services/consulting', views.consultingView, name='consulting'),
    path('services/data', views.service_dataView, name='service_data'),
   # path('services/consulting', views.consultingView, name='consulting'),
]