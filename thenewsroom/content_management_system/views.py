# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from category.models import Category,SubCategory,Language
from advertisements.models import Advertisement, Advertiserdetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
static_url = "https://thenewsroom.co.in"

# Create your views here.

def home(request):
    top_picks = Content.objects.filter(top_pick=True, status=2).order_by('-published_date')[:5]
    sports_contents = Content.objects.filter(category__id=5, status=2).order_by('-published_date')[:5]
    odisha_contents = Content.objects.filter(category__id=2, status=2).order_by('-published_date')[:5]
    politics_contents = Content.objects.filter(category__id=3, status=2).order_by('-published_date')[:5]
    economy_contents = Content.objects.filter(category__id=4, status=2).order_by('-published_date')[:5]
    entertain_contents = Content.objects.filter(category__id=6, status=2).order_by('-published_date')[:5]
    opinion_contents = Content.objects.filter(category__id=7, status=2).order_by('-published_date')[:5]
    india_contents = Content.objects.filter(category__id=8, status=2).order_by('-published_date')[:5]
    world_contents = Content.objects.filter(category__id=9, status=2).order_by('-published_date')[:5]
    photos_contents = Content.objects.filter(category__id=10, status=2).order_by('-published_date')[:5]
    try:
        ad1url,ad1img,ad2url,ad2img,ad3url,ad3img = '','','','','',''
        ad1 = Advertisement.objects.filter(id=2,active=True,is_category=False, subcateg=False)
        if ad1:
            ad1url = ad1[0].link
            ad1img = static_url + ad1[0].image.url
        ad2 = Advertisement.objects.filter(id=3,active=True,is_category=False, subcateg=False)
        if ad2:
            ad2url = ad2[0].link
            ad2img = static_url + ad2[0].image.url
        ad3 = Advertisement.objects.filter(id=4,active=True,is_category=False, subcateg=False)
        if ad3:
            ad3url = ad3[0].link
            ad3img = static_url + ad3[0].image.url
    except:
        pass
    try:
        content_dict = {"static_url": static_url, "top_picks": top_picks[1:], "top_picks1": top_picks[0],
                        "sports_contents": sports_contents[1:],
                        "sp1": sports_contents[0],"odisha_contents": odisha_contents,
                        "politics_contents": politics_contents[1:], "plc": politics_contents[0],"economy_contents": economy_contents,
                        "entertain_contents": entertain_contents,
                        "opinion_contents": opinion_contents, "indcon": india_contents[0], "india_contents": india_contents[1:],
                        "wrldc": world_contents[0], "world_contents": world_contents[1:],
                        "photos_contents": photos_contents, "ad1url": ad1url, "ad1img": ad1img,"ad2url": ad2url,"ad2img": ad2img,
                        "ad3url": ad3url,"ad3img": ad3img}
        return render(request, 'newsroom/index.html', content_dict)
    except Exception as e:
        return HttpResponse(str(e))

def category_content(request, category_name):
    page = request.GET.get('page', 1)
    if category_name == 'photogallery':
        category_name = 'Photo/Video Gallery'
    try:
        category_name = category_name.title()
        cat_slug = Category.objects.get(name=category_name).id
    except Exception as e:
        return HttpResponse(str(e))
    contents = Content.objects.filter(category__id=cat_slug, status=2).order_by('-published_date')[:100]
    paginator = Paginator(contents, 20)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    trending_contents = Content.objects.filter(category__id=cat_slug, trending=True, status=2).order_by('-published_date')[:30]
    not_miss_contents = Content.objects.filter(category__id=cat_slug, not_miss=True, status=2).order_by('-published_date')[:30]
    try:
        ad1url, ad1img = '', ''
        ad1 = Advertisement.objects.filter(id=5, active=True, is_category=True, subcateg=False)
        if ad1:
            ad1url = ad1[0].link
            ad1img = static_url + ad1[0].image.url
    except:
        pass
    return render(request, 'newsroom/category.html', {"static_url": static_url, "categ_contents": contents,
                                                      "trend_cont": trending_contents, "not_miss_cont": not_miss_contents,
                                                      "category_name": category_name,"ad1url": ad1url, "ad1img": ad1img})

