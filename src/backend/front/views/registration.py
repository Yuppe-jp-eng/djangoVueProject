from django.shortcuts import redirect, render
from django.views import View


class FrontRegistrationInputView(View):
    def get(self, request):
        context = {}
        return render(request, "front/entrance/registration/input.html", context)
