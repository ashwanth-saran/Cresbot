from django.urls import path
from .views import home,index, RegisterView,logout_view
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('logout_view/',logout_view,name='logout_view'),
    path('chatbot/', views.chatbot_response_view,name='chatbot'),
    
    
    
    
    ]


 