# Card manager
# Flashcard app service
import pdb


class Card:
    """
    Standardized card object which is used across services.
    """

    def __init__(self, tl_word: str, tl_sentence: str) -> None:
        self.tl_word = tl_word
        self.tl_sentence = tl_sentence


class FlashCardServiceInterface:

    def __init__(self) -> None:
        self.tl_word_field = ""
        self.tl_sentence_field = ""


    def connect_to_service(self) -> bool:
        """
        Checks that service is available at initialization
        """
        pass

    def getDeckLists() -> list[str]:
        """
        Return a list of all the decks of cards available
        """
        pass

    def set_field_mapping(self, mapping: dict) -> None:
        """Set/Update the FlashCard service field mapping"""
        pass

    def cast_raw_card_to_Card(raw_card_data: list[dict]) -> list[Card]:
        """
        Processing step to extract and format relevant data to create a Card
        """


class CardManager:
    def __init__(
        self,
        flashCardService: FlashCardServiceInterface,
        sentenceGenerator: str,
        lang: str,
    ) -> None:
        self.lang = lang
        self.sentenceGenerator = sentenceGenerator
        self.flashCardService = flashCardService


if __name__ == "__main__":
    CardManager(
        "anki",
        "en",
    )
