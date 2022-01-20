#Initialise
for i in range(1):
  num1 = input("Enter a denary number bigger than 0 ")
  try:
    int(num1)
    test = 0
    positive = int(num1)
    if positive<1:
      positive = "no"
    else:
      positive = int(num1)
  except ValueError:
    test = 1
    positive = "no"
  
  while test == 1 or positive == "no":
    num1 = input("Enter a number bigger than 0 ")
    try:
      int(num1)
      test = 0
      positive = int(num1)
      if positive<1:
        positive = "no"
      else:
        positive = int(num1)
    except ValueError:
      test = 1
      positive = "no"
  
  
  num = int(num1)
  answer = ""
  shifter = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  shift=[]

#Base settings
base = 0
while base < 2 or base > 36:
  base = int(input("What base should this number be converted to? (options are from 2-36)"))

#Converting to individual parts of the full number 
while num>0:
  binari = num%base
  num = num//base
  shift.append(binari)
  
#Converting to final number
for i in range(len(shift)):
  newnum = shifter[shift[i]]
  answer = str(newnum)+answer

print(answer)
  
