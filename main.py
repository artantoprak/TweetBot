import random
import logging
import time

# Selenium and related modules
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

# Gemini API and Twitter API libraries
import google.generativeai as genai
import tweepy

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ==========================================
# API Keys and Configuration
# ==========================================
GEMINI_API_KEY = "Gemini_API_Key"
genai.configure(api_key=GEMINI_API_KEY)

BEARER_TOKEN = "bearer_token"
CONSUMER_KEY = "consumer_key"
CONSUMER_SECRET = "consumer_secret"
ACCESS_TOKEN = "access_token"
ACCESS_TOKEN_SECRET = "access_token_secret"

TEST_MODE = True  # When TEST_MODE is True, tweets are not posted, only logged.
print("TEST_MODE:", TEST_MODE)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# ==========================================
# Helper Function: Create Selenium Driver
# ==========================================
def create_driver():
    firefox_options = FirefoxOptions()
    firefox_options.headless = True  # Run in headless mode
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_page_load_timeout(150)  # Set page load timeout
    return driver

# ==========================================
# Fetch Twitter Trends (from trends24.in)
# ==========================================
def fetch_twitter_trend_with_selenium():
    driver = create_driver()
    url = "https://trends24.in/turkey/"
    driver.get(url)
    time.sleep(3)  # Wait for the page to fully load
    trending_topics = []
    try:
        # First attempt: updated selector; trends are usually in an ordered list.
        elements = driver.find_elements(By.CSS_SELECTOR, "div.trend-card ol li a")
        for element in elements:
            text = element.text.strip()
            if text:
                trending_topics.append(text)
        if not trending_topics:
            logger.warning("Updated selector did not work for Twitter trends; trying alternative.")
            elements = driver.find_elements(By.CSS_SELECTOR, "div.trend-card a")
            for element in elements:
                text = element.text.strip()
                if text:
                    trending_topics.append(text)
    except Exception as e:
        logger.error("Error fetching Twitter trends: %s", e)
    finally:
        driver.quit()
    if trending_topics:
        selected = random.choice(trending_topics)
        logger.info("Selected Twitter trend: %s", selected)
        return selected
    else:
        logger.warning("No Twitter trend found.")
        return None

# ==========================================
# Fetch Topic from News Site 1
# ==========================================
def fetch_news_site_topic_1():
    driver = create_driver()
    url = "https://www.halktv.com.tr/"  # Generic news site URL; replace if needed.
    driver.get(url)
    time.sleep(3)
    topics = []
    try:
        # Attempt to fetch main news headlines from the news site.
        elements = driver.find_elements(By.CSS_SELECTOR, "h2")
        for element in elements:
            text = element.text.strip()
            if text and len(text) > 10:
                topics.append(text)
        # Note: Use developer tools to inspect the site and adjust selectors if necessary.
    except Exception as e:
        logger.error("Error fetching topics from news site 1: %s", e)
    finally:
        driver.quit()
    if topics:
        selected = random.choice(topics)
        logger.info("Selected topic from news site 1: %s", selected)
        return selected
    else:
        logger.warning("No topic found from news site 1.")
        return None

# ==========================================
# Fetch Topic from News Site 2
# ==========================================
def fetch_news_site_topic_2():
    driver = create_driver()
    url = "https://www.ahaber.com.tr/gundem"  # Generic news site URL; replace if needed.
    driver.get(url)
    time.sleep(3)
    topics = []
    try:
        # Attempt to fetch news headlines using h2 tags.
        elements = driver.find_elements(By.CSS_SELECTOR, "h2")
        for element in elements:
            text = element.text.strip()
            if text and len(text) > 10:
                topics.append(text)
        if not topics:
            logger.warning("h2 selector did not work for news site 2, trying alternative selector.")
            elements = driver.find_elements(By.CSS_SELECTOR, "a")
            for element in elements:
                text = element.text.strip()
                if text and len(text) > 10:
                    topics.append(text)
    except Exception as e:
        logger.error("Error fetching topics from news site 2: %s", e)
    finally:
        driver.quit()
    if topics:
        selected = random.choice(topics)
        logger.info("Selected topic from news site 2: %s", selected)
        return selected
    else:
        logger.warning("No topic found from news site 2.")
        return None

# ==========================================
# Fetch Topics from All Sources
# ==========================================
def fetch_all_topics():
    topics = []
    twitter_topic = fetch_twitter_trend_with_selenium()
    if twitter_topic:
        topics.append(twitter_topic)
    news_topic_1 = fetch_news_site_topic_1()
    if news_topic_1:
        topics.append(news_topic_1)
    news_topic_2 = fetch_news_site_topic_2()
    if news_topic_2:
        topics.append(news_topic_2)
    if topics:
        selected = random.choice(topics)
        logger.info("Overall selected topic: %s", selected)
        return selected
    else:
        logger.warning("No topic fetched from any source.")
        return None

# ==========================================
# Generate Tweet Content using Gemini API
# ==========================================
def generate_tweet_content(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate a compelling, concise, and fluent tweet about {topic}."
    try:
        response = model.generate_content(prompt)
        if response and response.text:
            tweet = response.text.strip()
            logger.info("Generated tweet: %s", tweet)
            return tweet
    except Exception as e:
        logger.error("Error generating tweet: %s", e)
    return f"Unable to generate a compelling tweet about {topic}."

# ==========================================
# Post Tweet via Twitter API
# ==========================================
def post_tweet(text):
    if TEST_MODE:
        logger.info("TEST_MODE: Tweet to be posted: %s", text)
        return
    try:
        response = client.create_tweet(text=text)
        logger.info("Tweet posted: %s", response)
    except Exception as e:
        logger.error("Error posting tweet: %s", e)

# ==========================================
# Main Workflow
# ==========================================
def main():
    topic = fetch_all_topics()
    if topic:
        tweet_content = generate_tweet_content(topic)
        tweet_text = f'"{tweet_content}"'
        post_tweet(tweet_text)
    else:
        logger.warning("No topic found. Tweet not posted.")

if __name__ == "__main__":
    main()
