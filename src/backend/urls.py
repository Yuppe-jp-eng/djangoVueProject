from django.urls import path
from backend.front.views.birth import FrontBirthGeneralGuideView, FrontBrithCategoryListView, FrontBrithToDoListView
from backend.front.views.event import FrontEventCompleteView, FrontEventConfirmView, FrontEventDatePickView, FrontEventDetailView, FrontEventInputPickView
from backend.front.views.event_edit import FrontEventEditDatePickView, FrontEventEditInputView

from backend.front.views.login import FrontLoginView, FrontLogoutView
from backend.front.views.password_reminder import FrontPasswordReminderCompleteView, FrontPasswordReminderInputView, FrontPasswordReminderRequestView
from backend.front.views.registration import FrontRegistrationInputView
from backend.front.views.remark import FrontRemarkContactView, FrontRemarkPrivacyView, FrontRemarkTermsView
from backend.front.views.user import FrontMyPageView
from backend.front.views.user_info import FrontUserInfoDetailView
from . import views
from backend.manage.views.manage.dashboard import AdminDashboardView
from backend.manage.views.manage.user import AdminUserListView
from backend.manage.views.manage.booking import AdminBookingListView, AdminBookingDetailView
from backend.manage.views.manage.event_category import AdminEventCategoryListView, AdminEventCategoryCreateView, AdminEventCategoryDetailView, AdminEventCategoryEditView
from backend.manage.views.manage.department import AdminDepartmentListView, AdminDepartmentCreateView, AdminDepartmentEditView
from backend.manage.views.manage.admin_user import AdminAdminUserListView, AdminAdminUserCreateView, AdminAdminUserEditView

from backend.manage.views.manage.entrance import AdminEntranceLoginView

app_name = "apps"

urlpatterns = [
    path('', views.index, name='index'),
    # ============
    # フロント画面
    # ============
    # フロントログイン
    path("login/", FrontLoginView.as_view(), name="front_login"),
    # フロントログアウト
    path("logout/", FrontLogoutView.as_view(), name="front_logout"),
    # フロント新規登録
    path("registration/", FrontRegistrationInputView.as_view(), name="front_registration"),
    # フロントパスワードリマインダーのリクエスト
    path("password_reminder/request/", FrontPasswordReminderRequestView.as_view(), name="front_password_reminder_request"),
    # フロントパスワードリマインダーの入力
    path("password_reminder/input/", FrontPasswordReminderInputView.as_view(), name="front_password_reminder_input"),
    # フロントパスワードリマインダーの入力
    path("password_reminder/complete/", FrontPasswordReminderCompleteView.as_view(), name="front_password_reminder_complete"),
    # フロントユーザーマイページ
    path("user/mypage", FrontMyPageView.as_view(), name="front_mypage"),
    # フロントユーザー情報詳細
    path("user/user_info/detail", FrontUserInfoDetailView.as_view(), name="front_user_info_detail"),
    # フロント妊娠・出産手続き一覧
    path("birth/category_list", FrontBrithCategoryListView.as_view(), name="front_birth_category_list"),
    # フロント妊娠・出産手続き総合案内
    path("birth/general_guide", FrontBirthGeneralGuideView.as_view(), name="front_birth_general_guide"),
    # フロント妊娠・出産手続きToDoリスト
    path("birth/todo_list", FrontBrithToDoListView.as_view(), name="front_birth_todo_list"),
    # フロントイベント詳細
    path("event/detail", FrontEventDetailView.as_view(), name="front_event_detail"),
    # フロントイベント日付選択
    path("event/date_pick", FrontEventDatePickView.as_view(), name="front_event_date_pick"),
    # フロントイベント申請情報入力
    path("event/input", FrontEventInputPickView.as_view(), name="front_event_input"),
    # フロントイベント入力内容確認
    path("event/confirm", FrontEventConfirmView.as_view(), name="front_event_confirm"),
    # フロントイベント完了
    path("event/complete", FrontEventCompleteView.as_view(), name="front_event_complete"),
    # フロントイベント編集入力
    path("event/edit/input", FrontEventEditInputView.as_view(), name="front_event_edit_input"),
    # フロントイベント編集日付選択
    path("event/edit/date_pick", FrontEventEditDatePickView.as_view(), name="front_event_edit_date_pick"),
    # フロントお問い合わせ
    path("event/remark/contact", FrontRemarkContactView.as_view(), name="front_remark_contact"),
    # フロントプライバシーポリシー
    path("event/remark/privacy", FrontRemarkPrivacyView.as_view(), name="front_remark_privacy_policy"),
    # フロント利用規約
    path("event/remark/terms", FrontRemarkTermsView.as_view(), name="front_remark_terms"),

    # ============
    # 管理画面
    # ============
    # ダッシュボード
    path('_admin/', AdminDashboardView.as_view(), name='admin_dashboard'),

    # ユーザー管理
    path('_admin/user/', AdminUserListView.as_view(), name="admin_user_list"),

    # 予約管理
    path('_admin/booking/', AdminBookingListView.as_view(), name="admin_booking_list"),
    path('_admin/booking/<int:id>/detail', AdminBookingDetailView.as_view(), name="admin_booking_detail"),

    # 予約枠管理
    # 開発中？

    # イベントカテゴリ管理
    path('_admin/event_category/', AdminEventCategoryListView.as_view(), name="admin_event_category_list"),
    path('_admin/event_category/create', AdminEventCategoryCreateView.as_view(), name="admin_event_category_create"),
    path('_admin/event_category/<int:id>/detail', AdminEventCategoryDetailView.as_view(), name="admin_event_category_detail"),
    path('_admin/event_category/<int:id>/edit', AdminEventCategoryEditView.as_view(), name="admin_event_category_edit"),

    # イベント管理
    # 開発中

    # 部署管理
    path('_admin/department/', AdminDepartmentListView.as_view(), name="admin_department_list"),
    path('_admin/department/create', AdminDepartmentCreateView.as_view(), name="admin_department_create"),
    path('_admin/department/<int:id>/edit', AdminDepartmentEditView.as_view(), name="admin_department_edit"),

    # 管理ユーザー管理
    path("_admin/admin_user/", AdminAdminUserListView.as_view(), name="admin_admin_user"),
    path("_admin/admin_user/<int:id>/edit", AdminAdminUserEditView.as_view(), name="admin_admin_user_edit"),
    path("_admin/admin_user/create", AdminAdminUserCreateView.as_view(), name="admin_admin_user_create"),

    # 管理画面ログイン画面
    path("_admin/login", AdminEntranceLoginView.as_view(), name="admin_login")
]
