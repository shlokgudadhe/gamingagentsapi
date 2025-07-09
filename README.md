
# Gaming Agents API

The Gaming Agents API is a conversational backend service that powers emotionally rich, persona-driven chat experiences. It enables interactions through unique personas and structured activity formats using FastAPI, CrewAI, and Gemini-based LLMs.

This API is built to serve creative applications such as virtual companionship, reflective journaling, romantic simulations, cultural exchanges, and role-play activities with intelligent agents.

---

## Features

- **Persona-based agents** with distinct names, cultural origins, personalities, and roles.
- **Activity-driven task system** to guide conversations like "Unsent Messages", "Breakup Simulation", "Mood Meal", etc.
- **CrewAI-based orchestration** with agents that generate context-aware, creative multi-turn responses.
- **Strict input validation and key-based security** to control access.
- **Extensible architecture** allowing easy addition of new personas and activities.

---

## System Architecture

![Untitled diagram _ Mermaid Chart-2025-07-09-072614](https://github.com/user-attachments/assets/a76af236-9118-400e-8c70-6b6f4e44b970)


---

## Project Structure

```
.
├── main.py               # FastAPI entry point and routing logic
├── activities.py         # Definitions of all activity templates and task logic
├── personas.py           # Persona data, agent definitions, and LLM initialization
├── requirements.txt      # List of Python package dependencies
├── persona_prompts/      # Text prompt files used to generate agent backstories
└── .env                  # Environment variables for API key configuration
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gaming-agents-api.git
cd gaming-agents-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> This installs FastAPI, CrewAI, litellm, python-dotenv, and other necessary libraries.

### 3. Configure environment variables

Create a `.env` file in the root directory with the following content:

```env
API_KEY=your_custom_api_key
GEMINI_API_KEY=your_google_gemini_api_key
```

These keys are required to authenticate incoming requests and communicate with the Gemini model via CrewAI.

### 4. Run the development server

```bash
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000/chat`.

---

## Example API Request

### Endpoint

```
POST /chat
```

### Headers

```
x-api-key: your_custom_api_key
Content-Type: application/json
```

### JSON Payload

```json
{
  "persona": "jayden_lim",
  "activity": "mood_meal",
  "user_input": "Today felt kind of stormy inside.",
  "username": "Alex",
  "history": []
}
```

### Example Successful Response

```json
{
  "reply": "A slice of black sesame cake—bittersweet, dense, but strangely comforting. What’s on your plate today, Alex?"
}
```

---

## Supported Activities

Each activity defines a unique conversational prompt style and behavioral pattern for the persona. These include:

- `love_in_another_life`
- `daily_debrief`
- `mood_meal`
- `unsent_messages`
- `i_would_never`
- `breakup_simulation`
- `compliment_mirror`
- `burning_questions_jar`
- `symbol_speak`
- `spiritual_whisper`
- `karma_knot`
- `nickname_game`
- `flirt_or_fail`
- `scenario_shuffle`
- `letter_from_the_future`
- `undo_button`
- `friendship_farewell`
- `date_duel`
- `divine_mirror`
- `dream_room_builder`
- `friendship_scrapbook`
- Many more...

See `activities.py` for the full list and logic associated with each.

---

## Adding a New Persona

1. Create a new prompt text file under `persona_prompts/` (e.g., `persona_prompts/emma_kim.txt`).
2. Define the persona’s descriptive prompt in the file.
3. Update `get_game_agent()` in `personas.py` to return a new agent when `persona_name` matches.

Each persona includes:
- `name`
- `origin`
- `relationship` (to the user)
- `prompt` (from file)
- `agent` (a CrewAI Agent with a role, goal, and backstory)

---

## Security

- All requests require an `x-api-key` header that must match `API_KEY` from `.env`.
- Unauthorized requests are rejected with `401 Unauthorized`.

---

## Requirements

Python 3.8 or later.

Dependencies are listed in `requirements.txt`:

```
fastapi
uvicorn
crewai
litellm
python-dotenv
```

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Author

Developed by [Your Name or Organization].  
If you find this useful or want to contribute, feel free to open an issue or pull request.
