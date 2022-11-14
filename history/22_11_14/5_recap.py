# super 함수의 사용과 중요성을 이해하는 것이 아주 중요하다.

# Django에서 클래스로부터 확장하는 일이 많은데 시간을 아낄 수 있다.
# 가끔 super를 호출하는 일, 메서드 오버라이딩 사용, 가끔 부모 클래스로부터 메서드 호출

class Dog:
  def woof(self):
    print("woof woof")

class Beagle(Dog):
  def woof(self):
    super().woof()
    print("super woof")

beagle = Beagle()
beagle.woof()

# super를 항상 init 메서드를 호출할 때만 사용할 필요는 없다. init 메서드가 아닌 다른 메서드에서도 사용할 수 있다.
# 부모 클래스를 사용하고 싶을 때 super를 사용할 수 있다.

# Django는 굉장히 많은 클래스들을 가지고있는데, 이것들을 상속받는다면 굉장히 시간을 아낄 수 있다.
