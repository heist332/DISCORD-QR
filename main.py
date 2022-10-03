from email.mime import image
import qrcode
import pyzbar.pyzbar as pyzbar
import cv2
import os
import discord

token = 'TOKEN

client = discord.Client()

cwd = os.getcwd()

print(cwd)
os.chdir(cwd)


@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    if msg.content.startswith('Q!GEN '):
        splits = msg.content.split('Q!GEN ')

        URL = splits[1]

        img = qrcode.make(URL)

        img.save(str(msg.author.id) + '.png')

        await msg.channel.send(content='Here Is!', file=discord.File(str(msg.author.id) + '.png'))

        os.remove(str(msg.author.id) + '.png')

    if msg.content.startswith('Q!DETECT'):
        await msg.attachments[0].save(str(msg.author.id) + '.png')
        # splits = msg.content.split('Q!DETECT')

        img = cv2.imread(str(msg.author.id) + '.png')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for i in pyzbar.decode(gray):
            await msg.channel.send(content=f'I DETECTED THIS!\n{i.data.decode("utf-8")}')

        os.remove(str(msg.author.id) + '.png')


client.run(token)
