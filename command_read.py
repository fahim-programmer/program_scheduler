with open("commands.txt", "r") as command_file:
    clean_commands = []
    commands = command_file.readlines()
    for each_command in commands:
        # Comment detection plus empty line detection
        command_length = len(each_command[1:])
        initial_char = each_command[:-command_length]
        if initial_char != "#":
            if command_length >= 8:
                clean_commands.append(each_command.rstrip('\n'))

print(clean_commands)
