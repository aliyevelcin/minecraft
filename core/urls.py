from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('',home,name='home'),
    path('games',games,name="games"),
    path('dates',dates,name="dates"),
    path('detailpages/<int:id>/',detailpages,name="detailpages")
]