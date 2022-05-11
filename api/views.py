from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from api.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from web.models import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth.models import User
from web.views import month_timer, bill_receipt_creation


# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        data = request.data
        try:
            user = User.objects.create_user(
                username=data.get("username"),
                email=data.get("email"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                password=data.get("password")
            )
            user.save()
            person = Person.objects.create(
                user=user,
                name=data.get('first_name') + data.get("last_name"),
                type=AccountType.objects.get(id=2)
            )
            person.save()
            serializer = PersonSerializer(person, many=False)
            pk = user.id
            bill_receipt_creation(pk)
            timer = MonthTimer.objects.create(
                person=person
            )
            timer.save()
            return Response({
                'data': serializer.data,
                'error': 'False'
            })
        except Exception as error:
            return Response({
                "data": str(error),
                "error": "True"
            })


class LoginView(APIView):
    def post(self, request):
        data = request.data
        uname = data.get("username")
        pwd = data.get("password")
        try:
            user = User.objects.get(username=uname)
            month_timer(user.id)

            if user.check_password(pwd) is True:
                person = Person.objects.get(user_id=user.id)
                serializer = PersonSerializer(person, many=False)
                return Response({
                    "data": serializer.data
                })
            else:
                return Response({
                    "data": "Worng Password"
                })
        except Exception as error:
            return Response({
                "data": str(error)
            })


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class BillReceiptViewSet(ModelViewSet):
    queryset = BillReceipt.objects.all()
    serializer_class = BillReceiptSerializer
    permission_classes = [IsAuthenticated]