from django.shortcuts import redirect, render
from django.views import View


class FrontUserInfoDetailView(View):
    def get(self, request):
        context = {}
        return render(request, "front/user/user_info/detail.html", context)
