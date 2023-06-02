Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ._anvil_designer import Form1Template
... from anvil import *
... import anvil.server
... 
... class Form1(Form1Template):
...     def __init__(self, **properties):
...         # Set Form properties and Data Bindings.
...         self.init_components(**properties)
... 
...         # Any code you write here will run before the form opens.
... 
...     def Categorise_button_click(self, **event_args):
...         """This method is called when the button is clicked"""
...         article = self.news_article_textbox.text
...         news = anvil.server.call('predict_news', article)
...         if news:
...             self.news_label.visible = True
...             lr_prediction = news["LR Prediction"]["Label"]
...             rfc_prediction = news["RFC Prediction"]["Label"]
