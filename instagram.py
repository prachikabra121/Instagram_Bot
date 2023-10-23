from instabot import Bot
bot=Bot()
bot.login(username="cameron_virgo12", password="P@rachi*888")
#bot.follow("wscubtechindia")

#bot.upload_photo("python.jpg",caption="&&")
#bot.unfollow("wscubetechindia")
#bot.send_message("Hello",['wscubetechindia'])
#followers=bot.get_user_followers("cameron_virgo12")
#for follower in followers:
    #print(bot.get_user_info(follower))
    
following=bot.get_user_following("cameron_virgo12")
for Following in following:
    print(bot.get_user_info(Following))