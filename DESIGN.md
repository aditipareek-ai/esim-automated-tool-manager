# Design Document: eSim Automated Tool Manager

## 1. Introduction

eSim is an open-source Electronic Design Automation (EDA) tool used for circuit design, simulation, analysis, and PCB design. It integrates multiple external tools such as KiCad and Ngspice to provide a complete electronic design workflow.

Managing external tools manually can be difficult because users may need to install different applications, verify versions, check dependencies, and configure installation paths.

The objective of this project is to develop a lightweight Automated Tool Manager for eSim using Python.

The prototype provides a command-line interface for checking installed tools, checking versions, installing supported tools, and verifying basic dependencies.

---

## 2. Problem Statement

An eSim installation may depend on multiple external tools and system components. Manual management can lead to problems such as:

* Missing tools
* Incorrect tool versions
* Missing system dependencies
* Installation-path issues
* Difficulty identifying whether a required tool is available

The proposed Tool Manager addresses these issues by providing a centralized interface for basic tool and dependency management.

---

## 3. Objectives

The main objectives are:

1. Automatically detect supported external tools.
2. Check the installed version of each tool.
3. Provide automatic installation of supported tools.
4. Check important system dependencies.
5. Handle common installation-path variations.
6. Provide a simple command-line interface.
7. Create a modular architecture that can be extended in the future.

---

## 4. Requirements Implemented

The FOSSEE screening task requires the submission to satisfy at least two of the listed requirements.

This prototype primarily implements:

### Requirement 1: Tool Installation Management

The system:

* Detects whether supported tools are installed.
* Uses Windows Package Manager (`winget`) for Windows installation.
* Supports KiCad and Ngspice as managed tools.
* Retrieves installed tool versions.
* Detects KiCad installations outside the system PATH.

### Requirement 4: Dependency Checker

The system:

* Checks the Python installation.
* Checks Git availability.
* Reports whether the dependency is available or missing.

---

## 5. System Architecture

The system consists of three main modules:

```text
                 +----------------------+
                 |       main.py        |
                 |   Command Line UI    |
                 +----------+-----------+
                            |
                +-----------+-----------+
                |                       |
                v                       v
      +-------------------+   +----------------------+
      | tool_manager.py   |   | dependency_checker.py|
      +-------------------+   +----------------------+
      | Tool detection    |   | Python check         |
      | Version checking  |   | Git check            |
      | Installation      |   | Dependency reporting |
      | Path detection    |   +----------------------+
      +---------+---------+
                |
                v
      +-----------------------+
      | External Tools        |
      | KiCad / Ngspice       |
      +-----------------------+
```

---

## 6. Module Description

### 6.1 main.py

`main.py` provides the command-line interface.

It presents the user with four options:

1. Check installed tools
2. Install a tool
3. Check dependencies
4. Exit

The module receives the user's selection and calls the appropriate functionality.

---

### 6.2 tool_manager.py

This module is responsible for external tool management.

Its main functionality includes:

* Detecting tools using the system PATH.
* Detecting KiCad in its Windows user installation directory.
* Checking tool versions.
* Installing tools through the appropriate package-management mechanism.

The implementation uses Python modules including:

* `platform`
* `shutil`
* `subprocess`
* `os`

---

### 6.3 dependency_checker.py

This module performs basic dependency verification.

Currently it checks:

* Python
* Git

The results are displayed clearly to the user as either available or missing.

---

## 7. Tool Detection and Version Checking

The Tool Manager first attempts to locate a tool using the operating system PATH.

For KiCad on Windows, the prototype also checks:

```text
%LOCALAPPDATA%\Programs\KiCad\10.0\bin\kicad-cli.exe
```

This was necessary during testing because KiCad was installed for the current user but its command-line executable was not available through the system PATH.

After locating the executable, the manager executes the tool's version command and displays the result.

Example:

```text
========== Installed Tools ==========
NGSPICE: NOT INSTALLED
KICAD: INSTALLED
Version: 10.0.5
=====================================
```

---

## 8. Tool Installation

On Windows, the prototype uses Windows Package Manager (`winget`) for automatic installation.

For KiCad, the package identifier used is:

```text
KiCad.KiCad
```

The installation command accepts the source and package agreements automatically.

