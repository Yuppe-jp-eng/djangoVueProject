import os
import re
import hashlib
from calendar import monthrange
from datetime import timedelta, date, datetime, time
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, Page
from django.utils.translation import activate, gettext as _, get_language
from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import DataError


def get_monday_of_the_week(day: date):
    monday = day - timedelta(days=day.weekday())
    return monday


def is_same_week(day1: date, day2: date):
    monday1 = get_monday_of_the_week(day1)
    monday2 = get_monday_of_the_week(day2)
    return monday1 == monday2


def get_start_time_setting():
    delta = settings.DELTA_MINUTES
    if settings.HEAD_START_TIME >= settings.LAST_START_TIME or settings.LAST_START_TIME + delta > settings.HEAD_START_TIME + timedelta(days=1):
        raise ImportError("The given start time is invalid.")
    if (settings.LAST_START_TIME - settings.HEAD_START_TIME) % delta:
        raise ImportError("The given delta minutes is invalid.")
    return settings.HEAD_START_TIME, settings.LAST_START_TIME, delta


def get_midnight(day: date):
    return datetime.combine(day, time())


def get_first_booking_from_time(today: date = date.today()):
    from_days = timedelta(days=settings.FIRST_BOOKING_FROM_DAYS)
    from_time = get_midnight(today) + from_days
    return from_time


def handle_uploaded_file(dir_path, file_obj):
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, file_obj.name)
    with open(file_path, "wb+") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)


def get_page_info(request, data_list, limit=100):
    def get_page_numbers(page: Page, total_num_of_page=5):
        result = [page.number]
        for i in range(1, total_num_of_page):
            if len(result) >= total_num_of_page:
                break

            prev = min(result) - 1
            if prev > 0:
                result = [prev] + result

            next_ = max(result) + 1
            if next_ <= page.paginator.num_pages:
                result.append(next_)

            if prev <= 0 and next_ > page.paginator.num_pages:
                break

        return result[:total_num_of_page]

    paginator = Paginator(data_list, limit)
    try:
        page = paginator.get_page(request.GET.get("p", 1))
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)
    page_numbers = get_page_numbers(page)

    page_info = {
        "paginator": paginator,
        "page": page,
        "page_numbers": page_numbers,
    }
    return page_info


def get_first_date(dt):
    return dt.replace(day=1)


def get_last_date(dt):
    return dt.replace(day=monthrange(dt.year, dt.month)[1])


def make_week_context(all_frames, display_date, filter_start, error_message):
    previous_week = display_date - timedelta(days=7)
    next_week = display_date + timedelta(days=7)
    context = {
        "frames": all_frames,
        "previous_week": previous_week.strftime("%Y%m%d") if filter_start <= previous_week or is_same_week(filter_start, previous_week) else None,
        "next_week": next_week.strftime("%Y%m%d"),
        "error_message": error_message,
    }
    return context


def send_sms(phone_number: str, message: str):
    if settings.USE_SMS:
        sns = settings.BOTO3_SESSION.client("sns")
        if len(message) > 70:
            raise Exception("70文字以内のメッセージを設定してください")
        if not re.match(r"^0[0-9]{9,10}$", phone_number):
            raise Exception("不正な電話番号です")
        phone_number = f"+81{phone_number[1:]}"
        sns.publish(
            PhoneNumber=phone_number,
            Message=message,
            MessageAttributes={
                "AWS.SNS.SMS.SenderID": {
                    "DataType": "String",
                    "StringValue": settings.SMS_SENDER_ID,
                },
                "AWS.SNS.SMS.SMSType": {
                    "DataType": "String",
                    "StringValue": "Promotional",
                },
            },
        )


def send_cancel_sms(phone_number: str, booking_number: int, start_time: datetime, language: str = settings.LANGUAGE_CODE):
    old_language = get_language()
    activate(language)
    messages = [
        _("日野町コロナワクチン集団接種の%(ordinal_number)s接種予約（%(j_start_time)s%(e_start_time)s）がキャンセルされました。")
        % {
            "ordinal_number": ordinal(booking_number),
            "number": booking_number,
            "j_start_time": f"{start_time:%-m月%-d日%-H:%M〜}",
            "e_start_time": f"{start_time:%a %b %d %H:%M-}",
        },
        _("お手数ですが、再予約をお願い致します。"),
    ]
    activate(old_language)
    send_sms(phone_number, " ".join(messages))


def hash_birth_date_and_my_number(birth_date: str, my_number: str):
    hash_value = ""
    num_split = 4
    if len(birth_date) != 8 or len(my_number) != 12:
        raise DataError

    birth_split = [birth_date[i : i + 2] for i in range(0, len(birth_date), 2)]
    my_number_split = [my_number[i : i + 3] for i in range(0, len(my_number), 3)]
    for i in range(num_split):
        divided_str = settings.SALT[i] + birth_split[i] + my_number_split[i]
        hash_value += hashlib.sha256(divided_str.encode()).hexdigest()

    return hash_value


def calc_age(birthdate: date, base_date: date = date.today()):
    age = relativedelta(base_date, birthdate).years
    return age
