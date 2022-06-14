from pystark import Stark


@Stark.cmd('Welcome', "Welcome the user")
async def text_plugin(bot, msg):
    text = 'Welcome to the Bot'
    await msg.react(text)
