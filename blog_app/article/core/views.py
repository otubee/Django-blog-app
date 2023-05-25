from django.shortcuts import render
import random
from core.models import Article
from core.forms import ArticleForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home_view(request):
  rand = random.randint(1, 3)
  article_obj = Article.objects.get(id=rand)
  lists = Article.objects.all()
  context={
    'object': article_obj,
    'lists': lists
  }
  return render(request, 'core/home.html', context)

def link_view(request, id=None):
  article_obj = None
  if id is not None:
    article_obj = Article.objects.get(id=id)
    context={
      'object': article_obj
    }
    return render(request, 'core/details.html', context=context)
  
@login_required
def create_view(request):
  form = ArticleForm()
  context={'form':form}
  print(request.POST)
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    category = request.POST.get('category')
    author = request.POST.get('author')
    date_published = request.POST.get('date_published')
    date_updated = request.POST.get('date_updated')
    article_obj = Article.objects.create(title=title, content=content, category=category, author=author, date_published=date_published, date_updated=date_updated)
    context = {
      'object': article_obj,
      'created': True
    }
  return render(request, 'core/create.html', context=context)


def search_view(request):
  query_dict = request.get

  try:
    query = int(query_dict.get('q'))
  except:
    query = None

  article_obj = None
  if query is not None:
    article_obj = Article.objects.get(id = query)

  context = {
    'objects':article_obj
  }
  return render(request, 'core/search.html', context=context)
