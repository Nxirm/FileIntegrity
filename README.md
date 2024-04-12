# File Integrity Monitoring
The File Integrity Monitoring (FIM) script is a Python-based tool designed to monitor specified directories for file changes and detect modifications to files in real-time. It uses hashing (SHA-256) for files and captures the last modification timestamp of each file to track when changes occur. 
<br>
![image](https://github.com/Nxirm/FileIntegrity/assets/86094721/4aeb9442-6132-40f9-87db-30ed6bca8686)
<br>
# Key Features:

    Interactive Directory Input: The script prompts the user to input one or more directory paths to monitor interactively. Users can specify directories containing important files or critical system components.

    SHA-256 Hash Calculation: For each file within the monitored directories, the script calculates a SHA-256 hash to uniquely identify the file based on its content. The hash serves as a fingerprint for the file.

    Last Modification Timestamp Tracking: In addition to the file hash, the script captures the last modification timestamp (in ISO 8601 format) of each file. This information helps track when files were last modified.

    Continuous Monitoring: The script runs continuously in a loop, periodically checking for changes within the specified directories. It compares the current file hashes and modification timestamps with previously recorded values to identify modifications or new files.

    Real-time Alerts: When a file modification is detected (i.e., the hash or modification timestamp differs from the recorded values), the script generates a real-time alert indicating the file that was modified and when it was last modified.

    New File Detection: The script also detects newly added files within the monitored directories. It notifies the user when a new file is detected, which may indicate unauthorized file additions.

    Persistence: The script uses a persistent data structure (file_info dictionary) to store and update file hashes and modification timestamps across monitoring iterations. This ensures continuity and accurate tracking of file changes over time.
# Usage Instructions:

    Execution: Open the terminal and run python <name of the script>
    Directory Input: Enter directory paths (e.g., C:\ImportantFiles) to monitor when prompted. Press Enter with no input to finish entering paths.
    Monitoring: The script continuously monitors the specified directories, checking for file changes at regular intervals (e.g., every 60 seconds).
    Alerts: If a file modification or new file is detected, the script prints a corresponding alert message to the console, providing details about the affected file and when the modification occurred.
    Termination: Exit the script gracefully by pressing Ctrl+C to handle a keyboard interrupt (SIGINT).

# Running the File Integrity Monitoring (FIM) Script
**Prerequisites:**
1. Python 3.x installed on your system (https://www.python.org/downloads/)
2. JSON
3. Date-time
4. hashlib

**Run the Script:**
<br>
python file_integrity_monitor.py

# Output
![image](https://github.com/Nxirm/FileIntegrity/assets/86094721/a5d24596-0e3a-4d37-9409-1f01315ef5a5)
