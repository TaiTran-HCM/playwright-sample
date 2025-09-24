import re
from time import sleep

from playwright.sync_api import expect, Page


def test_has_title(page: Page):
    page.goto("https://sandbox.applitools.com/bank")

def test_get_started_link(page: Page):
    page.goto("https://sandbox.applitools.com/bank")