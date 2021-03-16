from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc,  goodfunc, readfunc, ApartsnsCreate
from .views import ListView, DetailView

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('', loginfunc, name='login'),
    path('list/<str:aparts>', ListView.as_view(), name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', ApartsnsCreate.as_view(), name='create'),
]
