from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("blogs", views.BlogsView.as_view(), name="blogs"),
    path("get-page/<str:page_name>", views.GetPage),
    path("feedback", views.FeedbackView.as_view(), name="feedback"),
    path("careers", views.CareersView.as_view(), name=""),
    path("projects", views.ProjectsView.as_view(), name=""),
    path("team", views.Team.as_view(), name=""),
]
