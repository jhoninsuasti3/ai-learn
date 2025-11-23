# LangGraph Agents Module

Este modulo contiene todo lo relacionado con LangGraph y agentes AI.

## Estructura

```
langGraph/
├── .env                    # Variables de entorno (API keys)
├── .env.example           # Plantilla de variables de entorno
├── langgraph.json         # Configuracion de LangGraph
├── main.py                # Definicion del agente principal
├── pyproject.toml         # Dependencias del modulo
└── README.md              # Este archivo
```

## Configuracion

1. Copia `.env.example` a `.env` y configura tus API keys:
   ```bash
   cp .env.example .env
   ```

2. Edita `.env` con tus claves:
   - `ANTHROPIC_API_KEY`: Para usar modelos Claude
   - `OPENAI_API_KEY`: Para usar modelos OpenAI (opcional)
   - `LANGSMITH_API_KEY`: Para tracing y monitoring (opcional)

## Ejecutar el servidor de desarrollo

### Opcion 1: Usando el script (recomendado)

Desde el directorio `langGraph/`:

```bash
./run.sh [puerto]
```

Ejemplo:
```bash
./run.sh        # Usa puerto 2025 por defecto
./run.sh 3000   # Usa puerto 3000
```

### Opcion 2: Comando directo

```bash
langgraph dev --port 2025
```

Esto iniciara:
- API server en: http://127.0.0.1:2025
- Documentacion API en: http://127.0.0.1:2025/docs
- LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2025

## Modelo actual

El agente esta configurado para usar **Claude Sonnet 4.5** (`claude-sonnet-4-5-20250929`).

## Herramientas disponibles

- `get_weather(city: str)`: Ejemplo de herramienta que devuelve el clima de una ciudad
