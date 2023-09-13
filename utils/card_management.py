# Card manager
# Flashcard app service
import pdb
from utils.sentence_generation import SentenceGenerator


class Card:
    """
    Standardized card object which is used across services.
    """

    def __init__(self, id: str, tl_word: str, tl_sentence: str) -> None:
        self.tl_word = tl_word
        self.tl_sentence = tl_sentence
        self.id = id

    def set_tl_sentence(self, sentence: str):
        self.tl_sentence = sentence
        return self


class CardManager:
    def __init__(
        self, flashCardService, sentenceGenerator: str, lang: str, deck_name: str
    ) -> None:
        self.lang = lang
        self.sentenceGenerator = sentenceGenerator
        self.flashCardService = flashCardService
        self.deck_name = deck_name

    def update_sentence_due_cards(self):
        if not self.flashCardService.connect_to_service():
            raise Exception("Unable to connect to FlashCard service")

        # Get cards from FlashCard Service
        deck_cards = self.flashCardService.get_Cards_from_deck(self.deck_name)

        # Check which ones are due

        # Generate Sentences

        for i, c in enumerate(deck_cards):
            try:
                res = SentenceGenerator.generate_sentence(c)
                c.set_tl_sentence(res["generated_sentence"])

            except:
                raise Exception(
                    f"Something went wrong while generating a sentence for cardId {c.card_id}"
                )

            # Request cards to be updated at FlashCard Service
            # try:
            #     self.flashCardService.update_FlashCardService_card(c)
            # except:
            #     raise Exception(f"An error occured while updating cardId {c.card_id}")


if __name__ == "__main__":
    from utils.anki_connect import AnkiService

    cm = CardManager(AnkiService(), SentenceGenerator(), "en", "Mandarin")
    cm.flashCardService.set_field_mapping(
        {"tl_sentence": "Mined Sentence", "tl_word": "Mined Word"}
    )

    cm.update_sentence_due_cards()
# Standardize the returned object from FlashCard Service
# Instanciate card from object in CardManager
