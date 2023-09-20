# Presentation
This tool aims to help provide an improved way to remembering new words via Flashcards by generating a new sentence per studied word at each study session. Thus it will make the study session closer to a real life situation where a same word is met in different context and sentenced at each time.

The idea is as follows:
Given a word provided and due to be reviewed today on Anki, a new sentence using it in a certain context is generated. Additionally, a new audio could be generated for that sentence. 

The learner could then study as followed:
1. Review each card by first being presented the full (new) sentence with the word highlighted.
2. Or listen to the audio of the sentence first, and see the pronunciation of the word being reviewed. Leaving that person to guess what the meaning of the word is. 

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
## Generate a sentence and update card for cards due today
Running this command will generate new sentences using the word meaningfully.

# Local setup
## Anki setup
Follow the steps below to set up locally this project
1. [Download Anki App](https://apps.ankiweb.net/#download)
2. Once downloaded, create a user and select "Import File" at the bottom.
3. Import to Anki the mock data available at: /local_setup/Mandarin_local_dev.apkg

**Make sure to keep Anki running in the background while using this tool.** 
## Environment setup
```bash
pip install -r requirements.txt
```
## API Keys
For the Sentence Generator to run, it requires a valid API key to OpenAI. Make sure to export the following variable to your environment:
```bash
OPEN_AI_TOKEN=<your key>
```
# Misc.
Due to big difficulties with compatibility of the PyQt5 dependency of Anki's aqt package, it has been decided to implement the app using the http API (for now), and not make it an add on then... 

### Open questions 
- How to know the language of the word for which a sentence is meant to be generated
- How to handle wrong/mistyped input words. Eg: "Convinient" for "Convenient"
- How does that fit with the practice of sentence mining, if that mined sentence will get overwritten at the next study.



### Useful resources
- Anki Add-ons docs: https://addon-docs.ankiweb.net/intro.html
- Anki local server API - for local dev: https://github.com/FooSoft/anki-connect


# Questions for mentor


