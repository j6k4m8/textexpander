#!/usr/bin/env python3

import glob
import sys

import xmltodict


def should_convert(abbr, exp) -> bool:
    """
    may require more attn.
    """
    return exp and "\n" not in exp and "TextExpander.pasteboardText" not in exp


def abbreviations_to_yaml(abbrs: dict) -> str:
    return "\n".join(
        f"""  - trigger: "{abbr}"\n    replace: "{exp}" """
        for abbr, exp in abbrs.items()
        if should_convert(abbr, exp)
    )


def read_file_to_dict(file_path: str):
    return xmltodict.parse(open(file_path, "r").read())


def convert_file(file_path: str):
    data = read_file_to_dict(file_path)
    abbreviations = {}
    try:
        abbrs = data["plist"]["dict"]["array"]["dict"]
    except:
        try:
            abbrs = data["plist"]["dict"]["array"][0]["dict"]
        except:
            print(file_path)
            return
            abbrs = data["plist"]["dict"]["array"]["array"][1]["dict"]
    for ab in abbrs:
        (abbr, _, exp, _) = ab["string"]
        if abbr and exp:
            abbreviations[abbr.replace("\\", "\\\\")] = exp.replace('"', '\\"')
    return abbreviations


if __name__ == "__main__":
    files = glob.glob(sys.argv[-1])
    print("matches:")
    for fname in files:
        print("# ", fname)
        print(abbreviations_to_yaml(convert_file(fname)))
