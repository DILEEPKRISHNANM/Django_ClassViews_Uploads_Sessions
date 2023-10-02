from django.shortcuts import render

# Create your views here.

from django.views import View

from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserImage
from django.views.generic import ListView
from django.views.generic.edit import CreateView





# def store_file(file):
#     with open("temp/image.jpg","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

# class CreateView(View):


#     form = ProfileForm()


#     def get(self,request):
#         form = ProfileForm()
#         return render(request,"profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self,request):
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
#             profile = UserImage(user_image=request.FILES["user_Image"])
#             profile.save()
#         #store_file(request.FILES['image'])
#             return HttpResponseRedirect('/profiles')

#         else:
#             return render(request,"profiles/create_profile.html",{
#             "form":form
#         })






class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserImage
    fields = "__all__"
    success_url = "/profiles"


# To Work with images u need to set ImageField in th model and install some packages
# python3 -m pip install pillow




class ProfilelistView(ListView):
    model = UserImage
    template_name= "profiles/profile_listing.html"
    context_object_name = "profiles"
