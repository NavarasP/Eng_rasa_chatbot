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

text = "gec: " + "We no open, sorrry"
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)

print(result.text)