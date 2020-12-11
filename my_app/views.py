from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import FriendForm, FormData
from .models import Friend, Data


def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})


def postFriend(request):
    if request.is_ajax and request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)


from django.http import JsonResponse
from .models import Friend


def checkNickName(request):
    if request.is_ajax and request.method == "GET":
        nick_name = request.GET.get("nick_name", None)
        if Friend.objects.filter(nick_name=nick_name).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)
    return JsonResponse({}, status=400)


def data_view(request):
    # objects_all = Data.objects.all()
    # if request.method == 'POST':
    #     form = FormData(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('data save')
    #     else:
    #         return HttpResponse('please valid data')

    return render(request, 'data.html.j2', {'form': FormData()})


def get_data(request):
    return render(request, 'data.html.j2', {})
