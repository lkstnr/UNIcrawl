# Scrapy settings for unicrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "unicrawl"

SPIDER_MODULES = ["unicrawl.spiders"]
NEWSPIDER_MODULE = "unicrawl.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "unicrawl (+https://www.uni-potsdam.de/de/multimedia/team/wissenschaftlichehilfskraefte/lewin-kaestner)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure logging
# LOG_FILE = "log.txt"
LOG_LEVEL = "WARNING"

# CRITICAL - for critical errors (highest severity)
# ERROR - for regular errors
# WARNING - for warning messages
# INFO - for informational messages
# DEBUG - for debugging messages (lowest severity)

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "unicrawl.pipelines.UnicrawlPipeline": 300,
}

# MySQL settings
MYSQL_HOST = "db"
MYSQL_PORT = 3306
MYSQL_USER = "unicrawl"
MYSQL_PASSWORD = "scrapy2mysql"
MYSQL_DATABASE = "unicrawl"
MYSQL_TABLE = "unicrawl_items"
MYSQL_CHARSET = "utf8mb4"
MYSQL_COLLATION = "utf8mb4_0900_ai_ci"
MYSQL_RAISE_ON_WARNINGS = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'unicrawl.middlewares.UnicrawlSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'unicrawl.middlewares.UnicrawlDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
CLOSESPIDER_ITEMCOUNT = 100
# Timeout after 86400 seconds, 24 hours
# CLOSESPIDER_TIMEOUT = 86400

EXTENSIONS = {
    "scrapy.extensions.closespider.CloseSpider": 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Timeout for processing of DNS queries in seconds
DNS_TIMEOUT = 30
