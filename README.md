# Network Scan REST API

A FastAPI-based REST API that performs TCP port scanning and returns structured results for security diagnostics.

---

## Overview

This project is a Python-based network scanning tool built using FastAPI. It extends a traditional TCP port scanner into a REST API, allowing users to perform network scans through structured JSON requests and receive results in a standardized format.

The application demonstrates how security and network diagnostic tools can be exposed as backend services. It combines socket-level network scanning with modern API design, making it suitable for integration into automation pipelines, monitoring systems, or security platforms.

Originally developed as a TCP port scanner, the project has been enhanced to support API-based interaction, improving usability, scalability, and real-world applicability.

---

## Features

- TCP port scanning of remote hosts using Python sockets
- REST API built with FastAPI
- JSON-based request and response handling
- Identification of open network services
- Modular architecture separating API and scanning logic
- Interactive API testing via Swagger UI (/docs)
- Designed for security diagnostics and automation workflows

---

## Technologies Used

- Python 3
- FastAPI
- Uvicorn (ASGI server)
- Socket Programming
- Network Diagnostics

---

## How the Application Works

The application consists of two main components:

1. API Layer (main.py)
   - Receives HTTP requests
   - Validates JSON input
   - Calls the scanning logic
   - Returns structured JSON responses

2. Scanning Logic (scanner.py)
   - Uses Python’s socket library to attempt TCP connections
   - Iterates through a specified port range
   - Identifies open ports based on successful connections
   - Returns results to the API layer

### Scan Process

For each port in the specified range:

1. A TCP connection attempt is made  
2. If the connection succeeds, the port is identified as open  
3. Results are collected and returned as JSON  

---

## API Endpoint

### POST /scan

Performs a port scan on a specified target.

### Request Body

```json
{
  "target": "scanme.nmap.org",
  "start_port": 20,
  "end_port": 100
}

Response

{
  "target": "scanme.nmap.org",
  "start_port": 20,
  "end_port": 100,
  "open_ports": [22, 80],
  "status": "completed"
}

Running the Application
1. Clone the repository

git clone https://github.com/Adeolu-Noah-Agboola/Port_Scanner.git
cd Port_Scanner


2. Install dependencies
pip install fastapi uvicorn


3. Start the API server
uvicorn app.main:app --reload


4. Open in browser
http://127.0.0.1:8000/docs
Use the interactive interface to test the API.


PORT_SCANNER/
│
├── app/
│   ├── main.py        # FastAPI application (API layer)
│   └── scanner.py     # Port scanning logic
│
├── port_scan/         # Original scanner implementation
├── Dockerfile         # Container setup (in progress)
├── requirements.txt   # Project dependencies
└── README.md


Use Cases

This project can be used for:

Network diagnostics
Service discovery
Backend API development practice
Security tool prototyping
Automation workflows

Future Improvements
Asynchronous or multi-threaded scanning
Logging and monitoring integration
API authentication (API keys or JWT)
Persistent storage of scan results
Full Docker deployment and cloud hosting

isclaimer

This tool is intended strictly for educational purposes and authorized security testing. Only scan systems you own or have explicit permission to test.
