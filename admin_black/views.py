from django.shortcuts import render
from .models import Games
import matplotlib.pyplot as plt
from .utils import get_plot

# Create your views here.

def main_view(request):
    qs = Games.objects.all()
    x = [x.name for x in qs]
    y = [y.price for y in qs]
    #plt.plot(y, linestyle = 'dotted')
    #plt.show()
    chart = get_plot(x,y)
    return render(request, 'chart.html',{'chart': chart })