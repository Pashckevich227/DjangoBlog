from django.urls import path
from .views import BlogListView, BlogDetailView, LoginView, BlogCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post_detail'),
    path("", BlogListView.as_view(), name='home'),
    path("accounts/login/", LoginView.as_view(), name='login'),
]