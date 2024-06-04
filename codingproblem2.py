x,y=1,1
print(x,y,end=" ")
for i in range(8):
    new_term=x+y
    x=y
    y=new_term
    print(new_term,end=" ")
    i+=1