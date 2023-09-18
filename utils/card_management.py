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
        self, flash_card_service, sentence_generator: str, lang: str, deck_name: str
    ) -> None:
        self.lang = lang
        self.sentence_generator = sentence_generator
        self.flash_card_service = flash_card_service
        self.deck_name = deck_name

    def update_sentence_due_cards(self):
        if not self.flash_card_service.connect_to_service():
            raise Exception("Unable to connect to FlashCard service")

        # Get cards from FlashCard Service
        deck_cards = self.flash_card_service.get_Cards_from_deck(self.deck_name)

        # Generate Sentences
        success_count = 0

        for c in deck_cards:
            # Check which ones are due + if none are due, don't do. 
            try:
                print(vars(c))

                res = self.sentence_generator.generate_sentence(c)
                c.set_tl_sentence(res["generated_sentence"])
            
            except:
                print(
                    f"Something went wrong while generating a sentence for cardId {c.id}"
                )
                continue

            # Request cards to be updated at FlashCard Service
            try:
                self.flash_card_service.update_FlashCardService_card(c)
            
            except:
                print(f"An error occured while updating cardId {c.id}")
                continue
            
            success_count += 1

        print(f"In {len(deck_cards)} valid cards, {success_count} were successfully updated.")

if __name__ == "__main__":
    from utils.anki_connect import AnkiService

    cm = CardManager(AnkiService(), SentenceGenerator(), "en", "Mandarin")
    cm.flash_card_service.set_field_mapping(
        {"tl_sentence": "Mined Sentence", "tl_word": "Mined Word"}
    )

    cm.update_sentence_due_cards()

