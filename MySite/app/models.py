import uuid

from django.db import models
from django.urls import reverse


class CarPicture(models.Model):
    title = models.CharField(max_length=50, help_text='Enter title')
    image = models.ImageField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('carpicture-detail', args=[str(self.id)])

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title


# UUIDField используется для поля id, чтобы установить его как primary_key для этой модели. Этот тип поля выделяет
# глобальное уникальное значение для каждого экземпляра.
# DateField используется для данных due_back (при которых ожидается, что наклейка появится после заимствования или
# обслуживания).
# Это значение может быть blank или null (необходимо, когда наклейка доступна).
# Метаданные модели (Class Meta) используют это поле для упорядочивания записей, когда они возвращаются в запросе.


class CarPictureInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Уникальный идентификатор')
    image = models.ForeignKey('CarPicture', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Status')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s' % self.id
