# Libs
import subprocess
import datetime

# Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def run_bandit():
    project_path = input("Enter the directory path to scan: ")
    command = f"bandit -r {project_path}"
    current_time = datetime.datetime.now()

    # Start Time
    start_message = f"{Colors.HEADER}\n[+] Run started: {current_time}{Colors.ENDC}\n"
    print(start_message)

    # Save Results In File
    with open("bandit_scan_results.txt", "a") as file:
        file.write(start_message + "\n")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Validate Results
        if result.returncode == 0:
            success_message = f"{Colors.OKGREEN}No security issues found.{Colors.ENDC}\n"
            print(success_message)
            with open("review_scan_results.txt", "a") as file:
                file.write(success_message + "\n")
        else:
            error_message = f"{Colors.FAIL}Security issues found. Details:{Colors.ENDC}\n"
            print(error_message)
            print(result.stdout)
            with open("review_scan_results.txt", "a") as file:
                file.write(error_message + "\n")
                file.write(result.stdout + "\n")
    except Exception as e:
        error_message = f"{Colors.FAIL}Error running Bandit: {e}{Colors.ENDC}\n"
        print(error_message)
        with open("bandit_scan_results.txt", "a") as file:
            file.write(error_message + "\n")

# Use Founction
run_bandit()
