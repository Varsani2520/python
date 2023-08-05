# print hello world
print("hello world");

# data type 
#int float string boolean none
#advance data tyoe :list ,tuple ,set,dictionary


#variable
a=10;
print(a);
print(type(a));  #int

b=10.45;
print(b);
print(type(b)); #floaat

a="welcome to my python tutorial";
print(a);
print(type(a)); #string

x=10;
y=34;
print(bool(x>y)) #boolian work  like true or flase 


## type casting   :convert int into float
num=10; #int
print(float(num)) 


##input function:take value from users
name=input("enter your name:");
print(name)


###string in python :it in '',"",''' '''  all are same
x='hello'
y="how"
z='''are you?'''
print(x)
print(y)
print(z)


#method1:count  - it is useed to couunt specific element number
x="partner"
print(x.count('r')) #2 is ans
 #method2 :length
print(len(x))
#method3:title
print(x.title())
#method4:capitalize -first letter capital bija small
print(x.capitalize())
#method5:convert upper case
print(x.upper())
#method6:convert lower calse
print(x.lower())
#strip:remove whitespace
y="    hello  "
print(y.strip())
print(y.lstrip()) #remove left side whitespace
print(y.rstrip()) #remove right side whitespace

#find :used to find word or char  return index number
z="partner hello"
print(z.find('e'))

print(z.rfind('ll'))  #search string value

#replace
a="partner is a ...."
print(a.replace('partner','mental'));

#index
print(a.index('er'))

#slice
name="ramisgood hello how are you"
print(name[1])
print(name[1:4]) 
print(name[:6])
print(name[2:])
print(name[1:8:2])
print(name[0::2])

#escape
# \n new line
# \t tab
# \' single quotes
# \\ backslash

# list method
l1=[1,8,7,2,21,15]
l1.sort();
print(l1)
l1.reverse();
print(l1)
l1.append(34); #add element end of the list
print(l1)
l1.insert(3,65); #in 3 index add 65
print(l1)
l1.pop()
print(l1)
l1.pop(3)
print(l1)
l1.remove(8)
print(l1)
# l1[0]=333
# print(l1[0])



###tuple 
t=(1,2,4,5);
print(t[0])
# t[0]=34
# print(t[0])


###condition
age=34;
if age>34:print("age is valid for voting");
elif age<34:print("hello")
else: print("not valid in voting");


###LOOPS 
##2 TYPE :WHILE AND FOR







