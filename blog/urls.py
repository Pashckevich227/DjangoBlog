from django.urls import path
from .views import BlogListView, BlogDetailView, RegisterView, LoginView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post_detail'),
    path("", BlogListView.as_view(), name='home'),
    path("register", RegisterView.as_view(), name='register'),
    path("login", LoginView.as_view(), name='login'),
]