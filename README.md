# AI News Aggregator

A Python application that aggregates and displays the latest news about Artificial Intelligence from various sources.

## Requirements

- **Python 3.11.7** (or Python 3.7+)
- `requests` library

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install requests
```

Or using a requirements file:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the aggregator with default settings:
```bash
python main.py
```

### Command Line Options

- `-l, --limit N`: Limit the number of news items to display
  ```bash
  python main.py --limit 5
  ```

- `-j, --json`: Save news items to a JSON file
  ```bash
  python main.py --json
  ```

- Combine options:
  ```bash
  python main.py --limit 10 --json
  ```

## Example Output

```
================================================================================
AI NEWS AGGREGATOR - 2024-01-15 14:30:00
================================================================================

1. New Breakthrough in Large Language Models
   Source: Hacker News
   Author: john_doe
   Points: 245 | Comments: 42
   URL: https://example.com/article
   Date: 2024-01-15T10:00:00Z

2. AI Ethics: The Future of Responsible AI
   Source: Hacker News
   Author: jane_smith
   Points: 189 | Comments: 28
   URL: https://example.com/article2
   Date: 2024-01-15T09:30:00Z
```

## Project Structure

```
ai-news-aggregator/
├── main.py          # Main application file
├── README.md        # This file
├── requirements.txt # Python dependencies
├── .python-version  # Python version (3.11.7)
└── runtime.txt      # Runtime version specification
```

## Python Version

This project is configured for **Python 3.11.7**. 

- `.python-version` - Used by pyenv to set the Python version
- `runtime.txt` - Used by deployment platforms (Heroku, etc.)

To verify your Python version:
```bash
python --version
```

## Configuration

You can extend the aggregator by adding more news sources in the `AINewsAggregator` class. Modify the `sources` list in the `__init__` method to include additional APIs or RSS feeds.

## Future Enhancements

- Add more news sources (Reddit, Twitter, RSS feeds)
- Add filtering by keywords or topics
- Add date range filtering
- Add web interface
- Add email notifications
- Add database storage for historical news

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.

## Author

Created as part of the AI News Aggregator project.

