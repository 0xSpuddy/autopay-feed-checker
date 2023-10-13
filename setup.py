from setuptools import find_packages
from setuptools import setup


# Function to read the requirements file
def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


# Setup function
setup(
    name="your_package_name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": ["checkfeed=autopay_feed_checker.check_feeds:check_single_feed"],
    },
)
