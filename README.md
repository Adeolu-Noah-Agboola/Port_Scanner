# Python TCP Port Scanner

## Overview

This project is a Python-based TCP port scanner designed to identify open ports and running services on remote hosts. The scanner automates network reconnaissance by attempting connections to a specified range of ports and logging the results for later analysis.

The project was developed to strengthen understanding of network services, system exposure, and diagnostic techniques commonly used in infrastructure administration and security environments.

Scan results are automatically written to a log file, and the log file can be uploaded to a web server for centralized storage and review.

---

## Features

- TCP port scanning of remote hosts
- Identification of open network services
- Automated logging of scan results
- Upload of scan logs to a web server
- Configurable target host and port range
- Lightweight and easy to run

---

## Technologies Used

- Python 3
- Socket Programming
- Network Diagnostics
- File Logging
- Web Server Integration

---

## How the Scanner Works

The port scanner uses Python's socket library to attempt TCP connections to a target host across a range of ports.

For each port in the specified range:

1. A TCP connection attempt is made
2. If the connection succeeds, the port is identified as open
3. Results are recorded in a structured log file
4. The log file can optionally be uploaded to a web server

This process simulates reconnaissance techniques used in network diagnostics and security testing.

---

## Example Output

```
Starting scan on target: 192.168.1.10

Port 22  : OPEN
Port 80  : OPEN
Port 443 : OPEN
Port 8080: CLOSED
```

A log file is generated containing all scan results.

---

## Project Structure

```
Port_Scanner/
│
├── port_scanner.py
├── scan_log.txt
└── README.md
```

- **port_scanner.py** – main Python script used to perform the scan  
- **scan_log.txt** – generated file containing scan results  
- **README.md** – project documentation  

---

## Installation

Clone the repository:

```
git clone https://github.com/Adeolu-Noah-Agboola/Port_Scanner.git
```

Navigate to the project directory:

```
cd Port_Scanner
```

Run the scanner:

```
python port_scanner.py
```

---

## Use Cases

This project can be used for:

- Network diagnostics
- Service discovery
- Learning socket programming
- Infrastructure troubleshooting
- Security testing practice

---

## Future Improvements

Potential enhancements include:

- Multi-threaded scanning for faster performance
- Service banner grabbing
- Integration with vulnerability scanners
- Improved reporting and visualization

---

## Educational Context

This project was developed as part of hands-on networking and security coursework. It complements other practical labs involving:

- Linux system administration
- packet capture and traffic analysis using Wireshark
- network protocol experimentation
- security testing within virtualized environments

---

## Disclaimer

This tool is intended strictly for educational purposes and authorized security testing. Always ensure you have explicit permission before scanning networks or systems.
