import numpy as np
import pandas as pd
import re

df = pd.read_excel('C:/JKerving/Work Documents/直采数据质量稽核与提升工作/2017.6.1-6.9号BSS数据质量稽核集中会议/问题追踪表/第二周/31省问题列表-v0616.xlsx')
# print(df)
df_shape = df.shape
rows = df_shape[0]
columns = df_shape[1]

s1 = df['状态']
s2 = df['省份']
s2_no_null = s2.dropna()

l = list(s2_no_null)
unique_province = set(l)
lt = list(unique_province)
lt.sort(key=l.index)
print(len(lt))
print(lt)

def func(series1, series2):
    for k in range(len(lt)):
        count_inprocess = 0
        count_notsure = 0
        count_done = 0
        for i in range(len(series1)):
            if (type(series1[i]) is str and (series1[i].startswith('6')) and type(
                    series2[i]) is str and series2[
                i].startswith(lt[k])):
                count_inprocess += 1
        print(lt[k],count_inprocess)

func(series1=s1, series2=s2)
