a=int(input())
no_100=a//100
remaining_amount=a-(no_100*100)
no_50=remaining_amount//50
remaining_amount=remaining_amount%50 
no_20=remaining_amount//20
remaining_amount=remaining_amount%20 
no_10=remaining_amount//10

print("100 Notes: "+str(no_100))
print("50 Notes: "+str(no_50))
print("20 Notes: "+str(no_20))
print("10 Notes: "+str(no_10))
