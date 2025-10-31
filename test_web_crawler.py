"""
Test script for the web crawler.
This tests the WebCrawler class functionality with a simple HTML example.
"""

from web_crawler import WebCrawler
from bs4 import BeautifulSoup


def test_url_validation():
    """Test URL validation logic."""
    print("Testing URL validation...")
    crawler = WebCrawler('https://example.com', max_pages=5)
    
    # Same domain - should be valid
    assert crawler.is_valid_url('https://example.com/page1') == True
    assert crawler.is_valid_url('https://example.com/about') == True
    
    # Different domain - should be invalid
    assert crawler.is_valid_url('https://google.com') == False
    assert crawler.is_valid_url('https://other-site.com') == False
    
    print("✓ URL validation tests passed")


def test_data_extraction():
    """Test data extraction from HTML."""
    print("\nTesting data extraction...")
    
    # Create a sample HTML
    html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Main Heading</h1>
            <h2>Subheading</h2>
            <p>This is the first paragraph.</p>
            <p>This is the second paragraph.</p>
            <a href="/page1">Link 1</a>
            <a href="/page2">Link 2</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    crawler = WebCrawler('https://example.com')
    
    data = crawler.extract_data(soup, 'https://example.com/test')
    
    assert data['title'] == 'Test Page'
    assert len(data['headings']) == 2
    assert 'Main Heading' in data['headings']
    assert len(data['paragraphs']) == 2
    assert data['links_count'] == 2
    
    print("✓ Data extraction tests passed")


def test_link_extraction():
    """Test link extraction from HTML."""
    print("\nTesting link extraction...")
    
    html = """
    <html>
        <body>
            <a href="/page1">Page 1</a>
            <a href="/page2">Page 2</a>
            <a href="https://example.com/page3">Page 3</a>
            <a href="https://other.com/page4">External</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    crawler = WebCrawler('https://example.com')
    
    links = crawler.extract_links(soup, 'https://example.com')
    
    # Should extract internal links but not external ones
    assert len(links) >= 3  # At least the 3 internal links
    assert any('page1' in link for link in links)
    assert any('page2' in link for link in links)
    assert any('page3' in link for link in links)
    # Verify external domain is excluded (security feature)
    external_domain = 'other.com'
    assert not any(external_domain in link for link in links)
    
    print("✓ Link extraction tests passed")


def test_crawler_initialization():
    """Test crawler initialization."""
    print("\nTesting crawler initialization...")
    
    crawler = WebCrawler('https://example.com', max_pages=15, delay=2)
    
    assert crawler.base_url == 'https://example.com'
    assert crawler.max_pages == 15
    assert crawler.delay == 2
    assert len(crawler.visited_urls) == 0
    assert len(crawler.scraped_data) == 0
    
    print("✓ Crawler initialization tests passed")


if __name__ == "__main__":
    print("=" * 80)
    print("Running Web Crawler Tests")
    print("=" * 80)
    
    try:
        test_crawler_initialization()
        test_url_validation()
        test_data_extraction()
        test_link_extraction()
        
        print("\n" + "=" * 80)
        print("All tests passed! ✓")
        print("=" * 80)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        raise
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        raise
