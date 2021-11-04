
# 클래스에서 반드시 생성자는 없어도 된다 .
# 싱글톤 : 객체 인스턴스가 딱 하나인 경우 ( 유일한 객체 )
# 용도 : 사용중인 소프트웨어에서 글로벌하게 쓸 수 있는 기능을 만들려고

class Star:
    type = 'star'
    x = 100

    # 꼭 self를 쓰지 않아도 됨
    def change():   # parameter 를 안받기 때문에 에러가 발생함
        # 위 x는 전역인데 이와 다르게 아래 x는 지역변수이다.
        x = 200
        print('x is ', x)

print('x is ', Star.x) # ok
Star.change()
print('X is ', Star.x)

star = Star()
print('x is', star.x)
star.change()

# star.change()
#
# -->
# TypeError: change() takes 0 positional arguments but 1 was given
# 파이썬은 Star.change(star) 로 바꿔서 해석한다
# 파이썬의 변수는 그 자체가 포인터 이다.




