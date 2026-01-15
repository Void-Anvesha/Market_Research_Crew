#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from market_research_crew.crew import MarketResearchCrew
from dotenv import load_dotenv
load_dotenv()


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
         "topic" : "An AI powered tool that summaeizes youtuve videos on my channel and posts the summary on various social media platforms like Linkedin , Instagram , Facebook ,  X , Whatsapp" 
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


