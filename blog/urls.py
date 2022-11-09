"""blog_program URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, AnnouncementListView, AnnouncementCreateView, AnnouncementDetailView, AnnouncementUpdateView, AnnouncementDeleteView
from . import views

urlpatterns = [
    # empty path, views.home is the function created in views that returns the http response that we're
    # on the blog page, name is blog-home because perhaps we have another homepage for another app
    path("", PostListView.as_view(), name='blog-home'),
    path("about/", views.about, name='blog-about'),
    path("user/<str:username>", UserPostListView.as_view(), name='user-posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("post/new/", PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("announcement/", AnnouncementListView.as_view(), name='announcement'),
    path("announcement/<int:pk>/", AnnouncementDetailView.as_view(), name='announcement-detail'),
    path("announcement/new/", AnnouncementCreateView.as_view(), name='announcement-create'),
    path("announcement/<int:pk>/update/", AnnouncementUpdateView.as_view(), name='announcement-update'),
    path("announcement/<int:pk>/delete/", AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path("members/", views.members, name='blog-members')
]