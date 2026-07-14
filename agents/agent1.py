import logging
from datetime import datetime 

from dotenv import load_dotenv

from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool

load_dotenv()
logging.basicConfig(level=logging.WARNING)
#so that we dont get flooded my unnecessary logs on our terminal and just a necessary response is all we need to understand what's going on (right)..
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("conductor").setLevel(logging.WARNING)
#setting the logging level to WARNING so that we dont get bunch of info logs which are not relevant to us, we need relevant information to understand and act on in order to move forward while understanding the project, debugging, understanding its working etc


#=========================================================#
#===============Tools======================#

@tool
def get_current_time() -> str:
    """returns the current local time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#=========================================================#
#===============Memory for our Agent======================#
conversation_memory = ConversationMemory(max_messages=50)



#=========================================================#
#===============Defining our Agent======================#
assistant = Agent(
    name="Personal-Assistant",
    model="openai/gpt-4o-mini",
    instructions=(
        "you are a concise personal assistant, use tools while they are helpful and remember useful user details across turns"
    ),
    tools=[get_current_time],
    #A tool is something a AI Agent can call to get some kind of response or to take some kind of action.
    memory=conversation_memory,

)

if __name__ == "__main__":
    print("Starting the agent.....")

    with AgentRuntime() as runtime:
        while True:#asking the agent questions until we quit
            prompt = input("You: ").strip()
            if prompt.lower() == "q":
                break
            if not prompt:
                continue

            result = run(assistant,prompt,runtime=runtime)
            #adding the conversations into the memory
            readable_result = result.output.get('result')
            conversation_memory.add_user_message(prompt)
            conversation_memory.add_assistant_message(readable_result)

            # print(f"Assistant: {result}")#returned a dictionary
            print(f"Assistant: {readable_result}")


 