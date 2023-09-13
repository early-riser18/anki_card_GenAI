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
        return self


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
