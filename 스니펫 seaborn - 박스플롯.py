# 데이터프레임 칼럼 2개를 라인 그래프로 그려서 비교하기
plt.figure(figsize=(12, 6))  # 그래프 크기 설정하기

# x축을 데이터의 크기만큼 설정해서 데이터프레임의 칼럼값으로 그래프 그리기
sns.lineplot(x=range(585), y=test['src'], data=test)    # x축을 range를 이용해서 피처 갯수만큼 585개를 생성
sns.lineplot(x=range(585), y=test['predict'], data=test)

