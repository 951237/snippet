import pandas as pd 

# 스택과 인덱스 리셋하기
pd.DataFrame(df.stack()).reset_index.iloc[1:]

# 인덱스 정하고 스택 후 인덱스 리셋하기
pd.DataFrame(df.set_index(['items'])).stack().reset_index()

# 사용하지 않는 칼럼 삭제하기
df.iloc[:, 6:-2].drop(columns=['cols1', 'cols2'])

