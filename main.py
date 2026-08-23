from tool_manager import ToolManager
from dependency_checker import DependencyChecker


def show_tools(manager):
    print("\n========== Installed Tools ==========")

    for tool in ["ngspice", "kicad"]:
        if manager.is_installed(tool):
            print(f"{tool.upper()}: INSTALLED")
            print(f"Version: {manager.get_version(tool)}")
        else:
            print(f"{tool.upper()}: NOT INSTALLED")

    print("=====================================\n")


def install_tool(manager):
    print("\nAvailable tools:")
    print("1. Ngspice")
    print("2. KiCad")

    choice = input("Choose a tool: ")

    if choice == "1":
        tool = "ngspice"
    elif choice == "2":
        tool = "kicad"
    else:
        print("Invalid choice.")
        return

    print(f"\nInstalling {tool}...")
    result = manager.install_tool(tool)
    print(result)


def main():
    manager = ToolManager()
    dependency_checker = DependencyChecker()

    while True:
        print("""
========================================
          eSim Automated Tool Manager
========================================

1. Check installed tools
2. Install a tool
3. Check dependencies
4. Exit

========================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tools(manager)

        elif choice == "2":
            install_tool(manager)

        elif choice == "3":
            dependency_checker.run_check()

        elif choice == "4":
            print("Exiting eSim Tool Manager...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()