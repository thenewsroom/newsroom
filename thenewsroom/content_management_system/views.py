# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from category.models import Category,SubCategory,Language
from advertisements.models import Advertisement, Advertiserdetails
static_url = "https://thenewsroom.co.in"

# Create your views here.

def home(request):
    categories = Category.objects.all()
    advet_content = Advertisement.objects.all()
    top_picks = Content.objects.filter(top_pick=True, status=2)[:5]
    sports_contents = Content.objects.filter(category__id=5, status=2).order_by('created_on')[:5]
    odisha_contents = Content.objects.filter(category__id=2, status=2).order_by('created_on')[:5]
    politics_contents = Content.objects.filter(category__id=3, status=2).order_by('created_on')[:5]
    economy_contents = Content.objects.filter(category__id=4, status=2).order_by('created_on')[:5]
    entertain_contents = Content.objects.filter(category__id=6, status=2).order_by('created_on')[:5]
    opinion_contents = Content.objects.filter(category__id=7, status=2).order_by('created_on')[:5]
    india_contents = Content.objects.filter(category__id=8, status=2).order_by('created_on')[:5]
    world_contents = Content.objects.filter(category__id=9, status=2).order_by('created_on')[:5]
    photos_contents = Content.objects.filter(category__id=10, status=2).order_by('created_on')[:5]
    try:
        content_dict = {"static_url": static_url, "top_picks": top_picks[1:], "top_picks1": top_picks[0],
                        "sports_contents": sports_contents[1:],
                        "sp1": sports_contents[0],"odisha_contents": odisha_contents,
                        "politics_contents": politics_contents[1:], "plc": politics_contents[0],"economy_contents": economy_contents,
                        "entertain_contents": entertain_contents,
                        "opinion_contents": opinion_contents, "indcon": india_contents[0], "india_contents": india_contents[1:],
                        "wrldc": world_contents[0], "world_contents": world_contents[1:],
                        "photos_contents": photos_contents}
        return render(request, 'newsroom/index.html', content_dict)
    except:
        return HttpResponse("publish at least 5 contents from each category.")

def category_content(request, category_name):
    print category_name
    #return HttpResponse('comming.')
    if category_name == 'photogallery':
        category_name = 'Photo/Video Gallery'
    try:
        category_name = category_name.title()
        cat_slug = Category.objects.get(name=category_name).id
    except Exception as e:
        return HttpResponse(str(e))
    advet_content = Advertisement.objects.all()
    contents = Content.objects.filter(category__id=cat_slug, status=2).order_by('created_on')[:10]
    trending_contents = Content.objects.filter(category__id=cat_slug, trending=True, status=2).order_by('created_on')[:10]
    not_miss_contents = Content.objects.filter(category__id=cat_slug, not_miss=True, status=2).order_by('created_on')[:10]
    print contents.values('id')
    return render(request, 'newsroom/category.html', {"static_url": static_url, "categ_contents": contents,
                                                      "trend_cont": trending_contents, "not_miss_cont": not_miss_contents,
                                                      "category_name": category_name})

def subcategory_content(request, subcategory_name):
    print subcategory_name
    #return HttpResponse('comming.')
    try:
        subcategory_name = subcategory_name.title()
        print subcategory_name
        subcat_slug = SubCategory.objects.get(name=subcategory_name).id
    except Exception as e:
        return HttpResponse(str(e))
    advet_content = Advertisement.objects.all()
    contents = Content.objects.filter(subcategory__id=subcat_slug, status=2).order_by('created_on')[:20]
    trending_contents = Content.objects.filter(subcategory__id=subcat_slug, trending=True, status=2).order_by('created_on')[:10]
    not_miss_contents = Content.objects.filter(subcategory__id=subcat_slug, not_miss=True, status=2).order_by('created_on')[:10]
    return render(request, 'newsroom/category.html', {"static_url": static_url, "categ_contents": contents,
                                                      "trend_cont": trending_contents, "not_miss_cont": not_miss_contents,
                                                      "category_name": subcategory_name})

def story(request, story_id):
    print story_id
    c = Content.objects.get(id=int(story_id))
    advet_content = Advertisement.objects.all()
    category_name = c.category.name
    cid = c.category.id
    trending_contents = Content.objects.filter(category__id=cid, trending=True, status=2).order_by(
        'created_on')[:10]
    not_miss_contents = Content.objects.filter(category__id=cid, not_miss=True, status=2).order_by(
        'created_on')[:10]
    #return HttpResponse('comming.')
    return render(request, 'newsroom/story.html', {"category_name": category_name, "static_url": static_url, "content":c,
                                                   "trend_cont": trending_contents, "not_miss_cont": not_miss_contents})

def commingsoon(request):
    return render(request, 'home/home.html', {})

def about_us(request):
    return render(request, 'newsroom/about-us.html', {})

def contact_us(request):
    return render(request, 'newsroom/contact-us.html', {})

def copright(request):
    return render(request, 'newsroom/copyright.html', {})

def disclaimer(request):
    return render(request, 'newsroom/disclaimer.html', {})



