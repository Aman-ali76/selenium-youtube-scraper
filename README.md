# 📺 YouTube Video Scraper (Selenium-Based)

This Python script automates a YouTube search using Selenium, scrolls dynamically to load multiple video results, and saves each video’s HTML block into individual files. It's useful as a base for building full-featured scrapers or analyzing YouTube's video container structure.

---

## 🔍 What It Does

- Opens YouTube and performs a search (default: `"Selenium Python Tutorial"`)
- Scrolls the page until at least **50 videos** are loaded
- Captures the **outer HTML** of each video container element
- Saves each result in a separate file (e.g., `videos-0.html`, `videos-1.html`, ...)

---

## ✨ Key Features

- Handles infinite scroll using Selenium and `Keys.END`
- Dynamically waits for content to load
- Gracefully handles user interruptions (Ctrl+C)
- Simple structure for future enhancements (like title, views, channel scraping)

---

## 💻 Technologies Used

- Python 3.x  
- Selenium WebDriver  
- ChromeDriver  
- `time`, `Keys`, `By`, and basic file I/O

---

## ⚙️ How to Run

1. **Install dependencies**  

```bash
   pip install selenium
````

1. **Ensure ChromeDriver is installed and added to your system PATH**

   * Download: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

2. **Run the script**

   ```bash
   python main.py
   ```

---

## 📂 Output

* Files: `videos-0.html`, `videos-1.html`, ...
* Each file contains the full HTML block of one video listing

---

## 📌 Use Case

This script can be used to:

* Analyze YouTube's HTML structure for scraping
* Collect raw video containers for machine learning or data labeling
* Serve as a base for full YouTube data scrapers (title, views, links, etc.)

---

## 🧠 Learning Outcomes

* Automating search inputs with Selenium
* Handling infinite scroll dynamically
* Capturing and saving dynamic HTML elements
* Graceful termination and cleanup using `try/finally`

---

## 📁 Suggested Repo Structure

```
youtube-video-scroller/
├── main.py
├── README.md
└── videos-*.html        # Auto-generated
```

---
