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

![Screenshot 2023-10-13 at 2 56 31 PM](https://github.com/0xSpuddy/autopay-feed-checker/assets/72078372/1dd56801-6314-41b8-a0a7-a5066616dd31)
