"""
Main module for snipeittoqr which contains processing functions used by the
__main__ process.
"""
import os
import glob
import json

import qrcode
import qrcode.image.svg

DEFAULT_OUTPUT_DIR='TAGS'
ASSET_URL_SUFFIX="/hardware/bytag?assetTag="


def make_tag(data, file_path, **kwargs):
    """
    Makes a single QR tag and saves it in SVG format to the file_path.

    Args:
        data (str): A string payload
        file_name (str): Path of the file to generate
        kwargs (dict):
            method (str):
                'basic' - Uses qrcode.image.svg.SvgImage factory
                'fragment' - Uses qrcode.image.svg.SvgFragmentImage factory
                None - (default) Uses qrcode.image.svg.SvgPathImage factory
    """
    method = kwargs.get('method')
    if method == 'basic':
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        factory = qrcode.image.svg.SvgFragmentImage
    else:
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(data, image_factory=factory)
    img.save(file_path)


def process_tag(tag, **kwargs):
    """
    Processes a tag and creates a qr code with just the asset tag ID and if url
    is specified a QR code url link to the asset.

    Args:
        tag (str):
            The asset tag
        url (str, optional):
            The tenant url in the form of https://[DOMAIN] or http://[DOMAIN].
            Defaults to None.
    """
    url = kwargs.get('url')
    output_dir = kwargs.get('output_dir', os.getcwd())
    os.makedirs(output_dir, exist_ok=True)
    if url:
        asset_url = f"{url}{ASSET_URL_SUFFIX}{tag}"
        file_name = os.path.join(output_dir, f"{tag}_URL.svg")
        make_tag(asset_url, file_name)
    file_name = os.path.join(output_dir, f"{tag}.svg")
    make_tag(tag, file_name)


def process_file(json_path, **kwargs):
    """
    Processes an Snipe IT asset export and generates QR codes for all of them.

    Args:
        json_path (str): Path to json Stipe IT asset export
    """
    with open(json_path, encoding='utf8') as json_file:
        data = json.load(json_file)
        asset_tags = [
            asset.get('Asset Tag')
            for asset in data.get('data', [])
            if asset.get('Asset Tag') # Ignore empty strings and None
        ]
        for tag in asset_tags:
            process_tag(tag, **kwargs)


def process_directory(target_dir=None, output_dir=None, **kwargs):
    """
    Processes a directory which contains Snipe IT asset exports.

    Args:
        dir (str, optional):
            If not specified, the WORKSPACE_DIR environment variable is checked
            and if that is not specified it defaults to the current working
            directory.
        output_dir (str, optional):
            If not specified, the OUTPUT_DIR environment variable is checked
            and if that is not specified it defaults to the export directory
            under the subfolder specified by snipeittoqr.DEFAULT_OUTPUT_DIR.
    """
    target_dir = (
        os.environ.get("WORKSPACE_DIR", os.getcwd())
        if not target_dir
        else target_dir
    )
    output_dir = (
        os.environ.get(
            "OUTPUT_DIR", os.path.join(target_dir, DEFAULT_OUTPUT_DIR)
        )
        if not output_dir
        else os.path.join(target_dir, DEFAULT_OUTPUT_DIR)
    )
    print(target_dir)
    print(output_dir)
    for file in glob.glob(os.path.join(target_dir, "*.json"), recursive=True):
        process_file(file, output_dir=output_dir, **kwargs)
