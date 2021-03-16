# Create your views here.
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from .models import ApartsnsModel
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

# はも追記
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request , 'signup.html' , {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request ,'signup.html' ,{'some' : 100} )
    return render(request ,'signup.html' ,{'some' : 100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list', aparts=username2)
        else:
            return redirect('login')
    return render(request, 'login.html')

'''
@login_required
def listfunc(request):
    object_list = ApartsnsModel.objects.all()
    return render(request, 'list.html' , {'object_list':object_list})
'''

# はも追記
# LoginRequiredMixinというクラスを継承していますが、これを書いておくだけで未ログインの場合、ログイン必須になります。
class ListView(LoginRequiredMixin, ListView):
    template_name = 'list.html' # htmlファイルを指定します。
    model = ApartsnsModel # モデル名を指定します。ApartsnsModel.objects.all()と同義です
    context_object_name = 'object_list' # htmlファイル側でModelObjects(ApartsnsModel.objects.all())をどういう名称で使うかを指定します。デフォルトがobject_listなので定義しなくてもOKです。listfuncの {'object_list':object_list})と同義です。

    def get(self, request, *args, **kwargs):
        if self.request.user.username == self.kwargs['aparts']:
            return super().get(request, **kwargs)
        return render(self.request, '404.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')
'''
@login_required
def detailfunc(request , pk):
    object = ApartsnsModel.objects.get(pk=pk)
    return render(request , 'detail.html',{'object':object})
'''

# はも追記
# DetailViewを継承することで、detailfuncのようにpkを持ってくる必要がなくなります。
class DetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = ApartsnsModel  


def goodfunc(request, pk):
    post = ApartsnsModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = ApartsnsModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + '' + post2
        post.save()
        return redirect('list')

# class ApartsnsCreate(CreateView):
#     template_name = 'create.html'
#     model = ApartsnsModel
#     fields = ('title' , 'content' , 'author' , 'images')
#     success_url = reverse_lazy('list')

# はも追記
class ApartsnsCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = ApartsnsModel
    form_class = PostForm # fieldsの内容はforms.pyというファイルを用意して記述するようにしましょう。forms.pyに記述することでフォームの内容に関してできる幅が広がります。
    success_url = reverse_lazy('list')

