from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from users.forms.change_password_form import PasswordForm
from users.forms.create_post_form import CreatePostForm
from users.forms.loginform import LoginForm
from users.forms.posts_confirm_delete import PostConfirmDeleteForm
from users.forms.signupform import SignUpForm
from users.models import Posts, User


class PostListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'users/post_list.html'
    model = Posts

    def get_queryset(self):
        return self.model.objects.all().order_by('-last_edit_date')


class SignUpView(CreateView):
    template_name = 'users/register.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('post_list')


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('post_list')

        return render(request, self.template_name, {'form': LoginForm()})

    @staticmethod
    def post(request):
        username: str = request.POST.get('username')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')

        user: get_user_model() or None = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('post_list')

        messages.error(request, 'There is no such user...')
        return redirect('login')


class ChangePasswordView(View, LoginRequiredMixin):
    login_url = '/login'
    template_name = 'users/change_password.html'
    form_class = PasswordForm

    def get(self, request):
        context = {'form': self.form_class(user=request.user)}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.user, request.POST)

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(request=self.request, message="Password is changed...")
        form.save()
        return redirect(reverse('post_list'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    template_name = 'users/create_post.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    template_name = 'users/edit_post.html'
    model = Posts
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse('post_list')


class DeletePostView(DeleteView):
    template_name = 'users/posts_confirm_delete.html'
    model = Posts
    form_class = PostConfirmDeleteForm
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super(DeletePostView, self).get_context_data(form=self.form_class)
        return context


class UserProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    template_name = 'users/profile_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        return context


def logout_view(request):
    logout(request)
    return redirect('post_list')
