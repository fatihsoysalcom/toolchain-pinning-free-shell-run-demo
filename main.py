import subprocess
import sys

def run_command(command_parts, description):
    """
    Attempts to run a shell command and prints its output or error.
    This simulates a 'free shell run' where the script assumes the command exists.
    """
    print(f"\n--- Attempting to run: '{' '.join(command_parts)}' ({description}) ---")
    try:
        # The 'capture_output=True' is for demonstration; in a real 'free shell run'
        # you might just let it print to stdout/stderr directly.
        # 'text=True' decodes stdout/stderr as text.
        result = subprocess.run(
            command_parts,
            capture_output=True,
            text=True,
            check=False, # Do not raise an exception for non-zero exit codes immediately
            shell=False  # Prefer shell=False for security and explicit command parsing
        )

        if result.returncode == 0:
            print(f"SUCCESS: Command executed.")
            print("STDOUT:\n" + result.stdout.strip())
            if result.stderr:
                print("STDERR:\n" + result.stderr.strip())
        else:
            print(f"FAILURE: Command exited with code {result.returncode}.")
            print("STDOUT:\n" + result.stdout.strip())
            print("STDERR:\n" + result.stderr.strip())
            print(f"  -> This illustrates the 'it works on my machine' problem: "
                  f"this command might fail if '{command_parts[0]}' is not in PATH "
                  f"or has a different version on another system.")
    except FileNotFoundError:
        print(f"ERROR: Command '{command_parts[0]}' not found in system PATH.")
        print(f"  -> This is a classic 'free shell run' issue. "
              f"The script implicitly relies on the environment.")
    except Exception as e:
        print(f"AN UNEXPECTED ERROR OCCURRED: {e}")

print("--- Demonstrating 'Free Shell Run' vs. Toolchain Pinning ---")
print("This script attempts to run external commands, relying on the system's PATH.")
print("Its success and output will vary based on your environment, illustrating the problem.")

# Example 1: Relying on 'python' alias
# The 'python' command might point to python2, python3, or not exist.
run_command([sys.executable, "--version"], "Checking current Python interpreter version")
# COMMENT: The above command uses sys.executable to explicitly get the current interpreter.
# However, if a script *just* ran 'python --version' without this, its outcome would depend
# entirely on your system's PATH configuration for 'python'.
# On some systems, 'python' might be Python 2, on others Python 3, or it might not be defined at all.
# This is a prime example of a 'free shell run' where the environment dictates behavior.

# Example 2: Relying on 'python3' specifically
# This is slightly more specific but still relies on 'python3' being in PATH.
run_command(["python3", "--version"], "Checking specific 'python3' version")
# COMMENT: While 'python3' is more specific, its exact version and availability still depend on the system.
# A project requiring Python 3.9 might fail if only Python 3.6 is available in PATH.

# Example 3: Relying on an external tool 'jq' (JSON processor)
# 'jq' is a common tool but often not installed by default.
run_command(["jq", "--version"], "Checking 'jq' (JSON processor) version")
# COMMENT: 'jq' is a powerful tool, but not universally installed.
# If 'jq' is not found, this command will fail, even if the rest of the script works.
# This highlights the need to explicitly manage and pin external tool dependencies.

print("\n--- End of Demonstration ---")
print("To see the 'it works on my machine' problem, try running this script on different systems")
print("or after modifying your system's PATH or installing/uninstalling 'jq'.")
print("Toolchain pinning involves explicitly defining and managing these dependencies (e.g., via Docker, virtual environments, or specific installation scripts).")
