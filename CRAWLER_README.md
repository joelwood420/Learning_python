# Web Crawler

A simple and educational web crawler built with Python to scrape data from websites.

## Features

- **URL Crawling**: Automatically discovers and visits links within the same domain
- **Data Extraction**: Extracts titles, headings, paragraphs, and link counts from web pages
- **Polite Crawling**: Includes configurable delays between requests to be respectful to servers
- **Error Handling**: Robust error handling for network issues and invalid URLs
- **Customizable**: Easy to modify the `extract_data()` method for specific scraping needs
- **Data Export**: Save scraped data to text files

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install beautifulsoup4 requests
```

## Usage

### Basic Usage

```python
from web_crawler import WebCrawler

# Create a crawler instance
crawler = WebCrawler(
    base_url='https://example.com',
    max_pages=10,    # Maximum number of pages to crawl
    delay=1          # Delay in seconds between requests
)

# Start crawling
data = crawler.crawl()

# Save data to file
crawler.save_to_file('scraped_data.txt')

# Access scraped data
for page in data:
    print(f"Title: {page['title']}")
    print(f"URL: {page['url']}")
    print(f"Headings: {page['headings']}")
```

### Customizing Data Extraction

To extract specific data from pages, modify the `extract_data()` method in the `WebCrawler` class:

```python
def extract_data(self, soup, url):
    # Custom extraction logic
    data = {
        'url': url,
        'title': soup.title.string if soup.title else 'No title',
        # Add your custom extraction here
        'images': [img['src'] for img in soup.find_all('img', src=True)],
        'meta_description': soup.find('meta', attrs={'name': 'description'})
    }
    return data
```

## Important Notes

### Ethical Web Scraping

- **Always check robots.txt**: Respect the website's robots.txt file
- **Terms of Service**: Review and comply with the website's terms of service
- **Rate Limiting**: Use appropriate delays between requests (default is 1 second)
- **User Agent**: The crawler uses a proper User-Agent header
- **Legal Compliance**: Ensure your scraping activities are legal in your jurisdiction

### Best Practices

1. **Start Small**: Begin with a small `max_pages` value to test
2. **Increase Delays**: For production use, consider delays of 2-3 seconds or more
3. **Handle Errors**: The crawler includes error handling, but always monitor your scraping
4. **Data Privacy**: Don't scrape personal or sensitive information
5. **Server Load**: Be mindful of the load you're placing on target servers

## Example Output

When you run the crawler, it will display progress and create a data file:

```
Crawling: https://example.com
Crawling: https://example.com/about
Crawling: https://example.com/contact

Crawling completed! Visited 3 pages.
Data saved to scraped_data.txt
```

The output file will contain structured data from each page visited.

## Class Reference

### WebCrawler

**Constructor Parameters:**
- `base_url` (str): The starting URL for crawling
- `max_pages` (int, default=10): Maximum number of pages to crawl
- `delay` (int, default=1): Delay in seconds between requests

**Methods:**
- `crawl()`: Start the crawling process and return scraped data
- `save_to_file(filename)`: Save scraped data to a text file
- `extract_data(soup, url)`: Extract data from a page (customize for your needs)
- `get_page_content(url)`: Fetch and parse a webpage
- `extract_links(soup, current_url)`: Extract all links from a page
- `is_valid_url(url)`: Validate if a URL should be crawled

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'bs4'`
- **Solution**: Install dependencies with `pip install beautifulsoup4 requests`

**Issue**: `requests.exceptions.ConnectionError`
- **Solution**: Check your internet connection and the target URL

**Issue**: No data being scraped
- **Solution**: Check if the website blocks automated requests or requires authentication

## License

This is an educational project. Use responsibly and ethically.

## Contributing

Feel free to fork and improve this crawler for educational purposes!
