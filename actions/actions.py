from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from happytransformer import HappyTextToText
from happytransformer import TTSettings
happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
ttsettings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)


class ActionProcessParagraph(Action):
    def name(self) -> str:
        return "action_process_paragraph"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Extract the provided paragraph and topic from the user's message
        # topic = tracker.get_slot('topic')
        text = "gec: " + tracker.latest_message['text']
        result = happy_tt.generate_text(text, args=ttsettings)
        # Respond with a confirmation message
        dispatcher.utter_message(text="Thank you for providing the paragraph. I will process it for errors.")
        dispatcher.utter_message(text=result.text)

        return []
