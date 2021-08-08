'''
quiz) 표준 체중을 구하는 프로그램을 작성하시오
*표준체중: 각 개인의 키에 적당한 체중
(성별에 따른 공식)
남자:키(m)*키(m)*22
여자:키(m)*키(m)*21
조건1: 표준 체중은 별도의 함수 내에서 계산
* 함수명: std_weight
*전달값: 키(height), 성별(gender)
조건2: 표준체중은 소수점 둘쨰자리까지 표시
(출력 예제)
키 175 남자의 표준 체중은 67.38이다.
'''
height = input("키(m) = ")
height = float(height)
gender = input("성별(남자/여자) = ")

def std_weight(height, gender):
    if gender == "여자":
        weight = round(height * height * 21, 2)
        print("키 {0} 여자의 표준 체중은 {1}이다.".format(height, weight))
    elif gender == "남자":
        weight = round(height * height * 22, 2)
        print("키 {0} 남자의 표준 체중은 {1}이다.".format(height, weight))
std_weight(height, gender)