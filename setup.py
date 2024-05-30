from distutils.core import setup
from pathlib import Path

version = "1.0.0b1"
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="express",
    python_requires=">=3.10",
    packages=[
        "express"
    ],
    version=version,
    license="MIT",
    description="Seamless Flask Authentication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Deepak Soni",
    author_email="deepaksonii@outlook.in",
    url="https://github.com/diezo/express",
    download_url=f"https://github.com/diezo/express/archive/refs/tags/v{version}.tar.gz",
    keywords=[
        "express",
        "express-python"
    ],
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10"
    ]
)