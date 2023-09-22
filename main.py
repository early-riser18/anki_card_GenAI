from utils.card_management import CardManager
from utils.anki_connect import AnkiService
from utils.FlashCardServiceInterface import FlashCardServiceInterface


def main():
    flashcard_service = AnkiService()

    # CONFIG INTERFACE WITH USERS
    deck_name = get_config_deck_name(flashcard_service)

    # TODO Prompt user to provide mapping
    flashcard_service.set_field_mapping(
        {"tl_sentence": "Mined Sentence", "tl_word": "Mined Word"}
    )
    lang = "en"

    # TODO
    sentenceGenerator = None

    cardManager = CardManager(flashcard_service, sentenceGenerator, lang, deck_name)


def get_config_deck_name(card_service: FlashCardServiceInterface) -> str:
    """
    Given a FlashCard Service, validated and return the selected deck by user.
    """
    decks_list = card_service.get_decks_list()
    deck_name = input(f"Type the deck to update sentences  {decks_list}")

    if deck_name not in decks_list:
        raise Exception("Wrong value provided")

    return deck_name


if __name__ == "__main__":
    main()
