import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://client:password123@test3.ars.n2.mavendev.com/")
    page.get_by_role("button", name="Close").click()
    page.get_by_role("listitem").filter(has_text="Увійти").locator("a").click()
    page.get_by_role("link", name="Реєстрація").click()
    unic_tel = str(random.randint(10000000000, 99999999999))
    unic_email = str(random.randint(00000000000, 99999999999))
    page.get_by_role("textbox", name="Електронна пошта*").click()
    page.get_by_role("textbox", name="Електронна пошта*").fill(f"{unic_email}@auto.test")
    page.get_by_role("textbox", name="Телефон").click()
    page.get_by_role("textbox", name="Телефон").fill(unic_tel)
    page.get_by_role("button", name="Зареєструватися").click()
    page.get_by_role("button", name="Хочу знижку").click()
    page.goto("https://client:password123@test3.ars.n2.mavendev.com/")
    page.get_by_role("button", name="Close").click()
    expect(page.get_by_role("link", name="Доброго дня")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)