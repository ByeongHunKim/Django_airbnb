# V1 ------------------------------------------------------
class Human:
  def __init__(self, name):
    print("human class initialized")
    self.name = name

  def say_hello(self):
    print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
      self.xp = xp

class Fan(Human):
  def __init__(self, name, fav_team):
    self.fav_name = fav_team

nico = Fan("hunsman", "DRX")
# V1 ------------------------------------------------------

# V1을 실행시켰을 때 print("human class initialized") 가 콘솔에 찍히지 않는다.
# Human 클래스의 init 메서드를 호출하고 있지 않다.
# init 메서드를 호출해야만 하는 이유는 Human 클래스는 name이 필요하기 때문이다.
# Human 클래스의 init 메서드를 호출하기 위해서는 super라는 함수를 사용해야한다.
# super 함수는 Human 클래스에 접근할 수 있는 권한을 준다. -> super().__init__()

# V2 ------------------------------------------------------
class Human:
  def __init__(self, name):
    print("human class initialized")
    self.name = name

  def say_hello(self):
    print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
      self.xp = xp

class Fan(Human):
  def __init__(self, name, fav_team):
    super().__init__(name)
    self.fav_name = fav_team

nico = Fan("hunsman", "DRX")
nico.say_hello()
# V2 ------------------------------------------------------

# V2에서가 파이썬에서의 상속이다.
# __init__ 이라는 형식 때문에 js, ts, Java, C#과 다르다. 하지만 로직은 같다.
# 다른 클래스를 상속할때면, 그 클래스의 constructor를 호출해야한다.
# 파이썬에서는, super 함수를 사용해줘야한다. 이 함수가 해당 클래스에 접근할 권한을 주게 된다.