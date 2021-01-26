import discord, re, base64, io, aiohttp
from settings import BOT_TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(message.content)
        if(message.content[:4] == "~erd"):
            lines = message.content.split("\n")
            formatter = "graph LR;"
            for line in lines:
                try:
                    if(re.match("def ", line)):
                        pattern = 'def[\s]+([\w]+)[\s]*\(([\w\d,]*)\)'
                        name = re.match(pattern, line)[1]
                        print(name)
                        formatter += "\n"
                        formatter += '{0}[{0}];'.format(name)
                        attrs = re.match(pattern, line)[2].split(",")
                        attrs = list([attr.strip() for attr in attrs])
                        print(attrs)
                        for attr in attrs:
                            if(attr != ""):
                                formatter += "\n"
                                formatter += '{0}{1}([{1}])---{0};'.format(name,attr)
                    elif(re.match("rel ", line)):
                        pattern = 'rel[\s]+([\w]+)[\s]*\(([\w\d,-]*)\)'
                        name = re.match(pattern, line)[1]
                        print(name)
                        formatter += "\n"
                        formatter += '{0}[{0}];'.format(name)
                        attrs = re.match(pattern, line)[2].split(",")
                        attrs = list([attr.strip() for attr in attrs])
                        print(attrs)
                        rel1 = attrs.pop(0)
                        rel2 = attrs.pop(0)
                        card = attrs.pop(0).split("-")
                        formatter += "\n"
                        formatter += '{0}---|{1}|{2}{{{2}}}---|{3}|{4};'.format(rel1,card[0],name,card[1],rel2)
                        for attr in attrs:
                            if(attr != ""):
                                formatter += "\n"
                                formatter += '{0}{1}([{1}])---{0};'.format(name,attr)
                except:
                    return await message.channel.send('Sintaks tidak sesuai')
            graphbytes = formatter.encode("ascii")
            base64_bytes = base64.b64encode(graphbytes)
            base64_string = base64_bytes.decode("ascii")
            url = 'https://mermaid.ink/img/'+base64_string
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Sintaks tidak sesuai')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(file=discord.File(data, 'diagram.png'))
client = MyClient()
client.run(BOT_TOKEN)