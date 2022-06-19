from django.template.response import TemplateResponse as render
from django.views import View

class AdminDashboardView(View):
    def get(self, request):

        context = {}
        return render(request, "manage/dashboard.html", context)
