# Changelog

All notable changes to ChromeChronicle will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-03-07

### 🚀 Initial Release

#### Added
- Core functionality to extract Chrome browsing history
- Automatic daily execution via macOS LaunchD
- Markdown formatting with timestamps and visit counts
- Organization of history files by year-month directories
- Installation script for easy setup
- Comprehensive documentation
- MIT License

#### Technical Details
- SQLite database interaction for Chrome history
- Timestamp conversion from Chrome format
- Error handling for database locking issues
- Temporary file creation for database access

## [Unreleased]

### Planned Features
- Browser support for Firefox, Safari, and Edge
- Data visualization of browsing patterns
- Search functionality across history files
- Integration with popular note-taking apps
- Command-line interface for advanced usage
- Web UI for browsing history (optional)
- Multi-user support
- Domain categorization and analytics 