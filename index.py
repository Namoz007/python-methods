#string bilan ishlash
# a = "SALOM dunyo"
# b = "h\te\tl\tl\to"
# c = "Nimadir kimdir yana{new:.0f} nima lalala"
# son = "12345"
# a = a.capitalize()     matndagi eng birinchi sozdagi harfni katta harf qilip beradi
# a = a.title()          matndagi barcha sozlarni birinchi harfini katta harf bilan chiqaradi
# a = a.casefold()       matnni barcha sozlarini kichik harf qilip beradi
# a = a.center(25)       matndagi sozlarni surip beradi
# z = a.count("Salom")   matnda qidirilayotgan soz nechta ekanligini hisoblaydi. 
# a = a.encode()         matn qatorini kodlaydi
# x = a.endswith(".")    matn satrini tinish belgisi bilan tugashini aniqlaydi
# b = b.expandtabs(5)    matndagi sozlarni tab orqali qancha oringa surishni belgilaydi
# a = a.find("m")        matndan biror bir soz yoki harfni qidiradi va indeksini kursatadi
# c = c.format(new = 49) matnni hohlagan joyiga biror bir raqamni yozip bera oladi
# a = a.format_map()                organilmadi
# a = a.index("a")       matndan biror bir harf qaysi orinda turgaini tekshiradi
# a = a.isalnum()        matnda alfanurmek ekanini tekshiradi: harf va raqamlar bolsa true, probel bolsa false, yana boshqa
# a = a.isalpha()        matnni barchasi harf yoki yuqligini tekshiradi, agar probel bolsa ham false beradi
# a = a.isascii()        matnda acii bolmaganlardan qochishni anglatadi
# y = son.isdecimal()    matndagi sonlar 10 kasr ekanini tekshiradi va bu matn str kurinishida bulishi shart
# a = a.isdigit()        matn yoki elementni son ekanini tekshiradi
# a = a.isidentifier()   satr haqiqiy identifikator ekanini tekshiradi
# a = a.islower()        matn yoki elementni barchasi kichik harfmi yuqmi tekshiradi
# son = son.isnumeric()  matnni barchasi raqam yoki raqam emasligini tekshiradi
# a = a.isprintable()    matndagi barcha narsa chop etiladimi yoki yuq
# a = a.isspace()        matndagi barcha element probel ekanligini tekshiradi
# a = a.istitle()        matndagi har bitta soz katta harf bilan boshlangan yoki yuqligini tekshiradi
# a = a.isupper()        matndagi barcha sozlar katta harfda yozilgan yoki yozilgani yoqligini tekshiradi
# a = "&".join(a)        matndagi har bitta sozdan keyin biror bir belgini qoyip beradi
# a = a.ljust(20)        matndan keyin joytashlanadi
# a = a.lower()          matndagi barcha sozlarni kichik harfga ogirp beradi
# a = a.lstrip()        matnning chap tarafidan tosiqlarni olip tashlaydi
# b = a.partition("Salom")  matndan sozni qidirip uni uchga ajratadi
# a = a.zfill(20)       matn 20ta element bolmasa uni 0 bilan toldiradi
# a = a.swapcase()      matndagi kichik harflarni katta kattalarini esa kichik harf qilip beradi
# a = a.startswith("Salom") matn qaysi soz bilan boshlanganligini aniqlaydi
# a = a.splitlines()    matnni har bitta qatorini [] qausga olib beradi
# a = a.split()         matndagi har bitta sozni [] ni ichida ' '  olib beradi
# x = a.rstrip()        matn oxiridagi boshliqlarni olib tashlaydi
# a = a.removeprefix("Salom")    matnda berilgan biror bir sozni uchirip beradi
# a = a.rsplit()        matndagi har bitta sozni [] ni ichida ' '  olib beradi
# a = a.rpartition("dunyo") matndan biror bir sozni oxiridan qidirradi va uni ' ' oladi
# print(a)







#listlar bilan ishlash

# new = [1,9,7,6,8,5]
# num = [10,15,19]

