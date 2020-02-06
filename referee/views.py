from django.shortcuts import render

def referees(request):
    context = {}
    return render(request, 'referees.html', context)

