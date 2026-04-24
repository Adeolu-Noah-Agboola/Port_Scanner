from fastapi import FastAPI
from pydantic import BaseModel
from app.scanner import scan_ports

app = FastAPI(title="Network Scan REST API")

class ScanRequest(BaseModel):
    target: str
    start_port: int
    end_port: int

@app.get("/")
def home():
    return {"message": "Network Scan API is running"}

@app.post("/scan")
def scan(request: ScanRequest):
    open_ports = scan_ports(
        request.target,
        request.start_port,
        request.end_port
    )

    return {
        "target": request.target,
        "start_port": request.start_port,
        "end_port": request.end_port,
        "open_ports": open_ports,
        "status": "completed"
    }