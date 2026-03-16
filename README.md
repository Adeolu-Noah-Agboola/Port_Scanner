# Python TCP Port Scanner

## Overview

This project is a Python-based TCP port scanner designed to identify open ports and running services on remote hosts. The scanner automates network reconnaissance by attempting connections to specified port ranges and logging the results for further analysis.

The tool was developed to strengthen understanding of network services, system exposure, and diagnostic techniques used in infrastructure and security environments.

Results from scans are automatically logged and can be uploaded to a remote web server for centralized monitoring and analysis.

---

## Features

- TCP port scanning of remote hosts
- Automated detection of open ports
- Structured scan result logging
- Upload of log files to a web server
- Configurable target host and port range
- Lightweight and easy to run

---

## Technologies Used

- Python 3
- Socket Programming
- Network Diagnostics
- File Logging
- Basic Web Server Integration

---

## How It Works

The scanner works by attempting TCP socket connections to a target host across a range of ports.

For each port:

1. A TCP connection attempt is made
2. If the connection succeeds, the port is recorded as open
3. Results are written to a log file
4. The log file can optionally be uploaded to a remote web server

This approach simulates basic network reconnaissance techniques used in system diagnostics and security assessments.

---

## Example Output
