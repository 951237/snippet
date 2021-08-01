import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# 폰트 설정하기
mpl.rc('font', family='Malgun Gothic')

# usage 1 - 카운터 플롯 - 기본
sns.countplot(data=df, x='col1')


# usage 2 - 카운터 플롯 오버레이 출력
plt.figure(figsize=[10, 5])
sns.countplot(data=df, x='prodcut', hue='col1')
plt.legend(loc='right')


# usage 3 - 수치가 많은 칼럼들부터 정렬하기
plt.figure(figsize=[10, 5])
order_list = df['bank'].value_counts().index.tolist()
# display 10 order=order_list[0:10]
sns.countplot(data=df, x='bank', order=order_list)

