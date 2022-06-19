from enum import Enum
from typing import Type, Any, TypeVar
from django.utils.translation import gettext_lazy as _

TBaseEnum = TypeVar("TBaseEnum", bound="BaseEnum")


class BaseEnum(Enum):
    @classmethod
    def values(cls):
        return [x.value for x in cls]

    @classmethod
    def choices(cls):
        return [(x.value, x.name) for x in cls]

    @classmethod
    def value_of(cls, value: Any) -> Type[TBaseEnum]:
        for e in cls:
            if e.value == value:
                return e
        raise ValueError(f"Value not found '{value}'")


class KeyLabelEnum(BaseEnum):
    def __init__(self, key, label):
        self._key = key
        self._label = label

    @property
    def key(self):
        return self._key

    @property
    def label(self):
        return self._label

    @classmethod
    def keys(cls):
        return [e.key for e in cls]

    @classmethod
    def labels(cls):
        return [e.label for e in cls]

    @classmethod
    def choices(cls):
        return [(e.key, e.label) for e in cls]

    @classmethod
    def label_choices(cls):
        return [(e.label, e.key) for e in cls]

    @classmethod
    def key_of(cls, key: str):
        for e in cls:
            if e.key == key:
                return e
        raise ValueError(f"Key not found '{key}'")

    @classmethod
    def label_of(cls, label: str):
        for e in cls:
            if e.label == label:
                return e
        raise ValueError(f"Label not found '{label}'")

    @classmethod
    def key_to_label(cls, key: str) -> str:
        return cls.key_of(key).label

    @classmethod
    def label_to_key(cls, label: str) -> str:
        return cls.label_of(label).key


class Gender(KeyLabelEnum):
    MALE = ("male", "男性")
    FEMALE = ("female", "女性")


class Language(KeyLabelEnum):
    JAPANESE = ("ja", "日本語")
    ENGLISH = ("en", "英語")
    PORTUGUESE = ("pt", "ポルトガル")


class BookingModelStatus(KeyLabelEnum):
    COMPLETE = ("complete", _("完了"))
    AWAIT = ("await", _("接種待ち"))
    TEMP = ("temp", _("仮予約"))
    CANCEL = ("cancel", _("キャンセル"))


class BookingModelStatusExcludedTemp(KeyLabelEnum):
    COMPLETE = (BookingModelStatus.COMPLETE.key, BookingModelStatus.COMPLETE.label)
    AWAIT = (BookingModelStatus.AWAIT.key, BookingModelStatus.AWAIT.label)
    CANCEL = (BookingModelStatus.CANCEL.key, BookingModelStatus.CANCEL.label)


class UserStatus(KeyLabelEnum):
    ALL_RESERVED = ("all_reserved", "2回共に予約済み")
    ONETIME_RESERVED = ("onetime_reserved", "1回目のみ予約済み")
    ONETIME_COMPLETED = ("onetime_completed", "1回目接種済み、2回目予約済み")
    ALL_COMPLETED = ("all_completed", "1回目接種済み、2回目接種済み")
    UNRESERVED = ("unreserved", "未予約")


class APIError(KeyLabelEnum):
    WRONG_PARAM = ("WRONG_PARAM", "パラメータ不正")
    NOT_FOUND = ("NOT_FOUND", "該当ユーザ無し")
    AUTH_FAILED = ("AUTH_FAILED", "認証失敗（key が無効）")
    FULLY_RESERVED = ("FULLY_RESERVED", "予約が埋まっている")
    EXCEPTION_ERROR = ("EXCEPTION_ERROR", "API処理エラー")
