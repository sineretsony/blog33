from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Кюшка для поиска по многим "критериям" | или & и там и там
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, UserProfile
from .forms import CommentForm, PostForm, NewsletterForm, ProfileForm, \
    RegistrationForm, ProfileUpdateForm, ProfileUpdateForm2, ProfileForm2
from django.utils import timezone


def get_categories():
    all = Category.objects.all()
    count = all.count()
    return {'cat1': all[0:count // 2 + count % 2],
            'cat2': all[count // 2 + count % 2:]}


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by(
        '-published_date')  # выборка всех данных
    # posts_id = Post.objects.get(pk=1) #привязка к ид
    # posts = Post.objects.filter(title__contains='Python')
    # posts = Post.objects.filter(published_date__year=2023)
    # posts = Post.objects.filter(category__name__iexact='Автомобили')
    # categories = Category.objects.all()
    context = {'posts': posts}
    context.update(get_categories())

    return render(request, 'blog/index.html', context=context)


def post(request, id=None):
    post = get_object_or_404(Post, title=id)
    comments = Comment.objects.filter(post=post).order_by('-pub_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            # comment.pub_date = timezone.now()
            comment.save()
            return redirect('post', id=id)
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    context.update(get_categories())
    return render(request, 'blog/post.html', context=context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.user = request.user
            post.save()
            selected_tags = form.cleaned_data['tag']
            post.tag.set(selected_tags)

            return redirect('index')
    else:
        form = PostForm()

    context = {'form': form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context=context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context=context)


def services(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/services.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email_instance = form.save(commit=False)
            email_instance.published_date = timezone.now()
            email_instance.save()

            messages.success(request, 'Вы успешно подписались на обновления!')

            return redirect('contact')
    else:
        form = NewsletterForm()

    context = {'form': form}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context=context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) |
                                Q(title__icontains=query) |
                                Q(tag__tag__icontains=query)).order_by(
        '-published_date')
    context = {'posts': posts}
    context.update(get_categories())

    return render(request, 'blog/index.html', context=context)


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)

            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'blog/registration_user.html', {'form': form})


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = ProfileForm(instance=user_profile)
    form2 = ProfileForm2(instance=user_profile)

    context = {'form': form, 'form2': form2}
    context.update(get_categories())
    return render(request, 'blog/profile.html', context=context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form_user = ProfileUpdateForm(request.POST, instance=request.user)
        form_profile = ProfileUpdateForm2(request.POST, request.FILES, instance=request.user.userprofile)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect('profile')
    else:
        form_user = ProfileUpdateForm(instance=request.user)
        form_profile = ProfileUpdateForm2(instance=request.user.userprofile)

    context = {'form_user': form_user, 'form_profile': form_profile}
    return render(request, 'blog/update_profile.html', context)