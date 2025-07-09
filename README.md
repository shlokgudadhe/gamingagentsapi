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

```mermaid
flowchart TD
    subgraph API
        A[POST /chat]
    end

    subgraph RequestValidation
        A --> B[Check API Key]
        B -->|Invalid| Err1["Return 401 Error"]
        B -->|Valid| C[Get Persona]
        C -->|Not Found| Err2["Return 404 Error"]
        C -->|Found| D[Get Activity Task]
        D -->|Unsupported| Err3["Return 400 Error"]
    end

    subgraph CrewAI_Orchestration
        D --> E[Create Task with Persona Agent]
        E --> F[Create Crew with Task and Agent]
        F --> G["Run Crew kickoff"]
    end

    subgraph Response
        G --> H["Return reply result"]
        G -->|Exception| Err4["Return error message"]
    end
