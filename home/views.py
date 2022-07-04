import imp
from socket import gethostbyname
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
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
from home.serlializers import UserSerializer
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
import json
from django.http import QueryDict
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# print(make_password('1234'))
# print(check_password('RMER@123','pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))
# print(is_password_usable('pbkdf2_sha256$320000$r7xFrXJulbruIFi6z804kW$0Dz1NCAn3ueJt+STWU/ju8B3ZNYtBzzQDZRb7io9sSU='))

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def resetpassword(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        # print(fm)
        if fm.is_valid(): 
            fm.save()
            # print('====================')
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/index')
    else:
        fm= PasswordChangeForm(user=request.user)
    return render(request, 'resetpassword.html',{'form':fm})
    # return render(request,'resetpassword.html')
    

def userpage(request):
    # if request.method =='POST':
       
        # uid=request.session.get('_auth_user_id')
        # # username=User.objects.get(pk=uid)
        # print("===========",uid)
       

        
        # username = username,
                
      
            
    
    return render(request,'userpage.html')

def videos(request):
    return render(request,'videos.html')



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
    users = User.objects.get(id=id)

    # template = loader.get_template('update')
    # context = {
    #     'mymember': mymember,
    # }
    # return HttpResponseRedirect(reverse('update'))
    return render(request,'update.html',{'mymember':mymember,'users':users})

def updaterecord(request, id):
    n = request.POST['name']
    u = request.POST['username']
    g = request.POST['gmail']
    p = request.POST['phone']
    # pas=make_password(request.POST['password'])
    a = request.POST['address']
    member = user.objects.get(id=id)
    member.name = n
    member.username = u
    member.gmail = g
    member.phone_number = p
    # member.password = pas
    member.address = a
    member.save()
    # **************************************************
    users = User.objects.get(id=id)
    users.name = n
    users.username = u
    users.gmail = g
    users.phone_number = p

    users.address = a
    users.save()
    return HttpResponseRedirect(reverse('demo'))



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
        u=request.POST['username']
        g=request.POST['email']
        a=request.POST['address']
        # c=request.POST['city']
        pas=make_password(request.POST['password'])
        # print("print==================")
        
        form =user()
        form.name=n   
        form.phone_number=p
        form.username=u
        form.gmail=g
        form.address=a
        # form.city=c
        form.password=pas
        # signup.password=make_password(signup.password)
        form.save()
        # *****************
        form =User()
        form.name=n   
        form.phone_number=p
        form.username=u
        form.gmail=g
        form.address=a
        # form.city=c
        form.password=pas
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

        user = authenticate(username=username, password=password)
        # print(user)
        print("================")
        if user is not None and len(password)>7:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/userpage')
        else:
            messages.warning(request, 'Invalid Credentials, Please try again')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/')
    else:
        pageView(request, True)
    return render(request,'login.html')

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
#   users = User.objects.get(id=id)
  member.delete()
#   users.delete()
  return HttpResponseRedirect(reverse('demo')) 


# ******************************Get Data******************************

# def checkout(request):
#     if request.method =='POST':
       
        
#         address=request.POST.get('address')
       
#         state=request.POST.get('state')
#         city=request.POST.get('city')
#         pincode=request.POST.get('pincode')
    
#         phone=request.POST.get('phone')

#         cart=request.session.get('cart')
#         uid=request.session.get('_auth_user_id')
#         username=User.objects.get(pk=uid)
#         print(cart,uid,username)
       

#         for i in cart:
#             a=((cart[i]['price']))
#             b=cart[i]['quantity']
#             total=a*b
#             # print(i)
#             Order=order(
#                 username = username,
                
#                 product_name=cart[i]['name'],
#                 product_price=cart[i]['price'],
#                 product_qty=cart[i]['quantity'],
#                 product_image=cart[i]['image'],
#                 address=address,
#                 pincode=pincode,
#                 number=phone,
#                 total=total,
#                 city=city,
#                 state=state,
#             )
           
#             Order.save()
          

            
#             messages.success(request, 'This is Checkout')
#         request.session['cart'] = {}
           

#         return redirect("index")
            
#     return render(request,'cart.html')




# ******************************admin******************************
# def loginuser(request):  
#     if request.method == 'POST':
#         pageView(request)
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username =username, password=password)
#         if user is not None and len(password)>7:
#             login(request, user)
#             messages.success(request, 'Successfully Logged In')
#             try:
#                 return redirect(request.GET.get('return'))
#             except:
#                 return redirect('demo')
#         else:
#             messages.warning(request, 'Invalid Credentials, Please try again')
#             try:
#                 return redirect(request.GET.get('return'))
#             except:
#                 return redirect('/')
#     else:
#         pageView(request, True)
#         return render(request, '404.html')

# def logoutUser(request):
#     if request.method == 'POST':
#         pageView(request)
#         logout(request)
#         messages.success(request, 'Successfully Logged Out')
#         try:
#             return redirect(request.GET.get('return'))
#         except:
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         pageView(request, True)
#         return render(request, '404.html')





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

    



@api_view(['POST'])
def add_items(request):
    try:
        data=dict(request.data)
        for i in data.keys():
            data[i]=data[i][0]
        # stream=io.BytesIO(json_data)
        try:
            data['phone_number']=int(data['phone_number'])
        except:
            pass

        

        # ordinary_dict = {'a': 'one', 'b': 'two', }
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)

        values = query_dict.dict()

        obj = user(**values)
        # print(data)
        if user.objects.filter(username=obj.username).exists():
            # if request.method =='POST':
        
                # ipa=request.POST['ipaddress']
                # maca=request.POST['macaddress']
            
                # # print("print==================")
                
                # form =user()
            
                # form.ipaddress=ipa
                # form.macaddress=maca
                
                
                # form.save()
                
                
            return JsonResponse({'Response':'This data already exists'})
        else:
            return JsonResponse({'Response':'data is not exists.'})
    except:
        return JsonResponse({'Response':'Please provide data'})

# @api_view(['POST'])
# def add_items(request):
#     item = UserSerializer(data=request.data)
  
#     # validating for already existing data
#     if user.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
  
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_items(request):
    if request.method == 'GET':
        tutorials = user.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = UserSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

# @api_view(['POST'])
# def update_items(request, pk):
	# item = user.objects.get(pk=pk)
	# data = UserSerializer(instance=item, data=request.data)

	# if data.is_valid():
	# 	data.save()
	# 	return Response(data.data)
	# else:
	# 	return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(user, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)


