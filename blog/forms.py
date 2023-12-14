from django import forms
from .models import Post, Comment, Newsletter, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'poster', 'tag']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['poster'].widget.attrs['multiple'] = True


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['social_networks', 'avatar']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'social_networks']

