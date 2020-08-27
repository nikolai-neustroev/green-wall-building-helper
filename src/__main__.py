from src.calc import MessageCreator

username = 'nikolai-neustroev'  # TODO: replace with input
mc = MessageCreator(username)
mc.get_message()
print(mc.message)
