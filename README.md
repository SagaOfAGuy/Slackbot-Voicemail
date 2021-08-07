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

Inside the file, set the values similiar to the output below:

**NOTE**: To find your logout link for the **LOGOUT** variable, navigate to the login link or LINK in this case via web browser, and inspect the element of the logout button. The logout link should be stored within the href of an anchor tag.


```bash
  1 NUM=Your_Voicemail_Username
  2 SEC_CODE=Your_Security_Code
  3 LINK=Your_Login_Link
  4 LOGOUT=Your_Logout_Link
  5 CHANNEL_ID=your_slack_channel_id
  6 SLACK_TOKEN=xoxb-your_bot_token
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

Save the .env file, and source the LoadEnv file. This file should export the environmental variables you created within the .env file.

```bash
# Give bash file executable permissions
(Voicemail-Closing)[user@user Linux]$ chmod u+x LoadEnv.sh

# Source and execute LoadEnv file
(Voicemail-Closing)[user@user Linux]$ source ./LoadEnv.sh
```

Verify that environmental variables are included by running the `printev` command.

```bash
(Voicemail-Closing)[user@user Linux]$ printenv

# Printenv Sample Output
TERM_PROGRAM=vscode
TERM=xterm-256color
SHELL=/bin/zsh
SLACK_TOKEN=your_token
CHANNEL_ID=Your_Channel_ID
...
```

## **Scheduling**

Use Crontab to schedule the bot to execute on a regular interval:

```bash
[user@user Linux]$ crontab -e

# Crontab entry for scheduling bot to run every week at Friday, 4:00PM and piping output to a log file

00 16 * * 5 cd /your/directory/to/bot && ./SlackBot.sh &> info.log
```

Save this entry, and the bot should run every week at 4:00PM on Fridays

## **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## **License**

[MIT](https://choosealicense.com/licenses/mit/)
