# 📜 ChromeChronicle

<div align="center">

![ChromeChronicle Logo](./images/logo.png)

*Your browsing history, beautifully chronicled.*

[![GitHub stars](https://img.shields.io/github/stars/yourusername/ChromeChronicle?style=social)](https://github.com/yourusername/ChromeChronicle/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![macOS](https://img.shields.io/badge/platform-macOS-blue.svg)](https://www.apple.com/macos)

</div>

## 🌟 Overview

ChromeChronicle automatically extracts your daily Chrome browsing history and saves it as beautifully formatted markdown files, organized by month. Keep track of your digital journeys with minimal effort!

### ✨ Key Features

- 🔄 **Daily Automation**: Set it once, and forget it! Runs daily at your specified time
- 📊 **Beautiful Markdown Format**: Your history presented in an easy-to-read table format
- 📂 **Organized by Month**: Automatically creates and organizes files into year-month directories
- 📱 **Lightweight**: Minimal system impact, runs in the background
- 🔒 **Local Storage**: Your data stays on your machine, ensuring privacy

<div align="center">

![Example Output](./images/example-output.png)

</div>

## 📋 Requirements

- macOS (10.15 Catalina or newer)
- Python 3.6+
- Google Chrome browser
- Basic Terminal knowledge

## 🚀 Installation

### Option 1: Quick Install (Recommended)

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ChromeChronicle.git
   cd ChromeChronicle
   ```

2. Run the installation script:
   ```bash
   chmod +x install_chrome_history_automation.sh
   ./install_chrome_history_automation.sh
   ```

3. You're all set! ChromeChronicle will run daily at 11:45 PM by default.

### Option 2: Manual Installation

<details>
<summary>Click to expand manual installation steps</summary>

1. Clone this repository:
   ```bash
   git clone https://github.com/HelloPrkr/ChromeChronicle.git
   cd ChromeChronicle
   ```

2. Make the Python script executable:
   ```bash
   chmod +x chrome_history_extractor.py
   ```

3. Edit the plist file to update paths:
   ```bash
   nano com.user.chromehistory.plist
   ```
   Replace all instances of `REPLACE_WITH_FULL_PATH` with the full path to your ChromeChronicle directory.

4. Copy the plist file to your LaunchAgents directory:
   ```bash
   mkdir -p ~/Library/LaunchAgents
   cp com.user.chromehistory.plist ~/Library/LaunchAgents/
   ```

5. Load the launchd job:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.chromehistory.plist
   ```

</details>

## 🖥️ Usage

ChromeChronicle will automatically run every day at the scheduled time (default: 11:45 PM). Your browsing history will be saved in markdown format in the directory structure:

```
YYYY-MM/YYYY-MM-DD_URL-History.md
```

For example:
```
2025-03/2025-03-07_URL-History.md
```

### 📝 Manual Execution

You can run ChromeChronicle manually at any time:

```bash
python3 /path/to/ChromeChronicle/chrome_history_extractor.py
```

<div align="center">

![Usage Workflow](./images/workflow.png)

</div>

## 🛠️ Customization

### Changing the Schedule

To change when ChromeChronicle runs:

1. Unload the current configuration:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.chromehistory.plist
   ```

2. Edit the plist file:
   ```bash
   nano ~/Library/LaunchAgents/com.user.chromehistory.plist
   ```

3. Update the `Hour` and `Minute` values under `StartCalendarInterval`.

4. Reload the configuration:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.chromehistory.plist
   ```

### Output Format Customization

To customize the Markdown output format, edit the `extract_chrome_history()` function in `chrome_history_extractor.py`.

## 🔍 Troubleshooting

<details>
<summary>No history is being saved</summary>

Check the following:
- Ensure Chrome is installed in the default location
- Verify your LaunchAgent is loaded properly:
  ```bash
  launchctl list | grep chromehistory
  ```
- Check log files for errors:
  ```bash
  cat ~/path/to/ChromeChronicle/chrome_history_error.log
  ```
</details>

<details>
<summary>Installation script fails</summary>

- Make sure you have the proper permissions
- Try running the manual installation steps
- Check if Python 3 is installed correctly:
  ```bash
  python3 --version
  ```
</details>

## 🧩 Technical Details

### How It Works

<div align="center">

![Architecture Diagram](./images/architecture.png)

</div>

ChromeChronicle works by:

1. Creating a temporary copy of Chrome's SQLite history database
2. Querying for URLs visited on the current day
3. Converting Chrome's timestamp format (microseconds since Jan 1, 1601)
4. Formatting the data into a readable markdown table
5. Organizing files by year and month

## 📚 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💖 Acknowledgments

- Inspired by the need to better understand our digital journeys
- Thanks to the SQLite project for making database access so straightforward
- Special thanks to all Alxmnt Ai Labs Team for their support and guidance!

---

<div align="center">

Made with ❤️ by [HelloPrkr](https://github.com/HelloPrkr)

If you find ChromeChronicle useful, please consider giving it a ⭐ on GitHub and sharing it with friends!

</div> 