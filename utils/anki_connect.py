import json
import urllib.request
import requests
from utils.card_management import  Card
from utils.FlashCardServiceInterface import FlashCardServiceInterface
import pdb


class AnkiService(FlashCardServiceInterface):
    """
    Adapter/Wrapper class to interact with the Anki-connect HTTP API.
    """

    def __init__(self) -> None:
        super().__init__()

    def connect_to_service(self):
        try:
            url = "http://127.0.0.1:8765"
            requests.get(url)
        except:
            return False

        return True

       
    def get_decks_list(self):
        return self.__invoke("deckNames")

    def get_cards_data(self, deck_name: str) -> list[dict]:
        # Get the card Ids and then pass them directly to next function to get values of cards.
        note_ids = self.__invoke(action="findNotes", query=f"deck:{deck_name}")
        cards_info = self.__invoke("cardsInfo", cards=note_ids)

        return cards_info

    def cast_raw_card_to_Card(self, raw_card_data):
        if not self.field_mapping["tl_word"]:
            raise Exception("Field mapping is not defined.")
        
        try:
            my_Card = Card(
                id=raw_card_data["cardId"],
                tl_word=raw_card_data["fields"][self.field_mapping["tl_word"]]["value"],
                tl_sentence="",
            )
            return my_Card
        except:
            raise KeyError("Cannot create Card")
            
        

    def get_Cards_from_deck(self, deck_name) -> list[Card]:
       
        cards_raw_data = self.get_cards_data(deck_name)

        deck_of_Cards = []

        for c in cards_raw_data:
            try:
                deck_of_Cards.append(self.cast_raw_card_to_Card(c))
            except:
                try:
                    print(f"Failed at {c['cardId']}")
                except:
                    print(f"Corrupted card skipped: {c}")
        print(len(cards_raw_data), len(deck_of_Cards))

        return deck_of_Cards
    

    def update_FlashCardService_card(self, card: Card):
       
        params = {
            "note": {
                "id": card.id,
                "fields": {self.field_mapping["tl_sentence"]: card.tl_sentence},
            }
        }

        self.__invoke("updateNoteFields", **params)


    ### Utility functions for the Anki Connect API ###
    def __request(self, action, **params):
        return {"action": action, "params": params, "version": 6}

    def __invoke(self, action, **params):
        requestJson = json.dumps(self.__request(action, **params)).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request("http://127.0.0.1:8765", requestJson)
            )
        )
        if len(response) != 2:
            raise Exception("response has an unexpected number of fields")
        if "error" not in response:
            raise Exception("response is missing required error field")
        if "result" not in response:
            raise Exception("response is missing required result field")
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]
  
if __name__ == "__main__":
    card_service = AnkiService()
    card_service.set_field_mapping(
        {"tl_word": "Mined Word", "tl_sentence": "Mined Sentence", "card_id": "cardId"}
    )
    deck_name = card_service.get_decks_list()[1]
    # print(card_service.get_cards_data(deck_name))
    # print(card_service.get_Cards_from_deck("Mandarin::Mandarin Mined Sentences"))

    my_card = card_service.get_Cards_from_deck("Mandarin")[0]
    my_card.set_tl_sentence("This is a testdddd")
    print("Card values are: ", vars(my_card))
    card_service.update_FlashCardService_card(my_card)
    # print(json.dumps(card_service.get_cards_data(  deck_name)[100]))
