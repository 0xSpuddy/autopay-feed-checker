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
python3 -m venv venv
```
```sh
source venv/bin/activate
```

```sh
pip install -e .
```

### Usage
Add your rpc and webhook urls to `.env` file. Update the `INTERVAL` to your desired frequency.

**To begin monitoring block height**
```sh
monitor
```
