from django.shortcuts import render
from .models import Previous
from faker import Faker
import random
import requests


# Create your views here.

def index(request):
    return render(request, 'previous/index.html')

def result(request):
    fake = Faker()
    name = request.GET.get('name')
    # DB에 이름이 있으면,  
    previous = Previous.objects.filter(name=name).first() # 첫번쨰 값 가져와라 object가 있는 쿼리셋을 주는것이기 때문에
    # DB에 이름이 없으면,
    if not previous:
        age = random.randint(1,100)
        job = fake.job()
        previous = Previous(age=age, job=job, name=name)
        previous.save()

    # 직업 결과에 따라, giphy 요청
    job = previous.job
    from decouple import config
    api_key = config('GIPHY_API_KEY')
    # 1. url 설정
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
    # 2. 요청 보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'previous' : previous,
        'image_url' : image_url
    }
    return render(request, 'previous/result.html', context)
    

