# Chrome Browsing History Automation

This automation extracts your daily Chrome browsing history and saves it as a markdown file in your Memory-🧿 directory, organized by month (e.g., 2025-03).

## Components

1. `chrome_history_extractor.py` - Python script that extracts the Chrome history and saves it as a markdown file
2. `com.user.chromehistory.plist` - LaunchDaemon configuration file for macOS
3. `install_chrome_history_automation.sh` - Installation script

## Features

- Extracts Chrome browsing history for the current day
- Organizes files by month in dedicated folders
- Uses filename format: `YYYY-MM-DD_URL-History.md`
- Runs automatically at 11:45 PM daily
- Creates log files for debugging

## Installation

1. Open Terminal
2. Navigate to the Memory-🧿 directory
3. Run the installation script:

```bash
cd /path/to/Memory-🧿
chmod +x install_chrome_history_automation.sh
./install_chrome_history_automation.sh
```

## Manual Execution

To run the script manually:

```bash
python3 /path/to/Memory-🧿/chrome_history_extractor.py
```

## Troubleshooting

If the automation isn't working:

1. Check the log files in the Memory-🧿 directory
2. Ensure Chrome is installed in the default location
3. Verify the LaunchAgent is loaded:

```bash
launchctl list | grep chromehistory
```

## Uninstallation

To remove the automation:

```bash
launchctl unload ~/Library/LaunchAgents/com.user.chromehistory.plist
rm ~/Library/LaunchAgents/com.user.chromehistory.plist
```

## Notes

- The script creates a temporary copy of Chrome's history database to avoid locking issues
- Chrome stores timestamps in microseconds since January 1, 1601
- The Chrome history database may be locked if Chrome is running, but the script handles this gracefully 