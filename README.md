# Linux/Unix

## **Setting Environmental Variables**

Navigate to the root directory of this project

```bash
(Voicemail-Closing)[user@user]$ cd Voicemail-Closing
```

Create an .env file

```bash
(Voicemail-Closing)[user@user Voicemail-Closing]$ touch .env
```



**NOTE**: To find the logout link for the **LOGOUT** variable, navigate to the login link or LINK in this case via web browser, and inspect the element of the logout button. The logout link should be stored within the href of an anchor tag.

**NOTE:** To find the **VPYTHON** variable, run `pipenv --venv` to grab the directory housing the virtual environment. After acquiring it, append `bin/python3` to the end of it, and set this value to the VPYTHON variable.

Using your favorite text editor, set the values similiar to the output below:
```bash
  1 NUM=Your_Voicemail_Username
  2 SEC_CODE=Your_Security_Code
  3 LINK=Your_Login_Link
  4 LOGOUT=Your_Logout_Link
  5 CHANNEL_ID=your_channel_id
  6 SLACK_TOKEN=xoxb-your_bot_token
  7 VPYTHON=/your/Path/to/Virtual/bin/python3 
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
".env" 4L, 142B
```

## **Scheduling**

To schedule the bot, open the `Schedule.py` file and, change the timing parameter found for the `ScheduleSlackMessage()` function. 

For example, if you want the script to run every thursday at 3:00PM, change line 12 to `schedule.every().thursday.at(timing).do(Close)`, and pass the parameter `"15:00"` to the `ScheduleSlackMessage()` function
```bash
 1 import schedule
  2 import time
  3 import os
  4 
  5 # Enable voicemail and take screenshot
  6 def Close():
  7         os.system("./SlackBot.sh &>./Log.log")
  8         os.system("rm Close.png")
  9 
 10 # Send screenshot to slack channel
 11 def ScheduleSlackMessage(timing):
 12         schedule.every().thursday.at(timing).do(Close)
 13         while True:
 14                 schedule.run_pending()
 15                 time.sleep(1)
 16 
 17 # main method
 18 if __name__=="__main__":
 19         ScheduleSlackMessage("15:00")
 20 
```

Edit and save this file to your preferences

## **Running The Script**
```bash
(Voicemail-Closing)[user@user Voicemail-Closing]$ python3 Schedule.py &
```


## **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## **License**

[MIT](https://choosealicense.com/licenses/mit/)
