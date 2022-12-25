import matplotlib.pyplot as plt
import pandas as pd

data = {
    "東京の気温(2020年)": [7.1, 8.3, 10.7, 12.8, 19.5, 23.2, 24.3, 29.1, 24.2, 17.5, 14.0, 7.7],
    "大阪の気温(2020年)": [8.6, 8.0, 11.4, 13.7,20.8, 24.9, 26.0, 30.7, 25.8, 18.7, 14.7, 8.7]
}
df = pd.DataFrame(data)
df["東京の気温(2020年)"].plot.hist(bins=[0, 5, 10, 15, 20, 25, 30])
# fontname="MS Gothic"で文字化けを防ぐ
plt.title("東京の気温(2020年)", fontname="MS Gothic")
plt.show()
