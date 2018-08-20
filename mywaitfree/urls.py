
from django.urls import path
from mywaitfree import views 

urlpatterns = [
    path('', views.signupform, name='signupform'),
    path('results/', views.results, name='results'),
    path('submit/', views.results, name='submit'),
    ]