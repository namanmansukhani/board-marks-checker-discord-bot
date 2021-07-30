from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import discord
from discord.ext import commands
import os
import time

import random
import io
bot = commands.Bot(command_prefix='~',  intents = discord.Intents.all())

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1000, 800) 

driver.get("https://cbseresults.nic.in/class12/Class12th21.htm")

@bot.command(aliases = ['gr'])
async def get_board_result(ctx, roll_number:str ='14638024', school_code:str = '25070'):
    if roll_number == '14638041':
        await ctx.send('No')
        return

    roll_no = driver.find_element_by_name('regno')
    school_code_element = driver.find_element_by_name('sch')

    roll_no.send_keys(roll_number)
    school_code_element.send_keys(school_code)
    driver.find_element_by_name("B2").click()

    img_object = io.BytesIO()
    img_object.write(driver.get_screenshot_as_png())
    img_object.seek(0)

    await ctx.send(file=discord.File(img_object, f'{roll_number}.png'))
    driver.execute_script("window.history.go(-1)")


bot.run(os.environ['bot-token'])