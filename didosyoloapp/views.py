from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import africastalking

# Initialize Africa's Talking
africastalking.initialize(
    settings.AFRICASTALKING_USERNAME,
    settings.AFRICASTALKING_API_KEY
)


@csrf_exempt
def home(request):
    if request.method == 'POST':
        session_id = request.POST.get("session_id")
        service_code = request.POST.get("service_code")
        phone_number = request.POST.get("phone_number")
        text = request.POST.get("text", "")

        response = ""

        if text == "":
            response = "CON 99)Triple Data Promo :\n"
            response += "0) Gwamo\n"
            response += "1)Yolo guhamagara\n"
            response += "2)Yolo Internt\n"
            response += "3)Izindi Bundle\n"
            response += "4)Desade\n"
            response += "5)Ayo usigaranye\n"
            response += "6)Foleva\n"
            response += "7)Ihereze\n"
            response += "8)Yolo star\n"
            response += "n Next\n"

     


        elif text =="0":
            response = "CON \n"
            response += "1)1000 RWF = 800 Mins +20SMS\n"
            response += "2)1000 RWF = 7GB + 30 30SMS\n"
            response += "3)500 RWF = 700 Mins + 30SMS\n"
            response += "4)Gwamon's Weekend\n"
            response += "0)Subira inyuma\n"

        elif text =="0*1":
            response = "CON Ishyura 1500FRW= (8GB+800Mins)+30SMS ukoresheje:\n"
            response += "1)Inite\n"
            response += "2)Momo\n"
            response += "2)Gusubira Inyuma\n"

           



        elif text =="1":
            response = "CON Irangira Kucyueru 23:59 \n"
            response += "1)100 RWF = 50 Mins +20SMS/24hrs\n"
            response += "2)200 RWF = 250 Mins + 20SMS/24hrs\n"
            response += "3)500 RWF = 800 Mins + 20SMS/Iminsi 7\n"
            response += "4)2000 RWF = 4000 Mins + 100SMS/Iminsi 30\n"
            response += "5)Desade\n"
            response += "5)n Next\n"
        
        elif text =="2":
            response = "CON  \n"
            response += "1)Umunsi(24hrs)\n"
            response += "2)Icyumeru\n"
            response += "3)Desade\n"
            response += "4)Buriaha\n"
            response += "5)Bundle za social Media(24hrs)\n"
            response += "0)n Gusubira Inyuma\n"
        
        elif text =="3":
            response = "CON  \n"
            response += "1)100RWF=100MB/24hrs\n"
            response += "2)500RWF=500MB/Icyumeru\n"
            response += "3)1000RWF=800MB/Ukwezi\n"
            response += "4)Desade\n"
            response += "0)n Gusubira Inyuma\n"
        
        elif text =="4":
            response = "CON Desade irangira ki munsi wa 2 saa 23:59\n"
            response += "1)200 RWF = 200 Mins +200SMS/Iminsi 2\n"
            response += "2)200 RWF = 200MBs + 200SMS/Iminsi 2\n"
            response += "2)200 RWF = 100Mins + 100MBs/Iminsi 2\n"
            response += "n Next\n"

        elif text =="5":
            response = "END Irekure 100rwf Secs:1500,SMS:20 EXP:2025-10-03 17:30:03\n"


        
            
        
            



        return HttpResponse(response, content_type="text/plain")

    return HttpResponse("Welcome to Home.")
