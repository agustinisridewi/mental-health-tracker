from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306276004',
        'name': 'Agus Tini Sridewi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)