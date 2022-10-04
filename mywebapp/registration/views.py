from django.shortcuts import render,redirect
from django.views import View
from.models import User
from .forms import AddUserForm
# Create your views here.
class Home(View):
    def get(self,request):
        user_data=User.objects.all()
        return render(request,'registration/home.html',{'userdata':user_data})

class Add_User(View):
    def get(self,request):
        fm= AddUserForm()
        return render(request,'registration/add-user.html',{'form':fm})

    def post(self,request):
        fm=AddUserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'registration/add-user.html',{'form':fm})

class Delete_User(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        userdata=User.objects.get(id=id)
        userdata.delete()
        return redirect('/')


class EditUser(View):
    def get(self,request,id):
        usier=User.objects.get(id=id)
        fm= AddUserForm(instance=usier)
        return render(request,'registration/edit-user.html',{'form':fm})

    def post(self,request,id):
        usier=User.objects.get(id=id)
        fm= AddUserForm(request.POST,instance=usier)
        if fm.is_valid():
            fm.save()
            return redirect('/')

