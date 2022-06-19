from django.template.response import TemplateResponse as render
from django.views import View

class AdminEntranceLoginView(View):
    def get(self, request):
        context = {}
        return render(request, "manage/entrance/login.html", context)
