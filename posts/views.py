from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm, PostForm
from django.shortcuts import redirect, render


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/auth/login/"
    template_name = "signup.html"


def new_post(request):
    user = request.user
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            n_post = form.save(commit=False)
            n_post.author = user
            n_post.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form': form})
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})
