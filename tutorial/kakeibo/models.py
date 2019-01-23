from django.db import models
from datetime import datetime

class Category(models.Model):

    class Meta:
        #カテゴリ
        verbose_name ="カテゴリ"
        verbose_name_plural ="カテゴリ"
      
#カラム名の定義
    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name


class Kakeibo(models.Model):

    class Meta:
      
        verbose_name ="家計簿"
        verbose_name_plural ="家計簿"

    #カラムの定義
    date = models.DateField("日付",default=datetime.now)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name="カテゴリ")
    money = models.IntegerField("金額", help_text="単位は日本円")
    memo = models.CharField(verbose_name="メモ", max_length=500)

    def __str__(self):
        return self.memo



