"""
Main process logic for the snipeittoqr package which is mapped to the
snipe-it-to-qr application.
"""
import argparse

from snipeittoqr import process_directory


def main():
    """
    Main application logic mapped to the snipe-it-to-qr entrypoint.
    """
    parser = argparse.ArgumentParser()
    parser.add_help("""
    Processes a directory passed to the application creating QR codes for every
    asset specified in json Snipe IT asset exports. Arguments specified below
    are native to the application but others may be passed that can be utilized
    by the SVG factories of the qrcode library.""")
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
    target_dir = args.asset_json_directory
    url = args.tenant_url
    process_directory(target_dir, url=url, **vars(unknown_args))


if __name__ == "__main__":
    main()
