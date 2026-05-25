"""discordmess = '''
1 2 3
12'''
print(discordmess * 10)
"""
s1 = "Dhs fuck bitch"
s2 = "fuck"
s3 = ";bfnfnfwj"
#kiem tra co o str nào là con str nào k
if s2 in s1:
    print("disscoer wefjir")
else:
    print("CFGVU")
if s1 in s3:
    print("dd oon r")
else:
    print("hiwfhuwefh")
#viết hoa chữ cái đầu
s2 = s2.capitalize()
print(s2)
#viết hoa all
s2 = s2.upper()
print(s2)
#Đổi lại viết thường
s2 = s2.lower()
print(s2)

s = "Im friends with the monster that's under my bed Get along with the my my voices inside of my head You're trying to save me, stop holding your breath And you think I'm crazy, yeah, you think I'm crazy"
#tìm vị trí 1 cụm trong str nếu k có thì trả output = -1
print(s.find("crazy"))
print(s.find("fuck"))
#đếm xem xhien bao nhieu lan
print(s.count("my"))
#thay thế
s = s.replace("my" , "BD")
print(s)
#cắt chuỗi
huh = s.split(" ")
print(huh)



