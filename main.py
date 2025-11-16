"""
AI News Aggregator
A Python application that aggregates and displays the latest AI news from various sources.
Requires Python 3.7 or higher (tested with Python 3.11.7).
"""

import requests
import json
from datetime import datetime
from typing import List, Dict, Optional
import sys


class AINewsAggregator:
    """Main class for aggregating AI news from various sources."""
    
    def __init__(self):
        self.news_items: List[Dict] = []
        self.sources = [
            {
                "name": "Hacker News AI",
                "url": "https://hn.algolia.com/api/v1/search",
                "params": {"query": "artificial intelligence", "tags": "story", "hitsPerPage": 10}
            }
        ]
    
    def fetch_hacker_news(self) -> List[Dict]:
        """Fetch AI-related news from Hacker News API."""
        try:
            response = requests.get(
                self.sources[0]["url"],
                params=self.sources[0]["params"],
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            news_items = []
            for hit in data.get("hits", []):
                news_items.append({
                    "title": hit.get("title", "No title"),
                    "url": hit.get("url", hit.get("story_url", "")),
                    "author": hit.get("author", "Unknown"),
                    "points": hit.get("points", 0),
                    "comments": hit.get("num_comments", 0),
                    "created_at": hit.get("created_at", ""),
                    "source": "Hacker News"
                })
            return news_items
        except requests.RequestException as e:
            print(f"Error fetching from Hacker News: {e}", file=sys.stderr)
            return []
    
    def fetch_news(self) -> None:
        """Fetch news from all configured sources."""
        print("Fetching AI news...")
        self.news_items = []
        
        # Fetch from Hacker News
        hacker_news = self.fetch_hacker_news()
        self.news_items.extend(hacker_news)
        
        print(f"Fetched {len(self.news_items)} news items")
    
    def display_news(self, limit: Optional[int] = None) -> None:
        """Display aggregated news items."""
        if not self.news_items:
            print("No news items available.")
            return
        
        items_to_display = self.news_items[:limit] if limit else self.news_items
        
        print("\n" + "="*80)
        print(f"AI NEWS AGGREGATOR - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")
        
        for idx, item in enumerate(items_to_display, 1):
            print(f"{idx}. {item['title']}")
            print(f"   Source: {item['source']}")
            print(f"   Author: {item.get('author', 'N/A')}")
            if 'points' in item:
                print(f"   Points: {item['points']} | Comments: {item['comments']}")
            if item.get('url'):
                print(f"   URL: {item['url']}")
            if item.get('created_at'):
                print(f"   Date: {item['created_at']}")
            print()
    
    def save_to_json(self, filename: str = "ai_news.json") -> None:
        """Save news items to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.news_items, f, indent=2, ensure_ascii=False)
            print(f"News saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}", file=sys.stderr)
    
    def run(self, limit: Optional[int] = None, save_json: bool = False) -> None:
        """Main execution method."""
        self.fetch_news()
        self.display_news(limit=limit)
        
        if save_json:
            self.save_to_json()


def main():
    """Main entry point for the application."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="AI News Aggregator - Fetch and display the latest AI news"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit the number of news items to display"
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Save news items to JSON file"
    )
    
    args = parser.parse_args()
    
    aggregator = AINewsAggregator()
    aggregator.run(limit=args.limit, save_json=args.json)


if __name__ == "__main__":
    main()

