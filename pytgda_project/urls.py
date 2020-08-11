"""pytgda_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import SignUpView, LoginView, logout_view, ChangePasswordView, CreatePostView, PostListView, \
    EditPostView, DeletePostView, UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('<pk>/edit', EditPostView.as_view(), name='edit_post'),
    path('<pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('register', SignUpView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('change_password', ChangePasswordView.as_view(), name='change_password'),
    path('create_post', CreatePostView.as_view(), name='create_post'),
    path('user/<pk>', UserProfileView.as_view(), name='profile'),
    # path('profile/<pk>', ProfileUpdateView.as_view(), name='profile_edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
