from typing import Any, List


class DataImportError(Exception):
    """
    一括登録処理の基底エラー
    """


class TooManyWorksheetsError(DataImportError):
    """
    想定よりシート数が多い場合に送出される例外
    """

    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected

    def __str__(self):
        return f"ワークシートが多すぎます(想定: {self.expected}, 実際: {self.actual})"


class NoDataRowError(DataImportError):
    """
    データ行が無い場合に送出される例外
    """

    def __str__(self):
        return "データ行がありません"


class InvalidHeaderError(DataImportError):
    """
    ヘッダー行に想定外の列が存在する場合に送出される例外
    """

    def __init__(self, actual_columns: List, expected_columns: List):
        self.actual_columns = actual_columns
        self.expected_columns = expected_columns

        extra_col = sorted(set(actual_columns) - set(expected_columns), key=actual_columns.index)
        if len(extra_col) > 3:
            self.extra_col = ", ".join(map(str, extra_col[:3])) + "....."
        else:
            self.extra_col = ", ".join(map(str, extra_col))

        shortage_col = sorted(set(expected_columns) - set(actual_columns), key=expected_columns.index)
        if len(shortage_col) > 3:
            self.shortage_col = ", ".join(map(str, shortage_col[:3])) + "....."
        else:
            self.shortage_col = ", ".join(map(str, shortage_col))

    def __str__(self):
        if self.extra_col:
            return f"ヘッダ行が正しくありません(想定外の列: {self.extra_col})"
        elif self.shortage_col:
            return f"ヘッダ行が正しくありません(存在しない想定列: {self.shortage_col})"
        else:
            return "ヘッダ行が正しくありません"


class TooManyDataColumnsError(DataImportError):
    """
    想定より列数が多い場合に送出される例外
    """

    def __init__(self, row: int, column: int, value: Any):
        self.row = row
        self.column = column
        self.value = value

    def __str__(self):
        return f"ヘッダの無い列に値が入力されています(行番号: {self.row}, 列番号: {self.column}, 値: {self.value})"


class RowValidationError(DataImportError):
    """
    データ行のバリデーションエラー
    """

    def __init__(self, row: int, column_name: str, message: str):
        self.row = row
        self.column_name = column_name
        self.message = message

    def __str__(self):
        return f"行番号: {self.row}, 列名: {self.column_name} の入力エラー: {self.message}"


class RowError(DataImportError):
    def __init__(self, row, cell_error):
        self.row = row
        self.cell_error = cell_error

    def __str__(self):
        return f"行番号: {self.row}, {self.cell_error}"
