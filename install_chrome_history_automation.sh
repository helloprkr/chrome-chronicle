#!/bin/bash

# Get the absolute path of the directory containing the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Make the Python script executable
chmod +x "$SCRIPT_DIR/chrome_history_extractor.py"

# Update the plist file with the correct paths
PLIST_FILE="$SCRIPT_DIR/com.user.chromehistory.plist"
sed -i '' "s|REPLACE_WITH_FULL_PATH|$SCRIPT_DIR|g" "$PLIST_FILE"

# Copy plist to LaunchAgents directory
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
mkdir -p "$LAUNCH_AGENTS_DIR"
cp "$PLIST_FILE" "$LAUNCH_AGENTS_DIR/"

# Load the plist file
echo "Loading launchd job..."
launchctl unload "$LAUNCH_AGENTS_DIR/com.user.chromehistory.plist" 2>/dev/null
launchctl load "$LAUNCH_AGENTS_DIR/com.user.chromehistory.plist"

echo "Chrome history automation has been installed!"
echo "Your browsing history will be saved daily at 11:45 PM"
echo "Logs will be stored in:"
echo "  - $SCRIPT_DIR/chrome_history_output.log"
echo "  - $SCRIPT_DIR/chrome_history_error.log"
echo ""
echo "To run the script now for testing, execute:"
echo "python3 $SCRIPT_DIR/chrome_history_extractor.py" 