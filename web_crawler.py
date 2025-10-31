"""
Web Crawler Script
A simple web crawler to scrape data from websites using BeautifulSoup and requests.

Dependencies:
- beautifulsoup4
- requests

Install with: pip install beautifulsoup4 requests
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


class WebCrawler:
    """A simple web crawler for scraping data from websites."""
    
    def __init__(self, base_url, max_pages=10, delay=1):
        """
        Initialize the web crawler.
        
        Args:
            base_url (str): The starting URL to crawl
            max_pages (int): Maximum number of pages to crawl
            delay (int): Delay in seconds between requests (be polite!)
        """
        self.base_url = base_url
        self.max_pages = max_pages
        self.delay = delay
        self.visited_urls = set()
        self.scraped_data = []
        
    def is_valid_url(self, url):
        """
        Check if a URL is valid and belongs to the same domain.
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return bool(parsed.netloc) and parsed.netloc == base_parsed.netloc
    
    def get_page_content(self, url):
        """
        Fetch the content of a webpage.
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup object or None if request fails
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup, current_url):
        """
        Extract all links from a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            current_url (str): Current page URL for resolving relative links
            
        Returns:
            list: List of absolute URLs
        """
        links = []
        for link in soup.find_all('a', href=True):
            url = urljoin(current_url, link['href'])
            if self.is_valid_url(url) and url not in self.visited_urls:
                links.append(url)
        return links
    
    def extract_data(self, soup, url):
        """
        Extract data from a page. Customize this method for your needs.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            url (str): Current page URL
            
        Returns:
            dict: Extracted data
        """
        # Example: Extract title, headings, and paragraphs
        data = {
            'url': url,
            'title': soup.title.string if soup.title else 'No title',
            'headings': [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])],
            'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')[:5]],  # First 5 paragraphs
            'links_count': len(soup.find_all('a'))
        }
        return data
    
    def crawl(self):
        """
        Start crawling from the base URL.
        
        Returns:
            list: List of dictionaries containing scraped data
        """
        urls_to_visit = [self.base_url]
        
        while urls_to_visit and len(self.visited_urls) < self.max_pages:
            current_url = urls_to_visit.pop(0)
            
            if current_url in self.visited_urls:
                continue
            
            print(f"Crawling: {current_url}")
            self.visited_urls.add(current_url)
            
            # Fetch page content
            soup = self.get_page_content(current_url)
            if soup is None:
                continue
            
            # Extract data from the page
            page_data = self.extract_data(soup, current_url)
            self.scraped_data.append(page_data)
            
            # Find new links to crawl
            new_links = self.extract_links(soup, current_url)
            urls_to_visit.extend(new_links)
            
            # Be polite - wait between requests
            time.sleep(self.delay)
        
        print(f"\nCrawling completed! Visited {len(self.visited_urls)} pages.")
        return self.scraped_data
    
    def save_to_file(self, filename='scraped_data.txt'):
        """
        Save scraped data to a text file.
        
        Args:
            filename (str): Output filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            for i, data in enumerate(self.scraped_data, 1):
                f.write(f"\n{'='*80}\n")
                f.write(f"Page {i}: {data['url']}\n")
                f.write(f"{'='*80}\n")
                f.write(f"Title: {data['title']}\n\n")
                
                if data['headings']:
                    f.write("Headings:\n")
                    for heading in data['headings']:
                        f.write(f"  - {heading}\n")
                    f.write("\n")
                
                if data['paragraphs']:
                    f.write("Sample Paragraphs:\n")
                    for para in data['paragraphs'][:3]:
                        if para:
                            f.write(f"  {para[:200]}...\n")
                    f.write("\n")
                
                f.write(f"Total links found: {data['links_count']}\n")
        
        print(f"Data saved to {filename}")


# Example usage
if __name__ == "__main__":
    # Example: Crawl a website (replace with actual URL)
    print("Web Crawler Example")
    print("=" * 80)
    print("\nThis is a demonstration of the web crawler.")
    print("To use it, modify the base_url variable below.\n")
    
    # Example usage (commented out - replace with actual URL to use)
    # crawler = WebCrawler(
    #     base_url='https://example.com',
    #     max_pages=5,
    #     delay=1
    # )
    # 
    # data = crawler.crawl()
    # crawler.save_to_file('scraped_data.txt')
    # 
    # # Print summary
    # print(f"\nScraped {len(data)} pages:")
    # for item in data:
    #     print(f"  - {item['title']} ({item['url']})")
    
    print("\nTo use this crawler:")
    print("1. Install dependencies: pip install beautifulsoup4 requests")
    print("2. Uncomment the example code above")
    print("3. Replace 'https://example.com' with your target URL")
    print("4. Run the script: python web_crawler.py")
    print("\nNote: Always respect robots.txt and website terms of service!")
