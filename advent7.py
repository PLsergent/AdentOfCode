from dataclasses import dataclass
import typing


with open('./advent7.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

@dataclass
class Directory:
    name: str
    parent: typing.Any
    children: dict
    size: int = 0
    solved_size: int = 0

    def __repr__(self):
        return f"{self.name} {self.parent} {self.children}"

    def calculate_size(self):
        if self.children:
            for child in self.children.values():
                self.size += child.calculate_size()
        return self.size
    
    def solve(self):
        if self.children:
            for child in self.children.values():
                if child.size <= 100000:
                    self.solved_size += child.size
                self.solved_size += child.solve()
        return self.solved_size
    
    def list_dirs(self):
        all_dirs = []
        if self.children:
            for _, child in self.children.items():
                all_dirs += (child.list_dirs() + [child])
        return all_dirs
# Part 1

root = Directory("/", None, {})

# Populate the tree
current_dir = root
for line in content[1:]:
    if line.startswith("$"):
        if line.startswith("$ cd"):
            dir = line[4:].strip()
            if dir == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.children[dir]
    if line.startswith("dir"):
        dir = line[4:].strip()
        current_dir.children[dir] = Directory(dir, current_dir, {})
    if line.split(" ")[0].isdigit():
        current_dir.size += int(line.split(" ")[0])

print(root.calculate_size(), root.solve())

# Part 2

current_free_space = 70000000 - root.size
required_space_to_delete = 30000000 - current_free_space

eligible_dirs = [dir.size for dir in root.list_dirs() if dir.size >= required_space_to_delete]
eligible_dirs.sort()
print(eligible_dirs[0])