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

## what working on right now

* better wakeword for nala so that there are fewer false positives during conversations 
* making 1 script maintainable with environment vars for google transcription and/or pocketsphinx 
* google transcription only for things like documentation and diarization, etc. 
* detecting music with a ML model in background and/or mouse clicks, etc. as a query - if voice. etc. - if that don't worry about querying 
* make voice configurable - various female voices in pyttsx3 library - iterate through and set global parameter for all actions and main script. Convert all actions to use this variable. 

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
* [snowboy hotword detector](https://snowboy.kitt.ai/hotword/18587#)
* [building language model with pocketsphinx](https://cmusphinx.github.io/wiki/tutoriallm/#using-keyword-lists-with-pocketsphinx)
