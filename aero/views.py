import datetime

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from aero.forms import PostForm

trains = {
    'mon': (('1', '18:00'), ('2', '19:15')),
    'tue': (('3', '10:15'), ('4', '11:30'), ('5', '19:30')),
    'wen': (('6', '11:15'), ('7', '18:00'), ('8', '19:15')),
    'thu': (('9', '18:00'),('10', '19:15')),
    'fri': (('11', '10:15'), ('12', '11:30'), ('13', '19:30')),
    'sat': ('14', '12:15'),
}

menu = [{'title':"ЦЕНЫ", 'url_name': 'price'},
        {'title': "РАСПИСАНИЕ", 'url_name': 'schedule'},
        {'title': "ЗАПИСАТЬСЯ", 'url_name': 'book'},
        ]

images = [
          {'name': 'studio2', 'url': 'static/aero/images/studio2.jpg'},
          {'name': 'studio5', 'url': 'static/aero/images/studio5.jpg'},
          {'name': 'studio3', 'url': 'static/aero/images/studio3.jpg'},
          {'name': 'studio6', 'url': 'static/aero/images/studio6.jpg'},
          {'name': 'studio4', 'url': 'static/aero/images/studio4.jpg'},
          {'name': 'studio1', 'url': 'static/aero/images/studio1.jpg'},
          ]

def calendar():
    today = datetime.datetime.now()
    week = {}
    for i in range(7):
        date = (today+datetime.timedelta(days=i))
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
    return week

def index(request):
    return render(request, 'aero/index.html', {'menu': menu, 'title': 'Аэроплан', 'images': images})

def price(request):
    return render(request, 'aero/price.html', {'menu': menu, 'title': 'Цены',})

def schedule(request):
    return render(request, 'aero/schedule.html', {'menu': menu, 'title': 'Расписание',})

def book(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['soname'], form.cleaned_data['tel'],
                         form.cleaned_data['train_mon'], form.cleaned_data['train_tue'], form.cleaned_data['train_wed'],
                         form.cleaned_data['train_thu'], form.cleaned_data['train_fri'], form.cleaned_data['train_sat'])
            return render(request, 'aero/success.html', {'form': form, 'menu': menu, 'title': 'aeroplan', 'images': images, 'week': calendar()})
    else:
        form = PostForm()
        return render(request, 'aero/form.html', {'form': form, 'menu': menu, 'title': 'aeroplan', 'images': images, 'week': calendar()})

def send_message(name, soname, tel, train_mon, train_tue, train_wed, train_thu, train_fri, train_sat):
    trains = 'Запись: '
    if train_mon == '1':
        trains += 'Понедельник, 18:00/'
    elif train_mon == '2':
        trains += 'Понедельник, 19:15/'
    if train_tue == '3':
        trains += 'Вторник, 10,15/'
    elif train_tue == '4':
        trains += 'Вторник, 11:30/'
    elif train_tue == '5':
        trains += 'Вторник, 19:30/'
    if train_wed == '6':
        trains += 'Среда, 11:15/'
    elif train_wed == '7':
        trains += 'Среда, 18:00/'
    elif train_wed == '8':
        trains += 'Среда, 19:15/'
    if train_thu == '9':
        trains += 'Четверг, 18:00/'
    elif train_thu == '10':
        trains += 'Четверг, 19:15/'
    if train_fri == '11':
        trains += 'Пятница, 10:15/'
    elif train_fri == '12':
        trains += 'Пятница, 11:30/'
    elif train_fri == '13':
        trains += 'Пятница, 19:30/'
    if train_sat == '14':
        trains += 'Суббота, 12:15/'

    text = get_template('aero/message.html')
    html = get_template('aero/message.html')
    subject = 'Сообщение с сайта'
    context = {'name': name, 'soname': soname, 'tel': tel, 'trains': trains}
    from_email = 'from@gmail.com'
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['andrew.mahnach@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    # msg.send()