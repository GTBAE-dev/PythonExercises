'''퀴즈4
당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였다.
댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
추첨 프로그램을 작성하시오.
조건1: 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 과 샘플을 활용
(출력 예제)
--당첨자 발표--
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
--축하합니다--
'''

from random import*

lst = list(range(1, 21))
shuffle(lst)
print("치킨 당첨자:", lst[0])
print("커피 당첨자:", lst[1:4])

shuffle(lst)
winners = sample(lst, 4)
print("치킨 당첨자:", winners[0])
print("커피 당첨자:", winners[1:])