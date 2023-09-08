# Presentation
This tool aims to help provide a proxy to remembering new words by encountering them in real life situations, in different context and sentences. 

The idea is as follows:
Given a word provided and due to be reviewed today on Anki, a new sentence using it in a certain context is generated. Additionally, a new audio could be generated for that sentence. 

The learner could then study as followed:
1. Review each card by first being presented the full sentence with the word highlighted.
2. Listen to the audio of the sentence first, and see the pronunciation of the word being reviewed. Leaving that person to guess what the meaning of the word is. 

## Some considerations
- Can it work locally or does it require an internet connection
- What tool (GenAI) to use and what are the costs involved
- How does that fit with the practice of sentence mining, if that mined sentence will get overwritten at the next study.

## Compatibility
The focus is on the platform Anki. The front-end would probably be a chrome extension or perhaps a standalone webiste, as long as it can access the user's localhost urls. 

A dedicated field for the sentence is necessary, as well as an input field with the word 



### Open questions 
- How to know the language of the word for which a sentence is meant to be generated
- How to handle wrong/mistyped input words. Eg: "Convinient" for "Convenient"
-


# Useful resources
- Anki Add-ons docs: https://addon-docs.ankiweb.net/intro.html
- Anki local server API - for local dev: https://github.com/FooSoft/anki-connect


### Local setup notes
PyQt5 was not working due to missing qmake compiler. 
Solution: 
1. install qt5 via brew "brew install qt5",
2. then add qt5 to path PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' 
3. pip install PyQt5




# Misc.
Due to big difficulties with compatibility of the PyQt5 dependency of Anki's aqt package, it has been decided to implement the app using the http API (for now), and not make it an add on then... 


# Questions for mentor
- Should I make one card adapter per service? Like one Anki Card Adapter to my own Card Object, and then if there are different services in the future, I make another card adapter.
- Does it make sense that based on the flashcard service provided, I pass a different object to my CardManager? 