from django.views.generic import ListView,DetailView
from .models import Article
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy




class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = (
    "title",
    "body",
    )
    template_name = "article_edit.html"

class ArticleCreateView(CreateView):
    model= Article
    template_name="article_new.html"
    fields=("title","body",)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")