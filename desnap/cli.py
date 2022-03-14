from typing import List
import math
import click
import os


@click.command()
@click.option('--mode', default='list', help='list | del.')
def cli(mode: str):
    if mode == "del":
        mode = True
    else:
        mode = False  # type casting???
    root = 'Z:\\Steam\\userdata\\64232410\\760\\remote'
    list_of_directories: List[str] = os.listdir(root)
    list_of_directories.pop()  # delete the soft link from directory
    memory_to_save: int = 0
    list_to_delete: List[str] = []
    for directory in list_of_directories:
        current_dir: str = f"{root}\{directory}\\screenshots"
        if os.path.exists(current_dir):
            # scan for games with screenshot folders
            screenshots: List[str] = os.listdir(current_dir)
            # list all screenshots with _vr ending in them
            if len(screenshots) == 0:
                return 0

            i: int = 0
            while i < len(screenshots):
                if "_vr." not in screenshots[i] or screenshots[i] == "thumbnails":
                    del screenshots[i]
                    continue
                memory_to_save += os.path.getsize(
                    f"{current_dir}\\{screenshots[i]}")
                list_to_delete.append(f"{current_dir}\\{screenshots[i]}")
                if mode:
                    copy_location = "Z:\\testing\\" + screenshots[i]
                    os.rename(
                        f"{current_dir}\\{screenshots[i]}", copy_location)
                i += 1
    memory_taken = math.floor(memory_to_save / 8 / 1000 / 1024)

    if mode:
        click.echo(
            f"Successfully deleted ~{memory_taken}MB worth of data.")
    else:
        click.echo(
            f"Memory taken overall: ~{memory_taken} MB.")
        click.echo("Run the command with 'del' flag to delete said files.")
