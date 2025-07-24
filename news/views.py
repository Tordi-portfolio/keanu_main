from django.shortcuts import render

# Create your views here.
def more(request):
    return render(request, 'more.html')


from django.shortcuts import render, get_object_or_404
from .models import NewsPost

def news_list(request):
    posts = NewsPost.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'posts': posts})

def news_details(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'news_details.html', {'post': post})
