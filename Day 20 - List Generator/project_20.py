print("List Generator")
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int (input("Increment between values: "))
print()
for i in range(start, end + 1, increment):
  print(i)