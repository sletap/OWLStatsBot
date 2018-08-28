# stats from Over.gg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics():
	htmlParser = urlopen("https://www.over.gg/stats/?event_id=177&series_id=all&hero=all&map_id=all&patch_id=all&min_played=5")
	soup = BeautifulSoup(htmlParser, 'html.parser')

	fullDataSet = [] # this is where all the information will be stored

	table = soup.find('table', attrs={'class':'wf-table mod-stats'})
	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [element.text.strip() for element in cols]
	    fullDataSet.append([element for element in cols if element]) # Get rid of empty values

	return fullDataSet

# creates a list of only players so we can search through them when a user calls for a player
def makePlayersList(fullDataSet):
	players = [] # this is where we will index players
	for player in fullDataSet:
		players.append(player[0])

	return players

# returns the data given the name of a player, which is the query
def writeStats(query, players, fullDataSet):
	# finds where the player is located in the data set
	index = 0
	for person in players:
		if person.lower() == query.lower():
			break	
		else:
			index = index + 1

	# strings for if player does not exist or if a player does exist
	if index >= len(fullDataSet):
		reply = query + " is not available on over.gg. Is your player misspelled or been released?"
		return reply
	else:
		reply = "Statistics for **" + query + "**!:" + "\n\n"
		reply = reply + "**Current Role:** " + fullDataSet[index][1] + "\n\n"
		reply = reply +"**Current Team:** " + fullDataSet[index][2] + "\n\n"
		reply = reply + "---"
		reply = reply + "**Statistics:**"
		reply = reply +"**Total Playtime:** " + fullDataSet[index][3] + "\n\n"
		reply = reply +"**Kills Per 10:** " + fullDataSet[index][4] + "\n\n"
		reply = reply +"**Deaths per 10:** " + fullDataSet[index][6] + "\n\n"
		reply = reply +"**Ults per 10:** " + fullDataSet[index][8] + "\n\n"
		reply = reply +"**Kill/Death Ratio:** " + fullDataSet[index][10] + "\n\n"
		return reply

# example run for testing outside of a reddit instance
def main():
	fullDataSet = learnStatistics()
	players = makePlayersList(fullDataSet)
	print(writeStats("shaz", players, fullDataSet))

if __name__ == "__main__":
	main()