from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_networks = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/base.jpg', verbose_name='Аватар')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    tag = models.CharField(max_length=20, verbose_name='Тег')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name='Оглавление')
    content = models.TextField(verbose_name='Описание')
    published_date = models.DateTimeField(auto_created=True, verbose_name='Дата и время')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    poster = models.ImageField(upload_to='posters/', default='default_poster.jpg', verbose_name='Постер')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата и время')
    comment_text = models.TextField(max_length=200, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.author} - {self.comment_text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


class Newsletter(models.Model):
    email_name = models.EmailField(unique=True)

    def __str__(self):
        return self.email_name

    class Meta:
        verbose_name = "Подписчик на рассылку"
        verbose_name_plural = "Подписчики на рассылку"
