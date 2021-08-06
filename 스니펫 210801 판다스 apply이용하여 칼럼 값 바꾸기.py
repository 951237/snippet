# 적용함수 생성하기
def func1(row):
	if 'cat' in row:
		return 'C type'
	elif 'stl' in row:
		return 'S type'
	elif 'bw' in row:
		return 'B type'
	else:
		return 'Non type'

# item칼럼에 위의 함수 
df['item'].apply(func1)
