from typing import TypedDict, Optional

class File(TypedDict):
    name: str
    dir: 'Directory'

class Directory(TypedDict):
    name: str
    root: Optional['Directory']
    files: Optional[list[File]]
    sub_directories: Optional[list['Directory']]

def add_sub_directory(parent: Directory, child: Directory):
    child["root"] = parent
    if parent["sub_directories"] is None:
        parent["sub_directories"] = []
    parent["sub_directories"].append(child)

def remove_sub_directory(parent: Directory, child: Directory):
    child["root"] = None
    if parent["sub_directories"]:
        parent["sub_directories"].remove(child)

def add_file(directory: Directory, file: File):
    if directory["files"] is None:
        directory["files"] = []
    file["dir"] = directory
    directory["files"].append(file)

def remove_file(file: File):
    file["dir"]["files"].remove(file)
    file["dir"] = None