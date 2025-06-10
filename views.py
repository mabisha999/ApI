import json
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.http import JsonResponse
from .models import News
from .models import Image
def geeks_home(request):
    now= datetime.datetime.now()
    html="Time is {}".format(now)
    return HttpResponse(html)
def geeks_page2(request):
    data1={
        'name':'divya',
        'accountNumber':2346612234,
        'balance':20000
    };
    response= HttpResponse(json.dumps(data1), content_type='application/json')
    return response
def geeks_page1(request):
    data=[{
        'name': 'GeeksforGeeks',
        'startedIn': 2007,
        'city': 'noida'

    },{
        'name': 'santhiya',
        'age': 10,
        'city': 'chennai'

    },{
        'name': 'kumaran',
        'age': 12,
        'city': 'mumbai'

    }];
    m={
        'name': 'kumaran',
        'age': 12,
        'city': 'mumbai'

    }
    print(m)
    m['age']=34
    print(m)
    
    data[1]['age']="23"
    data[0]['name']="gelbero"
   
    response= HttpResponse(json.dumps(data), content_type='application/json')
    return response


@csrf_exempt
def Api3( request):
    json_data = json.loads(request.body.decode('utf-8'))
    a=request.body
    title=json_data['title']
    url=json_data['url']
    caption=json_data['caption']
    post = Post.objects.create(title=title, url=url, caption=caption)
    return HttpResponse('ok')
def Api4(request):
    posts = Post.objects.all()
    data = []

    for post in posts:
        post_data = {
            'title': post.title,
            'url': post.url,
            'caption': post.caption}
        data.append(post_data)
    return JsonResponse(data, safe=False)
def Api5(request):
    newsdata = News.objects.all()
    data = []

    for news in newsdata:
         news_data ={
            'title': news.title,
            'date' : news.day,
            'month': news.month,
            'year': news.year,
            'description' : news.description}

         data.append(news_data)
    return JsonResponse(data,safe = False)
def Gallery(request):
    images= Image.objects.all()
    data = []

    for image  in images:
         image_data= {
            'url': image.url}

         data.append(image_data)
    return JsonResponse(data,safe = False)
    

