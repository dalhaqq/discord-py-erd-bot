# discord-py-erd-bot
Python-based Discord bot that generates Entity Relationship Diagram
## Installation

 - Clone this repository

```bash
git clone https://github.com/dalhaqq/discord-py-erd-bot.git
cd discord-py-erd-bot
```

 - It is better to use a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate.bat # using cmd
venv\Scripts\activate.ps1 # using PowerShell

# Unix
python3 -m venv venv
source venv/bin/activate
```

 - Install the dependencies

```bash
# Windows
pip install -r requirements.txt

# Unix
pip3 install -r requirements.txt
```

 - Create a bot from your Discord Developer Portal and copy the token
 - Rename sample.env to .env
 - Put your bot token inside .env file
 - Launch your bot

```bash
# Windows
python main.py

# Unix
python3 main.py
```
## Usage
To generate the diagram, give command with format below

> ~erd
> ```
> def Entity1(Attribute1,Attribute2)
> def Entity2(Attribute1,Attribute2)
> rel Relation1(Entity1,Entity2,1-1)
> ```
Use triple backtick to make the block.
`def` is used to define an entity.
It may have attributes as many as you want.
`rel` is used to make relation
The first and second argument of relation must be an entity.
The third argument is the cardinality:
 - 1-1 means one-on-one relationship
 - 1-n means one-to-many relationship
 - m-n means many-to-many relationship
 
 You can add forth, fifth, and so on to the relationship so it will have attributes

