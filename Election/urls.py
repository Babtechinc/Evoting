
from django.contrib import admin
from django.urls import path
from Election import views

urlpatterns = [
    path('AddParty', views.AddParty, name='AddParty'),
    path('VoteforCandidates/<int:id>', views.VoteforCandidates, name='VoteforCandidates'),
    path('PickCandidates', views.PickCandidates, name='PickCandidates'),
    path('Analysis/<int:id>', views.Analysis, name='Analysis'),

]
