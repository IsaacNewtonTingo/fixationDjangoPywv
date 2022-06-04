from django.urls import path
from .views import AddCategoryView, AddPostView,LikeView, CategoryListView,AddCommentView, DeletePostView, HomeView,ArticleDetailView, UpdatePostView,CategoryView
from . import views
#from django import views

urlpatterns = [
    path('',HomeView.as_view(),name="home"),

    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    
    path('add-post/',AddPostView.as_view(),name='add-post'),
    
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    
    path('category/<str:cats>/',CategoryView,name='category'),
    
    path('category-list',CategoryListView,name='category-list'),
    
    path('like/<int:pk>',LikeView,name='like_post'),
    
    path('article/<int:pk>/comment',AddCommentView.as_view(),name='add_comment'),
   
   
    path('', views.Home, name="home"),
    path('contactUs', views.ContactUs, name="contactUs"),
    path('aboutUs', views.AboutUs, name="aboutUs"),
    path('adoptAGirlsMonth', views.AdoptAGirlsMonth, name="adoptAGirlsMonth"),
    path('endingViolence', views.EndingViolence, name="endingViolence"),
    path('flourish', views.Flourish, name="flourish"),
    path('lbqSupport', views.LbqSupport, name="lbqSupport"),
    path('mens', views.Mens, name="mens"),
    path('pywv2022_2026StrategicPlan', views.Pywv2022_2026StrategicPlan, name="pywv2022_2026StrategicPlan"),
    path('resources', views.Resources, name="resources"),
    path('theTeam', views.TheTeam, name="theTeam"),
    path('whatWeDo', views.WhatWeDo, name="whatWeDo"),
    path('Donate', views.Donate, name="Donate"),
    
]