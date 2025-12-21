from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Pet, Comment
from django.db.models import Q

# 1. Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# 2. Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

# 3. Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# 4. Create Pet View
@login_required
def create_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        bio = request.POST.get('bio')
        Pet.objects.create(owner=request.user, name=name, species=species, bio=bio)
        return redirect('feed')
    return render(request, 'core/create_pet.html')

# 5. Social Feed
@login_required
def feed(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        if caption and image:
            Post.objects.create(author=request.user, caption=caption, image=image)
            return redirect('feed')
            
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(caption__icontains=query) | 
            Q(author__username__icontains=query)
        ).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
        
    user_pets = Pet.objects.filter(owner=request.user) 
    return render(request, 'core/feed.html', {
        'posts': posts,
        'user_pets': user_pets,
        'search_query': query
    })

# 6. AJAX Like View (Instagram Style)
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'count': post.likes.count()})

# 7. Add Comment View
@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('feed')