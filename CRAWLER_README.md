# Web Crawler - Beginner's Guide

A simple and educational web crawler built with Python to scrape data from websites. This guide is designed for beginners who are just starting with Python and web scraping.

## Table of Contents
1. [What is a Web Crawler?](#what-is-a-web-crawler)
2. [What You'll Need](#what-youll-need)
3. [Installation Guide](#installation-guide)
4. [Quick Start Guide](#quick-start-guide)
5. [Step-by-Step Tutorial](#step-by-step-tutorial)
6. [Understanding the Code](#understanding-the-code)
7. [Common Use Cases](#common-use-cases)
8. [Troubleshooting](#troubleshooting)

---

## What is a Web Crawler?

A **web crawler** (also called a spider or scraper) is a program that automatically visits web pages and extracts information from them. Think of it like a robot that:
1. Opens a web page
2. Reads the content
3. Finds links to other pages
4. Visits those pages and repeats the process

**What can you do with this crawler?**
- Extract article titles and content from blogs
- Collect product information from websites
- Gather data for research projects
- Build datasets for learning purposes

**Important**: Always respect website rules and terms of service when scraping!

---

## What You'll Need

Before starting, make sure you have:

1. **Python 3.7 or newer** installed on your computer
   - Check by opening a terminal/command prompt and typing: `python --version` or `python3 --version`
   
2. **Internet connection** to download required libraries

3. **A text editor or IDE** (like VS Code, PyCharm, or even Notepad)

---

## Installation Guide

### Step 1: Download the Files

Make sure you have these files in your project folder:
- `web_crawler.py` (the main crawler code)
- `requirements.txt` (list of required libraries)
- `example_crawler_usage.py` (example to get you started)

### Step 2: Install Required Libraries

Open your terminal or command prompt, navigate to your project folder, and run:

```bash
pip install -r requirements.txt
```

This installs two libraries:
- **beautifulsoup4**: Helps parse and extract data from HTML
- **requests**: Helps download web pages

**Windows users**: You might need to use `pip3` instead of `pip`

**Mac/Linux users**: You might need to use `python3 -m pip install -r requirements.txt`

### Step 3: Verify Installation

Check if everything is installed correctly:

```bash
python -c "import requests; import bs4; print('All set!')"
```

If you see "All set!", you're ready to go! 🎉

---

## Quick Start Guide

The fastest way to see the crawler in action:

1. **Run the example script:**
   ```bash
   python example_crawler_usage.py
   ```

2. **Check the output file:**
   - Look for `example_scraped_data.txt` in your folder
   - Open it to see the scraped data!

---

## Step-by-Step Tutorial

### Tutorial 1: Your First Web Scrape

Let's scrape a simple website step by step.

**Step 1**: Create a new Python file called `my_first_scrape.py`

**Step 2**: Import the WebCrawler class:

```python
from web_crawler import WebCrawler
```

**Step 3**: Create a crawler object:

```python
# Create a crawler for example.com
crawler = WebCrawler(
    base_url='https://example.com',  # The website to scrape
    max_pages=3,                      # Only visit 3 pages
    delay=2                           # Wait 2 seconds between requests
)
```

**What these settings mean:**
- `base_url`: The starting website URL
- `max_pages`: How many pages to visit (start small!)
- `delay`: Seconds to wait between requests (be polite to websites!)

**Step 4**: Start crawling:

```python
print("Starting to crawl...")
data = crawler.crawl()
print(f"Done! Scraped {len(data)} pages")
```

**Step 5**: Save the results:

```python
crawler.save_to_file('my_results.txt')
print("Results saved to my_results.txt")
```

**Step 6**: Run your script:

```bash
python my_first_scrape.py
```

**Complete code** for `my_first_scrape.py`:

```python
from web_crawler import WebCrawler

# Create crawler
crawler = WebCrawler(
    base_url='https://example.com',
    max_pages=3,
    delay=2
)

# Start crawling
print("Starting to crawl...")
data = crawler.crawl()
print(f"Done! Scraped {len(data)} pages")

# Save results
crawler.save_to_file('my_results.txt')
print("Results saved to my_results.txt")
```

---

### Tutorial 2: Viewing the Scraped Data

After crawling, you can work with the data in Python:

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://example.com', max_pages=2, delay=1)
data = crawler.crawl()

# Loop through each page that was scraped
for i, page in enumerate(data, 1):
    print(f"\n--- Page {i} ---")
    print(f"URL: {page['url']}")
    print(f"Title: {page['title']}")
    print(f"Number of headings: {len(page['headings'])}")
    print(f"Number of paragraphs: {len(page['paragraphs'])}")
    print(f"Number of links: {page['links_count']}")
    
    # Show the first heading if available
    if page['headings']:
        print(f"First heading: {page['headings'][0]}")
```

**What each field contains:**
- `url`: The web page address
- `title`: The page title (what shows in browser tab)
- `headings`: List of all headings (h1, h2, h3) on the page
- `paragraphs`: List of text paragraphs
- `links_count`: Total number of links found

---

### Tutorial 3: Scraping a Specific Website

Let's say you want to scrape a blog or news site:

```python
from web_crawler import WebCrawler

# Example: Scraping a blog (replace with your target)
crawler = WebCrawler(
    base_url='https://your-target-website.com',
    max_pages=5,      # Scrape 5 pages
    delay=3           # Wait 3 seconds (be extra polite)
)

# Crawl and save
data = crawler.crawl()
crawler.save_to_file('blog_data.txt')

# Print summary
print(f"\nScraped {len(data)} pages!")
for page in data:
    print(f"- {page['title']}")
```

---

## Understanding the Code

### How the Crawler Works

1. **Starts at your base_url**
2. **Downloads the HTML** of that page
3. **Extracts data** (titles, headings, paragraphs)
4. **Finds all links** on the page
5. **Visits those links** (but only on the same website)
6. **Repeats** until max_pages is reached

### Important Settings Explained

**base_url** - Where to start crawling
```python
base_url='https://example.com'  # Start here
```

**max_pages** - How many pages to visit
```python
max_pages=10  # Stop after 10 pages
```
- Start with small numbers (3-5) when testing
- Increase once you're confident it works

**delay** - Seconds to wait between requests
```python
delay=2  # Wait 2 seconds
```
- Minimum: 1 second (be polite!)
- Recommended: 2-3 seconds
- Slower = more polite to the website

### What Data Gets Extracted

The crawler automatically extracts:

| Data Field | Description | Example |
|------------|-------------|---------|
| `url` | Page address | `https://example.com/about` |
| `title` | Page title | `"About Us - Example Site"` |
| `headings` | All headings | `["Welcome", "Our Mission"]` |
| `paragraphs` | Text paragraphs | `["We are a company...", "Our goal is..."]` |
| `links_count` | Number of links | `25` |

---

## Common Use Cases

### Use Case 1: Collecting Article Titles

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://blog-website.com', max_pages=5, delay=2)
data = crawler.crawl()

# Extract all titles
titles = [page['title'] for page in data]

# Save to a simple text file
with open('article_titles.txt', 'w') as f:
    for title in titles:
        f.write(f"{title}\n")

print(f"Saved {len(titles)} titles!")
```

### Use Case 2: Finding All Headings

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://website.com', max_pages=3, delay=2)
data = crawler.crawl()

# Collect all headings from all pages
all_headings = []
for page in data:
    all_headings.extend(page['headings'])

# Print unique headings
unique_headings = set(all_headings)
print(f"Found {len(unique_headings)} unique headings:")
for heading in unique_headings:
    print(f"  - {heading}")
```

### Use Case 3: Extracting Content for Research

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://research-site.com', max_pages=10, delay=3)
data = crawler.crawl()

# Save detailed results
with open('research_data.txt', 'w', encoding='utf-8') as f:
    for i, page in enumerate(data, 1):
        f.write(f"\n{'='*80}\n")
        f.write(f"Document {i}\n")
        f.write(f"{'='*80}\n")
        f.write(f"URL: {page['url']}\n")
        f.write(f"Title: {page['title']}\n\n")
        f.write("Content:\n")
        for para in page['paragraphs']:
            f.write(f"{para}\n\n")

print("Research data saved!")
```

---

---

## Troubleshooting

### Problem 1: "ModuleNotFoundError: No module named 'bs4'"

**What it means:** The beautifulsoup4 library is not installed.

**Solution:**
```bash
pip install beautifulsoup4 requests
```

Or:
```bash
python -m pip install beautifulsoup4 requests
```

---

### Problem 2: "ModuleNotFoundError: No module named 'requests'"

**What it means:** The requests library is not installed.

**Solution:**
```bash
pip install requests
```

---

### Problem 3: No data is being scraped

**Possible reasons:**
1. The website blocks automated requests
2. Your internet connection is down
3. The URL is incorrect

**Solutions:**
- Check your internet connection
- Verify the URL is correct (copy-paste from browser)
- Try a different website first (like example.com)
- Check if you're getting any error messages

---

### Problem 4: The crawler is too slow

**What it means:** The delay setting is high, or the website is slow to respond.

**Solutions:**
- Reduce the `delay` parameter (but keep it at least 1)
- Reduce the `max_pages` parameter
- Check your internet speed

---

### Problem 5: "Connection refused" or "Timeout" errors

**What it means:** The website is not responding or blocking your requests.

**Solutions:**
- Increase the `delay` parameter to 3-5 seconds
- Try again later (the website might be down)
- Some websites block automated access

---

### Problem 6: The output file is empty

**What it means:** No pages were successfully crawled.

**Solutions:**
- Check the console output for error messages
- Verify the base_url is accessible in your browser
- Make sure you have internet connection
- Try with a simpler website like 'https://example.com'

---

## Ethical Guidelines

### ⚠️ IMPORTANT: Legal and Ethical Considerations

**Before scraping any website:**

1. **Check robots.txt**
   - Visit: `https://website.com/robots.txt`
   - Look for rules about crawling
   - Respect "Disallow" directives

2. **Read Terms of Service**
   - Check if scraping is allowed
   - Some websites explicitly prohibit it

3. **Use Appropriate Delays**
   - Never set delay to 0
   - Recommended: 2-3 seconds minimum
   - More is better for larger sites

4. **Respect Copyright**
   - Don't republish scraped content
   - Use data for personal/educational purposes
   - Give credit to original sources

5. **Privacy Matters**
   - Don't scrape personal information
   - Don't scrape private/password-protected pages
   - Respect user privacy

6. **Be Responsible**
   - Don't overload servers
   - Don't scrape excessively
   - Stop if you receive errors

**Good websites to practice on:**
- `https://example.com` - Safe for testing
- `https://books.toscrape.com` - Made for scraping practice
- `https://quotes.toscrape.com` - Another practice site

**Remember:** Just because you *can* scrape a website doesn't mean you *should*!

---

## Advanced Tips

### Tip 1: Save Data as JSON

For easier data processing, save as JSON:

```python
import json
from web_crawler import WebCrawler

crawler = WebCrawler('https://example.com', max_pages=3, delay=2)
data = crawler.crawl()

# Save as JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Data saved as JSON!")
```

### Tip 2: Filter Data

Only keep pages with specific content:

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://website.com', max_pages=10, delay=2)
data = crawler.crawl()

# Only keep pages with "Python" in the title
python_pages = [page for page in data if 'Python' in page['title']]

print(f"Found {len(python_pages)} pages about Python!")
```

### Tip 3: Count Words in Scraped Content

```python
from web_crawler import WebCrawler

crawler = WebCrawler('https://website.com', max_pages=5, delay=2)
data = crawler.crawl()

total_words = 0
for page in data:
    for paragraph in page['paragraphs']:
        total_words += len(paragraph.split())

print(f"Total words scraped: {total_words}")
```

---

## Customizing the Crawler

### Adding More Data Fields

You can modify `web_crawler.py` to extract different data. Open the file and find the `extract_data` method (around line 90).

**Example: Extract image URLs**

Change this section:
```python
def extract_data(self, soup, url):
    data = {
        'url': url,
        'title': soup.title.string if soup.title else 'No title',
        'headings': [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])],
        'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')[:5]],
        'links_count': len(soup.find_all('a'))
    }
    return data
```

To this:
```python
def extract_data(self, soup, url):
    data = {
        'url': url,
        'title': soup.title.string if soup.title else 'No title',
        'headings': [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])],
        'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')[:5]],
        'links_count': len(soup.find_all('a')),
        'images': [img['src'] for img in soup.find_all('img', src=True)]  # NEW!
    }
    return data
