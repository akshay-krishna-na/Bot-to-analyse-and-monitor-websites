

from nltk.chat.util import Chat

pairs = [
    ['my name is (.*)', ['hi %1']],
    
['(hi|hello|hey|holla|hola|hai)', ['hey there', 'hi there', 'haayyy']],
    
['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    
['(.*)(location|city) ?',[ 'Ernakulam, Kerala']],
    
['(.*) created you ?', ['jos did using NLTK']],

['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    
['(.*)help(.*)', ['I can help you']],
    
['(.*) your name ?', ['my name is J.O.S and Im a chatbot']],
    
[r"how are you ?",["I'm doing very well\nHow about You ? happy or sad"]],
    
["happy",["I'm feeling happy too!"]],
    
['sad',["I'm sorry to hear that!"]],
    
['(.*)weather(.*)', ['partially cloudy']],
['(.*) (.*)',['%1 %2']],
  

    

]

my_dummy_reflections = {
    'go' : 'gone',
    'hello' : 'hey there',
    'i am' : 'you are',
    'i' : 'you',
}

chat = Chat(pairs, my_dummy_reflections)

chat.converse()

