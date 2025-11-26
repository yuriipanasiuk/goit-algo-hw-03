import argparse
import shutil
import sys
from pathlib import Path


def parse_arguments():
    """Parsing command line arguments."""
    parser = argparse.ArgumentParser(
        description="Recursively copies and sorts files by extension in a subdirectory."
    )
    parser.add_argument("source", type=str, help="Path to the source directory")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Path to the destination directory (default: dist)",
    )

    return parser.parse_args()


def get_extension(file_path: Path) -> str:
    if file_path.name.startswith(".") and not file_path.suffix:
        return "hidden"

    return file_path.suffix.lstrip(".").lower() or "no_extension"


def copy_file_to_destination(file_path: Path, dest_root: Path):
    """
    Copies a single file to the corresponding subdirectory by extension.
    """
    try:
        ext = get_extension(file_path)
        target_dir = dest_root / ext
        target_dir.mkdir(parents=True, exist_ok=True)

        destination_path = target_dir / file_path.name

        if destination_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            counter = 1
            while destination_path.exists():
                new_name = f"{stem}_({counter}){suffix}"
                destination_path = target_dir / new_name
                counter += 1

        shutil.copy2(file_path, destination_path)
        print(f"Copied: {file_path} → {destination_path}")

    except PermissionError as e:
        print(f"Access error (PermissionError): {file_path} — {e}", file=sys.stderr)
    except OSError as e:
        print(f"File system error (OSError): {file_path} — {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unknown error while copying {file_path}: {e}", file=sys.stderr)


def traverse_directory(source_path: Path, dest_root: Path):
    """
    Recursively traverses a directory and copies files.
    """
    if not source_path.exists():
        print(f"Error: Source does not exist: {source_path}", file=sys.stderr)
        return
    if not source_path.is_dir():
        print(f"Error: Source is not a directory: {source_path}", file=sys.stderr)
        return

    try:
        for item in source_path.iterdir():
            if item.is_dir():
                traverse_directory(item, dest_root)
            elif item.is_file():
                copy_file_to_destination(item, dest_root)
    except PermissionError as e:
        print(f"No access to directory: {source_path} — {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error while scanning directory {source_path}: {e}", file=sys.stderr)


def main():
    args = parse_arguments()

    source_dir = Path(args.source).resolve()
    dest_dir = Path(args.destination).resolve()

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(
            f"Failed to create destination directory {dest_dir}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)

    print("We start copying and sorting files...\n")
    traverse_directory(source_dir, dest_dir)
    print("\nDone! Files sorted by extension.")


if __name__ == "__main__":
    main()
