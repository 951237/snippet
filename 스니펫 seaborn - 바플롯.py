# 시각화 하기
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='NanumBarunGothic')

plt.figure(figsize=(12, 8)) # 그래프 크기 설정

# 활용 1 - 정렬해서 그리기
groupby_mean = groupby_mean.sort_values(
    ['조회'], ascending=False).reset_index(drop=True)  # 이전 인덱스 삭제
groupby_sum = groupby_sum.sort_values(
    ['조회'], ascending=False).reset_index(drop=True)

# 조회수 평균 그래프 그리기
sns.barplot(y='학년반', x='조회', data=groupby_mean)  # 그래프 그리기
plt.show()

# 활용2 - 조회수 전체 합 그래프 그리기
plt.figure(figsize=(12, 8))
sns.barplot(y='학년반', x='조회', data=groupby_sum)
plt.show()

