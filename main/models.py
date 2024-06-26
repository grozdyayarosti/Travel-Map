from django.db import models


class Mark(models.Model):
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    user_id = models.ForeignKey(
        verbose_name='ID пользователя',
        to='auth.user',
        on_delete=models.CASCADE)
    # user_id = models.IntegerField(verbose_name='ID пользователя')

    # content_id = models.IntegerField('ID контента')
    content_id = models.ForeignKey(
        verbose_name='ID контента',
        to='Content',
        on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f'{self.latitude}, {self.latitude}'

    class Meta:
        verbose_name = 'Отметка'  # Название таблицы в единственном числе
        verbose_name_plural = 'Отметки'  # Название таблицы в множественном числе


class Content(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Контент'  # Название таблицы в единственном числе
        verbose_name_plural = 'Контент'  # Название таблицы в множественном числе


class Photo(models.Model):
    photo = models.TextField('Фото')
    # content_id = models.IntegerField('ID контента')
    content_id = models.ForeignKey(
        verbose_name='ID контента',
        to='Content',
        on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Контент №{self.content_id}'

    class Meta:
        verbose_name = 'Фото'  # Название таблицы в единственном числе
        verbose_name_plural = 'Фотографии'  # Название таблицы в множественном числе
