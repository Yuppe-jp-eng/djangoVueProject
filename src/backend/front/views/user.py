from django.shortcuts import redirect, render
from django.views import View


class FrontMyPageView(View):
    def get(self, request):
        context = {}
        return render(request, "front/user/mypage.html", context)
