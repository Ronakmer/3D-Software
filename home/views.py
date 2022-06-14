import imp
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
from .models import signup
from django.contrib.auth.hashers import make_password,check_password,is_password_usable
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from home.serlializers import signupSerializer
from rest_framework import status

# print(make_password('1234'))
# print(check_password('RMER@123','pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))
# print(is_password_usable('pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))

# Create your views here.

def index(request):
    return render(request,'index.html')


def nav(request):
    mymembers = signup.objects.all()
    # template = loader.get_template('index.html')
    # context = {
    # '   mymembers': mymembers,
    # }
    return render(request,'nav.html',{'mymembers':mymembers})

def signupuser(request):

    if request.method =='POST':
        f=request.POST['name']
        p=request.POST['phone']
        # u=request.POST['username']
        g=request.POST['email']
        a=request.POST['address']
        # c=request.POST['city']
        # p=make_password(request.POST['pass1'])
        # print("print==================")
        
        form =signup()
        form.name=f   
        form.phone_number=p
        # form.user_name=u
        form.gmail=g
        form.address=a
        # form.city=c
        # form.password=p
        # signup.password=make_password(signup.password)
        form.save()
        
        # print(a,c)
        
    return HttpResponseRedirect(reverse('nav'))

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
  member = signup.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('nav')) 






# {
#         "id": 4,
#         "name": "ronak",
#         "city": "rajkot",
#         "number": "232232323",
#         "age": "12"
#     }

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
	item = signupSerializer(data=request.data)


	if signup.objects.filter(**request.data).exists():
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
        tutorials = signup.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = signupSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

@api_view(['POST'])
def update_items(request, pk):
	item = signup.objects.get(pk=pk)
	data = signupSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(signup, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
