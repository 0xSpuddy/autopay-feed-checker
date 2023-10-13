# Autopay Feed Checker

A script for reading information about Tellor Autopay Feeds.

### Clone repo and cd
```sh
git clone https://github.com/0xSpuddy/autopay-feed-checker
```
```sh
cd autopay-feed-checker
```
```sh
mv .env.example .env
```

### Setup

```sh
python3 -m venv env
```
```sh
source env/bin/activate
```

```sh
pip install -e .
```

### Usage
Add your rpc to the `.env` file.

**To See Information About a Single Feed**
```sh
checkfeed
```
