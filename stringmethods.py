txt = "how r u"
y = txt.capitalize()
print (y)
txt = "how r u"
y = txt.casefold()
print(y)
txt = "apple"
y = txt.center(10)
print(y)
txt = "I love mangoes, mango is my favorite fruit"
y = txt.count("mango")
print(y)
txt = "i am a student"
y = txt.encode()
print(y)
txt = "Hello."
y = txt.endswith(".")
print(y)
txt = "H\te\tl\tl\to"
y =  txt.expandtabs(7)
print(y)
txt = "i am a student"
y = txt.find("student")
print(y)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt = "i am a student"
y = txt.index("student")
print(y)
txt = "Coordinate12"
y = txt.isalnum()
print(y)
txt = "coordinateX"
y = txt.isalpha()
print(y)
txt = "Coordinate123"
y = txt.isascii()
print(y)
txt = "\u0033" #unicode for 3
y = txt.isdecimal()
print(y)
txt = "25"
y = txt.isdigit()
print(y)
txt = "Demonstration"
y = txt.isidentifier()
print(y)
txt = "i am a student"
y = txt.islower()
print(y)
txt = "25"
y = txt.isnumeric()
print(y)
txt = "how r u"
y = txt.isprintable()
print(y)
txt = "      "
y = txt.isspace()
print(y)
txt = "i am a student"
y = txt.istitle()
print(y)
txt = "How r u"
y = txt.isupper()
print(y)
myTuple = ("rose", "lilly", "jasmine")
y = "#".join(myTuple)
print(y)
txt = "mango"
y = txt.ljust(15)
print(y, "is my favorite fruit.")
txt = "hey how r u"
mytable = txt.maketrans("h", "P")
print(txt.translate(mytable))
txt = "I could eat mangoes all day"
y = txt.partition("mangoes")
print(y)
txt = "I like bananas"
y = txt.replace("bananas", "apples")
print(y)
txt = "Mi casa, su casa."
y = txt.rfind("casa")
print(y)
txt = "Mi casa, su casa."
y = txt.rindex("casa")
print(y)
txt = "mango"
y = txt.rjust(15)
print(y, "is my favorite fruit.")
txt = "I could eat mangoes all day, mangoes are my favorite fruit"
y = txt.rpartition("mangoes")
print(y)
txt = "apple, banana, cherry"
y = txt.rsplit(", ")
print(y)
txt = "     banana     "
y = txt.rstrip()
print("of all fruits", y, "is my favorite")
txt = "     mango     "
y = txt.rstrip()
print("of all fruits", y, "is my favorite")
txt = "Hello My Name Is rose"
y = txt.swapcase()
print(y)
txt = "     mango      "
y = txt.strip()
print("of all fruits", y, "is my favorite")
txt = "Welcome to my world"
y = txt.title()
print(y)
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
txt = "how r u"
y = txt.upper()
print(y)
txt = "5"
y = txt.zfill(10)
print(y)
