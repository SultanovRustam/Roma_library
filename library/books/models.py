from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    class ReadingStatus(models.TextChoices):
        NOT_STARTED = 'not_started', 'Не начата'
        READING = 'reading', 'Читаю'
        FINISHED = 'finished', 'Прочитана'
        POSTPONED = 'postponed', 'Отложена'

    title = models.CharField(
        max_length=200,
        verbose_name='Название книги'
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    added_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    reading_status = models.CharField(
        max_length=20,
        choices=ReadingStatus.choices,
        default=ReadingStatus.NOT_STARTED,
        verbose_name='Статус чтения'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
        verbose_name='Рейтинг (1-10)'
    )
    start_reading_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата начала чтения'
    )
    finish_reading_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата окончания чтения'
    )
    notes = models.TextField(
        blank=True,
        verbose_name='Заметки'
    )
    cover = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True,
        verbose_name='Обложка'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-added_date']

    def __str__(self):
        return f'{self.title} - {self.author}'


from django.db import models

# Create your models here.
