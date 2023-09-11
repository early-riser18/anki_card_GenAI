import json
import urllib.request
import requests
from utils.card_management import FlashCardServiceInterface, Card
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

    def set_field_mapping(self, mapping: dict) -> None:
        self.tl_sentence_field = mapping["tl_sentence"]
        self.tl_word_field = mapping["tl_word"]

    def get_decks_list(self):
        return invoke("deckNames")

    def get_cards_info(self, deck_name: str) -> dict:
        # Get the card Ids and then pass them directly to next function to get values of cards.
        note_ids = invoke(action="findNotes", query=f"deck:{deck_name}")
        cards_info = invoke("cardsInfo", cards=note_ids)
        return cards_info

    def __cast_raw_card_to_Card(self, raw_card_data):
        card_list = []

        for i in raw_card_data:
            try:
                card_list.append(
                    Card(
                        tl_word=i["fields"][self.tl_word_field]["value"], tl_sentence=""
                    )
                )

            except:
                pass

        return card_list

    def get_cards_from_deck(self, deck_name):
        """"""
        return self.__cast_raw_card_to_Card(self.get_cards_info(deck_name))


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
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
    raw_card_data = card_service.get_cards_info("Mandarin")
    card_service.set_field_mapping(
        {"tl_sentence": "Mined Sentence", "tl_word": "Mined Word"}
    )
    print(
        card_service.connect_to_service(),
        # card_service.get_decks_list(),
        # card_service.get_cards_info("Mandarin")[-134],
        card_service.__cast_raw_card_to_Card(raw_card_data[-110:-100]),
    )
