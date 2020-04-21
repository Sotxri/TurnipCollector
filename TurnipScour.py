import random
import sys
import time
import praw



##reddit initiates the praw instance. If you change the bot name in your .ini, you will need to change it here as well.
##stichwoerter is the list of keywords triggering the bot
##submissions is the subreddit you want to search in for. Pre-set to acturnips.
##Start_time is the exact time you started the bot. Uses it to go from that point forward.
##Wartezeit is an array of random times on how long to wait until the next posts
##non_bmp_map formats the output for the python console
##Antworten is an array of random Lines to comment in case there are none available.
##You can un-comment the "print(submission...))" down below to see the full text of each submission

##You can comment all the "time.sleep" lines to speed up the bot.
#WARNING: THIS IS NOT RECOMMEND AS IT WILL LIKELY GET YOU BANNED!

##Again, use the bot at your own risk!



reddit = praw.Reddit('bot1', user_agent='Owned by Quentin')

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
stichwoerter= ['selling', 'Timmy', 'Tommy', 'buying',
               'Selling', 'Buying', 'turnips', 'Turnips']
keywords = stichwoerter
submissions = reddit.subreddit('acturnips')
start_time = time.time()

wartezeit = [23, 56, 120, 32, 12, 63, 234]

print("Digging through:",submissions.display_name)
def kommentiere():
        Antworten = ["Count me in!", "Can I come over?", "Would love to join <3"]
        Antwort = random.choice(Antworten)
        if not len(comment_list) == 0:
            Random = random.choice(comment_list)
            Zeit = random.choice(wartezeit)
            if Random.author != "AutoModerator":
                Kommentar = Random.body
                print("Commented: ", Kommentar.translate(non_bmp_map))
                print(20*"-")
                submission.reply(Kommentar)
                time.sleep(Zeit)

                print("Waiting: ", Zeit, "seconds")
            else: print("Bot chosen")
        if len(comment_list) == 0:
            print("Random Line: ", Antwort)
            submission.reply(Antwort)


try:
        for submission in submissions.stream.submissions():
            if submission.created_utc < start_time:   
                continue
            if not submission.stickied:
                for stichwort in stichwoerter:
                    if stichwort in submission.title.lower():
                        print(20*"-")
                        print("Title: ", submission.title)
                        #print(submission.selftext.translate(non_bmp_map))
                        submission.comments.replace_more(limit=0)
                        time.sleep(18)
                        comment_list = list(submission.comments)
                        kommentiere()
except Exception as err:
        print("An Error Occurred! You probably can't post due to low Karma or a mute/ban")
        print("Press ENTER to close the script")
        input()


        


        

        

