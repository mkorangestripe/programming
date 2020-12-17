import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ping-scan-mkorangestripe",
    version="0.0.1",
    author="Gavin Purcell",
    author_email="mkorangestripe@gmail.com",
    description="Ping scan cidr range",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkorangestripe/python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "sys",
        "subprocess",
        "ipaddress",
        "argparse"
    ],
    python_requires='>=3.6',
)
