import pytest
import unittest
from selenium import webdriver

@pytest.fixture
def setup():
 driver = webdriver.Chrome("C:/Users/Admin/Downloads/Folders/chromedriver_win32 (3)/chromedriver.exe")
 return driver

