from django.shortcuts import render
from event import models
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.utils import timezone

# 勉強
def study(request):
    all_st = models.Study.objects.order_by("-id").all()
    all_kyouka = models.kyouka.objects.all()
    dct1 = {"all_st":all_st, "all_kyouka":all_kyouka}
    return render(request, "event/study.html", dct1)

def kyouka_henshuu(request):
    all_kyouka = models.kyouka.objects.all()
    dct = {"all_kyouka":all_kyouka}
    return render(request, "event/kyouka.html", dct)

def kyouka_shoukyo(request, event_id):
    event  = models.kyouka.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("event:kyouka_henshuu"))

def kyouka_tuika(request):
    kyouka = request.POST.get("text")
    if kyouka == "" or kyouka == None:
        return render(request, "event/kyouka.html")
    sv = models.kyouka(kyouka=kyouka)
    sv.save()
    return HttpResponseRedirect(reverse("event:kyouka_henshuu"))

def study_save1(request):
    s = request.POST.get("btoodtype")
    t_h = request.POST.get("hhh")
    t_m = request.POST.get("mmm")
    t  = t_h + ":" + t_m
    m = request.POST.get("memo")
    created = request.POST.get("kiroku")
    tb_name = None
    peji1 = None
    peji2 = None
    sv = models.Study(subject=s, time=t, memo=m, textbook_name=tb_name, peji1=peji1, peji2=peji2, created=created)
    sv.save()
    return HttpResponseRedirect(reverse("event:study"))

def study_save2(request):
    s = request.POST.get("btoodtype")
    tb_n = request.POST.get("textbook_name")
    peji1 = request.POST.get("peji1")
    peji2 = request.POST.get("peji2")
    m = request.POST.get("memo")
    c = request.POST.get("kiroku")
    if peji1 == "" :
        peji1 = 00
    if peji2 == "" :
        peji2 = 00
    time = None
    if tb_n == "" or tb_n == None:
        tb_n = "記録なし"
    sv = models.Study(subject=s, time=time, textbook_name=tb_n, peji1=peji1, peji2=peji2, memo=m, created=c)
    sv.save()
    return HttpResponseRedirect(reverse("event:study"))


def study_shousai(request, event_id):
    event = models.Study.objects.get(id=event_id)
    dct = {"event":event}
    return render(request, "event/study_shousai.html", dct)

def modoru_study(request):
    return HttpResponseRedirect(reverse("event:study"))

# 日記
def diary(request):
    all_di = models.diary.objects.order_by("-id").all()
    dct = {"all_di":all_di}
    return render(request, "event/diary.html", dct)

def diary_save(request):
    date = request.POST.get("date")
    tenki1 = request.POST.get("tenki1")
    tenki2 = request.POST.get("tenki2")
    title = request.POST.get("title")
    text = request.POST.get("text")
    hitokoto = request.POST.get("hitokoto")
    sonohoka = request.POST.get("sonohoka")
    if date == "" or date == None:
        date = datetime.date.today()
    sv = models.diary(tenki1=tenki1, tenki2=tenki2, date=date, title=title,text=text, hitokoto=hitokoto, sonohoka=sonohoka)
    sv.save()
    return HttpResponseRedirect(reverse("event:diary"))

def diary_shousai(request, event_id):
    event = models.diary.objects.get(id=event_id)
    dct = {"event":event}
    return render(request, "event/diary_shousai.html", dct)

def modoru_diary(request):
    return HttpResponseRedirect(reverse("event:diary"))


# 夢日記
def dd(request):
    all_dd = models.dd.objects.order_by("-id").all()
    dct = {"all_dd":all_dd}
    return render(request, "event/dream_diary.html", dct)

