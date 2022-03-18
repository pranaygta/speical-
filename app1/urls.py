from app1.views import app1_pushpa
from django.urls import path
app_name='app1'
urlpatterns=[
    path('app1_pushpa/',app1_pushpa,name='app1_pushpa'),
]
