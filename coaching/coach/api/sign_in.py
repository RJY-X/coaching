from django.shortcuts import render, redirect

def sign_in(request):
    
    return render(
        request,
        "coach/sign_in.html",
    
    )