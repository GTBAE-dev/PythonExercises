'''
퀴즈3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1: http:// 부분은 제외 ->naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 ->naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내'e' 갯수 + "!"로 구성
결과예: nav51!
'''

web = "http://naver.com"
rule1 = web[7:]
rule2 = rule1.find(".")
rule3 = rule1[0:rule2]
print("pw = ", rule3[0:3], len(rule3), rule3.count("e"), "!", sep = "")

web = "http://goodevening.com"
rule1 = web[7:]
rule2 = rule1.find(".")
rule3 = rule1[0:rule2]
print("pw = ", rule3[0:3], len(rule3), rule3.count("e"), "!", sep = "")
