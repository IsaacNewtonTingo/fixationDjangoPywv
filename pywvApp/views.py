from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import  Post,Comment
from .forms import PostForm,CommentForm


class HomeView(ListView):
    model= Post
    template_name='home.html'
    ordering=['-id']
    
    def get_context_data(self,*args, **kwargs):
        context=super(HomeView,self).get_context_data(*args, **kwargs)
        return context
   
class ArticleDetailView(DetailView):
    model=Post
    template_name= 'article_details.html'
    
    def get_context_data(self,*args, **kwargs):
        context=super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        
        return context
    
class AddPostView(CreateView):
    model= Post
    form_class=PostForm
    template_name='addPost.html'
    
   
class AddCommentView(CreateView):
    model= Comment
    form_class=CommentForm
    template_name='add_comment.html'
    success_url=reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
   
class UpdatePostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='update_post.html'
    #fields=['title','title_tag','body']
    
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
 
 

def Home(request):
        return render(request, "home.html")

def ContactUs(request):
        return render(request, "contactUs.html")
    
def AboutUs(request):
        return render(request, "aboutUs.html")

def AdoptAGirlsMonth(request):
        return render(request, "adoptAGirlsMonth.html")
    
def EndingViolence(request):
        return render(request, "endingViolence.html")
    
def Flourish(request):
        return render(request, "flourish.html")
    
def LbqSupport(request):
        return render(request, "lbqSupport.html")
    
def Mens(request):
        return render(request, "mens.html")
    
def Pywv2022_2026StrategicPlan(request):
        return render(request, "pywv2022-2026StrategicPlan.html")
    
def Resources(request):
        return render(request, "resources.html")
    
def TheTeam(request):
        return render(request, "theTeam.html")
    
def WhatWeDo(request):
        return render(request, "whatWeDo.html")

def Donate(request):
        return render(request, "donationPage.html")