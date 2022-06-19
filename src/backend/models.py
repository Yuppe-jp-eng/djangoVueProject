# , PermissionsMixin, UserManager
from django.contrib.auth.models import AbstractUser
from xmlrpc.client import Boolean
from django.db import models


class BaseModel(models.Model):
    """
    プロジェクトで作成するモデルクラスの抽象モデルクラス
    本プロジェクトで作成するモデルクラスは本クラスを継承すること。
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'apps'


class AdminUserModel(BaseModel, AbstractUser):
    department = models.ForeignKey("DepartmentModel", blank=True, null=True, related_name="admin_users", verbose_name="部署", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "管理ユーザ"
        db_table = "admin_user"


class UserModel(BaseModel):
    email = models.EmailField(unique=True, max_length=255)
    hashed_password = models.TextField("暗号化パスワード")
    name = models.CharField("名前", max_length=64)
    name_kana = models.CharField("名前フリガナ", max_length=64)
    address = models.CharField("住所", max_length=512)
    is_valid = models.BooleanField("有効")

    class Meta:
        verbose_name = "ユーザ"
        db_table = "user"


class UserTodoModel(BaseModel):
    status = models.CharField("ステータス", max_length=16)
    user = models.ForeignKey(
        "UserModel",
        blank=False,
        null=False,
        related_name="user_todos",
        verbose_name="ユーザ",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "会員ToDoリスト"
        db_table = "user_todo"


class UserTempInfoModel(BaseModel):
    latest_child_name = models.CharField("最新の子どもの名前", max_length=64)
    latest_child_birthday = models.DateTimeField("最新の子どもの生年月日")
    latest_father_name = models.CharField("最新の父の名前", max_length=64)
    latest_father_birthday = models.DateTimeField("最新の父の生年月日")
    latest_mother_name = models.CharField("最新の母の名前", max_length=64)
    latest_mother_birthday = models.DateTimeField("最新の母の生年月日")

    user = models.ForeignKey(
        "UserModel",
        blank=False,
        null=False,
        related_name="user_temp_infos",
        verbose_name="ユーザ",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "会員一時情報"
        db_table = "user_temp_info"


class DepartmentModel(BaseModel):
    name = models.CharField("部署名", max_length=32)

    class Meta:
        verbose_name = "部署"
        db_table = "department"


class EventCategoryModel(BaseModel):
    name = models.CharField("名前", max_length=32)
    str_id = models.CharField("識別子", max_length=32)
    order = models.IntegerField("並び順")
    icon_image_url = models.TextField("アイコン画像")

    class Meta:
        verbose_name = "イベントカテゴリ"
        db_table = "event_category"


class EventModel(BaseModel):
    name = models.CharField("名前", max_length=32)
    state = models.CharField("状態", max_length=16)
    str_id = models.CharField("識別子", max_length=32)
    is_use_form = models.BooleanField("申請フォーム使用")
    is_use_datepicker = models.BooleanField("予約フォーム使用")
    reservable_start_time = models.TimeField("予約受付開始時間")
    reservable_end_time = models.TimeField("予約受付終了時間")
    reservable_minute_interval = models.IntegerField("予約枠間隔")
    guidance_page_content = models.TextField("案内ページコンテンツ")
    complete_page_content = models.TextField("予約完了ページコンテンツ")

    event_category = models.ForeignKey(
        "EventCategoryModel",
        blank=False,
        null=False,
        related_name="events",
        verbose_name="イベントカテゴリ",
        on_delete=models.PROTECT)
    department = models.ForeignKey(
        "DepartmentModel",
        blank=True,
        null=True,
        related_name="events",
        verbose_name="部署名",
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "イベント"
        db_table = "event"


class EventEntryModel(BaseModel):
    status = models.CharField("ステータス", max_length=16)
    entry_code = models.CharField("受付番号", max_length=32)

    event = models.ForeignKey(
        "EventModel",
        blank=False,
        null=False,
        related_name="event_entries",
        verbose_name="イベント",
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        "UserModel",
        blank=False,
        null=False,
        related_name="event_entries",
        verbose_name="ユーザ",
        on_delete=models.PROTECT)
    entry_frame = models.ForeignKey(
        "EntryFrameModel",
        blank=True,
        null=True,
        related_name="event_entries",
        verbose_name="予約枠",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "イベント申請"
        db_table = "event_entry"


class EntryFrameModel(BaseModel):
    start_at = models.DateTimeField("開始日時")
    capacity = models.IntegerField("予約可能上限人数")

    event = models.ForeignKey(
        "EventModel",
        blank=False,
        null=False,
        related_name="entry_frames",
        verbose_name="イベント",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "予約枠"
        db_table = "entry_frame"


class GeneralGuideFormModel(BaseModel):
    order = models.IntegerField("並び順")
    form_type = models.CharField("フォームタイプ", max_length=32)
    label = models.CharField("ラベル", max_length=32)
    select_options = models.CharField("選択肢", max_length=256)
    is_required = models.BooleanField("必須")
    max_length = models.IntegerField("最大文字数バリデーション")
    valid_chars = models.CharField("入力可能文字バリデーション", max_length=256)
    regex_pattern = models.CharField("正規表現バリデーション", max_length=256)
    is_personal_name_kanji = models.BooleanField("人名使用可能漢字")
    form_help_text = models.TextField("フォーム説明")
    word_help_title = models.CharField("用語説明タイトル", max_length=32)
    word_help_text = models.TextField("用語説明")
    value_src = models.CharField("自動入力参照元", max_length=256)
    value_dest = models.CharField("データ連携先", max_length=256)
    display_conditions = models.TextField("表示条件")

    event_category = models.ForeignKey(
        "EventCategoryModel",
        blank=False,
        null=False,
        related_name="general_guide_forms",
        verbose_name="イベントカテゴリ",
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "総合案内フォーム"
        db_table = "general_guide_form"


class FormModel(BaseModel):
    order = models.IntegerField("並び順")
    form_type = models.CharField("フォームタイプ", max_length=32)
    label = models.CharField("ラベル", max_length=32)
    select_options = models.CharField("選択肢", max_length=256)
    is_required = models.BooleanField("必須")
    max_length = models.IntegerField("最大文字数バリデーション")
    valid_chars = models.CharField("入力可能文字バリデーション", max_length=256)
    regex_pattern = models.CharField("正規表現バリデーション", max_length=256)
    is_personal_name_kanji = models.BooleanField("人名使用可能漢字")
    form_help_text = models.TextField("フォーム説明")
    word_help_title = models.CharField("用語説明タイトル", max_length=32)
    word_help_text = models.TextField("用語説明")
    value_src = models.CharField("自動入力参照元", max_length=256)
    value_dest = models.CharField("データ連携先", max_length=256)
    display_conditions = models.TextField("表示条件")

    event = models.ForeignKey(
        "EventModel",
        blank=False,
        null=False,
        related_name="forms",
        verbose_name="イベント",
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "フォーム"
        db_table = "form"


class FormAnswerModel(BaseModel):
    answer = models.TextField("回答")

    user = models.ForeignKey(
        "UserModel",
        blank=False,
        null=False,
        related_name="form_answers",
        verbose_name="ユーザ",
        on_delete=models.CASCADE)
    event_entry = models.ForeignKey(
        "EventEntryModel",
        blank=False,
        null=False,
        related_name="form_answers",
        verbose_name="イベント申請",
        on_delete=models.PROTECT)
    form = models.ForeignKey(
        "FormModel",
        blank=False,
        null=False,
        related_name="form_answers",
        verbose_name="フォーム",
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "フォーム回答"
        db_table = "form_answer"
