from django.shortcuts import redirect, render


def indexView(request):
    if request.user.is_authenticated:
        return redirect("menu:index")
    return render(request, "accounts/index.html")