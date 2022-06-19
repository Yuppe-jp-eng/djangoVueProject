from django.template.response import TemplateResponse as render
from django.views import View


class AdminBookingDetailView(View):
    def get(self, request, id):
        context = {}
        return render(request, "manage/booking/detail.html", context)

class AdminBookingListView(View):
    def get(self, request):
        context = {"booking_id": 1}

        return render(request, "manage/booking/list.html", context)
