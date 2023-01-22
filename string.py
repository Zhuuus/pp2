print ('hello teacher')
print ("how are you?")
print (" ")



a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print (a) 


print (' ')
for x in "banana":
  print(x)

print (' ')
txt = "The best things in life are free!"
if(("free" in txt) == True):
    print ('Yes')

else :
    print ('No')


print (' ')
b = "Привет, мир!"
print(b[-5:-2])


print (' ')
c ="Hello world"
print (c.upper())
 
print (' ')
print (c.lower())

print (' ')
print(c.strip("Hello "))

print (' ')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  
