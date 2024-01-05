from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from happytransformer import TTSettings
from happytransformer import HappyTextToText


happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1")
tt_settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)

class ActionProcessParagraph(Action):
    def name(self) -> str:
        return "action_process_paragraph"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Extract the provided paragraph and topic from the user's message
        paragraph = tracker.latest_message['text']
        topic = tracker.get_slot('topic')

        
        text = "gec: " + paragraph
        

        result = happy_tt.generate_text(text, args=tt_settings)

        # Process the paragraph (You can use your grammar checking logic here)
        # For simplicity, let's just print the paragraph and topic for now

        # Respond with a confirmation message
        dispatcher.utter_message(text="Thank you for providing the paragraph. I will process it for errors.")
        dispatcher.utter_message(text=result.text)

        return []
