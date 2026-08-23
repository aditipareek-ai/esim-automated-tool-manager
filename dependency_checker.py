import shutil
import sys


class DependencyChecker:

    def check_python(self):
        version = sys.version.split()[0]
        return f"Python: OK ({version})"

    def check_command(self, command):
        if shutil.which(command):
            return f"{command}: OK"
        else:
            return f"{command}: MISSING"

    def run_check(self):
        print("\n========== Dependency Check ==========")

        print(self.check_python())

        commands = [
            "git",
            "python"
        ]

        for command in commands:
            print(self.check_command(command))

        print("======================================\n")