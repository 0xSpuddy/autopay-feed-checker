import os
from datetime import datetime
from datetime import timezone

from dotenv import load_dotenv
from eth_utils import to_checksum_address
from web3 import Web3

from autopay_feed_checker.autopay_abi import autopay_abi


load_dotenv()


NODE_ENDPOINT = os.getenv("NODE_ENDPOINT")


w3 = Web3(Web3.HTTPProvider(NODE_ENDPOINT))
autopay_contract = w3.eth.contract(
    address=to_checksum_address("0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"), abi=autopay_abi
)


def convert_unix_timestamp(timestamp: int) -> str:
    utc_time = datetime.utcfromtimestamp(timestamp)
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(tz=None)
    local_time_string = local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    return local_time_string


def check_single_feed() -> None:
    feed_to_check = input("Enter feedId: ")
    info_list = autopay_contract.functions.getDataFeed(_feedId=(feed_to_check)).call()
    reward, balance, start_time, interval, window, price_threshold, reward_increase, _ = info_list
    print(f"Base Reward: {reward / 10**18} TRB")
    print(f"Remaining TRB in Feed: {balance / 10**18} TRB (includes unclaimed)")
    print(f"Start Time of First Interval: {convert_unix_timestamp(start_time)}")
    print(f"Interval between tip windows: {(interval/60)/60} hours ({(interval/60)} minutes)")
    print(f"Tip window is open for: {(window/60)/60} hours ({(window/60)} minutes)")
    print(f"The reward will increase {reward_increase / 10**18} TRB per second until a qualifying submission is mined.")
    if price_threshold != 0:
        print(f"Tip will be paid if associated spot price changes {price_threshold/100}%")
    else:
        print("(No tips paid for price moves)")
