# STU-esports-discord-bot
Open source discord bot implementation for STU esports group.  
If you wanna help us to develop this community project PM (propher mopher#2647 on discord)  

# Commands

## Ais

### !ais

Kontrola či sa daný človek nachádza v aise, je študent STU.  
Prideluje rolu STU, potvrdenie že sa daný človek nachádza na STU.  

```bash
!ais [priezvisko krsne_meno], nie je potrebné dodržiavať diakritiku.  
```

Priklad : !ais Mrvička Jožko  

## Discordbot

### !commands

work in progress

### !bot

work in progress

## League of legends

### !lol

Prideluje rolu League of Legends a rolu ela podľa SoloQ umiestnenia daného hráča. Default server pre tento command je EUNE.  
Na použitie tohoto commandu je nutné mať rolu STU.

```bash
!lol [nickname] alebo !lol[nickname#server]  
```

Príklad : !lol Perkz alebo !lol Luka the Bazooka#EUW  

### !lolrole

Prideluje rolu pozície v hre (TOP, JUNGLE, MID, ADC, SUPP).  
Na použitie tohoto commandu je potrebné mať rolu League of Legends.  

```bash
!lolrole [rola] 
```

Príklad : !lolrole ADC

## Dota 2

### !dota

Prideľuje rolu Dota2 a zároveň aj dosiahnutý rank. Rank sa berie zo stránky Dotabuff.  
Na použitie tohoto commandu je nutné mať rolu STU.

```bash
!dota [steam:id]
```

Príklad : !dota 11131141232

## CS:GO

### !csgo

Prideľuje rolu csgo a level zo stránky Faceit.
Na použitie tohoto commandu je nutné mať rolu STU.  

```bash
!csgo [faceit_name]
```

Príklad : !csgo DIVIX  


# Setup

## Requirements
1. [python 3](https://www.python.org/)
2. [pip](https://pypi.org/project/pip/)

## Setup-steps
1. Clone this repo
```bash
git clone git@github.com:ramang22/STU-esports-discord-bot.git
```
2. Go into src
```bash
cd src
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run 
```bash
python main.py
```

# Links
[Discord Dev portal](https://discordapp.com/developers/applications/)  
[Discord.py docs](https://discordpy.readthedocs.io/en/latest/)
# STU DISCORD

[STU Discord](https://discord.gg/dvwGwMd)
