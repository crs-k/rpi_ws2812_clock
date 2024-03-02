from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="rpi_ws2812_clock",
    version="0.1",
    packages=find_packages(),
    author="Chris Kerins",
    description="A simple clock for the Raspberry Pi using WS2812 LEDs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/crs-k/rpi_ws2812_clock",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)