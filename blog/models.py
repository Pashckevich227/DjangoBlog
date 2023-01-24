import datetime
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)  # Строковое поле, для строк малого и большого размера.
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,  # Если удалиться пользователь, то и его статьи удаляться(каскадное отношение)
    )
    body = models.TextField()  # Большое текстовое поле
    time_create = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=str(self.id))
