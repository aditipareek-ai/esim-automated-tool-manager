import platform
import shutil
import subprocess
import os


TOOLS = {
    "ngspice": {
        "command": "ngspice",
        "version_args": ["-v"],
        "linux_package": "ngspice",
        "windows_package": "ngspice"
    },
    "kicad": {
        "command": "kicad-cli",
        "version_args": ["--version"],
        "linux_package": "kicad",
        "windows_package": "KiCad.KiCad"
    }
}


class ToolManager:

    def __init__(self):
        self.system = platform.system()

    def get_command(self, tool_name):
        command = TOOLS[tool_name]["command"]

        # First check if the command is available in PATH
        path = shutil.which(command)

        if path:
            return path

        # Check common Windows installation location for KiCad
        if tool_name == "kicad" and self.system == "Windows":
            local_path = os.path.join(
                os.environ.get("LOCALAPPDATA", ""),
                "Programs",
                "KiCad",
                "10.0",
                "bin",
                "kicad-cli.exe"
            )

            if os.path.exists(local_path):
                return local_path

        return None

    def is_installed(self, tool_name):
        if tool_name not in TOOLS:
            return False

        return self.get_command(tool_name) is not None

    def get_version(self, tool_name):
        command = self.get_command(tool_name)

        if not command:
            return "Not installed"

        try:
            result = subprocess.run(
                [command] + TOOLS[tool_name]["version_args"],
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout.strip()

            if not output:
                output = result.stderr.strip()

            return output.split("\n")[0]

        except Exception as error:
            return f"Error: {error}"

    def install_tool(self, tool_name):
        if tool_name not in TOOLS:
            return "Unknown tool."

        if self.is_installed(tool_name):
            return f"{tool_name} is already installed."

        tool = TOOLS[tool_name]

        try:
            if self.system == "Linux":
                subprocess.run(
                    ["sudo", "apt", "update"],
                    check=True
                )

                subprocess.run(
                    [
                        "sudo",
                        "apt",
                        "install",
                        "-y",
                        tool["linux_package"]
                    ],
                    check=True
                )

            elif self.system == "Windows":
                subprocess.run(
                    [
                        "winget",
                        "install",
                        "--id",
                        tool["windows_package"],
                        "--accept-source-agreements",
                        "--accept-package-agreements"
                    ],
                    check=True
                )

            else:
                return f"Automatic installation is not supported on {self.system}."

            return f"{tool_name} installation completed."

        except subprocess.CalledProcessError:
            return f"Installation failed for {tool_name}."

        except Exception as error:
            return f"Error: {error}"