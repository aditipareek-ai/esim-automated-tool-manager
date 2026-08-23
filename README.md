eSim Automated Tool Manager
1. Project Overview

The eSim Automated Tool Manager is a Python-based command-line utility designed to simplify the management of external tools required by eSim.

eSim integrates multiple external tools and libraries. Managing these tools manually can involve installation, version checking, dependency verification, and configuration of installation paths.

This project provides a lightweight prototype for automating these tasks.

2. Objectives

The main objectives of the project are:

Detect whether supported external tools are installed.
Display installed tool versions.
Install supported tools automatically.
Check important system dependencies.
Handle Windows installation paths for tools installed for the current user.
Provide a simple command-line interface.
3. Implemented Features
Tool Installation Management

The manager currently supports:

Ngspice
KiCad

The Windows implementation uses Windows Package Manager (winget) for automatic installation.

Version Checking

The application detects installed tools and retrieves their versions.

For example, the tested system detected:

KICAD: INSTALLED
Version: 10.0.5
Dependency Checking

The dependency checker verifies:

Python
Git

and reports whether each dependency is available.

Installation Path Detection

The manager first checks the system PATH.

For KiCad on Windows, it also checks the user installation directory:

%LOCALAPPDATA%\Programs\KiCad\10.0\bin\kicad-cli.exe

This allows the manager to detect KiCad even when its command-line executable has not been added to the system PATH.

4. Project Structure
esim-tool-manager/
│
├── main.py
├── tool_manager.py
├── dependency_checker.py
├── requirements.txt
├── README.md
└── DESIGN.md
main.py

Provides the command-line interface and connects the different modules.

tool_manager.py

Handles:

Tool detection
Version checking
Automatic installation
Windows installation-path handling
dependency_checker.py

Checks whether required system commands and Python are available.

DESIGN.md

Contains the system architecture, design decisions, research background, and implementation details.

5. Requirements
Python 3.x
Windows 10/11 for the Windows installation functionality
Windows Package Manager (winget)
Git

No external Python packages are required by the current prototype.

6. How to Run

Open a terminal in the project directory.

Run:

python main.py

The following menu will appear:

========================================
          eSim Automated Tool Manager
========================================

1. Check installed tools
2. Install a tool
3. Check dependencies
4. Exit
7. Usage
Check Installed Tools

Select:

1

The manager displays the installation status and version of supported tools.

Install a Tool

Select:

2

Then select the required tool.

On Windows, the manager uses winget to install the selected package.

Check Dependencies

Select:

3

The manager checks Python and Git availability.

Exit

Select:

4

to close the application.

8. Testing

The prototype was tested on Windows.

The tool detection functionality successfully detected KiCad 10.0.5 after installation.

Example output:

========== Installed Tools ==========
NGSPICE: NOT INSTALLED
KICAD: INSTALLED
Version: 10.0.5
=====================================

The dependency checker also successfully detected Python and Git.

9. Limitations

The current version is a prototype. Some improvements that can be implemented in future versions include:

Support for additional eSim dependencies.
More comprehensive dependency resolution.
Automatic update checking.
Configuration and environment-variable management.
Cross-platform support for Linux and macOS.
Graphical user interface.
Detailed persistent logging.
More sophisticated version compatibility checking.
10. Future Scope

The Tool Manager can be extended into a complete eSim environment-management utility.

Future versions could maintain a central tool configuration containing supported versions, installation methods, dependencies, and compatibility information. This would allow the manager to automatically determine whether an installed environment satisfies the requirements of a particular eSim version.

11. Conclusion

The project demonstrates a basic automated approach to external tool management for eSim.

The prototype implements tool installation, tool detection, version checking, dependency checking, and Windows installation-path handling through a modular Python architecture.

The implementation provides a foundation that can be extended with update management, configuration handling, logging, and additional platform support.