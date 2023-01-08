from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    # template_name: レンダリングするテンプレートを指定
    # model: 使用するモデルクラス名を指定
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        # 最新の記事を5件取得する
        return Article.objects.order_by('-created_at')[:5]


class ArticleView(DetailView):
    # template_name: レンダリングするテンプレートを指定
    # model: 使用するモデルクラス名を指定
    model = Article
    template_name = 'article.html'


class Newview(LoginRequiredMixin, CreateView):
    # form_class: 定義したフォームのクラスを指定
    form_class = ArticleForm
    template_name = 'form.html'
    # success_url: 処理が完了後にURL先
    success_url = "/"
    # login_url: 未ログインユーザーに対して遷移するURL先
    login_url = "/admin/"

