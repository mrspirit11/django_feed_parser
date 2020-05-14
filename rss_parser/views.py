from django.shortcuts import render
import rss_parser
from datetime import date, timedelta

# Create your views here.
def index(request):

    context = rss_parser()
    return render(request, 'rss_parser/index.html', context)