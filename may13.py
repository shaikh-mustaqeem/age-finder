jay=int(input("enter jay age"))
viru=int(input("enter viru age"))
gabbar=int(input("enter gabbar age"))
if jay>viru and jay>gabbar:
    print("jay is oldest")
elif viru>jay and viru>gabbar:
    print("viru is oldest")
else:
    print("gabbar is oldest")