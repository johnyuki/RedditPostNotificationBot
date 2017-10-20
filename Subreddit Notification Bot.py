import praw
import config
import time
from playsound import playsound

# Name of subreddits to watch.
# Separate subreddits with a + symbol as shown below.
# Do not include the "/r/" part, just the name of the sub.
SUBREDDITS = 'subreddit1+subreddit2+subreddit3'


def connect_to_reddit():
    try:
        reddit = praw.Reddit(
            username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent
        )
        return reddit
    except Exception as e:
        print(e)
        time.sleep(60)


def notify(submission):
    try:
        print('Found a new post in {}: {}'.format(submission.subreddit, submission.shortlink))

        # This is the name of the file that gets played when it finds a new post.
        # You can change the file to whatever you like, as long as you update it below.
        playsound('NotificationSound.mp3')
    except Exception as e:
        print(e)
        time.sleep(60)
    

def main():
    try:
        start_time = time.time()
        reddit = connect_to_reddit()
        while True:
            for submission in reddit.subreddit(SUBREDDITS).stream.submissions():
                if submission.created_utc > start_time:
                    notify(submission)
    except Exception as e:
        print(e)
        time.sleep(60)


if __name__ == '__main__':
    main()
