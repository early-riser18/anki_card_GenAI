
from utils.card_management import Card
class FlashCardServiceInterface:

    def __init__(self) -> None:
        self.field_mapping = {"tl_word": "", "tl_sentence": "", "card_id": ""}
        


    def connect_to_service(self) -> bool:
        """
        Checks that service is available at initialization
        """
        pass

    def get_decks_list(self) -> list[str]:
        """
        Return a list of all the decks of cards available
        """
        pass

    def set_field_mapping(self, mapping: dict) -> None:
        """Set/Update the FlashCard service field mapping"""
        pass

    def __cast_raw_card_to_Card(self, raw_card_data: dict) -> list[Card]:
        """
        Processing step to extract and format relevant data to create a Card
        Input is data for one card. 
        """
        pass
    def get_Cards_from_deck(self, deck_name: str) -> list[Card]:
        """Returns list of Cards from the deck. Returns None when Card failed to be created."""
        pass
    def generate_sentence(self, word, lang) -> str:
        """
        Wrapper function to interact with sentence generation service
        """
        pass
