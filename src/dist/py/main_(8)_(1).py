import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def parse_folder(path: Path, indent: int = ""):
    try:
        for el in sorted(path.iterdir()):
            if el.is_dir():
                print(f"{indent}{Fore.LIGHTMAGENTA_EX}📂 {el.name}{Fore.RESET}")
                parse_folder(el, indent + "   ")
            else:
                name = el.name
                suffix = el.suffix
            
                print(f"{indent}{Fore.LIGHTCYAN_EX}📜 {name}{Fore.LIGHTYELLOW_EX}{suffix}{Fore.RESET}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission denied]: {path}{Fore.RESET}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} You must pass a directory path!")
        print(f"{Fore.YELLOW} [INFO] {Fore.RESET} Example: python hw03.py /path/to/directory")
        sys.exit(1)

    path_dir = Path(sys.argv[1])

    if not path_dir.exists():
        print(f"{Fore.RED}[ERROR]{Fore.RESET} The specified path does not exist!")
        sys.exit(1)

    if not path_dir.is_dir():
        print(f"{Fore.RED}[ERROR]{Fore.RESET} path does not lead to directory!")
        sys.exit(1)

    parse_folder(path_dir)

