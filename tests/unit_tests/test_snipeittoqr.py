"""
Unit tests for snipeittoqr module
"""
from unittest.mock import MagicMock, patch, mock_open

import qrcode

from snipeittoqr import make_tag, process_file, process_tag, process_directory


TEST_EXPORT_DATA = {
    'header': [
        [
            'Asset Name', 'Asset Tag', 'Serial', 'Model', 'Category', 'Status',
            'Checked Out To', 'Location', 'Purchase Cost']
        ],
    'data': [
        {
            'Asset Name': 'Logitech K400+ 001', 'Asset Tag': 'TEST00001',
            'Serial': '', 'Model': 'Logitech K400+ Wireless Keyboard',
            'Category': 'PC Peripherals', 'Status': 'Ready to Deploy',
            'Checked Out To': '', 'Location': 'Home', 'Purchase Cost': ''
        },
        {
            'Asset Name': '', 'Asset Tag': '', 'Serial': '', 'Model': '',
            'Category': '', 'Status': '', 'Checked Out To': '', 'Location': '',
            'Purchase Cost': 0
        }
    ]}


@patch('qrcode.make')
def test_make_tag(mock_qrcode_make):
    """
    Test for make_tag
    """
    fake_data = "fubar"
    fake_path = "~/tag.svg"
    methods={
        'basic': qrcode.image.svg.SvgImage,
        'fragment': qrcode.image.svg.SvgFragmentImage,
        'fubar': qrcode.image.svg.SvgPathImage
    }
    mock_qrcode_make.return_value = MagicMock()

    for method, expected_factory in methods.items():
        make_tag(fake_data, fake_path, method=method)
        mock_qrcode_make.assert_called_with(
            fake_data,
            **{
                'image_factory': expected_factory
            }
        )

@patch('snipeittoqr.make_tag')
def test_process_tag(mock_make_tag):
    """
    test for process_tag
    """
    fake_tag = "fubar"
    cases = [
        {
            'args': {
                'tag': fake_tag
            },
            'make_tag_call_count': 1
        },
        {
            'args': {
                'tag': fake_tag,
                'url': 'https://snipit.mydomain.local'
            },
            'make_tag_call_count': 2
        }
    ]
    for case in cases:
        mock_make_tag.reset_mock()
        process_tag(**case['args'])
        assert mock_make_tag.call_count == case['make_tag_call_count']


@patch('snipeittoqr.process_tag')
@patch('json.load')
def test_process_file(mock_json_load, mock_process_tag):
    """
    test for process_file
    """
    mock_json_load.return_value = TEST_EXPORT_DATA
    with patch("builtins.open", mock_open()) as _:
        process_file("/some/path")
    assert mock_process_tag.call_count == 1
    assert mock_process_tag.called_with('TEST00001')


@patch('snipeittoqr.process_file')
def test_process_directory(mock_process_file):
    """
    test for process_directory
    """
    process_directory(target_dir='tests/files')
    assert mock_process_file.call_count == 1
