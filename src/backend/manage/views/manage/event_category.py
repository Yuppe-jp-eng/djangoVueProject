from django.template.response import TemplateResponse as render
from django.views import View

class AdminEventCategoryListView(View):
    def get(self, request):
        context = {"event_category_id": 1}
        return render(request, "manage/event_category/list.html", context)

class AdminEventCategoryCreateView(View):
    def get(self, request):
        context = {}
        return render(request, "manage/event_category/create.html", context)

class AdminEventCategoryDetailView(View):
    def get(self, request, id):
        context = {}
        return render(request, "manage/event_category/edit.html", context)

class AdminEventCategoryEditView(View):
    def get(self, request, id):
        context = {}
        return render(request, "manage/event_category/edit.html", context)
