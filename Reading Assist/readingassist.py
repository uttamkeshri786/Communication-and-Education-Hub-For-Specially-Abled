import speech_recognition as sr
from random import randint
from tkinter import *

class speech_text:
    '''
        Generate text which the user reads, closes the window.
        Speaks without seeing
        Judges the output and gives result as an output percentage.

        Why this ? We cant expelct a dyslexic person to get everything on the first try
        So we display the text, so the user can practice the sentence and then
        when confident, close the window and repeat from memory
    '''
    def __init__(self):

        '''
            Constructor
            Initialises default window
            Shows the text on the screen

            Param : None
            Return : None
        '''

        def close_window(): 
            self.master.destroy()
        
        self.r = sr.Recognizer()
        self.master = Tk()
        self.master.title("Speech judge")
        self.master.minsize(500,500)
        
        self.generate_text()
        self.button = Button (self.master, text = "Please try and read it, once complete press this and repeat", command = close_window)
        self.button.pack()
        self.master.mainloop()
        self.record_speaking()
        self.judge()

        
        self.qwe = "The sentence was " + self.line
        self.qwe += "\n You said "+ " ".join(self.text)

        self.result = Tk()
        self.result.title("Result of your performance")
        self.result.minsize(500,500)
        self.temp = "You Scored : " + str(self.accuracy) + "%"
        self.label = Label(self.result, text = self.temp)
        self.q = Label(self.result,text = self.qwe)
        self.label.pack()
        self.q.pack()
        self.result.mainloop()
        
    def generate_text(self):

        '''
            Picks a random line from pre-existing set of text.
            displays on the window
            Param : None
            Return : None
        '''
        
        file = "t"+str(randint(1,11))+".txt"
        f = open(file, "r")
        doc = f.read().split("\n")
        start = randint(0,len(doc)-1)
        self.line = doc[start:start+3] #This part change to number of sentences needed
        print(self.line)
        self.line = "\n".join(self.line)
        self.lbl = Label(self.master,text = self.line)
        self.lbl.pack()

        
    def record_speaking(self):
        '''
            Records the user saying the line
        '''
        with sr.Microphone() as source:
            print("Please Read the Passage")
            self.audio = self.r.listen(source)
            try:
                self.text = self.r.recognize_google(self.audio)
            except:
                print("Sorry we couldn't understand it")
        
                
    def judge(self):
        '''
            Judges the sentence spoken v actual sentence
            Then stores the result in a class variable accuracy

            Param : None
            Return : None
        '''
        
        #removing all punctuations
        self.test = ""
        for i in self.line:
            #special characters like ? , . ,./ hata rha hu
            if ((i.lower() >= "a" and i.lower() <= "z") or (i >= "0" and i <= "9") or i == " "):
                self.test += i
                
        self.test = self.test.lower()
        self.test = self.test.split()
        self.text = self.text.lower()
        self.text = self.text.split()
        
        t = set(self.test).intersection(set(self.text))
        self.accuracy = len(t)*100/len(set(self.test))

ob = speech_text()
