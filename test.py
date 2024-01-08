# import language_tool_python
# tool = language_tool_python.LanguageToolPublicAPI('en-US')
# text = 'He do not likes to go outside. Her writing skill  good.'
# text = 'Her writing skill are  good.'
# # corr = tool.correct(text)
# corr = text
# for i in range(3):
#     corr = tool.correct(corr)
# print(corr)
# # print(tool.check(text))

from happytransformer import HappyTextToText
from happytransformer import TTSettings

happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

text = "gec: " + "nature when you smile over your shoulder. for a minute i forget that i'm older. I wanna dance with you right now.and you ask me to stay over. i so in love with you. i hope you knw."
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)

print(result.text)

# ===========================================

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


        
        text="gec: " + tracker.latest_message['text'] 
        # result = happy_tt.generate_text(text, args=ttsettings).text


        while True:
            result = happy_tt.generate_text(text, args=ttsettings).text
            dispatcher.utter_message(text=result)
            if result == text:
                break
            text = "gec:" + result

        # text = "gec: " + result.text
        # result = happy_tt.generate_text(text, args=ttsettings)
        # Respond with a confirmation message
        dispatcher.utter_message(text="Thank you for providing the paragraph. I will process it for errors.")
        # dispatcher.utter_message(text=result.text)

        return []

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from happytransformer import HappyTextToText
# from happytransformer import TTSettings

# happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
# ttsettings = TTSettings(do_sample=True, top_k=10, temperature=0.5, min_length=1, max_length=100)

# class ActionProcessParagraph(Action):
#     def name(self) -> str:
#         return "action_process_paragraph"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
#         def correct_grammar(text):
#             return happy_tt.generate_text(text, args=ttsettings)
        
#         # Extract the provided paragraph from the user's message
#         text = tracker.latest_message['text']

#         # Correct grammar in a loop until there are no more corrections
#         while True:
#             result = correct_grammar(text)
#             if result.text == text:
#                 break
#             text = result.text

#         # Respond with a confirmation message and the corrected paragraph
#         dispatcher.utter_message(text="Thank you for providing the paragraph. I will process it for errors.")
#         dispatcher.utter_message(text=result.text)

#         return []

# version: "3.1"

# rules:
# - rule: Implementation of the Two-Stage-Fallback
#   steps:
#   - intent: rewrite_sentence
#   - action: action_accept
#   - action: action_process_paragraph
#   - action: action_nltk_process



