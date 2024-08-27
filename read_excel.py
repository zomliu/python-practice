# 使用 pandas 操作 excel 文件
# pandas 操作 Excel 是按列处理的, 写入也是

import pandas as pd

def name_processor(name: str):
    return name.split('-')[0]

def online_time_processor(online_time: str):
    if pd.isna(online_time):
        return 0
    return int(online_time[:4])

# 列上的数据加工
def column_process():
    df = pd.read_excel('movies.xlsx')
    # print(df.info())  # 打印整个 df 的基本信息
    
    df['Name'] = df['Name'].apply(name_processor)  # 处理整行数据, 如果 df.apply() 的话, 就是处理整个 dataframe 了, 传入 lambda 函数的参数是 dataframe 的列
    df['Duration'] = df['Duration'].apply(lambda x: x[:str(x).find(' ')])
    df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

    df.to_excel('movies_new.xlsx', index=False) # 处理后的数据写入到新的 excel 文件中

# 一些数据操作
def data_process():
    df = pd.read_excel('movies_new.xlsx')
    # print(df.info())  # 打印整个 df 的基本信息
    # print(df.head(2))  # 前 2 行数据
    # print(df.tail(2))  # 后 2 行数据
    # print(df.shape)  # 打印数据集的行数和列数
    # print(df.describe())  # 打印数据集的统计信息
    max_idx = df['Duration'].argmax() # 找到最大值的行索引(排除首行后, 索引从 0 开始)
    df['Duration'].max() # 找到最大值
    max_row = df.iloc[max_idx] # 找到最大值的行数据, iloc 还可以选定列, 比如: 第 2 行第 2 列 -> df.iloc[2, 1], 第 3 行第 2~4 列 -> df.iloc[2, 1:4], 第 2~5 行的第 2~4 列 -> df.iloc[1:5, 1:4]
    print(max_row)

    df['Duration'].mean() # 找到平均值
    df['Duration'].median() # 找到中位数
    df['Duration'] > 100 # 找到大于 100 的数据, 返回一个布尔值数组
    df[df['Duration'] > 100] # 根据里面的布尔值数组, 找到列 Duration 中大于 100 的数据
    new_df = df[df['Duration'] > 100 & (df['Region'].apply(lambda x: '中国' in x))] # 根据里面的布尔值条件, 找到 列 Duration 中大于 100  并且列 Region 中包含 '中国' 的数据
    print(new_df[['Name', 'Region', 'Duration']]) # 只打印 Name, Region, Duration 列的数据, 列是个list 形式
    print('--' * 10)
    print(df[df['Duration'] > 100]['Name'].count()) # 统计符合条件的行数 (如果不指定某列, 结果会输出每一列的统计结果)
    print('--' * 10)
    print(df.groupby(df['Online Time'].apply(online_time_processor)).count()['Online Time']) # 根据列 Online Time 的值, 分组统计

if __name__ == '__main__':
    # column_process()
    data_process()