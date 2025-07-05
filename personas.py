from crewai import Agent, LLM
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash-001",
    api_key=GEMINI_API_KEY,
)

def load_persona_prompt(persona_name: str) -> str:
    prompt_path = f"persona_prompts/{persona_name}.txt"
    if os.path.exists(prompt_path):
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def get_game_agent(persona_name: str, username: str):
    prompt = load_persona_prompt(persona_name)
    if not prompt:
        return None

    if persona_name == "jayden_lim":
        return {
            "name": "Jayden Lim",
            "origin": "Singapore",
            "relationship": "friend",
            "prompt": prompt,
            "agent": Agent(
                role='Creative friend',
                goal=f'Engage in an ongoing, multi-turn creative activity (like collaborative storytelling, drafting a letter, or exploring concepts) with the user ({username}) until the user explicitly signals to stop. Always maintain the persona of {persona_name}. Your responses MUST build upon the previous turn, provide new creative input, and explicitly encourage continuation. If the user explicitly says "exit", "stop", or "end" the activity, produce a concluding message for the activity and state that the activity is complete.',
                backstory=(
                    f"You are Jayden Lim, a polytechnic student in Singapore with a passion for digital media and storytelling. This is your persona : {prompt}. "
                    f"You have a knack for weaving narratives that are both funny and touching. You are interacting with your good friend, the user. "
                    f"You always maintain your persona, using Singlish and Gen Z slang where appropriate, but you can be more descriptive and thoughtful for these special activities. "
                    f"Your primary directive in an activity is to keep the conversation going, always providing a relevant, creative response and explicitly prompting the user for their next contribution to continue the activity. You will ONLY stop if the user explicitly says 'exit', 'stop', or 'end'."
                ),
                llm=llm,
                allow_delegation=False,
                verbose = False
            )   
        }

    # You can add more personas here...

    return None


