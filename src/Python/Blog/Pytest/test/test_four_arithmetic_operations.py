import sys
import pytest
sys.path.append('../')     # srcを読み込めるようにルートに追加する
from src.calc import Calc  # テスト対象のCalcクラスをimportする
from func.test_common import Common
from func.test_common import Test


@pytest.fixture(scope='class')
def setup_pytest():
    # csvファイルから各試験情報を取得する
    operation = Common.load_csv("csv/test_design.csv")

    # listに格納して各テストコードに渡す
    yield operation

def test_000(setup_pytest):
    # setup_pytestはoperationと同じ値である。
    # sys._getframe().f_code.co_nameは、自分の関数名を取得出来ます → ex.test_000
    # sys._getframe().f_code.co_name[-1]は、ex.test_000 → 0
    # 自分の関数名から自分の試験情報をlistから呼び出しテストを実行する
    # テストコードを統一する事でテストコード側のミスを取り除くする事が出来ます。
    assert Test.verify_check(setup_pytest[int(sys._getframe().f_code.co_name[-1])])

def test_001(setup_pytest):
    assert Test.verify_check(setup_pytest[int(sys._getframe().f_code.co_name[-1])])

def test_002(setup_pytest):
    assert Test.verify_check(setup_pytest[int(sys._getframe().f_code.co_name[-1])])

def test_003(setup_pytest):
    assert Test.verify_check(setup_pytest[int(sys._getframe().f_code.co_name[-1])])

def test_004(setup_pytest):
    assert Test.verify_check(setup_pytest[int(sys._getframe().f_code.co_name[-1])])
