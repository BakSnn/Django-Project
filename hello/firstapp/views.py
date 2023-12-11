from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person

# Получение данных из БД и загрузка index.html

def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people":people})
# Сохранение данных в БД
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.maker = request.POST.get("maker")
        klient.price = request.POST.get("price")
        klient.category = request.POST.get("category")
        klient.save()
    return HttpResponseRedirect("/")
# Изменение данных в БД
def edit(request,id):
    try:
        person = Person.objects.get(id = id)
        if request.method == "POST":
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.maker = request.POST.get('maker')
            person.price = request.POST.get('price')
            person.category = request.POST.get("category")
            person.save()
            return HttpResponseRedirect("/")
        else: return render(request, 'edit.html')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")

def delete(request,id):
    try:
        person = Person.objects.get(id = id)
        person.delete()

        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден </h2> ")


def home(request):
    return render(request,"home.html")


