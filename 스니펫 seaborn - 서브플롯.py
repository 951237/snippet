# 그래프 라이브러리 호출
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='NanumBarunGothic')  # 글꼴 설정하기

# plt.figure(figsize=(6,16))
fig, ax = plt.subplots(1, 3, figsize=(16, 4))  # 그래크 갯수 정하기 1줄에 3개 그리기

sns.lineplot(x="year", y='avgPrice', data=df_cabbage, ax=ax[0])  # 1번 그래프
sns.lineplot(x='year', y='avgTemp', data=df_cabbage, ax=ax[1])  # 2번 그래프
sns.lineplot(x="year", y='rainFall', data=df_cabbage, ax=ax[2])  # 3번 그래프
ax[0].set_title('Price')  # 1번 그래프 제목
ax[1].set_title('Temp')  # 2번 그래프 제목
ax[2].set_title('rainFall')  # 3번 그래프 제목
plt.suptitle('Main')  # 그래프 전체 제목
plt.show()

