import os
import subprocess
import time
from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

def print_fading_message(message, colors):
    """
    Prints a message with a smooth fade between specified colors.
    :param message: The text to display
    :param colors: List of Colorama color codes for the gradient
    """
    for i, char in enumerate(message):
        color = colors[i % len(colors)]
        print(f"{color}{char}", end="", flush=True)
        time.sleep(0.01)  # Delay for smooth fade effect
    print()  # Newline at the end

def open_first_cmd():
    message_1 = (
        " ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████ ▄████▄  ▄▄▄█████▓ ██▓ ███▄    █   ▄████              \n"
        "▓██▒ ██ ▀█   █    ▒██   ▓█   ▀▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒             \n"
        "▒██▒▓██  ▀█ ██▒   ░██   ▒███  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░             \n"
        "░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓             \n"
        "░██░▒██░   ▓██░ ▓███▒   ░▒████▒ ▓███▀ ░  ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒ ██▓ ██▓ ██▓\n"
        "░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▓▒ ▒▓▒ ▒▓▒\n"
        " ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░ ░  ▒       ░     ▒ ░░ ░░   ░ ▒░  ░   ░  ░▒  ░▒  ░▒ \n"
        " ▒ ░   ░   ░ ░  ░ ░ ░      ░  ░          ░       ▒ ░   ░   ░ ░ ░ ░   ░  ░   ░   ░  \n"
        " ░           ░  ░   ░      ░  ░ ░                ░           ░       ░   ░   ░   ░\n"
        "                              ░                                          ░   ░   ░  "
    )
    colors = [Fore.MAGENTA, Fore.BLUE]
    print_fading_message(message_1, colors)

def open_second_cmd():
    message_2 = (
        "⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠻⢄⠑⢄⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠀⠀⠠⡙⠢⣈⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣢⣿⣿⡄⠈⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠉⠻⣏⣺⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣤⣤⡄⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⡿⢷⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⡀⠀\n"⠀⠀⠀⠀⠀⠀⠀⠀⠀
    )
    colors = [Fore.MAGENTA, Fore.BLUE]
    print_fading_message(message_2, colors)

def main():
    # Open the first custom message
    open_first_cmd()

    # Wait before opening the second message
    time.sleep(2)

    # Open the second custom message
    open_second_cmd()

if __name__ == "__main__":
    main()