def subcategory_content(request, subcategory_name):
    page = request.GET.get('page', 1)
    #return HttpResponse('comming.')
    try:
        subcategory_name = subcategory_name.title()
        subcat_slug = SubCategory.objects.get(name=subcategory_name).id
    except Exception as e:
        return HttpResponse(str(e))
    advet_content = Advertisement.objects.filter(active=True, is_category=False, subcateg=True)
    contents = Content.objects.filter(subcategory__id=subcat_slug, status=2).order_by('-published_date')[:100]
    paginator = Paginator(contents, 20)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    trending_contents = Content.objects.filter(subcategory__id=subcat_slug, trending=True, status=2).order_by('-published_date')[:30]
    not_miss_contents = Content.objects.filter(subcategory__id=subcat_slug, not_miss=True, status=2).order_by('-published_date')[:30]
    try:
        ad1url, ad1img = '', ''
        ad1 = Advertisement.objects.filter(id=6, active=True, is_category=False, subcateg=True)
        if ad1:
            ad1url = ad1[0].link
            ad1img = static_url + ad1[0].image.url
    except:
        pass
    return render(request, 'newsroom/category.html', {"static_url": static_url, "categ_contents": contents,
                                                      "trend_cont": trending_contents, "not_miss_cont": not_miss_contents,
                                                      "category_name": subcategory_name,"ad1url": ad1url, "ad1img": ad1img})

def story(request, story_id):
    print story_id
    firstpara = ""
    secondpara = ""
    thirdpara = ""
    c = Content.objects.get(id=int(story_id))
    advet_content = Advertisement.objects.filter(active=True, story=True)
    category_name = c.category.name
    cid = c.category.id
    try:
        body = c.body_html
        splitcont = body.split('.')
        if not len(splitcont) % 3 == 0:
            for i in range(10):
                count = len(splitcont) + 1
                if count % 3 == 0:
                    break
        else:
            count = len(splitcont)
        fcont = count / 3
        scount = fcont * 2

        firstpara = '.'.join(splitcont[:fcont])
        secondpara = '.'.join(splitcont[fcont:scount])
        thirdpara = '.'.join(splitcont[scount:])
    except:
        firstpara = body[:100]
        secondpara = body[100:300]
        thirdpara = body[300:]

    trending_contents = Content.objects.filter(category__id=cid, trending=True, status=2).order_by(
        '-published_date')[:30]
    not_miss_contents = Content.objects.filter(category__id=cid, not_miss=True, status=2).order_by(
        '-published_date')[:30]
    try:
        ad1url, ad1img = '', ''
        ad1 = Advertisement.objects.filter(id=7, active=True, story=True)
        if ad1:
            ad1url = ad1[0].link
            ad1img = static_url + ad1[0].image.url
    except:
        pass
    return render(request, 'newsroom/story.html', {"category_name": category_name, "static_url": static_url, "content":c,
                                                   "trend_cont": trending_contents, "not_miss_cont": not_miss_contents,
                                                   'firstpara':firstpara, 'secondpara':secondpara, 'thirdpara':thirdpara,
                                                   "ad1url": ad1url, "ad1img": ad1img})

def commingsoon(request):
    return render(request, 'home/home.html', {})

def PhotoGallery(request):
    photocontents = Content.objects.filter(status=2).order_by('-published_date')[:50]
    images = []
    for img in photocontents:
        if img.image:
            images.append(static_url + img.image.url)
        if img.story_image1:
            images.append(img.story_image1)
        if img.story_image2:
            images.append(img.story_image2)
    category_name = 'Photo/Video Gallery'
    trending_contents = Content.objects.filter(trending=True, status=2).order_by('-published_date')[
                        :30]
    not_miss_contents = Content.objects.filter(not_miss=True, status=2).order_by('-published_date')[
                        :30]
    return render(request, 'newsroom/photo.html',
                  {"static_url": static_url,"category_name": category_name, 'image_contents': images, "trend_cont": trending_contents,
                   "not_miss_cont": not_miss_contents, 'img_actv': images[0]})

def top_picks(request):
    page = request.GET.get('page', 1)
    contents = Content.objects.filter(top_pick=True, status=2).order_by('-published_date')[:100]
    paginator = Paginator(contents, 20)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    trending_contents = Content.objects.filter(trending=True, status=2).order_by(
        '-published_date')[:30]
    not_miss_contents = Content.objects.filter(not_miss=True, status=2).order_by(
        '-published_date')[:30]
    category_name = 'Top Picks'
    try:
        ad1url, ad1img = '', ''
        ad1 = Advertisement.objects.filter(id=5, active=True, is_category=True, subcateg=False)
        if ad1:
            ad1url = ad1[0].link
            ad1img = static_url + ad1[0].image.url
    except:
        pass
    return render(request, 'newsroom/category.html', {"static_url": static_url, "categ_contents": contents,
                                                      "trend_cont": trending_contents,
                                                      "not_miss_cont": not_miss_contents,
                                                      "category_name": category_name,"ad1url": ad1url, "ad1img": ad1img})

def about_us(request):
    return render(request, 'newsroom/about-us.html', {})

def contact_us(request):
    return render(request, 'newsroom/contact-us.html', {})

def copright(request):
    return render(request, 'newsroom/copyright.html', {})

def disclaimer(request):
    return render(request, 'newsroom/disclaimer.html', {})