def dd_save(request):
    date = request.POST.get("date")
    title = request.POST.get("title")
    jinbutu = request.POST.get("jinbutu")
    text = request.POST.get("text")
    kansou = request.POST.get("kansou")
    if date == "" or date == None:
        date = datetime.date.today()
    sv = models.dd(date=date, title=title, jinbutu=jinbutu, text=text, kansou=kansou)
    sv.save()
    return HttpResponseRedirect(reverse("event:dd"))

def dd_shousai(request, event_id):
    event = models.dd.objects.get(id=event_id)
    jinbutu = event.jinbutu.split()
    dct = {"event":event, "jinbutu":jinbutu}
    return render(request, "event/dream_diary_shousai.html", dct)

def modoru_dd(request):
    return HttpResponseRedirect(reverse("event:dd"))

# タバコ
def smoke(request):
    all_sm = models.smoke.objects.order_by("-id").all()
    dct = {"all_sm":all_sm}
    return render(request, "event/smoke.html", dct)

def smoke_save(request):
    date = datetime.date.today()
    name = request.POST.get("name")
    mg = request.POST.get("mg")
    honn = request.POST.get("honn")
    memo = request.POST.get("memo")
    sv = models.smoke(date=date, name=name, mg=mg, honn=honn, memo=memo)
    sv.save()
    return HttpResponseRedirect(reverse("event:smoke"))

def smoke_shousai(request, event_id):
    event = models.smoke.objects.get(id=event_id)
    dct = {"event":event}
    return render(request, "event/smoke_shousai.html", dct)

def modoru_smoke(request):
    return HttpResponseRedirect(reverse("event:smoke"))


# ダイエット
def diet1(request):
    all_dt = models.diet.objects.order_by("-id").all()
    dct = {"all_dt":all_dt}
    return render(request, "event/diet1.html", dct)

def diet2(request):
    all_eat = models.eat.objects.order_by("-id").all()
    dct = {"all_eat":all_eat}
    return render(request, "event/diet2.html", dct)

def diet_save(request):
    date = request.POST.get("date")
    height = request.POST.get("height")
    kg = request.POST.get("kg")
    age = request.POST.get("age")
    play = request.POST.get("play")
    t_h = request.POST.get("hhh")
    t_m = request.POST.get("mmm")
    t  = t_h + ":" + t_m
    t_m = request.POST.get("mmm")
    t  = t_h + ":" + t_m
    if date == "" or date == None:
        date = datetime.date.today()

    if height == "" or height == None or kg == "" or kg == None :
        height = 0
        kg = 0
        age = 0
        bmi = "計測できませんでした"
    else:
        height = int(height)
        kg = int(kg)
        h = float(height / 100) ** 2
        bmi = kg / h
        bmi = round(bmi, 2)
    sv = models.diet(date=date, height=height, kg=kg, age=age, bmi=bmi, play=play, time=t)
    sv.save()
    return HttpResponseRedirect(reverse("event:diet1"))

def diet_shousai(request, event_id):
    event = models.diet.objects.get(id=event_id)
    dct = {"event":event}
    return render(request, "event/diet_shousai.html", dct)

def modoru_diet(request):
    return HttpResponseRedirect(reverse("event:diet1"))


def eat_save(request):
    eat = request.POST.get("eat")
    eat_time = request.POST.get("eat_time")
    eating = request.POST.get("eating")
    if eat_time == "" or None:
        eat_time = timezone.localtime()
    if eat == "朝ごはん":
        sv = models.eat(morning=eating, eat_time=eat_time)
    elif eat == "昼ごはん":
        sv = models.eat(lunch=eating, eat_time=eat_time)
    elif eat == "夜ごはん":
        sv = models.eat(dinner=eating, eat_time=eat_time)
    elif eat == "そのほか":
        sv = models.eat(sonohoka=eating, eat_time=eat_time)
    sv.save()
    return HttpResponseRedirect(reverse("event:diet2"))

def eat_shousai(request, e_id):
    event = models.eat.objects.get(id=e_id)
    dct = {"event":event}
    return render(request, "event/eat_shousai.html", dct)