"""
Say something interesting...
Syntax: .belo
    by @Deonnn
Quotes credits: Being logical Channel
"""

from telethon import events
import asyncio
import random


@borg.on(events.NewMessage(pattern=r"\.belo", outgoing=True))

async def _(event):
	quote_lst = [
		"`\"Underwater bubbles and raindrops are total opposites of each other.\"`",
		"`\"If you buy an eraser you are literally paying for your mistakes.\"`",
		"`\"The Person you care for most has the potential to destroy you the most.\"`",
		"`\"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger.\"`",
		"`\"Any video with “wait for it” in the title is simply too long.\"`",
		"`\"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you.\"`",
		"`\"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience.\"`",
		"`\"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof.\"`",
		"`\"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back.\"`",
		"`\"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils.\"`",
		"`\"A folder is for things that you don't want to fold.\"`",
		"`\"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching.\"`",
		"`\"If everything goes smoothly, you probably won't remember today.\"`",
		"`\"When you meet new people in real life, you unlock more characters for your dream world.\"`",
		"`\"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it.\"`",
		"`\"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass.\"`",
		"`\"Parents worry about what their sons download and worry about what their daughters upload.\"`",
		"`\"It's crazy how you can be the same age as someone, but at a completely different stage in your life.\"`",
		"`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`",
		"`\"Technically, no one has ever been in an empty room.\"`",
		"`\"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there.\"`",
		"`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`",
		"`\"Every single decision you ever made has brought you to read this sentence.\"`",
		"`\"The word 'quiet' is often said very loud.\"`",
		"`\"Everybody wants you to work hard, but nobody wants to hear about how hard you work.\"`",
		"`\"We brush our teeth with hair on a stick and brush our hair with teeth on a stick.\"`",
		"`\"No one remembers your awkward moments but they’re too busy remembering their own.\"`",
		"`\"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible.\"`",
		"`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`",
		"`\"The biggest irony is that computers & mobiles were invented to save out time!\"`",
		"`\"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects.\"`",
		"`\"You know you’re getting old when your parents start disappointing you, instead of you disappointing them.\"`",
		"`\"Humans are designed to learn through experience yet the education system has made it so we get no experience.\"`",
		"`\"By focusing on blinking, you blink slower... Same for breathing.\"`",
		"`\"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid.\"`",
		"`\"Characters that get married in fiction were literally made for each other.\"`",
		"`\"Babies are a clean hard drive that can be programmed with any language.\"`",
		"`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`",
		"`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`",
		"`\"Maybe we don't find time travelers because we all die in 25-50 years.\"`",
		"`\"Sleep is the trial version of death, It even comes with ads based on your activity.\"`",
		"`\"The most unrealistic thing about Spy movies is how clean the air ventilation system is!\"`",
		"`\"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes.\"`",
		"`\"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves.\"`",
		"`\"If Greenland actually turns green, we're all screwed.\"`",
		"`\"If someone says clever things in your dream, it actually shows your own cleverness.\"`",
		"`\"Famous movie quotes are credited to the actor and not the actual writer who wrote them.\"`",
		"`\"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out.\"`",
		"`\"Ask yourself why the the brain ignores the second the.\"`",
		"`\"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened.\"`",
		"`\"It will be a lot harder for kids to win against their parents in video games in the future.\"`",
		"`\"Everyone has flaws, if you don't recognize yours, you have a new one.\"`",
		"`\"Raising a child is training your replacement.\"`",
		"`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`",
		"`\"There's always someone who hated you for no reason, and still does.\"`",
		"`\"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect.\"`",
		"`\"The more important a good night's sleep is, the harder it is to fall asleep.\"`",
		"`\"Blessed are those that can properly describe the type of haircut they want to a new stylist.\"`",
		"`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`",
		"`\"Theme park employees must be good at telling the difference between screams of horror and excitement.\"`",
		"`\"6 to 6:30 feels more half-an-hour than 5:50 to 6:20\"`",
		"`\"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience.\"`",
		"`\"Listening to podcasts before bed is the adult version of story-time.\"`",
		"`\"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing.\"`",
		"`\"A ton of whales is really only like half a whale.\"`",
		"`\"When you get old, the old you is technically the new you, and your young self is the old you.\"`",
		"`\"You probably won't find many negative reviews of parachutes on the Internet.\"`",
		"`\"We show the most love and admiration for people when they're no longer around to appreciate it.\"`",
		"`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`",
		"`\"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for.\"`",
		"`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`",
		"`\"The most effective alarm clock is a full bladder.\"`",
		"`\"You probably just synchronized blinks with millions of people.\"`",
		"`\"Since we test drugs on animals first, rat medicine must be years ahead of human medicine.\"`",
		"`\"Night before a day off is more satisfying than the actual day off.\"`",
		"`\"We put paper in a folder to keep it from folding.\"`",
		"`\"Somewhere, two best friends are meeting for the first time.\"`",
		"`\"Our brain simultaneously hates us, loves us, doesn't care about us, and micromanages our every move.\"`",
		"`\"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice.\"`",
		"`\"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents.\"`",
		"`\"Wikipedia is what the internet was meant to be.\"`",
		"`\"A theme park is the only place that you can hear screams in the distance and not be concerned.\"`",
		"`\"A wireless phone charger offers less freedom of movement than a wired one.\"`",
		"`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`",
		"`\"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world.\"`",
		"`\"If someday human teleportation becomes real, people will still be late for work.\"`",
		"`\"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider\"`",
		"`\"Doing something alone is kind of sad, but doing it solo is cool af.\"`",
		"`\"Your brain suddenly becomes perfect at proofreading after you post something.\"`",
		"`\"There's always that one song in your playlist that you always skip but never remove.\"`",
		"`\"Kids next century will probably hate us for taking all the good usernames.\"`",
		"`\"Bubbles are to fish what rain is to humans.\"`",
		"`\"The more people you meet, the more you realise and appreciate how well your parents raised you.\"`",
		"`\"A comma is a short pause, a coma is a long pause.\"`",
		"`\"Someday you will either not wake up or not go to sleep.\"`",
		"`\"Bermuda Triangle might be the exit portal of this simulation.\"`",
		"`\"If we put solar panels above parking lots, then our cars wouldn't get hot and we would have a lot of clean energy.\"`"
	]
    if event.fwd_from:
        return
    await event.edit("Typing...")
    await asyncio.sleep(2)
    x = random.randint(1, len(quote_lst))
    await event.edit(quote_lst[x])
