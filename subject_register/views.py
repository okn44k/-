from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Subject,Option
from .forms import VoteForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import logging

class IndexView(FormView):
    template_name = 'subject_register/index.html'
    form_class = VoteForm
    success_url = 'index'

    def get_form_kwargs(self,*args,**kwargs):
        kwgs = super().get_form_kwargs(*args,**kwargs)
        products = Option.objects.values_list('title',flat=True)
        choice_ls = [(product,product) for product in products]
        kwgs['categories'] = choice_ls
        return kwgs

    def form_valid(self,form):
        message = f"{form.cleaned_data['choice']}"
        context = {'form':form,'msg':message}
        for f in form.cleaned_data['choice']:
            logging.debug(Option.objects.filter(title=f))
            logging.debug(f)
        return render(self.request,self.template_name,context)
