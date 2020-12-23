import unittest
from selenium import webdriver
from selenium.webdriver.firefox import options as FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from api.TodoListManager import *
from .TodoListElement import *


class RandomTodoListGenerator(unittest.TestCase):

    def setUp(self):
        firefox_options = FirefoxOptions.Options()
        firefox_options.add_argument("--headless")
        self.browser = webdriver.Firefox(executable_path='/Users/danieldiaz/Documents/geckodriver',
                                         firefox_options=firefox_options)
        self.addCleanup(self.browser.quit)

    def testContainer(self):
        learning_category = '//*[@id="section-to-print"]/div[1]/span/div[7]/span'

        self.browser.get('https://randomtodolistgenerator.herokuapp.com/library')
        self.browser.find_element_by_xpath(learning_category).click()  # changing to a different category

        # gets the main container
        element_card_container: WebElement = self.browser.find_element_by_class_name('tasks-card-container')

        # this is all cards (each element)
        element_cards: List[WebElement] = element_card_container.find_elements_by_class_name('taskCard.card')

        for index, element in zip(range(5), element_cards):
            # getting title
            title: WebElement = element.find_element_by_class_name('task-title').find_element_by_tag_name('div')

            # getting description
            description: WebElement = element.find_element_by_class_name('card-text')

            # getting all categories
            categories: List[WebElement] = element.find_elements_by_class_name('badge.badge-info.badge-pill')

            # getting time and unit
            time_and_unit: WebElement = element.find_element_by_class_name('badge.badge-danger')

            # this creates an instance of TodoListElement with the parameters received from WebElement
            todo_list_element = TodoListElement(
                name=title.text, description=description.text,
                categories=[category.text for category in categories],
                time_and_unit=time_and_unit.text
            )

            try:
                todo_list_manager: TodoListManager = TodoListManager()  # initializes TodoListManager
                todo_list_manager.add_task(todo_list_element)  # trying to add task through API
            except Exception as e:
                print('exception adding a task through todo list manager', e)
