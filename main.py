"""
=========================================================
Log Analyer
Copyright (c) 2022 Hayato Funahashi All Rights Reserved.
========================================================
"""
import pandas as pd
import matplotlib.pyplot as plt
import sys

def prepro(path):
    df = pd.read_csv(path, header=None)

    df = df[0].str.split(',', expand=True)      # param:expandでDfとして受ける
    df = df.drop(df.columns[[0,7,8]], axis=1)   # 不要な列をdrop

    s = df[1]+"-"+df[2]+"-"+df[3]+"-"+df[4]+"-"+df[5]+"-"+df[6] #DateTime変換可能な型に
    s = pd.to_datetime(s, format="%y-%m-%d-%H-%M-%S")

    df = df.drop(df.columns[[0,1,2,3,4,5]], axis=1) #不要なデータ列を削除
    df.columns = range(df.shape[1])
    df = df.rename(columns={0:'val1', 1:'val2', 2:'val3'}) #column名を振り直し
    df["dt"] = s

    return df

def draw(df):
    data_num = 3
    fig, axes = plt.subplots(nrows=data_num, ncols=1, sharex='col', tight_layout=True)
    for i in range(3):
        axes[i].plot(df["dt"], df.iloc[:,i])
        axes[i].set_ylabel(df.columns.values[i])

    plt.show()
    fig.savefig('sample.png', facecolor=fig.get_facecolor())

def main():
    if len(sys.argv) == 1:
        path = 'sample.csv'
    else:
        path = sys.argv[1]
        
    df = prepro(path)
    draw(df)

main()