```

Now when you crawl, each page will include a list of image URLs!

---

## Testing Your Changes

After making any changes, always test:

```bash
python test_web_crawler.py
```

If all tests pass, your changes are working correctly! ✅

---

## Quick Reference Card

### Basic Commands

| Command | Purpose |
|---------|---------|
| `pip install -r requirements.txt` | Install dependencies |
| `python example_crawler_usage.py` | Run example |
| `python test_web_crawler.py` | Run tests |

### WebCrawler Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `base_url` | string | Required | Starting URL |
| `max_pages` | integer | 10 | Max pages to visit |
| `delay` | integer | 1 | Seconds between requests |

### Scraped Data Fields

| Field | Type | Contains |
|-------|------|----------|
| `url` | string | Page URL |
| `title` | string | Page title |
| `headings` | list | All h1, h2, h3 tags |
| `paragraphs` | list | Text paragraphs |
| `links_count` | integer | Number of links |

---

## Need More Help?

### Common Questions

**Q: How do I scrape a specific part of a website?**
A: You'll need to customize the `extract_data()` method. Learn about BeautifulSoup selectors.

**Q: Can I scrape websites that require login?**
A: This basic crawler doesn't support authentication. You'll need more advanced tools.

**Q: How do I make it faster?**
A: Reduce the `delay`, but be careful not to overload servers. Never go below 1 second.

**Q: Can I scrape images and videos?**
A: The URLs yes, the files no. You'd need to add download functionality.

**Q: Is web scraping legal?**
A: It depends on the website and your location. Always check terms of service and local laws.

---

## Next Steps

Once you're comfortable with this crawler, you can:

1. **Learn BeautifulSoup** - Extract specific HTML elements
2. **Try Scrapy** - A more powerful scraping framework
3. **Learn about APIs** - Many websites offer official data access
4. **Practice Data Analysis** - Use pandas to analyze scraped data
5. **Build a Project** - Create something useful with your new skills!

---

## Files in This Project

- `web_crawler.py` - The main crawler class (YOU CAN CUSTOMIZE THIS!)
- `test_web_crawler.py` - Tests to verify everything works
- `example_crawler_usage.py` - Working example to learn from
- `requirements.txt` - List of required Python libraries
- `CRAWLER_README.md` - This guide you're reading now!

---

## Summary

**To get started:**
1. Install dependencies: `pip install -r requirements.txt`
2. Run the example: `python example_crawler_usage.py`
3. Check the output file
4. Modify the example for your needs
5. Always be ethical and respectful!

**Remember:**
- Start with small `max_pages` values (3-5)
- Use delays of at least 1-2 seconds
- Respect robots.txt and terms of service
- Test on practice websites first

Happy crawling! 🕷️

---

## License

This is an educational project. Use responsibly and ethically.

## Contributing

Feel free to fork and improve this crawler for educational purposes!