# new = new.count(5)        listda nechta raqam borligini aniqlaydi
# new = new.clear()         listni tozalaydi
# neww = new.copy()         listni boshqa bir uzgaruvchiga nusxalaydi
# new.append(5)             listni oxiriga biror bir element qoship beradi
# new.extend(num)           listga boshqa bir listni qoship qoyish
# a = new.index(5)          listdan biror bir element qayerda turganligini aytadi
# new.insert(0,555)         listni aytgan joyingizdan biror bir qiymat qoship beradi
# new.pop()                 listdagi eng oxirgi qiymatni ochiradi
# new.remove(6)             listdagi kursatilgan elementni ochirip yuboradi
# new.reverse()             listni oxiridan boshiga qarab sortlaydi
# new.sort()                listni osish tartibida sortlaydi

# print(new)




#setlar bilan ishlash
# st = {"Apple","Microsoft","Facebook","Amazon"}
# st1 = {"Apple","Microsoft"}
# st.add("Google")          setga qiymat qoshadi
# st.clear()                setni ichini tozalaydi
# lst = list()              set uchun yangi list ochish
# lst = st.copy()           3setdagi malumotlarni listga nusxalanyapti
# a = st.difference(st1)    ham birinchi ham ikkinchi setda yuq malumotlarni chiqaradi
# st.difference_update(st1) ikkala setda ham bor malumotlarni olib tashlaydi
# st.discard("Apple")       setdagi biror bir qiymatni olib tashlaydi,uni remove()dan farqi yuq malumot berilganda hatolik bermaydi
# a = st.intersection(st1)  ikkala setda ham bor malumotlarni chiqaradi
# st.intersection_update(st1) ikkala setda ham mavjud bolmagan narsalarni olib tashlaydi
# a = st.isdisjoint(st1)    birinchi setdagi narsalar ikkinchi setda umuman bolmasa True qaytaradi
# a = st1.issubset(st)      birinchi setdagi barcha malumotlar ikkinchi setda bolsa True qaytaradi
# a = st.issuperset(st1)    birinchi setdagi malumotlar ikkinchi setda mavjud bolsa True
# st.pop()                  doim birinchida turgan malumotni uchirip yuboradi
# st.remove("Apple")        listda berilgan qiymatni uchirip yuboradi
# a = st.symmetric_difference(st1) birinchi setda mavjud ikkinchisida esa yuq bolgan malumot qaytaradi
# st.symmetric_difference_update(st1) ikkala setda ham mavjud bolgan narsalarni olib tashlang
# a = st1.union(st)         ikkala setdagi barcha malumotlarni takrorlamasdan boshqa set qiladi
# st1.update(st)            ikkala setdagi malumotlarni takrorlamasdan qoshadi
# print(st)                  




#dictionary bilan ishlash

# dct = {
#     'apple' : 'olma',
#     'ananas' : 'ananas',
#     'watermelon' : 'tarvuz',
#     'melon' : 'qovun',
#     'orange' : 'apelsin',
#     'lemon' : 'lemon',
#     'strawberry' : 'qulupnay'
# }

# a = dct.values()          dictdagi valuelarni qaytaradi
# dct.clear()               dictni tozalaydi
# a = dct.copy()            dictdagi malumotlari nusxalaydi
# y = 0                     keys qiymatlari
# a = dct.fromkeys(dct,y)   dictning barcha keyslariga biror bir bir xil qiymat beradi
# a = dct.get("melon")      dictning biror bir qiymatini olib beradi
# a = dct.items()           dictning barcha qiymatlarini olib beradi
# a = dct.keys()            dictning barcha keylarini olib beradi
# dct.pop('apple')          dictdagi biror bir keyni uchirip tashlaydi
# dct.popitem()             dictdagi oxirgi keyni olib tashlaydi
# a = dct.setdefault('cherry','olcha') dictdan key orqali biror bir qiymatni oling, yoki biror bir qiymat qushing
# dct.update({'cherry': 'olcha'}) dictga biror bir element qoshadi
# print(dct)
# print(a)



#ichma ich dictga murojat qilish

# cars  = {
#     'bmw' : {
#         'full_name' : 'bmw m5',
#         'color' : 'black',
#         'motor' : 4.5,
#         'sped' : 2.3,
#         'audi' : {
#             'full_name' : 'audi',
#             'color' : 'white',
#             'motor' : 2.5,
#             'sped' : 4.7,
#             'bugatti' : {
#                 'full_name' : 'bugatti chiron',
#                 'color' : 'blue',
#                 'motor' : 4.2,
#                 'sped' : 2.4
#             }
#         }
#     }
# }

# print(cars['bmw']['audi']['bugatti']['motor'])