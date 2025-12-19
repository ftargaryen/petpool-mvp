from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Pet

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

# 4. Create Pet View (CRITICAL REQUIREMENT)
@login_required
def create_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        bio = request.POST.get('bio')
        Pet.objects.create(owner=request.user, name=name, species=species, bio=bio)
        return redirect('feed')
    return render(request, 'core/create_pet.html')

# 5. Social Feed & Post Creation
@login_required
def feed(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        if caption and image:
            Post.objects.create(author=request.user, caption=caption, image=image)
            return redirect('feed')
            
    posts = Post.objects.all().order_by('-created_at')
    user_pets = Pet.objects.filter(owner=request.user) # Keeps your sidebar working
    
    return render(request, 'core/feed.html', {
        'posts': posts,
        'user_pets': user_pets
    })