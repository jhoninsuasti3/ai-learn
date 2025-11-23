#!/bin/bash
# Script de ayuda para ejecutar LangGraph

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 LangGraph Agent Server${NC}"
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "langgraph.json" ]; then
    echo "Error: Ejecuta este script desde el directorio langGraph/"
    exit 1
fi

# Verificar que .env existe
if [ ! -f ".env" ]; then
    echo "Error: Archivo .env no encontrado"
    echo "Copia .env.example a .env y configura tus API keys"
    exit 1
fi

# Puerto por defecto
PORT=${1:-2025}

# Ruta al entorno virtual
VENV_PATH="../.venv/bin"

# Verificar que el entorno virtual existe
if [ ! -d "$VENV_PATH" ]; then
    echo -e "${YELLOW}Advertencia: Entorno virtual no encontrado en $VENV_PATH${NC}"
    echo "Ejecuta 'uv sync' desde la raiz del proyecto"
    exit 1
fi

echo -e "${GREEN}Iniciando servidor en puerto $PORT...${NC}"
echo ""

# Ejecutar langgraph dev usando el entorno virtual
$VENV_PATH/langgraph dev --port $PORT
