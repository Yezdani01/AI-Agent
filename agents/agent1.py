import logging
from datetime import datetime 

from dotenv import load_dotenv

from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool

load_dotenv()
logging.basicConfig(level=logging.WARNING)
#so that we dont get flooded my unnecessary logs on our terminal and just a necessary response is all we need..
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("conductor").setLevel(logging.WARNING)
#setting the logging level to WARNING so that we dont get bunch of info logs which are not relevant to us, we need relevant information to understand and act on in order to move forward while understanding the project, debugging, understanding its working etc
