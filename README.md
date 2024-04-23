# Twitter Retweet Bot

This script automates the process of liking a specific tweet using Twitter bot accounts.

## Requirements

- Python 3.x
- Selenium
- WebDriver for your chosen browser (in this case, Chrome WebDriver is used)

## Installation

1. Clone or download this repository.
2. Install the Tweepy library using pip:
3. Replace the placeholder credentials in the code with your own Twitter API credentials.

## Usage

1. Run the program in your preferred Python environment.
2. The program will search Twitter for tweets containing the specified keyword.
3. It will then retweet a maximum number of tweets (specified by `maxNumberOfTweets`) that match the search query.

## Installation

1. Clone or download this repository to your local machine.

2. Install the necessary dependencies using pip:

```bash
pip install selenium
```

3. Download the corresponding WebDriver for your browser and make sure to add its location to the system PATH.

## Configuration

- bot_accounts: List of dictionaries containing the credentials of the bot accounts. You can add as many bots as you wish in this format.
- tweet_url: URL of the tweet you want the bots to like.

## Note

- It's important to note that using bots to automate actions on Twitter may violate the platform's terms of service. Use it at your own risk and make sure to respect Twitter's policies.
- This script uses Selenium WebDriver to interact with the Twitter web interface. Make sure you have the correct version of WebDriver for your browser installed and configured correctly.