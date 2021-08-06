# Voicemail Closing SlackBot

Bot that automates enabling voicemail closing and sends screenshot of closing action to slack channel

## **Prerequisites**

This project requires the following:

* Slack account
* Sufficient permissions to create apps in a Slack Workspace
* Slack app that's created and ready to go

If you don't have a Slack app, visit [here](https://api.slack.com/authentication/basics#creating) to view the documentation on how to create a slack app.

After you've created a slack app, take note of the ***Bot User Token***, and then, proceed to the following sections:

## **Installation**

Use the package manager [pipenv](https://pipenv.pypa.io/en/latest/) to install dependency packages in the project directory.

```bash
[user@user]$ pipenv install .

Installing dependencies from Pipfile.lock (fdcab6)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
```

Drop into the virtual environment by running `pipenv shell`:

```bash
[user@user Voicemail-Closing]$ pipenv shell
Loading .env environment variables...
Launching subshell in virtual environment...

# The parentheses indicate immersion within a virtual environment
(Voicemail-Closing)[user@user Voicemail-Closing]$
```

Next, find the directory location that will be used by the 'Voicemail-Closing' virtual environment

```bash
[user@user]$ pipenv --venv

# Example output of python3 version used by the Virtual Environment
/Users/user/.local/share/virtualenvs/Voicemail-Closing-AAAAAA
```

Take note of this directory, and append `bin/python3` to the Virtual Environment directory above:

```bash
# Sample Output
/Users/user/.local/share/virtualenvs/Voicemail-Closing-AAAAAA/bin/python3
```

Add this directory to the .env file within the Linux folder under the variable **VPYTHON** if using Linux. If on Windows, simply create an Environmental variable named **VPYTHON** corresponding to this filepath.


## **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## **License**

[MIT](https://choosealicense.com/licenses/mit/)
