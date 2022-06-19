from django.shortcuts import redirect, render
from django.views import View


class FrontEventEditInputView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/edit/input.html", context)


class FrontEventEditDatePickView(View):
    def get(self, request):
        context = {}
        return render(request, "front/event/edit/date_pick.html", context)
