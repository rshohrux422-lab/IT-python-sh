print("WELCOME TO MARKET\n")
print("------OPEN------\n")
print("Salom xaridor")
mahsulotlar={"olma":1200,
             "sabzi":10000,
             "mandarin":9000
}
imkoniyat=1

while imkoniyat < 5:
    xaridor=input("Nima olasiz :").lower()
    if xaridor in mahsulotlar:
       kg=int(input("Nechi kilogram :"))
       print(f"Mana {mahsulotlar[xaridor]*kg}")
       break
    else:
        print("Afsus yo'q")
        imkoniyat+=1