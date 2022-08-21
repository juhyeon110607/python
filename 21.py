#capitalize = 0번째 인덱스의 문자를 대문자로 변경시킨다.
# file_name = "보고서.xlsx"[
# print(file_name.endswith("xls"))
# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))
# a = "hello world"
# print(a.split('_'))
# l = [] # l은 비어있는 리스트
# a = [1,2,3] #a는b = ] 원소 1, 2, 3이 들어있는 리스트
# b = ['A','B','C'] #b는 'A','B'가 들어있는 리스트
# c = [1,2,'a','B'] #c는 1,2,'A','B'
# d = [[1,2,3], [4,5,6]] #d는 [1,2,3]과 [4,5,6]이 들어간 리스트
# print(a[0])
# print(b[0])
# print(d[0])
# print(len(a))   # 리스트의 길이 == 리스트가 가지고 있는 원소의 개수
# a = [4,1,4,[5,8,[9,7],3],6]
# print(a)
# print(a[3])
# print(a[3][2])
# print(a[3][2][1])
# a = [4,1,3,2]
# b = [5,8,6]
# #리스트의 원소(값)수정
# #a[2] = 5 리스트 a에서 2위치에 5로 수정
# #리스트의 원소(값) 삭제
# del a[2] #리스트 a에서 2번째 위치한 값을 삭제하겠다.
# print(a)
# #리스트 끼리의 덧셈
# print(a+b)
# #리스트와 정수의
# print(b * 3)
a = [4,1,3,2]
#원소추가
# a.append(5) #append(값) = 리스트의 마지막 인덱스 번호에 값을 추가한다.
#원소 삽입
# a.insert(2,8) #insert(인덱스번호, 값) = 리스트의 해당 인덱스 위치에 값을 삽입한다.
#순서 반전
# a.reverse() #reverse() = 리스트의 순서를 반전 시킨다.
#정렬)
# 리스트의 순서를 정렬하다.(정렬 기준은 그기, 기본은 오름차순)
# a.sort()
# a.sort(reverse = True) #sort(reverse = True) ㅡ= 리스트의 순서 정렬(내림차순)
#원소
# print(a.pop(2))  #pop() = 마지막 인덱스 번호에 위치한 값을 추출
#pop(2) = 2번째 인덱스 번호에 위치한 값을 추출
# print(a.index(3)) #index(값) = 리스트 내에 해당 값이 있는지 확인
#있을 경우 인덱스 번호를 , 없을 경우 에러 반환
#원소 제거
# a.remove(3)   #remove(값) = 리스트 내에 해당 값을 삭제
#없는 값을 삭제할 경우 에러 반환
#리스트 확장
# b=[7,8,9]
# # a.extend(b)
#  #extend(리스트, 튜플 등 순서가 있는 자료형)
#             #괄호 안에 적은 자료형의 길이 만큼 확장
# # a.append(b)  #append(값/자료형) 자료형의 길이와 상관없이 마지막 인덱스의 추가
# print(a)
movie_rank=["닥터 스트레인지","스플릿","럭키"]
movie_rank.append("배트맨")
movie_rank.insert(1,"슈퍼맨")
del movie_rank[3] #remove도 있음
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
print(lang1+lang2)
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
#57번
# nums = [1,2,3,4,5,6,7]
# print(min(1,2,3,4,5)) #min(값1,값2,값3.......) = 여러 값들 중 최소값을 반환
# print(max(1,2,3,4,5)) #max(값1,값2,값3.....)  여러 값들 중 최소값을 반환
# print(min(nums))
# print(max(nums))
nums = [1, 2, 3, 4, 5]
total = sum(nums) #sum(a) == a안에 있는 값들을 모두 더한 값을 반환, 기본값이 0
print(total)
nums = [1, 2, 3, 4, 5]
#평균 = 총합 / 개수
total = sum(nums)
n = len(nums)
print(total / n)