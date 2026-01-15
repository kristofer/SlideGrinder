from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="slidegrinder",
    version="0.1.0",
    author="Kristofer",
    description="A tool that converts PDFs or URLs into presentation slides",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kristofer/SlideGrinder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyPDF2>=3.0.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "markdown>=3.5.0",
    ],
    entry_points={
        "console_scripts": [
            "slidegrinder=slidegrinder:main",
        ],
    },
)
