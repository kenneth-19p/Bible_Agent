#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from bible_agent.crew import BibleAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'What does the bible say about homosexuality?',
        'bible_version': 'NIV'
        
    }

    project = BibleAgent()
    crew = project.crew()
    results = crew.kickoff(inputs=inputs)

    print(results)

if __name__ == "__main__":
    run()