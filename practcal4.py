list1=[1,"hello","rinku",2]
print(type(list1))
print(list1)
print(list1[3:])
print(list1[0:3])
print(list1+list1)
print(list1*6)
list1.insert(1,3)
print(list1)
list1.insert(1,"abc")
print(list1)
list1.remove("hello")
print(list1)


tup=("hello","pavan",8)
print(type(tup))
print(tup)
print(tup[2:])
print(tup[0:2])
print(tup+tup)
print(tup*4)
my_list=list(tup)
my_list.insert(3,5)
print(my_list)

d={1:'pavan',2:'alex',3:'pankaj',4:'chandan'}
print("1st name is:"+d[1])
print("2nd name is:"+d[4])
