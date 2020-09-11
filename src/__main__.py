import schedule

from src.calc import ReportCreator


def job():
    mc = ReportCreator(username)
    mc.get_report()
    print(mc.report)


username = input("Please enter your GitHub username: ")
ask_time = input("Please enter the time at which you want to receive notifications (24h format): ")

schedule.every().day.at(ask_time).do(job)

while True:
    schedule.run_pending()
