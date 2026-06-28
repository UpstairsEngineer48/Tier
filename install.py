import os
import platform
import subprocess
import sys

TASK_NAME = "Dashboard"


def install_windows():

    project_dir = os.path.dirname(os.path.abspath(__file__))

    print("Creating virtual environment...")

    venv_path = os.path.join(project_dir, ".venv")

    if not os.path.exists(venv_path):

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "venv",
                ".venv",
            ],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(result.stderr)
            sys.exit(1)

        print("✓ Virtual environment created.")

    else:
        print("✓ Virtual environment already exists.")

    python_exe = os.path.join(
        project_dir,
        ".venv",
        "Scripts",
        "python.exe",
    )

    requirements = os.path.join(
        project_dir,
        "requirements.txt",
    )

    boot_py = os.path.join(
        project_dir,
        "boot.py",
    )

    if not os.path.exists(requirements):
        print("Error: requirements.txt not found.")
        sys.exit(1)

    if not os.path.exists(boot_py):
        print("Error: boot.py not found.")
        sys.exit(1)

    print("\nInstalling dependencies...")

    result = subprocess.run(
        [
            python_exe,
            "-m",
            "pip",
            "install",
            "-r",
            requirements,
        ],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

    print("✓ Dependencies installed.")

    print("\nCreating startup task...")

    command = [
        "schtasks",
        "/Create",
        "/TN",
        TASK_NAME,
        "/SC",
        "ONLOGON",
        "/TR",
        f'"{python_exe}" "{boot_py}"',
        "/F",
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

    print("✓ Startup task created.")
    print("\nInstallation completed successfully.")
    print("\n" + "=" * 70)
    print("IMPORTANT: Before using Dashboard, edit config.py")
    print("=" * 70)

    for _ in range(3):
        print("Update the following variables in config.py:")
        print("  • CODEFORCES_HANDLE")
        print("  • LEETCODE_USERNAME")
        print("  • CF_GOAL")
        print("  • LC_GOAL")
        print()

    print("After updating config.py, log out and log back in to start Dashboard automatically.")
    print("=" * 70)


def install_linux():

    print("Linux installer not implemented yet.")


def install_macos():

    print("macOS installer not implemented yet.")


def main():

    system = platform.system()

    if system == "Windows":
        install_windows()

    elif system == "Linux":
        install_linux()

    elif system == "Darwin":
        install_macos()

    else:
        print(f"Unsupported operating system: {system}")


if __name__ == "__main__":
    main()