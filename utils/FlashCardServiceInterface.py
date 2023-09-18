
from utils.card_management import Card
from abc import ABC, abstractmethod
from typing import final

class FlashCardServiceInterface(ABC):

    def __init__(self) -> None:
        self.field_mapping = {"tl_word": "", "tl_sentence": "", "card_id": ""}
        

    @abstractmethod
    def connect_to_service(self) -> bool:
        """
        Checks that service is available at initialization
        """
        pass

    @abstractmethod    
    def get_decks_list(self) -> list[str]:
        """
        Return a list of all the decks of cards available
        """
        pass
    
    @final
    def set_field_mapping(self, mapping: dict) -> None:
        """Set/Update the FlashCard service field mapping"""
        self.field_mapping["tl_word"] = mapping["tl_word"]
        self.field_mapping["tl_sentence"] = mapping["tl_sentence"]

    @abstractmethod  
    def cast_raw_card_to_Card(self, raw_card_data: dict) -> list[Card]:
        """
        Processing step to extract and format relevant data to create a Card
        Input is data for one card. 
        """
        pass

    @abstractmethod  
    def get_Cards_from_deck(self, deck_name: str) -> list[Card]:
        """Returns list of Cards from the deck. Returns None when Card failed to be created."""
        pass

    @abstractmethod  
    def update_FlashCardService_card(self, card: Card):
        """
        Given a Card, update the corresponding Anki card
        """
        pass