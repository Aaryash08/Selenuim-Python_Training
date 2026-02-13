from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_HUB_URL = "http://192.168.29.162:4444"

browser_configs = [
    ChromeOptions(),
    FirefoxOptions(),
    EdgeOptions()
]

def run_grid_test(options):
    driver = webdriver.Remote(
        command_executor=GRID_HUB_URL,
        options=options
    )

    try:
        target_url = "https://www.google.com"
        driver.get(target_url)
        caps = driver.capabilities
        print("-" * 30)
        print(f"Browser:  {caps['browserName']}")
        print(f"Platform: {caps['platformName']}")
        print(f"Title:    {driver.title}")
        if "Google" in driver.title:
            print("Status:   SUCCESS (Title verified)")
        else:
            print("Status:   FAILED (Title mismatch)")

    finally:
        driver.quit()

if __name__ == "__main__":
    for config in browser_configs:
        try:
            run_grid_test(config)
        except Exception as e:
            print(f"Could not run test for {config.capabilities['browserName']}: {e}")