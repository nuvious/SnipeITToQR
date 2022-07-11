"""
Integration tests
"""

import os

def test_basic_integration():
    """
    Basic integration tests that verifies svg's are generated
    """
    if os.name == 'nt':
        os.system(
            'snipe-it-to-qr.exe -d tests/files -t "https://snipeit.mydomain.local" --ignore-this --method basic'
        )
    else:
        os.system(
            'snipe-it-to-qr -d tests/files -t "https://snipeit.mydomain.local" --ignore-this --method basic'
        )
    assert os.path.exists('tests/files/TAGS/TEST00001.svg')
    assert os.path.exists('tests/files/TAGS/TEST00001_URL.svg')
