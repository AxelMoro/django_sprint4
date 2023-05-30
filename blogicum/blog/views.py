from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone as tz
from django.db.models import Count
from django.urls import reverse_lazy
from blog.models import Post, User, Comment, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from .forms import CommentForm, PostForm, UserForm


class PostMixin:
    model = Post


class CommentMixin:
    model = Comment
    comment = None
    form_class = CommentForm
    template_name = 'blog/comment.html'
    pk_url_kwarg = 'comment_id'

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Post, pk=kwargs['post_id'], author=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment = self.comment
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail',
                            kwargs={'pk': self.comment.pk})


class IndexListView(PostMixin, ListView):
    queryset = Post.objects.prefetch_related(
        'comments'
    ).select_related('author').filter(
            pub_date__lt=tz.now(),
            is_published=True,
            category__is_published=True,
        ).annotate(comment_count=Count('comments'))
    template_name = 'blog/index.html'
    ordering = '-pub_date'
    paginate_by = 10


class PostDetailView(PostMixin, DetailView):
    template_name = 'blog/detail.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = (
            self.object.comments.select_related('post')
        )
        return context


class CategoryListView(PostMixin, ListView):
    template_name = 'blog/category.html'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        queryset = (Post.objects.
                    prefetch_related('comments').
                    filter(
                        pub_date__lt=tz.now(),
                        is_published=True,
                        category__slug=self.kwargs['category_slug'],
                    ).annotate(comment_count=Count('comments')
                               ).order_by('-pub_date')
                    )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug'],
            is_published=True,
            )
        return context


class ProfileListView(ListView):
    model = Post
    template_name = 'blog/profile.html'
    ordering = 'id'
    paginate_by = 10

    def get_queryset(self):
        instance = Post.objects.select_related(
            'category',
            'location',
            'author'
        ).only(
            'id',
            'title',
            'pub_date',
            'location',
            'location__name',
            'author__username',
            'category__slug',
            'category__title',
            'text',
        ).filter(
            author__username__exact=self.kwargs['username']
        ).annotate(
            comment_count=Count('comments')
        )
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(username=self.kwargs['username'])
        return context


@login_required
def add_comment(request, post_id):
    comment = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        commentary = form.save(commit=False)
        commentary.author = request.user
        commentary.post = comment
        commentary.save()
    return redirect('blog:post_detail', pk=post_id)


class PostCreateView(LoginRequiredMixin, PostMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/create.html'

    def get_success_url(self):
        return reverse_lazy(
            'blog:profile',
            kwargs={'username': self.request.user}
        )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PostMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/create.html'
    pk_url_kwarg = 'post_id'
    posts = None

    def dispatch(self, request, *args, **kwargs):
        self.posts = get_object_or_404(Post, pk=kwargs['post_id'])
        if self.posts.author != request.user:
            return redirect('blog:post_detail', self.kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail',
                            kwargs={'pk': self.posts.pk})


class PostDeleteView(LoginRequiredMixin, PostMixin, DeleteView):
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index')
    pk_url_kwarg = 'post_id'

    def dispatch(self, request, *args, **kwargs):
        self.posts = get_object_or_404(Post, pk=kwargs['post_id'])
        if self.posts.author != request.user:
            return redirect('blog:post_detail', self.kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)


class CommentUpdateView(LoginRequiredMixin, CommentMixin, UpdateView):
    pass


class CommentDeleteView(LoginRequiredMixin, CommentMixin, DeleteView):
    pass


class ProfiletUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'blog/user.html'
    success_url = reverse_lazy('blog:index')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'blog:profile',
            kwargs={'username': self.request.user.username})
