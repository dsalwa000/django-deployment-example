from django.shortcuts import render

# Create your views here.
def view(request):
    context = {
        'variable': 1
    }
    return render(request, 'index.html', context=context)

