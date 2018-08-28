# OWLStatsBot
An Overwatch Statistics bot that pulls information on Overwatch League players from Overwatch League or over.gg 

## Getting Started 
There are two different standalone files that are capable of extracting information. OWLSiteStats and OverGGStats. OWLSiteStats is preferred, as it has the most content, but OverGG contains some released players that are no longer on the OWL website.

Comment IDs will be automatically be written in an external file that will ensure a comment is not replied to more than once

### Prerequisites
```
A reddit account with API access
A filled out config file
PRAW
Python 3.0+
Beautiful Soup 4
```
### Usage
start the bot with ```python3 OWLSiteStats.py```
when a user comments with ```!stats [PLAYER NAME]``` The reddit bot will then fetch stats from a list, format it, and post it to the user
