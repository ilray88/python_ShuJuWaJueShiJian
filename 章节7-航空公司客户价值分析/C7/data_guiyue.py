import pandas as pd
import numpy as np
datafile= 'data_cleaned.csv' #航空原始数据,第一行为属性标签
data = pd.read_csv(datafile,encoding='utf-8') #读取原始数据
data["LOAD_TIME"] = pd.to_datetime(data["LOAD_TIME"])
data["FFP_DATE"] = pd.to_datetime(data["FFP_DATE"])
data["入会时间"] = data["LOAD_TIME"] - data["FFP_DATE"]
data["平均每公里票价"] = (data["SUM_YR_1"] + data["SUM_YR_2"]) / data["SEG_KM_SUM"]
data["时间间隔差值"] = data["MAX_INTERVAL"] - data["AVG_INTERVAL"]
deal_data = data.rename(columns = {"FLIGHT_COUNT" : "飞行次数",
"SEG_KM_SUM" : "总里程", "avg_discount" : "平均折扣率"}, inplace = False)
filter_data = deal_data[["入会时间", "飞行次数", "平均每公里票价", "总里程",
"时间间隔差值", "平均折扣率"]]
filter_data['入会时间'] = filter_data['入会时间'].astype(np.int64)/(60*60*24*10**9)
filter_data.to_csv('filter _data.csv')
#print(filter_data.info('filter _data.csv'))
filter_zscore_data = (filter_data - filter_data.mean(axis=0))/(filter_data.std(axis=0))
filter_zscore_data.to_csv('filter_zscore_data.csv')