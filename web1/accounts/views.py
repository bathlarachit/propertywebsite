from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
from accounts import forms
from accounts.models import LandBuy,LandSellModel
from accounts import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
class Home(TemplateView):
    template_name = 'accounts/index.html'

class About(TemplateView):
    template_name = 'accounts/about.html'
class LandList(ListView):
    model = models.LandBuy
    context_object_name = 'land_list'
class LandDetail(DetailView):
    model = models.LandBuy
    template_name = 'accounts/detail.html'
    context_object_name = 'land_detail'

class LandPost(LoginRequiredMixin,CreateView):
    fields = ('Property_name','location','image','discription','size')
    model = models.LandSellModel
    success_url =reverse_lazy('accounts:sell')
    def form_valid(self,form):
        form.instance.post_by=self.request.user
        return super(LandPost,self).form_valid(form)
class SellList(LoginRequiredMixin,ListView):
    context_object_name = 'user_sell_list'
    def get_queryset(self):
        return LandSellModel.objects.filter(post_by=self.request.user)
    template_name ='accounts/landsell_list.html'
class sellDetail(LoginRequiredMixin,DetailView):
    model=models.LandSellModel
    context_object_name='sell_detail'
    template_name='accounts/sell_detail.html'
class SellRequest(ListView):
    model=models.LandSellModel
    context_object_name='requests'
    template_name='accounts/requests.html'
class PostDelete(LoginRequiredMixin,DeleteView):
    model=models.LandSellModel
    success_url=reverse_lazy('accounts:requests')
    template_name='accounts/delete.html'
class BuyCreate(LoginRequiredMixin,CreateView):
        fields = ('name','location','image','discription','size')
        model = models.LandBuy
        success_url =reverse_lazy('accounts:buy')
        template_name='accounts/addbuy.html'
class BuyDelete(LoginRequiredMixin,DeleteView):
    model=models.LandBuy
    success_url=reverse_lazy('accounts:buy')
    template_name='accounts/buydelete.html'
