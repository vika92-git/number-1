from django.shortcuts import render
from myapp.models import wear
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect


def index(request):
    name = request.session.get("is_auth", "Не авторизован")
    if name != "Не авторизован":
        res = wear.objects.all()
        if request.method == "POST":
            data = request.POST
            new = wear(name=data["field1"], cost=data["field2"],
                       description=data["field3"], size=data["field4"], count=data["field5"])
            new.save()

            return render(request, 'index.html', {"wear": res, "username": name})
        else:
            return render(request, 'index.html', {"wear": res,  "username": name})
    else:
        return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        data = request.POST
        newUser = User.objects.create_user(
            data["lgn"], data["eml"], data["psw"],)
        newUser.save()
        return HttpResponse(f'Пользователь {data["lgn"]} успешно создан')
    else:
        return render(request, "registr.html")


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(
            username=data["lgn"], password=data["psw"])
        if user is not None:
            request.session["is_auth"] = user.username
            return redirect(index)
            # return HttpResponse(f'Привет {user}')
        else:
            return HttpResponse(f"Неправильный пароль")
    else:
        return render(request, 'auth.html')


def card(request, wear_id):
    data = wear.objects.filter(id=wear_id)
    # print(data)
    if data:
        return render(request, "card.html", {"wear": data})
    else:
        return redirect(index)


def basket(request):
    # data = wear.objects.filter()
    return render(request, "basket.html")


def log_out(request):
    logout(request)
    return redirect(index)

# Create your views here.
