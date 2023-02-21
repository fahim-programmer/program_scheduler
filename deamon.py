import os


def function(target_directory):
    command = f"start {target_directory}"
    #print(command + r"\boot")
    os.system(command + r"\boot")
    return None


if __name__ == '__main__':
    setting_path = os.path.exists('settings.ini')
    if setting_path is True:
        with open('settings.ini', 'r') as file:
            command_file_name = file.readlines()
            #print(command_file_name[1])
        #command_path = command_file_name[0]
            function(command_file_name[1])
