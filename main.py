import os
import subprocess

def find_roblox_shortcut():
    # Get the Desktop directory for the current user
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    roblox_shortcut = os.path.join(desktop_path, "Roblox Player.lnk")

    if os.path.exists(roblox_shortcut):
        return roblox_shortcut
    else:
        return None

def open_executables():
    # Find the Roblox Player shortcut
    roblox_path = find_roblox_shortcut()

    # Define the path to BootstrapperNew.exe in the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bootstrapper_path = os.path.join(script_dir, "BootstrapperNew.exe")

    # Open Roblox Player if the shortcut is found
    if roblox_path:
        try:
            subprocess.Popen(["cmd", "/c", "start", roblox_path], shell=True)
            print("Roblox Player opened successfully.")
        except Exception as e:
            print(f"Failed to open Roblox Player: {e}")
    else:
        print("Roblox Player shortcut not found on the Desktop.")

    # Open BootstrapperNew.exe if it exists
    if os.path.exists(bootstrapper_path):
        try:
            subprocess.Popen(bootstrapper_path)
            print("BootstrapperNew.exe opened successfully.")
        except Exception as e:
            print(f"Failed to open BootstrapperNew.exe: {e}")
    else:
        print("BootstrapperNew.exe not found in the script directory.")

    # Open the first Command Prompt with a custom message
    custom_message_1 = (
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

    try:
        subprocess.Popen(f"cmd /c echo {custom_message_1} && pause", shell=True).wait()
    except Exception as e:
        print(f"Failed to open first Command Prompt: {e}")

    # Open the second Command Prompt with a different custom message
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

    try:
        subprocess.Popen(f"cmd /c echo {custom_message_2} && pause", shell=True).wait()
    except Exception as e:
        print(f"Failed to open second Command Prompt: {e}")
