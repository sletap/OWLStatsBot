from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
import time
import html5lib



# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics():
	url = "https://overwatchleague.com/en-us/stats"
	options = Options()
	# options.add_argument('--headless')
	# options.add_argument('--disable-gpu')
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(url)
	time.sleep(3)
	fullDataSet = [] # this is where all the information will be stored

# I have NO idea why this doesn't count page 6 and doublecounts page 2. that's why i had to drop this to work with the sites manually
	page_number = 1
	while page_number <= 6:
		print("current page number is 	" + str(page_number))
		html = browser.page_source
		soup = BeautifulSoup(html, 'html.parser')

		table = soup.find('table', attrs={'class':'Table'})
		table_body = table.find('tbody')
		rows = soup.find_all('tr')

		for row in rows:
			cols = row.find_all('td')
			cols = [element.text.strip() for element in cols]
			fullDataSet.append([element for element in cols if element]) # Get rid of empty values

		link = browser.find_element_by_link_text(str(page_number))
		link.click()
		page_number = page_number + 1


	print(fullDataSet)
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
		reply = query + " is not available. Is your player misspelled or been released?"
		return reply
	else:
		reply = "Statistics for **" + query + "**!:" + "\n\n"
		reply = reply + "**Current Role:** " + fullDataSet[index][1] + "\n\n"
		reply = reply +"**Current Team:** " + fullDataSet[index][2] + "\n\n"
		reply = reply + "---"
		reply = reply + "**Statistics:**"
		reply = reply +"**Total Playtime:** " + fullDataSet[index][3] + "\n\n"
		reply = reply +"**Kills Per 10:** " + fullDataSet[index][4] + "\n\n"
		reply = reply +"**Deaths per 10:** " + fullDataSet[index][5] + "\n\n"
		reply = reply +"**Ults per 10:** " + fullDataSet[index][6] + "\n\n"
		reply = reply +"**Kill/Death Ratio:** " + fullDataSet[index][7] + "\n\n"
		return reply

# example run for testing outside of a reddit instance
def main():
	fullDataSet = learnStatistics()
	# players = makePlayersList(fullDataSet)
	# print(writeStats("shaz", players, fullDataSet))

if __name__ == "__main__":
	main()