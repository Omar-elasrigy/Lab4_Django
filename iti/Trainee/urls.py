from django.urls import path
# from .views import *
from .views import *

urlpatterns = [
    path('',list,name='list'),
    path('Update/<int:id>',update_trainee,name='update_trainee'),
    path('Delete/<int:id>',delete_trainee,name='delete_trainee'),
    path('Create/',NewTrainee.as_view(),name='create'),
    path('show_details/<int:id>',show_details_trainee,name='show_details_trainee'),
]
