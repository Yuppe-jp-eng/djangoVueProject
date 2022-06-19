from django.template.response import TemplateResponse as render
from django.views import View

class AdminUserListView(View):
    def get(self, request):
        context = {}
        return render(request, "manage/user/list.html", context)
