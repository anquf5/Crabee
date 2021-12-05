
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, JsonResponse
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes



from .models import Company, CompanyReview
from rest_framework import authentication
from .serializers import CompanySerializer, CompanyListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class indexCompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.filter(on_index=1)
        if len(companies) > 6:
            companies = companies[:6]
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)


class CompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

    # get other companies
    def post(self, request, format=None):
        cid = request.data.get('company_id')
        companies = Company.objects.exclude(pk=cid)
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):
    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def add_review(request):

    # error info:
    # 1 - Lack of Parameter
    cid = request.data.get('cid')
    company = Company.objects.get(pk=cid)
    if request.user.id == None:
        request.user = User.objects.get(username="admin")

    review_obj = CompanyReview.objects.get_or_create(company=company, reviewer=request.user)[0]

    job = request.data.get('job')
    title = request.data.get('title')
    content = request.data.get('content')
    rate = request.data.get('rate')
    difficulty = request.data.get('difficulty')
    if (job != None) & (title!= None) & (content!=None) & (rate!=None) & (difficulty !=None):
        review_obj.job_title = job
        review_obj.review_title = title
        review_obj.review_cont = content
        review_obj.rate = rate
        if difficulty == 'Easy':
            review_obj.iv_difficulty = 0
        elif difficulty == 'Medium':
            review_obj.iv_difficulty = 1
        elif difficulty == 'Difficulty':
            review_obj.iv_difficulty = 2
        review_obj.save()
        return Response({'msg': 'OK'})
    else: return JsonResponse({'msg': 1})


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        companies = Company.objects.filter(Q(name__icontains=query))
        serializer = CompanyListSerializer(companies, many=True)
        print(serializer)
        return Response(serializer.data)
    else:
        return Response({"companies": []})