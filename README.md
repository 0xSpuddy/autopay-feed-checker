# Autopay Feed Checker

A script for reading information about Tellor Autopay Feeds.

### Clone repo and Setup
```sh
git clone https://github.com/0xSpuddy/autopay-feed-checker
cd autopay-feed-checker
python3 -m venv env
source env/bin/activate
pip install -e .
mv .env.example .env
```
Add your node endpoint to the `.env` file using your favorite text editor.

### Usage

**To See Information About a Single Feed**
```sh
checkfeed
```
You will be prompted to enter the `feedId`.
Enjoy!
