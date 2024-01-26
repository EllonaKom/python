# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#  Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
print()
data = pd.DataFrame({'whoAmI':lst})
#data1=pd.get_dummies(data['whoAmI'])
data.loc[data['whoAmI'] == 'robot', 'robot_gr'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot_gr'] = '0'
data.loc[data['whoAmI'] == 'human', 'human_gr'] = '1'
data.loc[data['whoAmI'] != 'human', 'human_gr'] = '0'

data.head(n=20) 
print(data)
