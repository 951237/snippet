# merge dataframe
df_merge = pd.merge(df6, df5, how = 'right', on = 'item')

# date 칼럼을 날짜 형식으로 바꾸기
df_merge['date_modified'] = pd.to_datetime(df_merge['date'])

# 날짜 칼럼에서 '월' 값 추울하여 칼럼 만들기
df_merge['month'] = df_merge['date_modified'].to_month

# 날자를 인덱스로 해서  count칼럼의 합계를 피봇테이블로 만들기 / 엑섹 파일 생성
pd.pivot_table(data = df_merge, index='date_modified', values='counts', aggfunc='sum').to_excel('result.xlsx')

# 인덱스를 가게와 아이템으로 설정후 count의 값을 합치기 
pd.pivot_table(dfata = df, index=['store', 'items'], values='counts', aggfunc='sum').reset_index()
