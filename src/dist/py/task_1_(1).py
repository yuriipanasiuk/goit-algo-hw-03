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


def sort_files_recursive(source_dir: Path, dest_root: Path):
    """Рекурсивно обходить теку та копіює файли."""

    for item in source_dir.iterdir():

        if item.is_dir():
            sort_files_recursive(item, dest_root)

        elif item.is_file():
            try:
                ext_category = get_extension(item)
                target_dir = dest_root / ext_category

                target_dir.mkdir(parents=True, exist_ok=True)

                destination_path = target_dir / item.name

                if destination_path.exists():
                    stem = item.stem
                    suffix = item.suffix
                    counter = 1
                    while destination_path.exists():
                        new_name = f"{stem}_({counter}){suffix}"
                        destination_path = target_dir / new_name
                        counter += 1

                shutil.copy2(item, destination_path)
                print(f"Copied: {item} -> {destination_path.relative_to(dest_root)}")

            except Exception as e:
                print(f"Error processing {item}: {e}", file=sys.stderr)


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
    sort_files_recursive(source_dir, dest_dir)
    print("\nDone! Files sorted by extension.")


if __name__ == "__main__":
    main()
