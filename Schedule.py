import schedule
import time
import os

# Enable voicemail and take screenshot
def Close():
	os.system("./SlackBot.sh &>./Log.log")
	os.system("rm Close.png")

# Send screenshot to slack channel
def ScheduleSlackMessage(timing):
	schedule.every().thursday.at(timing).do(Close)
	while True:
		schedule.run_pending()
		time.sleep(1)

# main method
if __name__=="__main__":
	ScheduleSlackMessage("23:12")
	
