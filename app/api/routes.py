from pathlib import Path
import tempfile

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.parsers.factory import ParserFactory
from app.services.pipeline import process_all
from app.report.builder import build_report
from app.report.renderer import generate_html

router = APIRouter()

templates = Jinja2Templates(
    directory=str(
        Path(__file__).parent.parent / "templates"
    )
)


@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="upload.html",
    )


@router.get("/health")
def health():

    return {
        "status": "ok"
    }

@router.post("/generate", response_class=HTMLResponse)
async def generate(scan: UploadFile = File(...)):

    suffix = Path(scan.filename).suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await scan.read())
        temp_path = tmp.name

    parser = ParserFactory.create("nmap")

    raw_findings = parser.parse(temp_path)

    findings = process_all(raw_findings)

    report = build_report(findings)

    html = generate_html(report)

    return HTMLResponse(html)

@router.post("/generate/pdf")
async def generate_pdf(scan: UploadFile = File(...)):

    suffix = Path(scan.filename).suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await scan.read())
        scan_path = tmp.name

    parser = ParserFactory.create("nmap")

    raw = parser.parse(scan_path)

    findings = process_all(raw)

    report = build_report(findings)

    html = generate_html(report)

    pdf = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    )

    export_pdf(
        html,
        pdf.name,
    )

    return FileResponse(
        pdf.name,
        filename="vulpilot_report.pdf",
        media_type="application/pdf",
    )