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
        message = tracker.latest_message['text']
        while True:
            result = happy_tt.generate_text("gec: " +message, args=ttsettings).text
            if result == message:
                break
            message = result

        # Respond with a confirmation message
     
        dispatcher.utter_message(text=result)
        dispatcher.utter_message(text="Here is you error free sentence :)")

        return []