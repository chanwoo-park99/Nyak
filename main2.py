count = 1
while count < 4:
  print(str(count) + "!")
  count = count + 1
  
count = 3
while count > 0:
  print(count)
  count = count -1

egg_list = ["달걀1", "달걀2", "달걀3"]
for egg in egg_list:
  print("달걀 프라이를 만듭니다.")

egg_list = ["달걀1", "달걀2", "달걀3"]
for egg in egg_list:
  print(egg + ": 달걀 프라이를 만듭니다.")

egg_list = range(3)
for egg in egg_list:
  print("달걀 프라이를 만듭니다.")

egg_list = range(3)
for egg in egg_list:
  print(str(egg) + " : 달걀 프라이를 만듭니다.")

count = range(3)
for n in count:
  print(str(n + 1) + "!")
  break
  print("이후의 코드는 처리되지 않습니다.")

count = range(30)
for n in count:
  print(str(n + 1) + "!")
  if (n + 1) == 3:
    print("그만!")
    break

count = range(10)
for n in count:
  if(n + 1) % 3 != 0:
    continue
  print(str(n+1) + "!")
  