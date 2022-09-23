print()
print()
from time import sleep
 
note_1 = "** Hello! My name is TrinhHien"

 
for c in note_1 :
    print(c, end='', flush=True)
    sleep(0.05) 
print()
 
input('>> Nhập họ và tên của bạn:\n')
print()
 
from time import sleep
note_1 = "*                       Tuyệt Vời"
print()
for c in note_1:
    print(c, end='', flush=True)
    sleep(0.03) 
print()
 
import time as t
countdown = range(10,110, +10)
for i in range(len(countdown)):
    print("*                       Đang xử lý: ",countdown[i], end = "")
    print("%")
    t.sleep(0.5) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("*                       Hoàn tất....")
 
with open("aa.txt", "r") as fh: 
    for line in fh:
        print(line.strip())
        t.sleep(0.1)