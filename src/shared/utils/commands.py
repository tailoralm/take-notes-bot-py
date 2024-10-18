from typing import Optional


class CommandOptions:
    def __init__(self, save: bool = False, receipt: bool = False, random: bool = False, name: Optional[str] = None):
        self.save = save
        self.receipt = receipt
        self.random = random
        self.name = name


def parse_commands(input_str: Optional[str]) -> CommandOptions:
    options = CommandOptions()

    if not input_str:
        return options

    parts = input_str.split()

    i = 0
    while i < len(parts):
        part = parts[i]

        if part.startswith('-'):
            if part == '-s':
                options.save = True
            elif part == '-r':
                options.receipt = True
            elif part == '-rnd':
                options.random = True
            elif part == '-n' and i + 1 < len(parts):
                options.name = parts[i + 1]
                i += 1  # Skip the next part since it's used as the name

        i += 1

    return options

