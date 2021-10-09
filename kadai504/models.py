from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Fruits(models.Model):
    no = models.IntegerField(
        'No.',
        validators=[MinValueValidator(1, 'Noは1以上を入力してください')]
        )
    name = models.CharField(
        '果物名',
        max_length=255, 
        validators=[MaxLengthValidator(10, '果物名は10文字以内で入力してください')])
    memo = models.TextField(
        'メモ',
        blank=True,
        max_length=50,
        validators=[MinLengthValidator(5, 'メモは5～50文字で入力してください')])

    def __str__(self):
        return self.name

    