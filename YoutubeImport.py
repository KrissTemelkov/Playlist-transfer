import time

import undetected_chromedriver as UC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from addSong import add_song, add_song_slower

link = "https://music.youtube.com/library/playlists"


def login(gmail, password, driver):
    accept_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
    ActionChains(driver) \
        .click(accept_button) \
        .perform()

    time.sleep(0.4)
    accept_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
    ActionChains(driver) \
        .send_keys(gmail) \
        .click(accept_button) \
        .perform()

    time.sleep(2)
    accept_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
    ActionChains(driver) \
        .send_keys(password) \
        .click(accept_button) \
        .perform()
    time.sleep(2)


def create_playlist(playlist_name, driver):
    create_playlist_btn = driver.find_element(By.CLASS_NAME, "ytmusic-two-row-item-renderer")
    ActionChains(driver) \
        .click(create_playlist_btn) \
        .perform()

    ActionChains(driver) \
        .send_keys(playlist_name) \
        .click(driver.find_element(By.CLASS_NAME, "style-primary")) \
        .perform()
    time.sleep(1.5)


def create(gmail, password, playlist_name, songs, driver):
    driver.get(link)

    login(gmail, password, driver)
    create_playlist(playlist_name, driver)
    for song in songs:
        try:
            add_song(song, driver)
        except Exception:
            try:
                add_song_slower(song, driver)
            except Exception:
                pass


def youtube_import(gmail, password, playlist_name, songs):
    driver = UC.Chrome(use_subprocess=True)
    create(gmail, password, playlist_name, songs, driver)

