import schedule
import time
from datetime import datetime
import os
import threading
from random import randint
from colorama import Back, Fore, Style

thread_container = []

def nothread(target_process):
    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + f"Running Job ==> {target_process} :: Process on {datetime.now()} :: Scheduler Running from {startedTime}")
    os.system(f"{target_process}")


def thread(target_process):
    """ This function is a wrapper function for the function above
        the only addition this function does is to run the jobs in
        parallel and don't wait for the current job to finish

        This utilizes a very basic Java-like thread builtin module,
        it could have be done better with the concurrent futures
        module but some easy maintaining and running threading
        module is used."""
    thread = threading.Thread(target=nothread, args=[target_process])
    thread.start()
    thread_container.append(thread)


def job_loader(commands_text):
    os.path.exists(commands_text)


def main(command_file_):
    global startedTime
    startedTime = datetime.now()
    with open(command_file_, "r") as command_file:
        clean_commands = []
        commands = command_file.readlines()
        for each_command in commands:
            # Comment detection plus empty line detection
            command_length = len(each_command[1:])
            initial_char = each_command[:-command_length]
            if initial_char != "#":
                if command_length >= 8:
                    clean_commands.append(each_command.rstrip('\n'))
    try:
        count = 0
        for each_clean_command in clean_commands:
            try:
                exec(f"{each_clean_command}")
                print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + f"|Scheduled| JN:: {count + 1} :: {each_clean_command}")
            except Exception as e:
                print(Fore.WHITE + Back.RED + Style.BRIGHT + f"Failed to execute the schedule script; JN::{count + 1}")
            count += 1
        while True:
            if count != 0:
                schedule.run_pending()
                time.sleep(1)
            else:
                print("Nothing to do")
                break
    except KeyboardInterrupt:
        print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "Terminating, Termination Signal Received")
        for process in thread_container:
            process.join()


if __name__ == "__main__":
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset = True)
    setting_path = os.path.exists('settings.ini')
    os.system('cls')
    os.system('title Program Scheduler')
    print(Fore.WHITE + Back.CYAN + Style.BRIGHT + " ========================================== ")
    print(Fore.WHITE + Back.CYAN + Style.BRIGHT + " | Program Scheduler v1.1.0 Release 1.1.0 | ")
    print(Fore.WHITE + Back.CYAN + Style.BRIGHT + " ========================================== ")
    if setting_path is True:
        with open('settings.ini', 'r') as file:
            command_file_name = file.readlines()
        command_path = os.path.exists(command_file_name[0])
        if command_path is True:
            main(command_file_name[0])
    else:
        print(Fore.WHITE + Back.RED + Style.BRIGHT + "Error: settings.ini must exist with the name of .txt file containing commands to run")
