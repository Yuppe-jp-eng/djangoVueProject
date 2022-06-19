from django.shortcuts import redirect, render
from django.views import View


class FrontPasswordReminderRequestView(View):
    def get(self, request):
        context = {}
        return render(request, "front/entrance/password_reminder/request.html", context)


class FrontPasswordReminderInputView(View):
    def get(self, request):
        context = {}
        return render(request, "front/entrance/password_reminder/input.html", context)


class FrontPasswordReminderCompleteView(View):
    def get(self, request):
        context = {}
        return render(request, "front/entrance/password_reminder/complete.html", context)
