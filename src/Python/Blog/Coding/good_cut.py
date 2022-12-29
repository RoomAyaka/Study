import pandas as pd

class Padnas():

    def __init__(self, df):
        self.__df = df

    # ラッパー関数を作成し、bins、rightは固定で使うものとする
    def wrapper_cut(self, column, bins=[0, 5, 10, 15, 20, 25, 30], right=False):
        cut = pd.cut(self.__df[column], bins=bins, right=right)
        print(cut.value_counts(sort=False))

data = {
    "東京の気温(2020年)": [7.1, 8.3, 10.7, 12.8, 19.5, 23.2, 24.3, 29.1, 24.2, 17.5, 14.0, 7.7],
    "大阪の気温(2020年)": [8.6, 8.0, 11.4, 13.7,20.8, 24.9, 26.0, 30.7, 25.8, 18.7, 14.7, 8.7]
}
pandas = Padnas(pd.DataFrame(data))
pandas.wrapper_cut("東京の気温(2020年)")
