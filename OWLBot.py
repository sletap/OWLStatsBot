import praw
import config
import os
import time
import OWLSiteStats
import pages

commentFile = "CommentsRepliedTo.txt"

# logs the bot in
# credentials are stored in an external file (config) for security
def initializeBot():
	print("Currently Logging in \n")
	login = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "/u/Sahil0719's OVERgg Bot")
	return login

# what comment to search for on what subreddit, and what to reply with
def runBot(Bot, CommentsRepliedTo, fullDataSet, players):
	for comment in Bot.subreddit('test').comments(limit=25):
		if "!stats" in comment.body and comment.id not in CommentsRepliedTo and comment.author != Bot.user.me():
			body = comment.body.split(" ")
			player = body[1]

			reply = OWLSiteStats.writeStats(player, players, fullDataSet)
			comment.reply(reply + "\n ^(stats are provided by) ^[OWL](https://overwatchleague.com/en-us/stats), ^(this bot was created by /u/Sahil0719)")

			print("a reply has been made for " + str(comment.author))

			CommentsRepliedTo.append(comment.id)
			with open (commentFile, "a") as f:
				f.write(comment.id + "\n")

# this helps make sure a comment is not replied to more than once
def get_saved_comments():
	if not os.path.isfile(commentFile):
		comments_replied_to = []
	else:
		with open(commentFile, "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")

	return comments_replied_to

def main():
	RedditBot = initializeBot()
	CommentsRepliedTo = get_saved_comments()
	fullDataSet = []
	OWLSiteStats.statisticsFactory(fullDataSet,pages)
	players = OWLSiteStats.makePlayersList(fullDataSet)

	while True:
		print("running instance of server")
		runBot(RedditBot,CommentsRepliedTo,fullDataSet,players)
		time.sleep(10)

if __name__ == "__main__":
	main()