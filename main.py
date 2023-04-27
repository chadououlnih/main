print("salam")
myName = "Ahmed"
print("my name is "+ myName)
myAge = 60
#print("I am "); print(myAge)
a = input("Whats your name visitor: ")
print("hello "+a)
b = int(input("What's your age: "))
if b < myAge:
    print("you are younger then me, still have to grow", myAge - b, " years")
elif b > myAge:
    print("You are older then me, I still have to grow"+ b - myAge+ " years")
guess = int(input("Can you guess my age: "))
while myAge!= guess:
 if guess < myAge:
  print("I am sorry")
  guess = int(input("try Again: "))
 elif guess > myAge:
  print("I am sorry")
  guess = int(input("try Again: "))
 else:
  break
print("you guessed it right!!")