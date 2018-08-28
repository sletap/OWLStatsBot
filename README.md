# OWLStatsBot
An Overwatch Statistics bot that pulls statistics on Overwatch League players from Overwatch League or over.gg

## Getting Started 
There are two different standalone files that are capable of extracting information. OWLSiteStats and OverGGStats. OWLSiteStats is preferred, as it has the most content, but OverGG contains some released players that are no longer on the OWL website.

Comment IDs will be automatically be written in an external file that will ensure a comment is not replied to more than once

### Prerequisites
```
A reddit account with API access
A completed config file
PRAW
Python 3.0+
Beautiful Soup 4
```
### Usage
start the bot with ```python3 OWLSiteStats.py```
while running, when a user comments with ```!stats [PLAYER NAME]``` The reddit bot will then fetch stats from a list, format it, and post it to the user

## File Rundown
* OWLBot.py - Reddit bot that runs using information from OWLSiteStats.py
* OWLSiteStats.py - parses information from Overwatch League website, but it uses HTML files from pages.py. At the moment gathering information from the Overwatch League Website is not automated, so HTML files are posted in form of strings in pages.py.
* OverGGStats.py - parses information from Over.gg, fully automated
* config.py - example file for how the config should be set up using reddit API information
* pages.py - Overwatch League html files that are parsed by Beautiful Soup 


## Author
* Sahil Patel
