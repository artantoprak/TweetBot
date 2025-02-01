# TweetBot - Automated Twitter Content Generator & Scheduler

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/your_username/tweetbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

TweetBot is a sophisticated Python application that automatically generates and posts tweets by combining live data scraping, AI-powered content generation, and social media automation. It scrapes trending topics and headlines from various online sources using Selenium, leverages the Gemini API to create engaging tweet text, and finally posts the tweet via Twitter’s API using Tweepy.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Usage](#usage)
- [Detailed Module Overview](#detailed-module-overview)
  - [Data Scraping with Selenium](#data-scraping-with-selenium)
  - [AI Tweet Generation](#ai-tweet-generation)
  - [Twitter API Integration](#twitter-api-integration)
- [Troubleshooting & Debugging](#troubleshooting--debugging)
- [Roadmap](#roadmap)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Overview

TweetBot was created to streamline the process of keeping a Twitter account active and engaging by automatically generating content based on real-time trends and news headlines. By integrating multiple web services and APIs, TweetBot aims to reduce the manual overhead of social media management while showcasing the power of modern automation, AI, and web scraping technologies.

### Motivation

- **Stay Relevant:** Automatically fetch trending topics from sources like Twitter trends, Halk TV, and A Haber.
- **Engage Your Audience:** Generate compelling tweet content using AI (Gemini API) that is both concise and impactful.
- **Automate Routine Tasks:** Use Tweepy to post tweets without manual intervention, with a built-in test mode to avoid accidental live postings.

---

## Features

- **Multi-source Data Collection:**  
  - Scrapes live trending topics and news headlines using Selenium.
  - Aggregates data from multiple websites for a diverse range of topics.

- **AI-Powered Content Generation:**  
  - Uses the Gemini API to craft creative, tailored tweet content based on the selected topic.

- **Twitter Automation:**  
  - Integrates with the Twitter API via Tweepy.
  - Supports a test mode (`TEST_MODE=True`) that logs tweets without posting them.

- **Configurable Web Automation:**  
  - Supports both Chrome (via ChromeDriver) and Firefox (via GeckoDriver) in headless mode.
  - Customizable page load timeouts and selectors for dynamic web content.

- **Robust Logging & Error Handling:**  
  - Comprehensive logging using Python’s built-in `logging` module.
  - Detailed error messages for troubleshooting network or scraping issues.

---

## Architecture

TweetBot is organized into three core components:

1. **Data Scraping Module:**  
   Utilizes Selenium to load webpages and extract trending topics and headlines via CSS selectors.

2. **Content Generation Module:**  
   Sends a prompt to the Gemini API to generate tweet text that is engaging, succinct, and tailored to the fetched topic.

3. **Twitter Posting Module:**  
   Uses Tweepy to authenticate with Twitter and post the generated tweet. A test mode is included to ensure safe testing.

The main workflow orchestrates these modules to fetch a topic, generate tweet content, and post it (or log it if in test mode).

---

## Prerequisites

- **Python:** Version 3.8 or higher.
- **WebDrivers:**  
  - **Chrome:** [ChromeDriver](https://chromedriver.chromium.org/downloads)  
  - **Firefox:** [GeckoDriver](https://github.com/mozilla/geckodriver/releases)  
  Ensure the driver is installed and added to your system PATH.

- **API Credentials:**  
  - Gemini API Key  
  - Twitter API credentials (Bearer Token, Consumer Key, Consumer Secret, Access Token, Access Token Secret)

- **Python Libraries:**  
  - [selenium](https://pypi.org/project/selenium/)
  - [google-generativeai](https://pypi.org/project/google-generativeai/)
  - [tweepy](https://pypi.org/project/tweepy/)

Install these using pip:
```bash
pip install selenium google-generativeai tweepy
```

> **Note:** Installation details (e.g. setting up WebDrivers) are also documented within the code itself.

---

## Configuration

Edit `main.py` to configure your API keys and settings:

```python
# Gemini API configuration
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)

# Twitter API credentials
BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"
CONSUMER_KEY = "YOUR_TWITTER_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_TWITTER_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"

# Test mode (True = log tweets without posting)
TEST_MODE = True
```

---

## Usage

Run the application with:
```bash
python main.py
```

---

## Troubleshooting & Debugging

- **Timeout Errors:**  
  Increase the page load timeout:
  ```python
  driver.set_page_load_timeout(150)
  ```

- **Driver Compatibility:**  
  Verify that the installed WebDriver matches your browser version.

- **CSS Selector Changes:**  
  If the target website’s layout changes, inspect the page using developer tools and update the selectors accordingly.

- **API Credential Issues:**  
  Double-check that your API keys and tokens are correctly set and that they have the necessary permissions.

---

## Roadmap

- **Feature Enhancements:**  
  - Add more data sources for trending topics.
  - Improve error handling and retries for network requests.
  - Integrate additional AI models for varied content styles.

- **Deployment:**  
  - Containerize the application using Docker.
  - Schedule automated execution using cron jobs or cloud-based functions.

---

## Contribution Guidelines

Contributions are welcome! Open a pull request with a detailed explanation of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any questions, suggestions, or issues, please open an issue on GitHub.

---

Happy tweeting and happy coding!
