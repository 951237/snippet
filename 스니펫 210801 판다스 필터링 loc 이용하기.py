# condition 1
cond1 = (df['item'].isnull()) # 조건1
cond2 = (df['item'] == 'sum') # 조건2

# 필터링하기
df.loc[(~cond1) & (cond2)]  # 조건1이 아니고 조건2
