from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import discord
from discord.ext import commands
import os

import random

bot = commands.Bot(command_prefix='~',  intents = discord.Intents.all())

@bot.command(aliases = ['gr'])
async def get_board_result(ctx, roll_number:str ='14638024', school_code:str = '25070'):
    if roll_number == '14638041':
        await ctx.send('No')
        return
    print('running')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1000, 800) 

    driver.get("https://cbseresults.nic.in/class12/Class12th21.htm")
    print('completed')

    roll_no = driver.find_element_by_name('regno')
    school_code_element = driver.find_element_by_name('sch')

    roll_no.send_keys(roll_number)
    school_code_element.send_keys(school_code)
    clear_button = driver.find_element_by_name("B2").click()

    result = driver.find_elements_by_tag_name('table')[1]
    result.screenshot('trial.png')
    driver.save_screenshot(f"cbse-results/{roll_number}.png")

    await ctx.send(file=discord.File(f'cbse-results/{roll_number}.png', f"{roll_number}.png"))

    # img_object = io.BytesIO()
    # screenshot_as_bytes = driver.screenshot_as_png
    # img_object.write(screenshot_as_bytes)
    # img_object.seek(0)
    # await ctx.send(f'Requested by {str(ctx.author)}',file=discord.File(img_object, f'board-results-{roll_number}.{img.format}'))

bot.run(os.environ['bot-token'])