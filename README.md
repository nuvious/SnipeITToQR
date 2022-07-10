# Snipe-It-To-QR

A simple application to generate SVG QR Codes for use with the
[Snipe IT](https://snipeitapp.com/) platform.

## Installation

Install via pip:

```bash
pip install https://git+github.com/nuvious/SnipeITToQR.git
```

Install specific version via pip:

```bash
pip install https://git+github.com/nuvious/SnipeITToQR.git@v0.0.1
```

## Usage

### Basic Usage

Export your Snipe IT assets to a directory as json files. You can have multiple
files to keep things organized and/or incrementally updated. Once you have
a directory you can run the following from within the directory:

```bash
snipe-it-to-qr
```

Or specify the directory:

```bash
snipe-it-to-qr -d /path/to/snipeit/exports
```

Once executed the json exports are parsed and asset tags in the form of QR
codes are generated under /path/to/exports/TAGS with the filename
[Asset Tag].svg. These tags will only contain the text of the asset tag and
are useful for using the SnipeIT Asset Manager app or qr scanner enabled
scanner guns.

### Advanced Usage

You can also specify a tenant URL which will generate QR codes that when
scanned provide an absolute link to the asset tag. This can be useful for those
that do not wish to install then native app on their phone or for when the
native app doesn't support the features you're looking for like uploading
images to assets.

```bash
snipe-it-to-qr \
    -d /path/to/snipeit/exports\
    -t https://snipeit.mycompanydomain.com
```

This will generate 2 QR tags; the [Asset Tag].svg with just the asset tag
encoded as well as [Asset Tag]_URL.svg for the direct url link to the asset.

## Docker Container

### Build

```bash
docker build -t snipe-it-to-qr .
```

### Docker Usage

```bash
docker run --rm -it -v /path/to/exports:/workspace snipe-it-to-qr [ADDITIONAL ARGS]
```

## Development

### Running Unit Tests

Run the unit tests. By default we fail if coverage is under 90%

```bash
pip install -e .[test]
pytest --cov=snipeittoqr
coverage report --fail-under=90
```
