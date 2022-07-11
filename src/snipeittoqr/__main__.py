"""
Main process logic for the snipeittoqr package which is mapped to the
snipe-it-to-qr application.
"""
import argparse
import re

from snipeittoqr import process_directory

def _parse_unknowns(unknown_args):
    """
    Converts a list of unknown arguments into a dictionary

    Args:
        unknown_args (Iterable): A list of unknown arguments

    Returns:
        dict:
            A dictionary of argument name to value. If the argument does not
            specify a value (flag) it's given the value True
    """
    ret = {}
    while len(unknown_args) > 0:
        arg = re.sub('^-+', '', unknown_args.pop(0))
        value = (
            True
            if unknown_args[0].startswith('-')
            else unknown_args.pop()
        )
        ret[arg] = value
    return ret


def main():
    """
    Main application logic mapped to the snipe-it-to-qr entrypoint.
    """
    parser = argparse.ArgumentParser()
    parser.description = """
    Processes a directory passed to the application creating QR codes for every
    asset specified in json Snipe IT asset exports. Arguments specified below
    are native to the application but others may be passed that can be utilized
    by the SVG factories of the qrcode library."""
    parser.add_argument(
        "-d", "--asset-json-directory", type=str, default="/workspace",
        help="A directory containing json exports of Snipe IT assets.")
    parser.add_argument(
        "-t", "--tenant-url", type=str, default=None,
        help=("""
If specified QR codes will be generated that link directly to the asset via a
URL rather than just the asset tag. The tenant domain used in generating asset
url qr codes. Will generate urls in the format: 

TENANT_URL/hardware/bytag?assetTag=ASSET_TAG""")
    )
    args, unknown_args = parser.parse_known_args()
    unknown_args = _parse_unknowns(unknown_args)
    target_dir = args.asset_json_directory
    url = args.tenant_url
    print(target_dir)
    print(url)
    process_directory(target_dir, url=url, **unknown_args)


if __name__ == "__main__":
    main()
