# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Content
from category.models import Category,SubCategory,Language
from advertisements.models import Advertisement, Advertiserdetails
static_url = "https://thenewsroom.co.in"

# Create your views here.

def home(request):
    categories = Category.objects.all()
    advet_content = Advertisement.objects.all()
    top_picks = Content.objects.filter(top_pick=True)[:5]
    sports_contents = Content.objects.filter(category__id=5).order_by('created_on')[:5]
    odisha_contents = Content.objects.filter(category__id=2).order_by('created_on')[:5]
    politics_contents = Content.objects.filter(category__id=3).order_by('created_on')[:5]
    economy_contents = Content.objects.filter(category__id=4).order_by('created_on')[:5]
    entertain_contents = Content.objects.filter(category__id=6).order_by('created_on')[:5]
    opinion_contents = Content.objects.filter(category__id=7).order_by('created_on')[:5]
    india_contents = Content.objects.filter(category__id=8).order_by('created_on')[:5]
    world_contents = Content.objects.filter(category__id=9).order_by('created_on')[:5]
    photos_contents = Content.objects.filter(category__id=10).order_by('created_on')[:5]
    content_dict = {"static_url": static_url, "top_picks": top_picks[1:], "top_picks1": top_picks[0],
                    "sports_contents": sports_contents[1:],
                    "sp1": sports_contents[0],"odisha_contents": odisha_contents,
                    "politics_contents": politics_contents[1:], "plc": politics_contents[0],"economy_contents": economy_contents,
                    "entertain_contents": entertain_contents,
                    "opinion_contents": opinion_contents, "indcon": india_contents[0], "india_contents": india_contents[1:],
                    "wrldc": world_contents[0], "world_contents": world_contents[1:],
                    "photos_contents": photos_contents}
    print len(top_picks[1:]), len(top_picks)
    return render(request, 'newsroom/index.html', content_dict)
