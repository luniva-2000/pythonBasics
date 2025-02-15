Sname= input("Enter your name:")
len_of_name= len(Sname)
space_index=0
for i in range (len_of_name):
    if Sname[i]==' ':
        space_index = i
print (f"Your email is {Sname[0:space_index].capitalize()}.{Sname[(space_index+1):]}@westminstercollege.edu.np")
#******************************************
lon=[1,2,3,4,5,6]
lon.sort()#method
sorted(lon)#function
print(lon)
lon.pop(1)
lon.pop()
#*******************************************
lon= [1,2,3,4,5,1,9]
lon