"""
Example: Using the Web Crawler
This script demonstrates how to use the web crawler with example.com
"""

from web_crawler import WebCrawler


def main():
    print("Web Crawler - Practical Example")
    print("=" * 80)
    
    # Create a crawler for example.com (a safe site for testing)
    print("\nInitializing crawler for example.com...")
    crawler = WebCrawler(
        base_url='https://example.com',
        max_pages=3,     # Limit to 3 pages for demonstration
        delay=2          # 2 second delay between requests
    )
    
    print("Starting crawl...")
    print("-" * 80)
    
    # Start crawling
    data = crawler.crawl()
    
    print("-" * 80)
    print(f"\nCrawling completed! Collected data from {len(data)} page(s)")
    
    # Display results
    print("\nResults Summary:")
    print("=" * 80)
    
    for i, page in enumerate(data, 1):
        print(f"\nPage {i}:")
        print(f"  URL: {page['url']}")
        print(f"  Title: {page['title']}")
        print(f"  Headings found: {len(page['headings'])}")
        if page['headings']:
            for heading in page['headings'][:3]:  # Show first 3 headings
                print(f"    - {heading}")
        print(f"  Paragraphs found: {len(page['paragraphs'])}")
        if page['paragraphs']:
            # Show first paragraph preview
            first_para = page['paragraphs'][0][:100] if page['paragraphs'] else "N/A"
            print(f"    Preview: {first_para}...")
        print(f"  Total links: {page['links_count']}")
    
    # Save to file
    print("\n" + "=" * 80)
    output_file = 'example_scraped_data.txt'
    crawler.save_to_file(output_file)
    print(f"\nFull data has been saved to: {output_file}")
    
    print("\n" + "=" * 80)
    print("Example completed successfully!")
    print("\nTo crawl a different website:")
    print("1. Change the base_url in this script")
    print("2. Adjust max_pages and delay as needed")
    print("3. Run: python example_crawler_usage.py")
    print("\nRemember to:")
    print("- Check robots.txt")
    print("- Respect terms of service")
    print("- Use appropriate delays")
    print("=" * 80)


if __name__ == "__main__":
    main()
