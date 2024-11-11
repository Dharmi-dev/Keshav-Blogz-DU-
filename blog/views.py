from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm
from django.contrib import messages

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 9  # Show 9 posts per page

def home(request):
    """
    Home page view showing featured posts and latest content
    """
    # Get latest posts for the featured section
    latest_posts = Post.objects.all()[:6]  # Limit to 6 posts for the grid
    
    context = {
        'posts': latest_posts,
        'featured_post': latest_posts.first() if latest_posts else None,
    }
    return render(request, 'home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })