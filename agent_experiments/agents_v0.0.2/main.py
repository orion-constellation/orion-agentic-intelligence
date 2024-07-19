import os
import autogen
from agents import init_agents
from dotenv import load_dotenv
load_dotenv()


def main():
    output = init_agents()
    return print(output)

    