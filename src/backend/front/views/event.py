from django.shortcuts import redirect, render
from django.views import View


class FrontEventDetailView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/detail.html", context)


class FrontEventDatePickView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/date_pick.html", context)


class FrontEventInputPickView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/input.html", context)


class FrontEventConfirmView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/confirm.html", context)


class FrontEventCompleteView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/complete.html", context)
