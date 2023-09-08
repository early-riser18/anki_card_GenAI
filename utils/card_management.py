# Card manager
# Flashcard app service
import pdb



class FlashCardServiceInterface:
    

    def connect_to_service(self) -> bool:
        """
        Checks that service is available at initialization
        """
        pass
    def getDeckLists() -> list[str]:
        "Return a list of all the decks of cards available"
        pass



class CardManager:
    def __init__(
        self, flashCardService: FlashCardServiceInterface, sentenceGenerator: str, lang: str
    ) -> None:
     
        self.lang = lang
        self.sentenceGenerator = sentenceGenerator
        self.flashCardService = flashCardService
       
    



if __name__ == "__main__":
    CardManager("anki","en",)