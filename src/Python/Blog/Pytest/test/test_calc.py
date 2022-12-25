import sys
sys.path.append('../')     # srcを読み込めるようにルートに追加する
from src.calc import Calc  # テスト対象のCalcクラスをimportする

# add_num関数をテストする
def test_add_num_001():
    result = Calc.add_num(1, 2)
    assert result == 3

def test_add_num_002():
    result = Calc.add_num(5, 7)
    assert result == 12

# sub_num_num関数をテストする
def test_sub_num_001():
    result = Calc.sub_num(2, 1)
    assert result == 1

def test_sub_num_002():
    result = Calc.sub_num(5, 2)
    assert result == 3
