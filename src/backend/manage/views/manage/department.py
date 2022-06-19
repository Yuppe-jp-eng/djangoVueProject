from django.template.response import TemplateResponse as render
from django.views import View

class AdminDepartmentListView(View):
    def get(self, request):
        context = {"department_id": 1}
        return render(request, "manage/department/list.html", context)

class AdminDepartmentCreateView(View):
    def get(self, request):
        context = {}
        return render(request, "manage/department/create.html", context)

class AdminDepartmentEditView(View):
    def get(self, request, id):
        context = {}
        return render(request, "manage/department/edit.html", context)
