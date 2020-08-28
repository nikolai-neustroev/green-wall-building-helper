from src.calc import MessageCreator

print("Please enter your GitHub username: ")
username = input()
mc = MessageCreator(username)
mc.get_message()
print(mc.message)
