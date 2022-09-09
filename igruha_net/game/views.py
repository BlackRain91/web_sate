from django.shortcuts import render


def farthest_frontier(request):
    return render(request, 'game/farthest_frontier.html')


def snow_runner(request):
    return render(request, 'game/snow_runner.html')
