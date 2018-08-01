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

To active Nala, all you need to do is query her with 'Hey Nala!'

You then can do any number of queries. This is the active list:
* sleep
* reboot
* shut down 
* ...

Nala uses machine learning to parse through user intents.

### Multi-query capability 

Nala is equipped with multi-query capability. All you need to do is add 'AND' into your query and she'll automatically execute actions serially that you request to her. 

For example, you may say, "Hey Nala" --> "close spotify and sleep" 

She will then close spotify and then go to sleep for 30 minutes. 

This makes Nala incredibly versatile to do multiple things quickly and is an advantage over other chatbot systems. 

## how this works

we use snowbird hotword detector (). We trained a model on a male's voice. 

## what can Nala do

[Post video]

Nala has an event-driven structure with queries and responses to those queries. 

* get the weather 
* get food 
* get coffee 
* set the alarm
* exercise 
* shut down or restart the computer 
* [surprise me!]

- put all the commands here. 

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
