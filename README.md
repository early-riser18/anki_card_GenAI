# Presentation
This tool aims to help provide an improved way to remembering new words via Flashcards by generating a new sentence per studied word at each study session. Thus it will make the study session closer to a real life situation where a same word is met in different context and sentenced at each time.

The idea is as follows:
Given a word provided and due to be reviewed today on Anki, a new sentence using it in a certain context is generated. Additionally, a new audio could be generated for that sentence. 

The learner could then study as followed:
1. Review each card by first being presented the full (new) sentence with the word highlighted.
2. Or listen to the audio of the sentence first, and see the pronunciation of the word being reviewed. Leaving that person to guess what the meaning of the word is. 

## Some considerations
- Can it work locally or does it require an internet connection
- What tool (GenAI) to use and what are the costs involved
- How does that fit with the practice of sentence mining, if that mined sentence will get overwritten at the next study.

## Compatibility
The focus is on the platform Anki. The front-end would probably be a chrome extension or perhaps a standalone webiste, as long as it can access the user's localhost urls. 

A dedicated field for the sentence is necessary, as well as an input field with the word 

# Functionalities
## Select a flashcard service
This tool has been built with offering multi flashcard service compatibility.
Currently, only [Anki](https://apps.ankiweb.net/) is supported.
## Configure service
1. Authenticate
2. Select decks to generate sentence for
3. Provide fields mapping (Word, Sentence) and language
## Update sentences for due cards
Running this command will generate new sentences using the word meaningfully.

# Misc.
Due to big difficulties with compatibility of the PyQt5 dependency of Anki's aqt package, it has been decided to implement the app using the http API (for now), and not make it an add on then... 

### Open questions 
- How to know the language of the word for which a sentence is meant to be generated
- How to handle wrong/mistyped input words. Eg: "Convinient" for "Convenient"
-


### Useful resources
- Anki Add-ons docs: https://addon-docs.ankiweb.net/intro.html
- Anki local server API - for local dev: https://github.com/FooSoft/anki-connect


### Local setup notes
PyQt5 was not working due to missing qmake compiler. 
Solution: 
1. install qt5 via brew "brew install qt5",
2. then add qt5 to path PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' 
3. pip install PyQt5



# Questions for mentor
- Should I make one card adapter per service? Like one Anki Card Adapter to my own Card Object, and then if there are different services in the future, I make another card adapter.
- Does it make sense that based on the flashcard service provided, I pass a different object to my CardManager? 
- Is my adapter structure (FlashcardService, Card, Card Manager) correctly set up? 
- FlashCardService.set_field_mapping() should be defined identically for all FlashCard services. Therefore, where to define it to keep code DRY?
- Is it correct that I set some methods as private like __cast_raw_card_to_Card
- Is my decomposition of the methods in the CardManager good? (not too small/too big)
