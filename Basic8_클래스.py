'''
퀴즈: 주어진 코드를 활용하여 프로그램을 작성하시오.
(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년(중공)
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    #매물 정보 표시
    def show_detail(self):
        pass
'''

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

total = []
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")
total.append(h1)
total.append(h2)
total.append(h3)
print("총 {0}대의 매물이 있습니다.".format(len(total))) # 리스트 내 갯수는 len으로 찾을 수 있음
for i in total:
    i.show_detail()