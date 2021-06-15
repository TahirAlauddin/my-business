from services.forms import Adjournment, CaseFiling
from django.contrib import admin
from .models import (SCCopy,HCCopy,LCCopy,
                    CM, CaseFiling, Adjournment,
                    ServicesListModel)

admin.site.register(ServicesListModel)     
admin.site.register(SCCopy)
admin.site.register(HCCopy)
admin.site.register(LCCopy)
admin.site.register(CM)
admin.site.register(CaseFiling)
admin.site.register(Adjournment)

