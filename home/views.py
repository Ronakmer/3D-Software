import imp
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
from .models import signup,user
from django.contrib.auth.hashers import make_password,check_password,is_password_usable
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from home.serlializers import userSerializer
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer


# print(make_password('1234'))
# print(check_password('RMER@123','pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))
# print(is_password_usable('pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))

# Create your views here.

def index(request):
    return render(request,'index.html')

def demo(request):
    mymembers = user.objects.all()
    # template = loader.get_template('index.html')
    # context = {
    # '   mymembers': mymembers,
    # }
    
    return render(request,'demo.html',{'mymembers':mymembers})
    # return render(request,'demo.html')

def update(request, id):
    mymember = user.objects.get(id=id)
    # template = loader.get_template('update.html')
    context = {
      'mymember': mymember,
    }
    # return HttpResponseRedirect(reverse('update'))
    # return HttpResponse(template.render(context, request))



def nav(request):
    mymembers = user.objects.all()
    # template = loader.get_template('index.html')
    # context = {
    # '   mymembers': mymembers,
    # }
    return render(request,'nav.html',{'mymembers':mymembers})

def signupuser(request):

    if request.method =='POST':
        n=request.POST['name']
        p=request.POST['phone']
        # u=request.POST['username']
        g=request.POST['email']
        a=request.POST['address']
        # c=request.POST['city']
        # p=make_password(request.POST['pass1'])
        # print("print==================")
        
        form =user()
        form.name=n   
        form.phone_number=p
        # form.user_name=u
        form.gmail=g
        form.address=a
        # form.city=c
        # form.password=p
        # signup.password=make_password(signup.password)
        form.save()
        
        # print(a,c)
        
    return HttpResponseRedirect(reverse('demo'))

def pageView(request, isError=False):
    # Page View Counter
    pass 


def loginuser(request):  
    if request.method == 'POST':
        pageView(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username, password=password)
        if user is not None and len(password)>7:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/')
        else:
            messages.warning(request, 'Invalid Credentials, Please try again')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/')
    else:
        pageView(request, True)
        return render(request, '404.html')

def logoutUser(request):
    if request.method == 'POST':
        pageView(request)
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        try:
            return redirect(request.GET.get('return'))
        except:
            return HttpResponseRedirect(reverse('index'))
    else:
        pageView(request, True)
        return render(request, '404.html')   

def delete(request, id):
  member = user.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('demo')) 

# def update(request, id):
#     mymember = signup.objects.get(id=id)
#     # template = loader.get_template('update.html')
#     # context = {
#         # 'mymember': mymember,
#     # }
#     return render(request,'nav.html',{'mymember':mymember})




# {
# "name":"jayu",
# "phone_number":"123456",
# "gmail":"roakmwer@gmail.com",
# "address":"dfsfsfs"


# }

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer     




@api_view(['POST'])
def add_items(request):
	item = userSerializer(data=request.data)


	if user.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer 



@api_view(['GET'])
def view_items(request):
    if request.method == 'GET':
        tutorials = user.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = userSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

@api_view(['POST'])
def update_items(request, pk):
	item = user.objects.get(pk=pk)
	data = userSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(user, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)



# @csrf_exempt
# def student_details(request):
#     stu=signup.objects.get()
#     serializer=signupSerializer(stu)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)

# def student_create(request):
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=signupSerializer(data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data Inserted"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method=="PUT":
#         json_data = request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=signup.objects.get(id=id)
#         serializer= signupSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Updated'}
#             json_data= JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data= JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method=="DELETE":
#          json_data = request.body
#          stream=io.BytesIO(json_data)
#          pythondata=JSONParser().parse(stream)
#          id=pythondata.get('id')
#          stu=signup.objects.get(id=id)
#          stu.delete()
#          res={'msg':'Data Deleted'}
#          json_data=JSONRenderer().render(res)
#          return HttpResponse(json_data,content_type='applicaton/json')

# def view_items(request):
#     if request.method == 'GET':
#         tutorials = signup.objects.all()
        
#         title = request.query_params.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = signupSerializer(tutorials, many=True)
#         return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)