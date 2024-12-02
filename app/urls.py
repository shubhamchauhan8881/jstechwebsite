from django.urls import path
from . import views
from django.shortcuts import render
from .sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("blogs", views.BlogsView.as_view(), name="blogs"),
    path("get-page/<str:page_name>", views.GetPage),
    path("feedback", views.FeedbackView.as_view(), name="feedback"),
    path("careers", views.CareersView.as_view(), name="careers"),
    path("projects", views.ProjectsView.as_view(), name="projects"),
    path("team", views.Team.as_view(), name="team"),

    path("sitemap.xml/",sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]
