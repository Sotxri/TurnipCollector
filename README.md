# TurnipCollector
**_Hear ya, hear ya! Get your Turnips sold fast and easy!_**
![](images/Daisy.png)
_Drawn by Kreamy Kae. Visit her on [her Tumblr](https://kreamykae.tumblr.com/)_

This bot is designed to scour through the acturnips subreddit to find any posts related to selling/buying.
## Requirements
- [ ] A Reddit account
- [ ] Your OAuth Tokens
- [ ] A basic text editor

I won't go into much detail, but it is explained [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example).
You will need to go [there](https://www.reddit.com/prefs/apps) and follow the [Guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example) on how to set everything up!

After you have all the neccessary tokens, open up the _praw.ini_ and just paste the tokens at the written position. Save, and you're done! 
It should look something like this:
```
[bot1]
client_id=XXXXXXXXXXXX
client_secret=XXXXXXXXXXXXXXXXXXXXX
username=XXXXXXXXXXXXXXXX
password=XXXXXXXXXXXXXX

```
Of course, the Xs are replaced by your IDs.

I just want to point out, that having a little bit of Karma on the used account is kinda neccessary, without it, you will only be able to post **ONCE** in 10 Minutes.
 

## Features

- Bot copies other peoples comments -> gets around questions like "Whats your favourite Villager"
- Bot doesn't copy the AutoModerator (would be pretty obvious lol)
  - print out: 
    > "Bot chosen"
- Bot doesn't spam, waits a semi-random amount of time after each comment
  - print out:
    > "Waiting X seconds"
- If no comments exists, bot posts a random, pre-written Line. 
  - print out: 
    > "Random Line X"
- Constant scanning of new submissions for set keywords


## Clearing a few things up
This bot can only post on a Reddit submission, so the author notices you. Actually taking the spot in the line is your task.

Thats it! Happy Hunting


## Upcoming Updats
- [X] Make the Bot recognize Mod
- [X] Get Error Print
- [ ] Be able to give minimum Amount of price



