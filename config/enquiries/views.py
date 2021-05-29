from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Enquiries

""" Enquiries View """


class SubmitEnquiries(View):
    template_name = 'enquiries/submit-enquiries.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            Enquiries.objects.create(
                name=request.POST.get('name'),
                number=request.POST.get('number'),
                email=request.POST.get('email'),
                enquiry=request.POST.get('enquiry'),
            )
            messages.success(request, 'Successfully submitted an enquiry')
            return redirect('submit-enquiry')
        except:
            messages.warning(request, 'Something went wrong whilst submitting your enquiry, please try again')
            return redirect('submit-enquiry')


""" View Enquiries View """


class ViewEnquiries(ListView):
    model = Enquiries
    template_name = 'enquiries/view-enquiries.html'


""" Home View """


class Home(TemplateView):
    template_name = 'enquiries/home.html'


""" Services View """


class Services(TemplateView):
    template_name = 'enquiries/services.html'
