import pytest
import socket
import logging

from _pytest import unittest
from selenium import webdriver
from dataclasses import dataclass
from pageObjects.LoginPage import LoginPage

from pytest import fixture

from pageTestCases.confitest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUserEmail()
    password = ReadConfig.getApplicationPassword()
    logger = logGen.loggen()


    def test_HomePage_Title(self, setup):
        self.logger.info("****************Test_001_Login********************")
        self.logger.info("****************Verify Home Page Title********************")
        self.driver = setup
        self.logger.info("****************Browser Opened********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("****************Application Launched********************")
        act_Title_one = self.driver.title
        self.logger.info('Page Title is:' + act_Title_one)
        self.logger.info("****************Present in Application Home Page********************")
        if act_Title_one == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************Home Page Title is Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePage_Title.png")
            self.driver.close()
            self.logger.error("****************Home Page Title is Failed********************")
            assert False

    def test_Login(self, setup):
        self.logger.info("****************Verify Login Test********************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("****************Enter into the Login Page********************")
        self.lp.setUserName(self.username)
        self.logger.info("****************Provide the UserName into the Login Page********************")
        self.lp.setPasswordName(self.password)
        self.logger.info("****************Provide the Password into the Login Page********************")
        self.lp.clickLogin()
        self.logger.info("****************Click the Login Button into the Login Page********************")
        act_title_two = self.driver.title
        self.logger.info('Page Title is:' + act_title_two)
        self.logger.info("****************Enter into the Login Home Page********************")
        if act_title_two == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****************Login Test is Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            assert False
            self.logger.error("****************Login Test is Failed********************")

        self.lp.clickLogout()
        self.driver.close()