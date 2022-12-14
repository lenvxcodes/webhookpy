#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Webhook.py"""
#IMPORTS
import sys
import os
from warnings import filterwarnings as filter_warnings
from colorama import Fore
import ujson
import readline
from discord_webhook import DiscordWebhook  # type: ignore
from discordwebhook import Discord
from random import randint

#UJSON
with open("config.json", "r") as cfg:
    config: dict = ujson.load(cfg)
with open("web.json", "r") as hok:
    web: dict = ujson.load(hok)

#VAR'S
prefix = config['prefix']
bye_message = config['bye']
hi_message = config['hi']
webhookrn = '1'
lucktip = randint(0, 50)
luck = lucktip

if luck == 45:
    print(f"{Fore.YELLOW}Fun Fact{Fore.RESET}: Ur got lucky today! U got the rare message. Hope ur having a great day.")

#WEBHOOK JSON PORT DEF
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
#LOGIN
def login(): 
    msg = None
    print(f"{Fore.RED} Would u like to import a webhook?".strip())
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
        WEBHOOK_URI: str = webhookrn  
    if yn == "n":
        print(Fore.RESET)
        webhookrn =input(f"{Fore.BLUE}webwook:{Fore.RESET}")
        WEBHOOK_URI: str = webhookrn  
WEBHOOK_URI: str = webhookrn    
discord = Discord(url=webhookrn)
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
            login()

        if msg == f"{prefix}.quit":
            DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=bye_message).execute()
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

        if msg == f"{prefix}.help":
            print(f"""
            {Fore.YELLOW + "FIND" + Fore.RESET}.prefix - prints out ur prefix.
            {Fore.YELLOW + prefix + Fore.RESET}.logout - logs out and prints ur bye message, if is it null it does not print.
            {Fore.YELLOW + prefix + Fore.RESET}.range - spams, "u can get ip banned -ari" stay safe.
            {Fore.YELLOW + prefix + Fore.RESET}.src - if u want to print out my github link to webhook.py
            {Fore.YELLOW + prefix + Fore.RESET}.help - for list of the commands (Used)
            {Fore.YELLOW + prefix + Fore.RESET}.pic - Sends a file. in files folder.
            {Fore.YELLOW + prefix + Fore.RESET}.embed - embed message
            {Fore.YELLOW + prefix + Fore.RESET}.quit - quits script with a bye message
            """)
            continue

        if msg == f"{prefix}.embed":
            print(f"{Fore.RED}Embed Edior{Fore.RESET}")
            titleembed=input("Title:")
            contentembed=input("Content:")
            discord.post(embeds=[{"title": titleembed, "description": contentembed}],)
            continue
        
        if msg == f"{prefix}.pic":
            print("Type the files name Example: helloworld.png")
            fileok=input("pic.")
            discord.post(file={"webhookpy": open(f"files/{fileok}", "rb")})
            os.system('clear')
            print(f"Posted {fileok}")
            continue

            
            
        if msg == f"{prefix}":
            print(f"Usage: {Fore.YELLOW + prefix + Fore.YELLOW}.[COMMAND]") 
            continue

        if msg == f"{prefix}.":
            print(f"Usage: {Fore.YELLOW + prefix + Fore.YELLOW}.[COMMAND]") 
            continue

        if f"{prefix}." in msg:
            print(f"{Fore.RED}INVALID COMMAND{Fore.RESET}. Use {prefix}.help for list of comamnds.") 
            continue

        DiscordWebhook(url=WEBHOOK_URI, rate_limit_retry=True, content=msg).execute()

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"
    filter_warnings("error", category=Warning)
    sys.exit(main())
