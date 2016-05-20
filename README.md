# CSUIBot

## How the Bot Works

There are two ways for the bot to get updates from Telegram: long polling and webhook. In this project, we are using webhook. Using `setWebhook` method provided by Telegram API, we can associate a bot with a webhook URL so that whenever there is an update (a new message, a new member joining a group, etc.), Telegram will send the update data to the webhook URL in a JSON format. The general steps are as follows:

1. An update occurs in a chat or group of which the bot is a member.
1. Telegram sends the update to the bot's webhook URL as HTTP POST request containing JSON data.
1. Server makes a request to Telegram via its Bot API to initiate bot's response, while responding with 200 status to the HTTP POST request made by Telegram.

More detailed information can be found [here](https://core.telegram.org/bots/api#getting-updates).

## Development Guide

### How to set up your machine

1. Setup your Python virtual environment using [venv](https://docs.python.org/3/library/venv.html) as you did in week 8 tutorial. Name your virtual environment folder as `env`. If you use PyCharm, you may want to configure it to recognize your virtual environment too.

1. Navigate to the directory where you've cloned this repo and create a virtual environment under the `env` directory. Then, activate the virtual environment.

1. Still in the directory where you've cloned this repo, install all its dependencies.

    ```bash
    pip install -r requirements.txt
    ```

    Dependencies are all listed in `requirements.txt`. To re-generate this file (after you've installed new packages), simply run `pip freeze > requirements.txt`. For Linux users, if you have a problem installing the dependencies, install `python3-dev` or `python3-devel` system package first.

1. Create `.env` file under the project root directory. It contains the configuration variables for the application. Sample `.env` file can be found in `.env.example`.

1. Run the app

    ```bash
    python manage.py runserver
    ```

1. The app is now running! To check that the bot is actually running, try to send a GET request to it, for instance:

    ```bash
    curl http://127.0.0.1:5000
    ```

    or open `http://127.0.0.1:5000` from your browser. You should get a response that says:

    ```bash
    Bot is running
    ```

### How to run the tests/linters

1. Make sure you already installed [pytest][pytest] and [flake8][flake8]. Both are listed in `requirements.txt` so if you followed the instructions to setup your machine above then they should already be installed.

1. Put an `.env` file under your `tests` directory. This file could be identical to the one in project root directory or you may also set some environment variables for testing to your liking.

1. You can run the tests and linters with `python manage.py test` and `python manage.py lint` respectively.

1. To run both linters and tests in one command, you can use `python manage.py check`. This is useful to check your code before making a merge request.

1. For more info on what you can do with `manage.py`, run `python manage.py --help`.

[pytest]: http://pytest.org/latest/
[flake8]: https://pypi.python.org/pypi/flake8

### How to Contribute

If you want to write new features to CSUIBot or fix bugs, that's great! Here is a step-by-step guide to contribute to CSUIBot's development.

#### General Flow

1. You need an issue on Pivotal Tracker about your contribution. This can be a bug report (in which case your contribution is the bug fix) or feature suggestion (in which case your contribution is the implementation).

1. Make sure that you are in `master` branch by running `git status`. If not, run `git checkout master` to move to `master` branch.

1. Create a new branch on which you write your code. Use any branch name as you which. For example, `cool-feature`:

    ```bash
    git checkout -b cool-feature
    ```

1. Implement your contribution in the branch.

1. Periodically, and after you committed your changes, pull the latest changes from master. This ensures your branch is always up-to-date with the origin.

    ```bash
    git pull --rebase origin master
    ```

    Fix any conflicts that may arise.

1. After you really finished writing the code, commit your changes. You may create one or more commits.

1. Push the feature branch to `origin`:

    ```bash
    git push origin cool-feature
    ```

1. Create a new merge request on Gitlab for `cool-feature` branch to be merged to `master`. Refer the Pivotal Tracker's issue in the merge request description.

1. Wait for other project members and class instructors to review your contribution.

1. If they approve your contribution, congrats! Your contribution may be merged to master. First, don't forget to rebase your branch against master:

    ```bash
    git pull --rebase origin master
    ```

    Again, fix any conflicts that may arise.

1. Then, clean up your commits. Do a interactive rebase (please Google this term).

    ```bash
    git rebase -i origin/master
    ```

    Squash all your commits into one commit only and rewrite the commit message into a meaningful one, preferably mentioning what feature/bugfix your changes introduce.

1. Force-push your feature branch to origin:

    ```bash
    git push -f origin cool-feature
    ```

1. Ask the class instructors to merge your contribution to master.

1. After your contribution is merged, you may safely delete your feature branch:

    ```bash
    git branch -D cool-feature
    ```

    Also delete your feature branch on origin from Gitlab.

    ```bash
    git push origin :cool-feature
    ```

1. Done!

### How to Test Your Bot Locally

Suppose we're going to test our handler for `/about` command.

1. Set your `.env` file if you'd like. The following instructions will assume that you set your `.env` file exactly the same as the example provided in `.env.example`:

    ```
    APP_ENV="development"
    DEBUG="true"
    TELEGRAM_BOT_TOKEN="somerandomstring"
    LOG_LEVEL="DEBUG"
    WEBHOOK_HOST="127.0.0.1"
    ```

1. Start your bot locally by running `python manage.py runserver`. Make sure you've already activate your virtual environment before issuing this command.

1. Open `csuibot/handlers.py` file and take a look at `help` handler.

    ```python
    @bot.message_handler(commands=['about'])
    def help(message):
        app.logger.debug("'about' command detected")
        about_text = (
            'CSUIBot v0.0.1\n\n'
            'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
        )
        bot.reply_to(message, about_text)
    ```
    
    Notice that we have `bot.reply_to(message, about_text)`. This line means that we're sending a reply message containing the text stored in `about_text` variable to Telegram. However, note that in our configuration file (i.e. `.env` file) we are using a fake Telegram bot token, i.e. `somerandomstring`. So, this line will fail. Even if we're using real bot token, this line will most likely fail since we're going to use a fake data (this will be clear later). So, for testing locally, we don't want this behavior. We should assume that this line will work correctly since we're using `PyTelegramBotAPI` library for this. We should replace that line, for instance with a `print` statement:
    
    ```python
    # bot.reply_to(message, about_text)
    print(about_text)  # we print the about text instead of sending it
    ```

1. Now, we are going to simulate someone invoking `/about` command to our bot. From [Telegram Bot API](https://core.telegram.org/bots/api#setwebhook),

    > Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update.

    so we need to make a POST request containing an `/about` command. To do this, you may want to use an HTTP client tool, such as [Cocoa REST client](http://mmattozzi.github.io/cocoa-rest-client/) for OSX, [Postman extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop) for Google Chrome, or [RESTclient add-on](https://addons.mozilla.org/en-US/firefox/addon/restclient/) for Firefox. If you prefer to use `curl` it's fine too.

    Our webhook URL is `http://localhost:5000/somerandomstring`. Telegram's Update object containing `/about` command in JSON format look like this:

      ```json
      {
          "update_id": 1,
          "message": {
              "message_id": 1,
              "date": 12345,
              "chat": {
                  "id": 123,
                  "type": "group"
              },
              "text": "/about"
          }
      }
      ```

    The data above is obviously fake. The most important thing is our message has `/about` as its text. Other fields are mandatory so we can simply fill them with fake data. You can find what fields are required for each types in [Telegram Bot API types documentation](https://core.telegram.org/bots/api#available-types).

    Now, make a POST request to our webhook URL with the above JSON as its payload. If you're using `curl`, the command look like this

    ```bash
    curl -H "content-type: application/json" --data '{"update_id": 1, "message": {"message_id": 1, "date": 12345, "chat": {"id": 123, "type": "group"}, "text": "/about"}}' http://localhost:5000/somerandomstring
    ```

    Please find out by yourself on how to make such request using your chosen HTTP client.

1. Take a look at your terminal window where you've started the bot. You should see the about text printed to the screen like so:

    ```
    CSUIBot v0.0.1

    Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!
    ```
    
    This means when the `/about` command is invoked, our handler is run.

In summary, to test your bot locally all you need to do is simulating Telegram sending an Update to your webhook URL via HTTP POST request with the update data in JSON format as its payload. But be careful not to actually send a bot reply since the bot token and/or the data are fake.