The implementation also checks whether the tool is already installed before attempting a new installation.

This prevents unnecessary installation attempts.

---

## 9. Dependency Checking

The dependency checker provides a basic environment verification mechanism.

Example:

```text
========== Dependency Check ==========
Python: OK (3.12.6)
git: OK
python: OK
======================================
```

This functionality can be expanded in future versions to check all dependencies required by a particular eSim version.

---

## 10. Error Handling

The prototype handles several common errors:

* Unknown tool selection
* Missing executable
* Failed installation
* Unsupported operating system
* Exceptions during version checking

Errors are converted into readable messages instead of terminating the application unexpectedly.

---

## 11. Research Background and Related Work

Open-source EDA environments often integrate multiple tools to provide a complete design workflow.

Paknikar et al. presented eSim as an open-source EDA tool for mixed-signal and microcontroller simulations. The work describes the role of eSim as an integrated environment for electronic design and simulation.

This project builds on the same idea of tool integration by focusing specifically on the management of the external software components required by such an environment.

Research and development work around open-source EDA tools also highlights the importance of accessible, reproducible, and integrated software environments.

In addition, the eSim project documentation identifies Tool Manager for modular installation and Package Manager for single-click installation as development directions for eSim.

Therefore, an automated tool-management layer is relevant to improving the usability and maintainability of an open-source EDA environment.

---

## 12. References

### [1]

R. Paknikar, S. Bansode, G. Nandihal, M. P. Desai, K. M. Moudgalya and A. Jha, "eSim: An Open Source EDA Tool for Mixed-Signal and Microcontroller Simulations," 2021 4th International Conference on Circuits, Systems and Simulation (ICCSS), Kuala Lumpur, Malaysia, 2021, pp. 212-217.

DOI: 10.1109/ICCSS51193.2021.9464198

### [2]

S. Kar et al., "Mixed Signal Simulation Marathon for Education and Employment," 2022 International Conference on Electrical, Computer, Communications and Mechatronics Engineering (ICECCME), Maldives, 2022, pp. 1-6.

DOI: 10.1109/ICECCME55909.2022.9988191

### [3]

FOSSEE, IIT Bombay, "eSim 2.5 Release Announcement," 2025.

The announcement describes Tool Manager for modular installation and Package Manager for single-click installation as planned eSim capabilities.

---

## 13. Testing

The prototype was tested on Windows.

### Test 1: Tool Detection

Expected behavior:

* Detect installed KiCad.
* Report its version.
* Report Ngspice as unavailable when it is not installed.

Observed result:

```text
NGSPICE: NOT INSTALLED
KICAD: INSTALLED
Version: 10.0.5
```

### Test 2: Dependency Checking

Expected behavior:

* Detect Python.
* Detect Git.

Observed result:

```text
Python: OK (3.12.6)
git: OK
python: OK
```

### Test 3: KiCad Installation

KiCad was installed using:

```text
winget install --id KiCad.KiCad
```

The installation was successfully completed and the installed version was detected by the Tool Manager.

---

## 14. Limitations

The current implementation is a prototype and has several limitations:

* Only a small number of tools are supported.
* Version compatibility rules are not yet comprehensive.
* Dependency checking is currently basic.
* Automatic update functionality has not yet been implemented.
* Configuration management is limited.
* The current user interface is command-line based.
* Windows-specific KiCad path handling is currently implemented for the tested KiCad version.

---

## 15. Future Scope

The project can be extended with:

1. Automatic update detection.
2. Automatic tool upgrades.
3. Complete dependency resolution.
4. Version compatibility checking.
5. Configuration-file support.
6. Environment-variable management.
7. Persistent activity logs.
8. Graphical user interface.
9. Linux and macOS support.
10. Support for additional eSim tools.
11. Tool health/status monitoring.
12. Rollback support for failed updates.

---

## 16. Conclusion

The eSim Automated Tool Manager demonstrates a modular Python-based approach to managing external software components required by an EDA environment.

The prototype successfully implements tool detection, version checking, automatic installation through the Windows package manager, dependency checking, and installation-path handling.

The architecture is intentionally modular so that additional tools, dependency rules, update mechanisms, configuration management, and user-interface features can be added in future versions.
