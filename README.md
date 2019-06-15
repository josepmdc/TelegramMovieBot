# TelegramMovieBot
This is a Telegram bot made with Flask for getting movie links from Putlocker. 
It uses web scraping to search for links in the Putlocker website and then send them through the Telegram Webhook API.
In order to connect to the webhook it uses ngrok to expose the localhost, but you can use your own domain and hosting if you wish.

![Demo Gif](https://github.com/josepmdc/TelegramMovieBot/blob/master/MovieBot.gif)

# How to use
First of all you have to create a virtual enviroment and install all the pip packages. To do that use the following commands on the project directory:
```
$ python -m venv venv
$ source venv/bin/activate      (If you are on Windows use this command instead: venv\Scripts\activate)
$ pip install -r requirements.txt
```
Go to Telegram and search for the Botfather bot on the search bar. Once you find it follow the 
instructions to create a new bot.

Botfather will give you a token. Copy that token and paste it in the config.py file on the TOKEN variable.

Download ngrok and start it on port 5000 (It has to be the same port we will have our flask server) with ```ngrok http 5000```. Then copy the https url that it displays on the console. It will be something like this: https://7l2f7c9b.ngrok.io
It is important that you use the https url since Telegram doesn't accept http for security reasons. 

Once everything is set up you can start the falsk server and test your bot. Send a message with the movie title and wait for the response with all the links.
