import schedule

from src.calc import MessageCreator


def job():
    mc = MessageCreator(username)
    mc.get_message()
    print(mc.message)


print("Please enter your GitHub username: ")
username = input()

schedule.every().day.at("19:00").do(job)  # TODO: add custom time

while True:
    schedule.run_pending()
