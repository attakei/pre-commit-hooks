#!/usr/bin/env python
import argparse
import re
import sys
from pathlib import Path


VALID_TYPES = [
    # Rule 1 and 2.
    "feat",
    "fix",
]


parser = argparse.ArgumentParser()
parser.add_argument("msg_file_path", type=Path)


def validate_commit_message(src_path: Path) -> bool:
    msg = src_path.read_text()
    rule = re.compile(
        r"(?P<type>[a-z]+)(\((?P<scope>\w+)\))?!?: (?P<desc>[^\r\n].+)(\n\n(<?P<body>.+))?"
    )
    matched = rule.match(msg)
    if not matched:
        print("Invalid format for 'Conventional Commits'.")
        print("Please see https://www.conventionalcommits.org/en/v1.0.0/")
        return False
    if matched.group("type") not in VALID_TYPES:
        print(f"Invalid type section. select one from [{', '.join(VALID_TYPES)}]")
        return False
    return True


def main():
    args = parser.parse_args()
    result = validate_commit_message(args.msg_file_path)
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
