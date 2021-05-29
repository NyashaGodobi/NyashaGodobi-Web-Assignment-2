from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('submit-enquiry/', SubmitEnquiries.as_view(), name='submit-enquiry'),
    path('view-enquiries/', ViewEnquiries.as_view(), name='view-enquiries'),
    path('services/', Services.as_view(), name='services'),
]
