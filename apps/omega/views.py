from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from .models import User, Travel
from django.contrib import messages
from django.contrib.sessions.models import Session
import datetime
from django.utils.dateparse import parse_date
import bcrypt
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request,'omega/index.html')

def registerprocess(request):
	errors = False
	check1 = User.UserManager.first_name(request.POST['first_name'])
	check1_char = User.UserManager.first_name_charcheck(request.POST['first_name'])
	check2 = User.UserManager.last_name(request.POST['last_name'])
	check3 = User.UserManager.reg_email(request.POST['email'])
	check4 = User.UserManager.password(request.POST['password'])
    # check5 = User.UserManager.password(request.POST['password'])
	# check6 = Userlog.UserManager.birthday(request.POST['birthday'])
	# print request.POST['password']
	# print bcrypt.gensalt()
	check5 = User.UserManager.confirm_password(request.POST['password'] ,request.POST['confirm_password'])
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid firstname", extra_tags="regtag")
		errors = True
	if check1_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in firstname", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid lastname", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Email", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		print check4[1]
		errors = True
	if check5[0] == False:
		messages.add_message(request, messages.INFO, "Passwords don't match", extra_tags="regtag")
		errors = True
	# if check6[0] == False:
	# 	print check6[1]
	# 	messages.add_message(request, messages.INFO, "Invalid BirthDate", extra_tags="regtag")
	# 	errors = True
	# To check DB whether Email already registered or not....
	if User.objects.filter(email = request.POST['email']):
	    messages.add_message(request, messages.INFO, "This email already existed!", extra_tags="regtag")
	    errors = True
	# Errors Route
	if errors == True:
		return redirect('/')
	elif (check1[0] == True & check2[0] == True & check3[0] == True & check4[0] == True & check5[0] == True  ):
		user = User.UserManager.create(first_name=check1[1], last_name=check2[1], email=check3[1], password=check4[1])
		request.session['user'] = check1[1]
        # if user.id == 1:
        #     print user.id
        #     print "user" *10
        #     print user.user_level
        #     user.user_level = 9
        #     user.save()
        #     print user.user_level
	    # messages.add_message(request, messages.INFO, "Successfully Registered", extra_tags="regtag")
        return redirect('/travels')

#login process
def signinprocess(request):
	check7 = User.UserManager.log(request.POST['email'], request.POST['password'])
	if check7[0] == False:
		messages.add_message(request, messages.INFO, check7[1], extra_tags='logtag')
		print check7[1]
		return redirect('/')
	else:
		request.session['user'] = check7[1]
        # request.session['poker_id'] = check7[2]
        return redirect('/travels')

# Main page
def travels(request):
	# user = User.objects.get(id=id)
	context={
		'travels':Travel.objects.all(),
		# 'user' : User.objects.get(id=id)
	}

	return render(request, 'omega/travels.html', context)

def add(request):
	user = request.session['user']
	# id = request.session['id']
	print user
	print id
	# user = User.objects.get(id=id)
	return render(request,'omega/add.html')

def processadd(request):
	# user = User.objects.get(id=id)
	context = { 'id' : id}
	request.POST['start_date']
	print "date test "*10
	start_date = datetime.datetime.strptime(request.POST['start_date'], "%Y-%m-%d")
	end_date = datetime.datetime.strptime(request.POST['end_date'], "%Y-%m-%d")
	Travel.objects.create(destination=request.POST['destination'], description=request.POST['description'], start_date=start_date, end_date=end_date)
	return render(request, 'omega/travels.html', context)



def logout(request):
	del request.session['user']
	return render(request,'omega/index.html')
