from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    list_of_hashtag = models.CharField(max_length=255, null=True, blank=True, verbose_name='Хэштэги')
    short_name = models.CharField(max_length=255, verbose_name='Короткий текст')
    body = models.TextField(verbose_name='Тело новости')
    image = models.ImageField(upload_to='news/', verbose_name='Картинка')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тэга')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'


class Post_Tag(models.Model):
    article_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость - тэг'
        verbose_name_plural = 'Новость - тэг'
