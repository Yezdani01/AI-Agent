import logging
from datetime import datetime 

from dotenv import load_dotenv

from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool

load_dotenv()
logging.basicConfig(level=logging.WARNING)
#so that we dont get flooded my unnecessary logs on our terminal and just a necessary response is all we need..
