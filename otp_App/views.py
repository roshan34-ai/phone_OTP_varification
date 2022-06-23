from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomeUserSerializer, varifyAccountSerializer
from rest_framework import status
import random
from django.conf import settings
from twilio.rest import Client


# Create your views here.
class UserRegister(APIView):

    def post(self, request):
        serializer = CustomeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone = serializer.data['phone']
            client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
            otp = random.randint(1000, 9999)
            request.session['otp']=otp
            message = client.messages.create(
                                    body = f"Hii there, Your OTP is {otp}",
                                    from_ = '+19807059672',
                                    to = phone
                                    )
            user_obj = CustomUser.objects.get(phone=phone) 
            # user_obj.otp=otp
            user_obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def login(request):

    serializer = varifyAccountSerializer(data=request.data)

    if serializer.is_valid():
        phone = serializer.data['phone']
        otp = serializer.data['otp']
        print(type(otp))

        user = CustomUser.objects.filter(phone = phone)
        if not user.exists():
            return Response({
                        'status':400,
                        'message':'Something went wrong',
                        'data':'Invalid phone number'
                        })

        user = user.first() 
        s_otp = request.session.get('otp')
        print(type(s_otp))  
        if str(s_otp) != otp:
            return Response({'status':400,
                        'message':'Something went wrong',
                        'data':'Invalid otp'
                        })         
        user.is_varified = True
        user.save()
        return Response({'status':200,
                    'message':'phone Varified',
                    })  

    return Response({'status':200,
                    'message':'Pleaze enter phone and otp',
                    })   



