"""
Setup file for the snipeittoqr package
"""
from setuptools import find_packages, setup

REQUIREMENTS = open('requirements.txt', encoding='utf8').readlines()
REQUIREMENTS_TEST = open('requirements-test.txt', encoding='utf8').readlines()

setup(
    name="snipeittoqr",
    version=open("VERSION", encoding='utf8').read(),
    description="Converts a SnipeIt asset export to QR codes.",
    long_description=open("README.md", encoding='utf8').read(),
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    url="TBD",
    project_urls={
        "Documentation": "TBD",
        "Source": "TBD",
        "Changelog": "TBD",
    },
    author="David Cheeseman",
    author_email="david@cheeseman.club",
    package_dir={"": "src"},
    packages=find_packages(
        where="src"
    ),
    install_requires=REQUIREMENTS,
    extras_require={
        'test': REQUIREMENTS_TEST
    },
    entry_points={
        "console_scripts": [
            "snipeit-to-qr=snipeittoqr.__main__:main"
        ],
    },
    zip_safe=False,
    python_requires=">=3.8",
)
