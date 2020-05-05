#データの扱うためのライブラリを読み込む
import pandas as pd
import numpy as np
from collections import Counter

#図示のためのライブラリ
import matplotlib.pyplot as plt


import csv
import time


#csv読み込み
df = pd.read_csv("fav.csv")

#日付型に変換、#時間ごとの列を追加
df['created_at'] = pd.to_datetime(df['created_at'])
df['hour'] = df['created_at'].dt.hour


#時間・fav・RTのデータフレームを作成
time_df = df[['fav','RT','hour']]


#時刻順に並び替える、#時刻ごとにデータを集計
time_df = time_df.sort_values(by=['hour'], ascending=True)
mean=time_df.groupby(['hour']).mean()

#時刻ごとのfav,RT数の平均を出す。
size = time_df.groupby(['hour']).size()
mean.plot.bar(xlim=[0,24], ylim=[0,1600],figsize=(16,9))
plt.savefig('fav_rt.png')
plt.figure() #初期化しないとグラフが残っている

#時刻ごとの平均RTとツイート数のグラフを描写
mean['RT'].plot.bar(xlim=[0,24], ylim=[0,1600],figsize=(16,9),color="orange")
size.plot(xlim=[0,24], ylim=[0,1600],figsize=(16,9))
plt.savefig('RT.png')
plt.figure() #初期化しないとグラフが残っている

#時刻ごとの平均いいね数とツイート数のグラフ描写
mean['fav'].plot.bar(xlim=[0,24], ylim=[0,1600],figsize=(16,9))
size.plot(xlim=[0,24], ylim=[0,1600],figsize=(16,9))
plt.savefig('fav.png')