from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post


def all_posts(request):
    page_number = request.GET.get('page')
    paginate_by = int(request.GET.get('per_page', 5))
    posts = Post.objects.all()
    paginator = Paginator(posts, paginate_by)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts.html', {'page_obj': page_obj})
