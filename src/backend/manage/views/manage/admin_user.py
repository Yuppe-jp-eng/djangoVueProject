from django.template.response import TemplateResponse as render
from django.views import View


class AdminAdminUserCreateView(View):
    def get(self, request):
        context = {}
        return render(request, "manage/admin_user/create.html", context)

class AdminAdminUserEditView(View):
    def get(self, request, id):
        context = {"admin_user_id": id}
        return render(request, "manage/admin_user/edit.html", context)

class AdminAdminUserListView(View):
    def get(self, request):
        context = {"admin_user_id": 1}
        return render(request, "manage/admin_user/list.html", context)

