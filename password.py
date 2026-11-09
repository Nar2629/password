password = "admin123"

while True:
  if input("enter password: ") == password:
    print("access granted!")
    break
  print("incorrect password. try again.")
