# Nala

Nala is an agile open-source voice assistant to improve the workflow of your daily life. 

![](https://media.giphy.com/media/VDzVG8lvNRufu/giphy.gif)

Nala uses actions which can be triggered by user voice queries. All the user needs to do is say 'hey nala' and it will spark Nala to listen and respond to requests - like getting the weather or the news.

And yes, her name is inspired after Nala from the Lion King :-) 

## how to setup

It's super easy to setup Nala. All you need to do is:

    git clone 
    cd nala
    python3 setup.py
    python3 nala.py
    
You will then be asked to register with your name and email.

After that, you're ready to begin using Nala! 

## how to query Nala

![](https://github.com/jim-schwoebel/nala/blob/master/data/other/Webp.net-gifmaker.gif)

### Single queries 

To active Nala, all you need to do is query her with 'Hey Nala!' (1) - which then triggers a response from Nala - (3) in this case, “How can I help you?.” Then, a user provides another query (usually after some beeping sound) - such as (4) “I’d like the weather.” Nala transcribes this query to understand it, and parses the query for keyword intents; for example, if the response is “I’d like the weather” the only word that really matters is “weather” and that would be used to provoke a response (5). Then, after this keyword maps onto an action dictionary (or a map of responses to keywords), the action is executed (6). Then, the intent loop repeats itself, looking for another wakeword (“Hey Nala”) before triggering another action. 

### Multi-query capability 

Nala is equipped with multi-query capability. All you need to do is add 'AND' into your query and she'll automatically execute actions serially that you request to her. 

For example, you may say, "Hey Nala" --> "close spotify and sleep" 

She will then close spotify and then go to sleep for 30 minutes. 

This makes Nala incredibly versatile to do multiple things quickly and is an advantage over other chatbot systems. 

## what can Nala do

[Post video]

Here are some actions that Nala can currently do along with the query intents needed to activate them. If you have any other ideas, let us know on the [github issues tab](https://github.com/jim-schwoebel/nala/issues) (as an enhancement)! 

| Action  | Description | Example query intent | 
| ------------- | ------------- | ------------- |
| alarm.py | Plays an alarm sound (e.g. to wake up in morning) based on the time of day you specified during user registration. | “set alarm”, “stop alarm” | 
| chillout.py | Plays music in the background to help you calm down.| “chill out” | 
| espn.py | Scrapes ESPN website to find any events going on later tonight. This is a work-in-progress.| “get sports”|
| events.py | Scrape meetup.com for events in your local area. | “find events” | 
| generate_poem.py | Generate a poem based on the generate poetry script we wrote a while back.| “make a poem”| 
| grateful.py | Helps you keep a gratitude journal by recording a sample of what you’re grateful for today. | “be grateful” | 
| makeajoke.py | Plays back a joke from the database. | “make a joke” | 
| meditation.py | Guides you through a simple 60 second meditation.| “meditate” | 
| music.py | YouTube music links - based on a genre. | “play music” | 
| news.py | searches some basic news sites related to computer science and machine learning (e.g. Hacker News). | “grab the news” | 
| nutrition.py | Searches for some healthy food nearby | “be healthy” | 
| plan_trip.py | Schedules a trip in terms of AirBnB suggestions and flights | “plan trip” | 
| reboot.py | Restarts the computer. | “restart” |
| search.py | search bing with a query. | First query: “search”, Second query: [search term] | 
| shutdown.py | Shuts down the computer. | “shut down” |
| sleep |  Puts the computer to sleep for a designated time period. | ‘go to sleep’|
| social.py | Alternative script to give you some suggestions based on your budget to go out later. | ‘be social’|
| weather.py | Searches weather.com for the current weather at your location. | ‘get the weather’|
| yelp.py | Based on the query, searches yelp for coffee, restaurants, food, nightlife, ice cream, or bars. |‘get me coffee’, ‘get me some food’, ‘nightlife’, ‘get ice cream’, ‘grab beer’| 

... more to come into the future! 

## references 

If you're looking for a place to start to learn how to code voice computing, Nala has some great documentation in [Chapter 7 of the Voicebook repository](https://github.com/jim-schwoebel/voicebook/tree/master/chapter_7_design).

Here are some other modules and things you could look into for further guidance:

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Google speech API](https://cloud.google.com/speech-to-text/docs/)
* [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
* [Pocketsphinx](https://github.com/cmusphinx/pocketsphinx)
* [Porcupine](https://github.com/Picovoice/Porcupine)
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/)
* [Soundfile](https://github.com/bastibe/SoundFile)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) 
* [Voicebook](https://github.com/jim-schwoebel/voicebook/tree/master)
