import datetime
from django import forms

today = datetime.datetime.now()
week = {}
for i in range(7):
    date = (today + datetime.timedelta(days=i))
    if date.strftime('%w') == '0':
        day = 'Вс'
    elif date.strftime('%w') == '1':
        day = 'Пн'
    elif date.strftime('%w') == '2':
        day = 'Вт'
    elif date.strftime('%w') == '3':
        day = 'Ср'
    elif date.strftime('%w') == '4':
        day = 'Чт'
    elif date.strftime('%w') == '5':
        day = 'Пт'
    elif date.strftime('%w') == '6':
        day = 'Сб'
    num = date.day
    month = date.month
    if month == 1:
        month = 'янв'
    elif month == 2:
        month = 'фев'
    elif month == 3:
        month = 'мар'
    elif month == 4:
        month = 'апр'
    elif month == 5:
        month = 'мая'
    elif month == 6:
        month = 'июня'
    elif month == 7:
        month = 'июля'
    elif month == 8:
        month = 'авг'
    elif month == 9:
        month = 'сен'
    elif month == 10:
        month = 'окт'
    elif month == 11:
        month = 'ноя'
    elif month == 12:
        month = 'дек'

    date = str(num) + month
    if day != 'Вс':
        week[day] = date

trains = {
    'mon': (('0', ''), ('1', '18:00'), ('2', '19:15')),
    'tue': (('0', ''), ('3', '10:15'), ('4', '11:30'), ('5', '19:30')),
    'wen': (('0', ''), ('6', '11:15'), ('7', '18:00'), ('8', '19:15')),
    'thu': (('0', ''), ('9', '18:00'), ('10', '19:15')),
    'fri': (('0', ''), ('11', '10:15'), ('12', '11:30'), ('13', '19:30')),
    'sat': (('0', ''), ('14', '12:15'))
}


class PostForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=25, widget=forms.TextInput(attrs={'class': 'form-input'}))
    soname = forms.CharField(min_length=2, max_length=25, widget=forms.TextInput(attrs={'class': 'form-input'}))
    tel = forms.CharField(min_length=9, max_length=12, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '29-XXX-XX-XX'}))

    train_mon = forms.ChoiceField(choices=trains['mon'])
    train_tue = forms.ChoiceField(choices=trains['tue'])
    train_wed = forms.ChoiceField(choices=trains['wen'])
    train_thu = forms.ChoiceField(choices=trains['thu'])
    train_fri = forms.ChoiceField(choices=trains['fri'])
    train_sat = forms.ChoiceField(choices=trains['sat'])
