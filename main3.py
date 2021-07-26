print(abs(3.23))
print(abs(-3.23))
#abs 함수가 숫자의 절댓값을 만들기에 음수가 양수로 출력됨.

print(len("혼공프"))
print(len([1, 2]))
print(len({"이름": "혼공프", "사용언어": "파이썬", "대상독자": "입문자"}))
#문자의 개수를 구할수있음.

print(sum([500, 20, 3]))
print(sum([3, 0.23]))
#데이터의 합계를 구할수있음.

def print_names():
  print("커피 장인")
  print("여의도 본점")
print_names()
#함수 써보기

def get_shop_name():
  return "커피 장인"
print(get_shop_name())

def get_shop_name():
  return "커피 장인"
def get_branch_name():
  return "여의도 본점"
def print_names():
  print(get_shop_name())
  print(get_branch_name())
print_names()

order_detail = []
def make_order(name, qty):
  order_detail.append({"이름": name, "수량": qty})
print(order_detail)
make_order("아메리카노",2)
make_order("플랫 화이트", 1)
print(order_detail)

numbers = [1, 3, 5, 7, 9]
numbers.append(2)
print(numbers)

def is_odd_number(arg):
  if arg % 2 == 1:
    return True
  return False
print(is_odd_number(3))
print(is_odd_number(2))