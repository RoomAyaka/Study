import csv  # CSVを扱ライブラリーをインポートする
import sys
import pytest
sys.path.append('../')     # srcを読み込めるようにルートに追加する
from src.calc import Calc  # テスト対象のCalcクラスをimportする
from copy import copy

class Common():

    def is_int(data):
        """ 文字列がint型であるかを確認する """
        try:
            int(data, 10)
        except ValueError:
            return False
        else:
            return True

    def is_float(data):
        """ 文字列がfloat型であるかを確認する """
        try:
            float(data)
        except ValueError:
            return False
        else:
            return True

    def load_csv(csv_path):
        """ csvファイルを読み込んでdict型を作成する """
        # 各試験情報をに格納するようのlist型
        operation_list = []
        # csvファイルのパスからcsvデータを取得する
        with open(csv_path) as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # 0番目はheader情報であり、それ以外はデータになる
                if i == 0:
                    # headerを保存する
                    header_row = copy(row)
                    # 取得次第次のループに進む
                    continue
                else:
                    # copyで参照渡しで同じidにならないようにしている
                    deta_row = copy(row)

                # 各試験情報のdict型を初期化
                operation = {}
                # header, detaを同時にfor文で渡してdict型を作成する
                for header, deta in zip(header_row, deta_row):
                    # csvデータは全て文字列のデータなので"convert_type"で適切なデータ型に変換する
                    operation[header] = Common.convert_type(deta)
                # 各試験情報をに格納する
                operation_list.append(operation)
            return operation_list

    def convert_type(data):
        """
        文字列のデータを適切なデータ型に変換する
            capitalizeで先頭大文字にし、データの比較を容易にする
            if分岐の比較対象をlistしている理由:比較対象を追加削除を容易にする為
        """
        # True
        if data.capitalize() in ["True"]:
            return True
        # False
        elif data.capitalize() in ["False"]:
            return False
        # None
        elif data.capitalize() in ["None", "Null"]:
            return None
        # int
        elif Common.is_int(data):
            return int(data)
        # float
        elif Common.is_float(data):
            return float(data)
        # str
        else:
            return data

class Test():

    def verify_check(operation):
        try:
            # 試験情報から必要なデータを取得する
            __x = operation["x"]
            __y = operation["y"]
            __action = operation["action"]
            # 引数をテスト対象のコードに渡して結果を取得する
            result = Calc.four_arithmetic_operations(__x, __y, action=__action)
            # 期待値と一致するか確認する
            if result == operation["expected_value"]:
                print(f'result:{result} == {operation["expected_value"]}')
                return True
            else:
                print(f'result:{result} != {operation["expected_value"]}')
                return False
        except:
            # 例外処理の場合は、意図的な例外処理が発生しているかを確認する
            with pytest.raises(ValueError) as e:
                Calc.four_arithmetic_operations(__x, __y, action=__action)
            # 期待値と一致するか確認する
            if str(e.value) == operation["expected_value"]:
                print(f'result:{e.value} == {operation["expected_value"]}')
                return True
            else:
                print(f'result:{e.value} != {operation["expected_value"]}')
                return False

