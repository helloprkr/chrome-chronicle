# ChromeChronicle System Architecture 🏗️

This document outlines the architecture and workflow of ChromeChronicle.

## System Components

```
┌────────────────┐     ┌─────────────────┐     ┌────────────────────┐
│                │     │                 │     │                    │
│  Chrome        │────▶│  ChromeChronicle│────▶│  Markdown Files    │
│  History DB    │     │  Python Script  │     │  (Organized by Date)│
│                │     │                 │     │                    │
└────────────────┘     └─────────────────┘     └────────────────────┘
        │                       ▲                         │
        │                       │                         │
        │                       │                         │
        │                  ┌────┴────────┐                │
        │                  │             │                │
        └──────────────────▶  macOS      │◀───────────────┘
                           │  LaunchD    │
                           │             │
                           └─────────────┘
```

## Workflow

1. **Initialization**:
   - LaunchD starts ChromeChronicle at the scheduled time (default: 11:45 PM)
   - The script determines today's date and prepares directory paths

2. **Data Acquisition**:
   - A temporary copy of Chrome's history database is created to avoid locking issues
   - SQLite queries extract URLs visited during the current day
   - Chrome timestamp format (microseconds since Jan 1, 1601) is converted to human-readable dates

3. **Data Processing**:
   - URLs, titles, timestamps, and visit counts are extracted
   - Data is formatted into a clean markdown table structure
   - Special characters are escaped to ensure valid markdown

4. **File Organization**:
   - Year-month directories are created if they don't exist (e.g., "2025-03/")
   - Files are named with the format "YYYY-MM-DD_URL-History.md"
   - The markdown content is written to the appropriate file

5. **Cleanup**:
   - Database connections are closed
   - Temporary database copies are deleted
   - Log files record successful completion or any errors

## Technical Notes

### Chrome History Database

The Chrome history database is a SQLite database located at:
```
~/Library/Application Support/Google/Chrome/Default/History
```

Key tables used:
- `urls`: Contains information about visited URLs
- Schema includes: url, title, visit_count, last_visit_time

### LaunchD Integration

ChromeChronicle uses macOS LaunchD for scheduling via a property list (plist) file:
- Located in `~/Library/LaunchAgents/com.user.chromehistory.plist`
- Sets execution time via `StartCalendarInterval` 
- Defines standard output and error log paths

### Markdown Formatting

The markdown output follows this structure:
```markdown
# Browsing History for YYYY-MM-DD

*Collected at: HH:MM:SS*

| Time | Title | URL | Visit Count |
|------|-------|-----|------------|
| HH:MM:SS | Page Title | https://example.com | 1 |
...
```

## Security Considerations

- All data remains on the local machine
- No external API calls or data transmission
- Temporary database copies use secure file handling
- File permissions follow standard macOS conventions 