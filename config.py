from pathlib import Path
import os

from dotenv import load_dotenv

# -------------------------------------------------
# Load Environment Variables
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


# -------------------------------------------------
# API Keys
# -------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# -------------------------------------------------
# LLM Configuration
# -------------------------------------------------

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0"
    )
)


# -------------------------------------------------
# Research Settings
# -------------------------------------------------

MAX_ITERATIONS = int(
    os.getenv(
        "MAX_ITERATIONS",
        "3"
    )
)


# -------------------------------------------------
# Output Folder
# -------------------------------------------------

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


REPORT_PATH = OUTPUT_DIR / "report.md"

PDF_PATH = OUTPUT_DIR / "report.pdf"