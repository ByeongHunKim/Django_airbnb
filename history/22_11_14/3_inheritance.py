# V1 ------------------------------------------------------
# class Player:
#   def __init__(self, name, xp):
#     self.name = name
#     self.xp = xp

#   def say_hello(self):
#     print(f"hello my name is {self.name}") 

# class Fan:
#   def __init__(self, name, fav_team):
#     self.name = name
#     self.fav_name = fav_team
# V1 ------------------------------------------------------

# 이 상황에서 상속을 활용하여 이 두 class에서 반복적인 부분을 추상화하는 것

# 솔루션은 반복되는 코드를 저장할 다른 클래스를 만드는 것

# V2 ------------------------------------------------------
class Human:
  def __init__(self, name):
    self.name = name

  def say_hello(self):
    print(f"hello my name is {self.name}") 

class Player(Human):
  def __init__(self, name, xp):
    self.xp = xp



class Fan(Human):
  def __init__(self, name, fav_team):
    self.fav_name = fav_team


hunsman_player = Player("hunsman", 100)
hunsman_player.say_hello()

hunsman_fan = Fan("hunsman_fan", "DRX")
hunsman_fan.say_hello()
# V2 ------------------------------------------------------

# Human은 Player와 Fan class의 공통된 부분의 코드를 갖게될 것.

# Player와 Fan을 위해 self.name, say_hello를 받아오고 싶다면 받고싶은 class함수에서 괄호를 열고 Human이라고 해주면 된다.
# class Fan(Human): <- 이걸 해줌으로써 Human class에서부터 모든 것을 가져온다.