#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example webhook implementation"""
import sys
from warnings import filterwarnings as filter_warnings
from colorama import Fore
import ujson
import readline

from discord_webhook import DiscordWebhook  # type: ignore
with open("config.json", "r") as cfg:
    config: dict = ujson.load(cfg)
bye_message = config["bye"]
hi_message = config["hi"]
print(f"{Fore.RED} Would u like to import a webhook?")
yn =input("Y/n: ")
if yn == "Y" or  "y":
    print("Import:")
if yn == "N" or "n":
    print(Fore.RESET)
    pass
    
webhookrn =input(f"{Fore.BLUE}webwook:{Fore.RESET}")
WEBHOOK_URI: str = webhookrn


def main() -> int:
    """Entry/main function"""
    DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=hi_message).execute()
    while True:
        if not (msg := input(f"{Fore.RED}Message:{Fore.RESET} ")).strip():
            continue
        if msg == "DISCORD.logout":
            DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=bye_message).execute()
            print("Logged out.")
            print(Fore.RESET)
            exit()
        if msg == "DISCORD.range":
            print("spam:")
            msg = input("message: ")
            spamm = input("times: ") 
            for _ in range(int(spamm) - 1):
                DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=msg).execute()
            pass
            
        DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=msg).execute()

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())