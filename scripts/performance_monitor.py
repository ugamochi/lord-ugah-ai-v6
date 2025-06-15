"""
Lord-Ugah-AI-v6 Performance Monitor Script

This script analyzes the system for performance metrics:
- Counts Ugahbases and notes
- Calculates total and average file size
- Lists the largest files
- Flags potential performance issues (e.g., large files, too many notes)
"""
import os
from glob import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Try both possible locations for ugahbases
CANDIDATES = [
    os.path.join(SCRIPT_DIR, "..", "ugahbases"),
    os.path.join(SCRIPT_DIR, "..", "..", "ugahbases"),
]
UGAHBASES_DIR = None
for candidate in CANDIDATES:
    abs_candidate = os.path.abspath(candidate)
    if os.path.isdir(abs_candidate):
        UGAHBASES_DIR = abs_candidate
        break
if UGAHBASES_DIR is None:
    raise FileNotFoundError("Could not find 'ugahbases' directory relative to script location.")

MAX_NOTE_SIZE = 50 * 1024  # 50KB
MAX_TOTAL_NOTES = 1000


def get_note_files():
    """Return a list of all markdown note files in Ugahbases."""
    return glob(os.path.join(UGAHBASES_DIR, "**", "*.md"), recursive=True)


def analyze_performance():
    notes = get_note_files()
    ugahbases = [d for d in os.listdir(UGAHBASES_DIR) if os.path.isdir(os.path.join(UGAHBASES_DIR, d)) and not d.startswith('.')]
    total_size = 0
    largest_files = []
    for note in notes:
        size = os.path.getsize(note)
        total_size += size
        largest_files.append((note, size))
    largest_files.sort(key=lambda x: x[1], reverse=True)
    avg_size = total_size // len(notes) if notes else 0
    return {
        "ugahbase_count": len(ugahbases),
        "note_count": len(notes),
        "total_size_kb": total_size // 1024,
        "avg_size_kb": avg_size // 1024,
        "largest_files": largest_files[:5],
        "oversized_files": [f for f in largest_files if f[1] > MAX_NOTE_SIZE],
    }


def print_report(stats):
    print("[Lord-Ugah-AI-v6] Performance Report")
    print(f"Ugahbases: {stats['ugahbase_count']}")
    print(f"Notes: {stats['note_count']}")
    print(f"Total note size: {stats['total_size_kb']} KB")
    print(f"Average note size: {stats['avg_size_kb']} KB")
    print("Largest files:")
    for f, sz in stats['largest_files']:
        print(f"  {f} ({sz // 1024} KB)")
    if stats['oversized_files']:
        print("Warning: Oversized notes detected (>50KB):")
        for f, sz in stats['oversized_files']:
            print(f"  {f} ({sz // 1024} KB)")
    if stats['note_count'] > MAX_TOTAL_NOTES:
        print(f"Warning: High note count ({stats['note_count']}) may impact performance.")
    print("Performance check complete.")


def main():
    stats = analyze_performance()
    print_report(stats)


if __name__ == "__main__":
    main() 