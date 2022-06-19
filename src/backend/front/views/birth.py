from django.shortcuts import redirect, render
from django.views import View


class FrontBrithCategoryListView(View):
    def get(self, request):
        context = {}
        return render(request, "front/birth/category_list.html", context)


class FrontBirthGeneralGuideView(View):
    def get(self, request):
        context = {}
        return render(request, "front/birth/general_guide.html", context)


class FrontBrithToDoListView(View):
    def get(self, request):
        context = {}
        return render(request, "front/birth/todo_list.html", context)
