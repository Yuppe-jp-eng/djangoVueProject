from django.shortcuts import redirect, render
from django.views import View


class FrontRemarkContactView(View):
    def get(self, request):
        context = {}
        return render(request, "front/remark/contact.html", context)


class FrontRemarkPrivacyView(View):
    def get(self, request):
        context = {}
        return render(request, "front/remark/privacy.html", context)


class FrontRemarkTermsView(View):
    def get(self, request):
        context = {}
        return render(request, "front/remark/terms.html", context)
