import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# グラフにstyleとfontを設定する
sns.set(style="whitegrid", font=["Yu Gothic"])

data = {
    "つぶあん": [62, 47, 18],
    "こしあん": [35, 26, 12]
}
index = ["好き", "普通", "嫌い"]
df = pd.DataFrame(data, index)
# 円グラフを表示する
# startangle=90, counterclock=False データの始まりを真上から開始するオプション
# labeldistance=0.5 データのindexを内側に入れるオプション
df["つぶあん"].plot.pie(startangle=90, counterclock=False, labeldistance=0.5)
plt.show()
