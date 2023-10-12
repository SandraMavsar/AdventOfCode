#--- Day 7: No Space Left On Device ---

import re
from collections import defaultdict

with open('input.txt') as f:
    terminal_output = f.read().strip().split("\n")

    def get_sizes(output):
        sizes = defaultdict(int)
        sizes["/root"] = 0
        curr_dir = "/root"
        for command in output:
            cmd = re.search(r'\$ (cd|ls) (.+)', command)
            if cmd:
                op, folder = cmd.groups()
                if op in ["dir", "ls"]:
                    continue
                if op == "cd":
                    if folder == "/":
                        curr_dir = "/root"
                    elif folder == "..":
                        curr_dir = curr_dir[0:curr_dir.rfind("/")]
                    else:
                        curr_dir += f'/{folder}'

            file_size = re.search(r'(\d+) (.+)', command)
            if file_size:
                size, file = file_size.groups()
                folder = curr_dir
                for _ in range(curr_dir.count("/")):
                    sizes[folder] += int(size)
                    folder = folder[:folder.rfind("/")]
        return sizes

    sizes = get_sizes(terminal_output)
    target = sizes["/root"] - 39999999
    folders = []
    total = 0
    for size in sizes.values():
        if target <= size:
            folders.append(size)
        if size <= 100000:
            total += size
    print("Part One: ", total)
    print("Part Two: ", min(folders))
