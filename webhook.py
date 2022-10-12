#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Webhook.py"""
#IMPORTS
import sys
from warnings import filterwarnings as filter_warnings
from colorama import Fore
import ujson
import readline
from discord_webhook import DiscordWebhook  # type: ignore

#UJSON
with open("config.json", "r") as cfg:
    config: dict = ujson.load(cfg)
with open("web.json", "r") as hok:
    web: dict = ujson.load(hok)

#VAR'S
prefix = config['prefix']
bye_message = config['bye']
hi_message = config['hi']

#WEBHOOK JSON PORT
print(f"{Fore.RED} Would u like to import a webhook?")
yn =input("Y/n: ")
if yn == "Y":
    print("Type out value. 'web.json'")
    webhookput=input("value: ")
    webhookrn = web["replaceme".replace("replaceme", webhookput)]
if yn == "y":
    print("Type out value. 'web.json'")
    webhookput=input("value: ")
    webhookrn = web["replaceme".replace("replaceme", webhookput)]
if yn == "N":
    print(Fore.RESET)
    webhookrn =input(f"{Fore.BLUE}webwook:{Fore.RESET}")
if yn == "n":
    print(Fore.RESET)
    webhookrn =input(f"{Fore.BLUE}webwook:{Fore.RESET}")

WEBHOOK_URI: str = webhookrn    

def main() -> int:
    """Entry/main function"""
    DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=hi_message).execute()
    while True:
        if not (msg := input(f"{Fore.RED}Message:{Fore.RESET} ")).strip():
            continue
        
        if msg == f"{prefix}.logout":
            DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=bye_message).execute()
            print("Logged out.")
            print(Fore.RESET)
            exit()
        if msg == f"{prefix}.range":
            print("spam:")
            msg = input("message: ")
            spamm = input("times: ") 
            for _ in range(int(spamm) - 1):
                DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=msg).execute()
            continue
    
        if msg == "FIND.prefix":
            print(f"Ur current prefix is: {prefix}")
            continue
        
        if msg == f"{prefix}.src":
            DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content="https://github.com/lenvxcodes/webhookpy").execute()
            continue
        
        DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=msg).execute()

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"
    filter_warnings("error", category=Warning)
    sys.exit(main())
