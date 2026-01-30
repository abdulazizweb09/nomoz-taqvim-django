# from django.shortcuts import render
# import requests
# from datetime import date
# # Create your views here.
# def home(request):
#     today = date.today()
#     year = today.year
#     month = today.month
#     print('today-',today,'year-',year,'month-',month)
#     manzil='Fergana'
#     if request.method=='POST':
#         manzil=request.POST.get('manzil')


#     # data=requests.get(f"https://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={manzil}&country=Uzbekistan")
#     data = requests.get(f"https://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={manzil}&country=Uzbekistan&method=2")
#     data=data.json()
#     data=data['data']

#     # if data :
        
#     context={
#         'data':data
#     }

#     return render(request,'index.html',context)


from django.shortcuts import render
import requests
from django.utils import timezone

def home(request):
    today_date = timezone.localdate()
    year = today_date.year
    month = today_date.month

    city = "Fergana"


    if request.method == "POST":
        city = request.POST.get("manzil") or "Fergana"

    
    url = f"https://api.aladhan.com/v1/calendarByCity/{year}/{month}"
    params = {
        "city": city,
        "country": "Uzbekistan",
        "method": 3,   
    }

    response = requests.get(url, params=params)
    data = response.json()["data"]

    context = {
        "data": data,
        "today": today_date.strftime("%d-%m-%Y"),
        "city": city,
    }

    return render(request, "index.html", context)
