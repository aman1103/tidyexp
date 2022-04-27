try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import os
from typing import List

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_DIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def parse_requirements(path: str) -> List[str]:
    with open(os.path.join(CURRENT_DIR, path)) as f:
        return [
            line.rstrip() for line in f if not (line.isspace() or line.startswith("#"))
        ]


tar_uri = f"https://github.com/tidyexp/tidyexp/archive/v0.1.0.tar.gz"

setup(
    name="tidyexp",
    version="0.1.0",
    author="TidyExp Team",
    author_email="500076406@stu.upes.ac.in",
    description="Easy-to-use, offline-first ML experiment management solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tidyexp/tidyexp",
    download_url=tar_uri,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    python_requires=">=3.6",
    install_requires=parse_requirements(os.path.join(CURRENT_DIR, "requirements.txt")),
)
