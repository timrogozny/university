sit = int(input("enter sit number"))
if sit % 2 == 0:
    print ("upper sit in coupe")
elif sit % 3 == 0:
    print ("upper sit on the side")
elif sit % 6 == 1:
    print("down sit in coupe")
else:
    print("dowm sit on the side")
