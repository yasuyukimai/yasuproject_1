from django.urls import path
from .views import loginfunc , logoutfunc ,ListView , DetailView , CreateView , CommentView ,ApartCreate,ApartDelete,ApartUpdate

urlpatterns = [
    path('', loginfunc, name='login'),
    path('list/', ListView.as_view(), name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('create/', ApartCreate.as_view(), name='create'),
    path('comment/<int:post_pk>', CommentView.as_view(), name='comment'),
    path('delete/<int:pk>', ApartDelete.as_view(), name='delete'),
    path('update/<int:pk>', ApartUpdate.as_view(), name='update'),
]
