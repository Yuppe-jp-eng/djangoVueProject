from django.shortcuts import redirect, render
from django.views import View


class FrontLoginView(View):
    def get(self, request):
        context = {}
        return render(request, "front/entrance/login.html", context)


class FrontLogoutView(View):
    def get(self, request):
        return redirect("apps:front_login")
