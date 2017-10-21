# Reddit Notification Bot

*Plays and sound and gives you the link when a new post has been made in any of the subreddits that you have defined.*

# Setup instructions
*Instructions are for Windows. I've never done this on any other OS so I cannot help, sorry.*

- Download Python 3.6 from the Python website here - https://www.python.org/downloads/

- When installing, make sure you select "add python to PATH environment" or whatever that box is. I can't remember the exact wording, but it is something along those lines. You can just spam click "next" after checking that box.

- After it is completed, open your command prompt and type in *pip install praw* and wait for it to install. Then type *pip install playsound*. Once they are both installed you can close the command prompt. 

- Download this program by clicking on the green *Clone or Download* button, followed by *Download ZIP*. After it downloads, extract the *Subreddit Notification Bot.py*, *config.py*, and *NotificationSound.mp3* files anywhere you like. Make sure you keep them together in the same folder/directory.

- Open your start menu and type *IDLE*, and open the program that is called *IDLE (Python 3.6 32-bit)*. It might also be 64-bit instead of 32-bit. 

- When the window opens, go to *File > Open* and select the *config.py* file that you just extracted.

- Next, to create a bot account on Reddit, create a new Reddit account like you normally would. After it is created, go to *preferences > apps > create new app*. Make sure you select *script*. Call the bot whatever you like, and in the *redirect uri* box, enter *http://localhost:8080*. Then click create.

- Go back to IDLE and follow the instructions that I commented in for you in the *config.py* file. (Everything with a hash symbol before it. The text should be red.)

- After you entered in all of the credentials for your bot, save *config.py*, close it, and open *Subreddit Notification Bot.py*. Enter in the subreddits that you would like it to watch for you, and then press F5 to run it. If everything works correctly, a shell window (black window that looks like windows command prompt) should appear, and any time a post is made, it should display text in the shell, as well as the link to the post. You can close the window that has all the code in if you want to. 

If you cannot get the bot set up using these instructions or the bot crashes with an error message, head over to https://www.reddit.com/r/redditdev and make a text post there. Make sure you link this github page so that we can help you quicker and let us know what the problem is. 

