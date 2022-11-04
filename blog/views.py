from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from blog.models import Configuracion
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post



def index(request):
    configuracion = Configuracion.objects.first()
    posts = Post.objects.order_by('-date_published').all()
    return render(request, "blog/index.html", {'configuracion': configuracion, "posts": posts})
    #return render(request, "blog/index.html",{"posts": posts})

class ListPost(ListView):
    model=Post

class CreatePost(LoginRequiredMixin,CreateView): #el login required tiene que ir primero, esto me sirve para que me pida un Login si quiero ver una funcionalidad
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")
    
class DetailPost(DetailView):
    model=Post

class UpdatePost(LoginRequiredMixin,UpdateView): #el login required tiene que ir primero, esto me sirve para que me pida un Login si quiero ver una funcionalidad
    model=Post
    fields=['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DeletePost(LoginRequiredMixin,DeleteView): #el login required tiene que ir primero, esto me sirve para que me pida un Login si quiero ver una funcionalidad
    model=Post
    success_url = reverse_lazy("list-post")

class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")