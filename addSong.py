import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def add_song(song, driver):
    search = driver.find_element(By.TAG_NAME, 'ytmusic-search-box')
    ActionChains(driver) \
        .click(search) \
        .send_keys(song) \
        .send_keys(Keys.ENTER) \
        .perform()

    time.sleep(2)
    drop_down = driver.find_element(By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/a')
    ActionChains(driver) \
        .context_click(drop_down) \
        .perform()

    time.sleep(0.4)
    add_playlist = driver.find_elements(By.XPATH, '//*[@id="navigation-endpoint"]')
    ActionChains(driver) \
        .click(add_playlist[1]) \
        .perform()

    time.sleep(0.4)
    add_playlist = driver.find_element(By.XPATH,
                                       '//*[@id="playlists"]/ytmusic-playlist-add-to-option-renderer[1]/button')
    ActionChains(driver) \
        .click(add_playlist) \
        .perform()
    time.sleep(0.4)

    clear_field = driver.find_element(By.XPATH, '//*[@id="icon"]')
    ActionChains(driver) \
        .click(clear_field) \
        .perform()


def add_song_slower(song, driver):
    clear_field = driver.find_element(By.XPATH, '//*[@id="icon"]')
    ActionChains(driver) \
        .click(clear_field) \
        .perform()
    time.sleep(1)

    search = driver.find_element(By.TAG_NAME, 'ytmusic-search-box')
    ActionChains(driver) \
        .click(search) \
        .send_keys(song) \
        .send_keys(Keys.ENTER) \
        .perform()

    time.sleep(6)

    drop_down = driver.find_element(By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/a')
    ActionChains(driver) \
        .context_click(drop_down) \
        .perform()

    time.sleep(4)
    add_playlist = driver.find_elements(By.XPATH, '//*[@id="navigation-endpoint"]')
    ActionChains(driver) \
        .click(add_playlist[1]) \
        .perform()

    time.sleep(4)
    add_playlist = driver.find_element(By.XPATH,
                                       '//*[@id="playlists"]/ytmusic-playlist-add-to-option-renderer[1]/button')
    ActionChains(driver) \
        .click(add_playlist) \
        .perform()
    time.sleep(4)

    clear_field = driver.find_element(By.XPATH, '//*[@id="icon"]')
    ActionChains(driver) \
        .click(clear_field) \
        .perform()
