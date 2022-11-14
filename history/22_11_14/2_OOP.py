# constructor 메서드가 python class에서 어떻게 동작하는가?
# constructor 메서드는 class가 생성될 때 호출되는 함수다.


# V1 ------------------------------------------------------
# class Player:

#   # self는 class의 instance를 가리킨다.
#   def __init__(self):
#     self.name = "nico"

# nico = Player()
# print(nico.name)
# output : nico

#-------------------------------------------------------

# 배운 점 : Python class에 constructor 이름의 메서드가 없다는 것을 배웠고 
# constructor가 아니라 __init__ 이라고 불린다는 것을 배웠다.
# 그리고 우리는 이 메서드가 여기서 self와 함께 불린다는 것을 배웠다.
# self는 여기 있는 class 자체를 가리킨다. (TS의 this의 의미)

# Player의 이름을 dynamic하게 생성하고 싶다면(1000개의 Player를 만들면 모두 Nico라는 이름이 될 것이기 때문)
# 우리가 할 수 있는 것은 여기에 더 많은 parameter를 추가하는 것







# V2 ------------------------------------------------------
class Player:

  # self는 class의 instance를 가리킨다.
  def __init__(self, name, xp):
    self.name = name
    self.xp = xp

# nico = Player()
# parameter를 넣어줘야한다. 아니면 아래 에러 발생
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'xp'

nico = Player("hunsman", 1000)
print(nico.name, nico.xp)
# output : hunsman 1000
#-------------------------------------------------------

# python은 private이나 public을 지원하지 않고, type도 지정해주지 않는다.
# 그래서 우리는 문자열인지, 숫자인지 지정해줄 필요가 없다.

# 가장 중요한 건 python class 안에 있는 "모든" 메서드는 self를 가장 첫번째 parameter로 한다는 것