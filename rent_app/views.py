from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect   
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import User, Iha, RentRecord
from .forms import IhaCreateUpdateForm, IhaUpdateForm, IhaRentForm
from .serializers import RentRecordListSerializer

class WelcomePageView(generic.TemplateView):
    template_name = 'rent/layout.html'

# this view list all the iha.
class HomePageView(generic.ListView):
    template_name = 'rent/homepage.html'
    model = Iha
    context_object_name ='iha'

# this view create user account.
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username,email,password)
            user.save()

        except IntegrityError:
            return render(request,"blog/register.html",{
                "message": "Username already taken."
            })
    return render(request,"rent/register.html")

# this view to login website.
@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        psw = request.POST["password"]

        user = authenticate(request,username=username,password=psw)

        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return render( request,"blog/login.html",{
                "message":"Invalid username and/or password."
            })

    return render(request, "rent/login.html")

# this view to logout website.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("layout"))

# this view to create another iha.
class IhaCreateView(CreateView):
    model = Iha
    form_class = IhaCreateUpdateForm
    template_name = 'rent/addIha.html'
    success_url = reverse_lazy('home-page')

# this view to update existing iha.
class IhaUpdateView(UpdateView):
    model = Iha
    form_class = IhaCreateUpdateForm
    template_name = 'rent/updateIha.html'
    success_url = reverse_lazy('home-page')

# this view to delete iha.
def iha_delete_view(request,id):
    posts = Iha.objects.get(id=id)
    posts.delete()
    return redirect("/home")

# this view to create rent record for iha.
class RentalRecordCreateView(CreateView):
    template_name = 'rent/createRent.html'
    form_class = IhaRentForm
    success_url = reverse_lazy('home-page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.initial['user_rent'] = self.request.user
        return form

# this view to rent list.
class RentRecordListView(generic.ListView):
    template_name = 'rent/rentRecord.html'
    model = RentRecord
    context_object_name ='rent_record'


class RentRecordApiV(ListAPIView):
    
    serializer_class = RentRecordListSerializer
    queryset = RentRecord.objects.all()




# this view to update rent.
class RentRecordUpdateView(UpdateView):
    model = RentRecord
    form_class = IhaRentForm
    template_name = 'rent/rentUpdate.html'
    success_url = reverse_lazy('rent-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.initial['user_rent'] = self.request.user
        form.fields['user_rent'].disabled = False
        return form
    
# this view to delete rent.
def rent_delete_view(request,id):
    posts = RentRecord.objects.get(id=id)
    posts.delete()
    return redirect("/rent")

# this view list to user's rent.
class UserRentRecordView(LoginRequiredMixin, generic.ListView):
    model = RentRecord
    template_name = 'rent/userRentList.html'
    success_url = reverse_lazy('home-page')
    context_object_name ='user_rent_record'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_rent=self.request.user)
    

