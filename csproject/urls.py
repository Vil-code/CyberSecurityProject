from django.contrib import admin
from django.urls import path, include

from .views import homePageView, likeView, profileView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', homePageView, name='home'),
    path('like/', likeView, name='like'),
    path('profile/', profileView, name='profile'),
    path('login/', LoginView.as_view(template_name='./login.html')),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('admin/', admin.site.urls),
]

