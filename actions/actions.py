from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProcessParagraph(Action):
    def name(self) -> str:
        return "action_process_paragraph"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Extract the provided paragraph and topic from the user's message
        paragraph = tracker.latest_message['text']
        topic = tracker.get_slot('topic')

        # Process the paragraph (You can use your grammar checking logic here)
        # For simplicity, let's just print the paragraph and topic for now
        print(f"User provided paragraph about {topic}: {paragraph}")

        # Respond with a confirmation message
        dispatcher.utter_message(text="Thank you for providing the paragraph. I will process it for errors.")

        return []
