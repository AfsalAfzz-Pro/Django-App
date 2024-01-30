from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_control
from django.db.models import Q
from django.db import connection



@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def AdminPage(request):
    if request.user.is_authenticated:   
        if request.user.is_superuser:
            print('user is in')
            if request.method == 'POST':
                search_word = request.POST.get('search_box', '')
                record = User.objects.filter(Q(username__icontains = search_word)| Q(email__icontains=search_word)).order_by('id').values()
                print('request passed')
                print('SQL Query:', str(connection.queries[-1]['sql']))
                print(connection.queries)
                # print(record)
            else:
                record = User.objects.all().order_by('id').values()
                print('you are gonna see no change')
               
                
            dict1 = {'val1':record}
            return render(request, 'admin.html',context=dict1)
        
        else:
            return redirect('login')
    return redirect('login')
    


        # print(user)
    # if user.is_superuser:
    #     print('superuser is in')
    #     return redirect('Admin') 
    # elif user is not None and not user.is_superuser:
    #     print(' you are correct ')
    #     login(request, user)
    #     return redirect('home')



# here lied
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def Add(request):
    print('hi there')  
    if request.user.is_superuser:
        print('hey bro')
        if request.user.is_authenticated:
            print('your task was executed succesfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            if request.method == 'POST':
                print('heloooo')
                uname1 = request.POST.get('username')
                email1 = request.POST.get('email')
                pass1 = request.POST.get('password1')
                my_user1 = User.objects.create_user(uname1,email1,pass1)
                my_user1.save()
                print('its working bro')
                return redirect('Admin')

        
        return render(request, 'add.html')

    else:
        return redirect('home')
        # return HttpResponse("You must be logged in")
    # return redirect('login')


        


def customer_record(request, id):
    if request.user.is_authenticated:
        customer_record = User.objects.get(id=id)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        return HttpResponse("You must be logged in")
        return redirect('Admin')



def delete_record(request, id):
    delete_it = User.objects.get(id=id)
    delete_it.delete()
    return redirect('Admin')


# def update_record(request, id):
#     customer_record = User.objects.get(id=id)
#     if request.method == 'POST':
#                 print('heloooo')
#                 uname1 = request.POST.get('username')
#                 email1 = request.POST.get('email')
#                 pass1 = request.POST.get('password1')
#                 my_user1 = User.objects.create_user(uname1,email1,pass1)
#                 my_user1.save()
#                 return redirect('login')
#     # context = {'customer_record':customer_record}
#     # print(context)
#     return render(request, 'edit.html', {'customer_record':customer_record})


def update_record(request, id):
    # Fetch the existing user record
    customer_record = User.objects.get(id=id)

    if request.method == 'POST':
        # Get updated data from the form
        uname1 = request.POST.get('username')
        email1 = request.POST.get('email')
        pass1 = request.POST.get('password1')

        # Update the existing user record
        customer_record.username = uname1
        customer_record.email = email1
        customer_record.set_password(pass1)  # Set the password securely

        # Save the updated user record
        customer_record.save()

        return redirect('login')

    # Pass the existing user record to the template
    return render(request, 'edit.html', {'customer_record': customer_record})


# def search(request):
#     if request.user.is_authenticated:
#         print('123')
#         if request.method == 'POST':
#             print('boom success!')
#             usernme = request.POST.get('search')
#             dict2 = {'val1':usernme}
#             return render(request, 'search.html',context=dict2)
        