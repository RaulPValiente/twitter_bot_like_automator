# Twitter Retweet+Like Bot

This script automates the process of liking and retweeting a specific tweet using Twitter bot accounts.

## Requirements

- Python 3.x
- Selenium
- WebDriver for your chosen browser (in this case, Chrome WebDriver is used)

## Usage

1. Make sure Google Chrome is completely closed, including from the bottom right menu.
2. Run the program in your preferred Python environment.
3. The program will like and retweet a specific tweet.
4. It will do it one time per bot.

## Installation

1. Clone or download this repository to your local machine.

2. Install the necessary dependencies using pip:

```bash
pip install selenium
```

3. Download the corresponding WebDriver for your browser and make sure to add its location to the system PATH.

## Configuration

- bot_accounts: List of dictionaries containing the credentials of the bot accounts. You can add as many bots as you wish in this format.
- tweet_url: URL of the tweet you want the bots to like and RT.

## Note

- It's important to note that using bots to automate actions on Twitter may violate the platform's terms of service. Use it at your own risk and make sure to respect Twitter's policies.
- This script uses Selenium WebDriver to interact with the Twitter web interface. Make sure you have the correct version of WebDriver for your browser installed and configured correctly.
