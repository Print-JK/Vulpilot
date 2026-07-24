# Vulpilot MVP: Automated Penetration Testing Reporting Platform

Vulpilot is a modular application designed to automate the process of converting raw penetration testing scan outputs from various tools (Nmap, Nuclei) into professional, consistent HTML and PDF reports. It incorporates intelligent normalization pipelines and optional AI summarization to create actionable documentation efficiently.

## Features

*   **Multi-Scanner Parsing:** Native support for parsing Nmap XML and Nuclei JSON outputs.
*   **Normalization Pipeline:** A unified system to convert heterogeneous scanner findings into a single, consistent internal data model.
*   **Severity Standardization:** Maps disparate scanner severity labels into a standardized scale (Critical, High, Medium, Low, Informational).
*   **Finding Deduplication:** Identifies and consolidates duplicate findings reported by different scanners to ensure report clarity.
*   **Structured Report Generation:** Builds comprehensive reports containing metadata, executive summaries, detailed findings, and evidence.
*   **Report Export:** Generates professional HTML reports and exports them as shareable PDF documents using WeasyPrint.
*   **Optional AI Executive Summary:** Integrates a locally hosted Ollama model to generate optional, deterministic executive summaries offline.
*   **API Interface:** A FastAPI-based web interface for file uploads, report viewing, and downloading.

## Architecture & Workflow

Vulpilot operates on a structured, multi-stage pipeline, ensuring data integrity from raw input to final output.

### Data Processing Pipeline

The core functionality relies on the following sequential steps:

1.  **Scan File Upload:** The user provides raw scan files (Nmap XML or Nuclei JSON).
2.  **Scanner Parser Selection:** The application detects the file type and selects the appropriate parser (`nmap.py` or `nuclei.py`).
3.  **Raw Findings Extraction:** Specific data is extracted based on the chosen parser.
4.  **Normalization Pipeline:** All extracted findings are converted into Vulpilot's standardized internal format.
5.  **Severity Standardization:** Scanner-specific severities are mapped to the unified scale.
6.  **Deduplication:** Duplicate findings across different scanners are merged and consolidated.
7.  **Report Builder:** A single Source of Truth (`Report Object`) is constructed from the normalized, deduplicated data.
8.  **AI Summarization (Optional):** The `Report Object` is passed to the AI module for generating optional Executive Summaries using a local Ollama instance.
9.  **HTML Rendering & Export:** The final structured report object is rendered into an HTML document and exported as a PDF via WeasyPrint.

### Internal Module Structure

The project follows a clear separation of concerns:

| Directory | Responsibility | Key Components |
| :--- | :--- | :--- |
| `app/parsers/` | Handling specific file formats. | `nmap.py`, `nuclei.py` |
| `app/services/` | Core data manipulation logic. | `pipeline.py`, `deduplicate.py`, `severity.py` |
| `report/` | Generating the final output artifacts. | `builder.py`, `renderer.py`, `summary.py` |
| `ai/` | Integrating local AI models. | `ollama.py`, `service.py` |
| `api/` | Web interface and routing. | `routes.py` (FastAPI) |

## Setup & Installation

Follow these steps to set up the environment and run Vulpilot locally.

### Prerequisites

*   Python 3.12+
*   Ollama (optional, for AI summaries)
*   Git

### Installation Steps

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/Print-JK/Vulpilot.git
    cd Vulpilot
    ```

2.  **Create Virtual Environment:**
    ```bash
    # Linux/macOS
    python -m venv .venv
    source .venv/bin/activate
    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment (.env):**
    Create a `.env` file in the project root to configure AI settings.

    **Example `.env` Content:**
    ```ini
    AI_PROVIDER=ollama
    OLLAMA_MODEL=qwen2.5-coder:7b
    OLLAMA_URL=http://localhost:11434
    # To disable AI and rely on deterministic summaries, set:
    # AI_PROVIDER=none
    ```

5.  **AI Setup (Optional):**
    If you intend to use Ollama for summarization, ensure the service is running and the model is available:
    ```bash
    # Start the Ollama service in a separate terminal if not already running
    ollama serve
    
    # Verify models are installed or pull them if necessary
    ollama list
    # Example command to pull a model
    ollama pull qwen2.5-coder:7b 
    ```

6.  **Run Vulpilot:**
    Start the FastAPI server to launch the web interface:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage Guide

### Accessing the Interface

Navigate to the local host address in your browser:
`http://127.0.0.1:8000`

### Generating a Report

1.  **Upload Scan File:** Use the web interface to upload your Nmap XML or Nuclei JSON file.
2.  **Generate Report:** Click the "Generate Report" button.
3.  **Select Output:** Choose your desired output format:
    *   View HTML Report
    *   Download PDF Report

### AI Integration Verification

*   If **AI is enabled**, the generated report will include an AI-generated executive summary from Ollama.
*   If Ollama is unavailable or if settings dictate, Vulpilot will automatically generate a deterministic summary instead, ensuring the report generation process remains uninterrupted.

## Typical Development Workflow

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. (Optional) Start Ollama service in a separate terminal
ollama serve

# 3. Run the application server
uvicorn app.main:app --reload
```

## Project Structure

```
Vulpilot/
├── app/                  # Core application logic and services
├── sample_scans/         # Directory for test input files
├── tests/                # Unit and integration tests
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── .env.example          # Template for environment configuration
└── pyproject.toml        # Project configuration (e.g., Poetry or Flit setup)
```
