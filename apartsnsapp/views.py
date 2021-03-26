# Create your views here.
from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from .models import ApartsnsModel , CommentModel
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView,DeleteView,UpdateView
from .forms import CommentCreateForm ,PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

class ListView(LoginRequiredMixin, ListView):
    template_name = 'list.html' 
    model = ApartsnsModel 
    context_object_name = 'object_list' 

class DetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = ApartsnsModel  

class ApartCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = ApartsnsModel
    form_class = PostForm
    success_url = reverse_lazy('list')

class ApartDelete(DeleteView):
    template_name = 'delete.html'
    model = ApartsnsModel
    success_url = reverse_lazy('list')

class ApartUpdate(UpdateView):
    template_name = 'update.html'
    model = ApartsnsModel
    fields = ('name', 'title','content')
    success_url = reverse_lazy('list')

class CommentView(LoginRequiredMixin, CreateView):
    template_name = 'commentmodel_form.html'
    model = CommentModel
    form_class = CommentCreateForm
    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False) 
        comment.post = get_object_or_404(ApartsnsModel, pk=post_pk)
        comment.save() 
        return redirect('detail', pk=post_pk)