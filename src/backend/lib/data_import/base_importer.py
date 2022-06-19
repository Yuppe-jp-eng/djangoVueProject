from typing import Optional, Tuple

from backend.lib.data_import.exceptions import DataImportError


class BaseImporter(object):
    lineage = None

    def execute(self) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        一括登録処理を行う。

        :return: 成否、行数(見出し行数を除く)、エラーメッセージのtuple
        """
        try:
            self._validate()
            self._import()
        except DataImportError as e:
            return False, self.lineage, str(e)

        return True, self.lineage, None

    def column_length(self) -> Optional[int]:
        """
        処理対象ファイルで許容される列数

        列数が可変の場合は_validate_formatの呼び出しが終わるまでNone。

        :return: 列数
        """
        raise NotImplementedError

    def _validate(self):
        self._validate_registered_data()
        self._validate_format()
        self._validate_data()

    def _validate_registered_data(self) -> None:
        """
        既存データに対するチェックを行う。

        チェックの結果、不正が見つかった場合はDataImportErrorを継承した例外を投げる。
        既存データチェックが必要であればサブクラスでオーバライドすること。

        :return: None
        """

    def _validate_format(self) -> None:
        """
        ヘッダ行、列数、データ行数などフォーマットに関するチェックを行う。

        チェックの結果、不正が見つかった場合はDataImportErrorを継承した例外を投げる。

        :return: None
        """
        raise NotImplementedError()

    def _validate_data(self) -> None:
        """
        データ行のバリデーションを行う。

        チェックの結果、不正が見つかった場合はDataImportErrorを継承した例外を投げる。

        :return: None
        """
        raise NotImplementedError()

    def _import(self) -> None:
        """
        データ行を読み込み永続処理を行う。

        :return: None
        """
        raise NotImplementedError()
