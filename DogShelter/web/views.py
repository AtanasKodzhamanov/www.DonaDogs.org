import datetime
from django.core import serializers
from django.shortcuts import render
import django.utils.translation
from DogShelter.web.models import Dog, NoticeBoard, About
from django.forms.models import model_to_dict

# Create your views here.

lang = django.utils.translation.get_language()
print(lang)


def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
    print(dataPeople)

    #dataDogs2 = Dog.objects.filter(status="Active")

    context = {
        "dataPeople": dataPeople,
        "dataDogs": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "index.html", context)


def show_infirmary(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))

    context = {
        "dataDogs": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "infirmary.html", context)


def show_about(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataAbout = serializers.serialize(
        'python', About.objects.all().order_by("order"))

    context = {
        "dataAbout": dataAbout,
        "dataNoticeBoard": dataNoticeBoard,
        "lang": lang
    }
    return render(request, "about.html", context)


def show_adoptions(request):
    dataDogs = serializers.serialize(
        'python', Dog.objects.all().order_by("-adoption_year"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))

    context = {
        "dataAdoptions": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "adoptions.html", context)


def show_donations(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("?"))
    dataAbout = serializers.serialize(
        'python', About.objects.all().order_by("order"))

    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
    print(dataPeople)

    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)

    context = {
        "last_month": last_month,
        "dataPeople": dataPeople,
        "dataAbout": dataAbout,

        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "donations.html", context)


def show_giftAdoption(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = serializers.serialize(
        'python', Dog.objects.all().exclude(va_name_eng=""))

    # return list of virtual adopters

    #ip = request.META.get('REMOTE_ADDR', None)

    context = {
        # "ip": ip,

        "dataPeople": dataPeople,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "giftadoption.html", context)


#dataDogs = serializers.serialize('python', Dog.objects.all())
#dataNoticeBoard = serializers.serialize('python', NoticeBoard.objects.all())
# print(dataDogs)

# for instance in dataDogs:
#    print("INSTANCE")
#   print(instance)
#  print(instance["fields"]["nameENG"])

#dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
#dataPeople = serializers.serialize('python', People.objects.all().order_by("?"))


# for instance in dataDogs:
    # print(instance)
    # print(instance["fields"]["person"])
    # id=instance["fields"]["person"]
    # print(dataPeople["id"==id]["fields"]["person_name_eng"])
    # print(dataPeople)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]

    else:
        ip = request.META.get('REMOTE_ADDR')
