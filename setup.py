from setuptools import find_packages, setup

setup(
    name="chat-miner",
    description="chat-miner provides lean parsers for every major platform transforming chats into dataframes.\
         Artistic visualizations allow you to explore your data and create artwork from your chats.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "chatminer = chatminer.cli:main",
        ],
    },
)
