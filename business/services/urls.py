from django.urls import path
from .views import (SC_Copies_View, HC_Copies_View, about,
                    LC_Copies_View, Adjournment_View, help,
                    CM_View, Case_Filing_View, ServicesListView)


urlpatterns = [
    path('', ServicesListView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('help/', help, name='help'),
    path('sc_copies/', SC_Copies_View, name='sc_copies'),
    path('hc_copies/', HC_Copies_View, name='hc_copies'),
    path('lc_copies/', LC_Copies_View, name='lc_copies'),
    path('adjournment/', Adjournment_View, name='adjournment'),
    path('cm/', CM_View, name='cm'),
    path('case_filing/', Case_Filing_View, name='case_filing'),
        
]