import time
import undetected_chromedriver as UC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# scrolls to last song element presented in the html
def scroll_to(driver):
    tracks = driver.find_elements(By.CLASS_NAME, "gvLrgQXBFVW6m9MscfFA")  # scans the new html elements
    scroll = len(tracks)
    ActionChains(driver) \
        .scroll_to_element(tracks[scroll - 2])\
        .perform()  # scroll-2 because the title field has 2 elements with the same class name
    time.sleep(0.4)
    tracks = driver.find_elements(By.CLASS_NAME, "gvLrgQXBFVW6m9MscfFA")
    return tracks


def extract(link, driver):
    driver.get(link)
    track_list = {}  # Remove duplicates and keep the order
    time.sleep(2.5)  # wait page to loads

    while True:
        tracks = scroll_to(driver)

        done = len(list(track_list.keys()))  # gets the number of songs extracted
        for track in tracks:
            track = " ".join(track.text.split("\n"))
            track_list[track] = None

        if done == len(list(track_list.keys())):  # checks if it`s ready
            break

    driver.close()
    return list(track_list.keys())


def spotify_extract(link):
    driver = UC.Chrome(use_subprocess=True)
    return extract(link, driver)

