# stats from OWL website
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pages

# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics(fullDataSet, page):
	htmlParser = page
	soup = BeautifulSoup(htmlParser, 'html.parser')

	table = soup.find('table', attrs={'class':'Table'})
	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [element.text.strip() for element in cols]
	    fullDataSet.append([element for element in cols if element]) # Get rid of empty values

	return fullDataSet

def statisticsFactory(fullDataSet, pages):
	learnStatistics(fullDataSet, pages.page1)
	learnStatistics(fullDataSet, pages.page2)
	learnStatistics(fullDataSet, pages.page3)
	learnStatistics(fullDataSet, pages.page4)
	learnStatistics(fullDataSet, pages.page5)
	learnStatistics(fullDataSet, pages.page6)

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
		reply = query + " is not available on the OWL Statistics page. Is your player misspelled or been released?"
		return reply
	else:
		reply = "# Statistics for " + query + ":" + "\n\n"
		reply = reply +"**Current Team:** " + fullDataSet[index][1] + "\n\n"
		reply = reply + "---" + "\n\n"
		reply = reply + "**Statistics:**" + "\n\n"
		reply = reply + query + "|stats|" + "\n"
		reply = reply + "---|---:|" + "\n"
		reply = reply + "Eliminations per 10 minutes|" + fullDataSet[index][2] + "|\n"
		reply = reply + "Deaths per 10 minutes|" + fullDataSet[index][3] + "|\n"
		reply = reply + "Damage per 10 minutes|" + fullDataSet[index][4] + "|\n"
		reply = reply + "Healing per 10 minutes|" + fullDataSet[index][5] + "|\n"
		reply = reply + "Total Playtime|" + fullDataSet[index][6] + "|\n"
		reply = reply + "---" + "\n\n"
		return reply

# example run for testing outside of a reddit instance
def main():
	fullDataSet = []
	statisticsFactory(fullDataSet, pages)
	players = makePlayersList(fullDataSet)
	print(writeStats("space", players, fullDataSet))

if __name__ == "__main__":
	main()
