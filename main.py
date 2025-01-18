import os
import subprocess

def find_roblox_shortcut():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    roblox_shortcut = os.path.join(desktop_path, "Roblox Player.lnk")
    return roblox_shortcut if os.path.exists(roblox_shortcut) else None

def open_executables():
    roblox_path = find_roblox_shortcut()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bootstrapper_path = os.path.join(script_dir, "BootstrapperNew.exe")

    if roblox_path:
        try:
            subprocess.Popen(["cmd", "/c", "start", roblox_path], shell=True)
            print("Roblox Player opened successfully.")
        except Exception as e:
            print(f"Failed to open Roblox Player: {e}")
    else:
        print("Roblox Player shortcut not found on the Desktop.")

    if os.path.exists(bootstrapper_path):
        try:
            subprocess.Popen(bootstrapper_path, shell=True)
            print("BootstrapperNew.exe opened successfully.")
        except Exception as e:
            print(f"Failed to open BootstrapperNew.exe: {e}")
    else:
        print("BootstrapperNew.exe not found in the script directory.")

    # Display the first custom message
    custom_message_1 = (
        "echo.\n"
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
        "pause"
    )
    subprocess.Popen(f"cmd /c {custom_message_1}", shell=True)

    # Display the second custom message
    custom_message_2 = (
        "     ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⢀⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢠⣿⠻⢄⠑⢄⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠉⠀⠀⠠⡙⠢⣈⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠈⣢⣿⣿⡄⠈⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠈⠉⠉⠻⣏⣺⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣤⣤⡄⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⡿⢷⢀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠄⡀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢄⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⡀⠀\n"
    )
    subprocess.Popen(f"cmd /c {custom_message_2}", shell=True)

open_executables()
