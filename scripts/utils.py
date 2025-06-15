"""
Lord-Ugah-AI-v6 Shared Utilities

Provides a function to get the current date and time from the OS shell.
"""
import subprocess

def get_current_datetime():
    """Get the current date and time as YYYY-MM-DD HH:MM:SS using a shell command."""
    return subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S"]).decode().strip() 