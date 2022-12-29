import pandas as pd

data = {
    "東京の気温(2020年)": [7.1, 8.3, 10.7, 12.8, 19.5, 23.2, 24.3, 29.1, 24.2, 17.5, 14.0, 7.7],
    "大阪の気温(2020年)": [8.6, 8.0, 11.4, 13.7,20.8, 24.9, 26.0, 30.7, 25.8, 18.7, 14.7, 8.7]
}
df = pd.DataFrame(data)
"""
right=False, bins = [0, 5, 10, 15, 20, 25, 30]の設定で
    0℃以上5℃未満, 5℃以上10℃未満, 10℃以上15℃未満
    15℃以上20℃未満, 20℃以上25℃未満, 25℃以上30℃未満の範囲を指定する
"""
bins = [0, 5, 10, 15, 20, 25, 30]
cut = pd.cut(df["東京の気温(2020年)"], bins=bins, right=False)
print(cut.value_counts(sort=False))

cut = pd.cut(df["大阪の気温(2020年)"], bins=bins, right=False)
print(cut.value_counts(sort=False))
