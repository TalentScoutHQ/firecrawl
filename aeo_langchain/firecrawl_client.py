import requests
import time

FIRECRAWL_BASE = "http://localhost:3002"
DEFAULT_LIMIT = 3
POLL_INTERVAL = 2


def start_crawl(url: str) -> dict:
    r = requests.post(
        f"{FIRECRAWL_BASE}/v2/crawl",
        json={
            "url": url,
            "limit": DEFAULT_LIMIT,
            "scrapeOptions": {"formats": ["markdown"]}
        },
        timeout=30
    )
    r.raise_for_status()
    return r.json()


def poll_crawl(status_url: str) -> dict:
    data = []

    while True:
        r = requests.get(status_url, timeout=30)
        r.raise_for_status()
        res = r.json()

        if isinstance(res.get("data"), list):
            data.extend(res["data"])

        if res.get("status") == "completed":
            return data

        if res.get("next"):
            status_url = res["next"]
        else:
            time.sleep(POLL_INTERVAL)
