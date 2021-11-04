class Player:
    type = 'player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

# 클래스 변수 사용
print(Player.type)

# 클래스 함수 호풀
Player.where() # error
Player.where(player) # ok : palyer.where() 와 같다.
