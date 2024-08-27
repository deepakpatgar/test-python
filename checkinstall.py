import subprocess

def check_parquet_tools_installed():
    try:
        # Run the command to check version
        result = subprocess.run(['parquet-tools', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("parquet-tools is installed.")
            print("Version:", result.stdout.strip())
        else:
            print("parquet-tools is not installed or not found in PATH.")
    except FileNotFoundError:
        print("parquet-tools is not installed or not found in PATH.")

check_parquet_tools_installed()
