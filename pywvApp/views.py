from django.shortcuts import render


# class HomeView(ListView):
#     model= Post
#     template_name='home.html'
#     cats=Category.objects.all()
#     ordering=['-id']
    
#     def get_context_data(self,*args, **kwargs):
#         cat_menu=Category.objects.all()
#         context=super(HomeView,self).get_context_data(*args, **kwargs)
#         context["cat_menu"]=cat_menu
#         return context
    
# def LikeView(request,pk):
#     post= get_object_or_404(Post, id=request.POST.get('post_id'))
#     liked=False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked=False
#     else:
#         post.likes.add(request.user)
#         liked=True
    
#     return HttpResponseRedirect(reverse('article-details',args=[str(pk)]))

# def CategoryView(request,cats):
#     category_posts=Post.objects.filter(category=cats.replace('-',' '))
#     return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})
       
# def CategoryListView(request):
#     cat_menu_list=Category.objects.all()
#     return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})
   
# class ArticleDetailView(DetailView):
#     model=Post
#     template_name= 'article_details.html'
    
#     def get_context_data(self,*args, **kwargs):
#         cat_menu=Category.objects.all()
#         context=super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        
#         stuff=get_object_or_404(Post,id=self.kwargs['pk'])
#         total_likes=stuff.total_likes()
        
#         liked=False
#         if stuff.likes.filter(id=self.request.user.id).exists():
#             liked=True
        
#         context["cat_menu"]=cat_menu
#         context["total_likes"]=total_likes
#         context["liked"]=liked
#         return context
    
# class AddPostView(CreateView):
#     model= Post
#     form_class=PostForm
#     template_name='addPost.html'
    
   
# class AddCommentView(CreateView):
#     model= Comment
#     form_class=CommentForm
#     template_name='add_comment.html'
#     success_url=reverse_lazy('home')
    
#     def form_valid(self,form):
#         form.instance.post_id=self.kwargs['pk']
#         return super().form_valid(form)
    
    
# class AddCategoryView(CreateView):
#     model= Category
#     #form_class=PostForm
#     template_name='add_category.html'
#     fields='__all__'
   
# class UpdatePostView(UpdateView):
#     model=Post
#     form_class=PostForm
#     template_name='update_post.html'
#     #fields=['title','title_tag','body']
    
# class DeletePostView(DeleteView):
#     model=Post
#     template_name='delete_post.html'
#     success_url=reverse_lazy('home')
 
 

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