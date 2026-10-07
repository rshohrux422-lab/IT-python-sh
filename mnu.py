import calendar

foydalanuvchi=int(input("Yilni kiriting :"))
oy=int(input("Oyni kiriting :"))

print(calendar.month(foydalanuvchi,oy))

print("Balki bugun sizni tug'ulgan kuniyizdir")

while True:
    jonitin=input("Qachon tug'ilgan kuniyiz :")
    joni=int(input("raqamda yozish uchun :"))
    if joni == 29:
        print("Tabrik jonitin")
        break