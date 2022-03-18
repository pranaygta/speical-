from app2.views import app2_rrr
from django.urls import path
app_name='app2'
urlpatterns=[
    path('app2_rrr/',app2_rrr,name='app2_rrr'),
]