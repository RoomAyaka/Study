from django.db import models
# Create your models here.


class Article(models.Model):
    # verbose_name: 管理サイト上で指定の文字列を表示が出来る
    # auto_now_add: 投稿時に現在日時を設定する
    # blank: 投稿時に空白を許容する
    title = models.CharField(max_length=100, verbose_name='タイトル')
    message = models.TextField(verbose_name='本文')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='投稿日')

    def __str__(self):
        # 管理画面の一覧にタイトルを表示できるように設定
        return self.title

    class Meta:
        # 属性と属性値を参照してそのモデルのオブジェクトの扱い方を変更する
        # 管理サイト上のモデルの表記方法を変更する
        verbose_name_plural = "記事"
