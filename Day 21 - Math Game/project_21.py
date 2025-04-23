print("Math Game!")
user_number = int(input("Name your multiples: "))
score = 0

for i in range(1, 11):
  user_answer = int(input(f"{i} x {user_number} = "))
  if user_answer == user_number * i:
    print("Great work!")
    score += 1
  else:
    print(f"Nope. The answer is {user_number * i}.")

if score == 10:
  print("Wow 10/10 🥳! You are great at math!")
else:
  print(f"You scored {score} out of 10 correct.")