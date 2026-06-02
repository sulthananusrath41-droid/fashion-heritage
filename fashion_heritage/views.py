from django.shortcuts import render

# Create your views here.
from .models import Gown, Comment, Like, Save, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    gowns = Gown.objects.all()
    return render(request, "fashion_heritage/index.html", {
        "gowns": gowns
    })

def gown_detail(request, gown_id):
    gown = Gown.objects.get(id=gown_id)
    comments = Comment.objects.filter(gown=gown)
    return render(request, "fashion_heritage/gown_detail.html", {
        "gown": gown,
        "comments": comments
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))   
        else:
            return render(request, "fashion_heritage/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "fashion_heritage/login.html")     
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "fashion_heritage/register.html", {
                "message": "Passwords must match."
            })
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "fashion_heritage/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "fashion_heritage/register.html")
    
@login_required
def like_gown(request, gown_id):
    if request.method == "POST":
        gown = Gown.objects.get(id=gown_id)
        like_exists = Like.objects.filter(
            user=request.user,
            gown=gown
        ).exists()

        if like_exists:
            Like.objects.filter(
                user=request.user,
                gown=gown
            ).delete()
            liked = False
        else:
            Like.objects.create(
                user=request.user,
                gown=gown
            )
            liked = True

        return JsonResponse({
            "liked": liked,
            "likes_count": gown.likes.count()
        }, status=200)
        
@login_required
def save_gown(request, gown_id):
    if request.method == "POST":
        gown = Gown.objects.get(id=gown_id)
        save_exists = Save.objects.filter(
            user=request.user,
            gown=gown
        ).exists()

        if save_exists:
            Save.objects.filter(
                user=request.user,
                gown=gown
            ).delete()
            saved = False
        else:
            Save.objects.create(
                user=request.user,
                gown=gown
            )
            saved = True

        return JsonResponse({
            "saved": saved,
        }, status=200)
        
def saved_gowns(request):
    saves = Save.objects.filter(user=request.user)
    return render(request, "fashion_heritage/saved_gowns.html", {
        "saves": saves
    })

def add_comment(request, gown_id):
    gown = Gown.objects.get(id=gown_id)
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(
            author=request.user,
            gown=gown,
            content=content
        )
        return HttpResponseRedirect(reverse("gown_detail", args=[gown_id]))
    
def search(request):
    query = request.GET.get("q")
    gowns = Gown.objects.filter(
        Q(name__icontains=query) |
        Q(country_of_origin__icontains=query)|
        Q(era__icontains=query)
    )
    return render(request, "fashion_heritage/search.html", {
        "gowns": gowns,
        "query": query
    })