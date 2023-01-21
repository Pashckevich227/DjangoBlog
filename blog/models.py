from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  # Строковое поле, для строк малого и большого размера.
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,  # Если удалиться пользователь, то и его статьи удаляться(каскадное отношение)
    )
    body = models.TextField()  # Большое текстовое поле

    def __str__(self):
        return self.title
