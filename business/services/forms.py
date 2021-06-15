from django import forms



with open('Districts.txt') as districts_file:
    city_list = districts_file.read()
    # List of districts
    city_list = city_list.split('\n')



class Copies(forms.Form):
    label= 'Urgent Delivery (within 3 days)'
    label_suffix = 'Note: It will charge extra 500(Rs)'
    case_no = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    pucca = forms.DateField()
    kuccha = forms.DateField()
    judge = forms.CharField(max_length=255)
    judge2 = forms.CharField(max_length=255)
    judge3 = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    district = forms.ChoiceField(choices=city_list)
    urgent = forms.BooleanField(label_suffix=label_suffix, label=label)


class CM:
    case_no = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    pucca = forms.DateField()
    kuccha = forms.DateField()
    judge = forms.CharField(max_length=255)
    lawyer = forms.CharField(max_length=255) 
    detail = forms.CharField(widget=forms.Textarea)



class CaseFiling:
    pages = forms.IntegerField(max_value=500)
    address = forms.CharField(max_length=255)
    stamps = forms.IntegerField(max_value=10)



class Adjournment:
    pass
#     title = 
#     judge =
#     case_no = 
#     date = 





