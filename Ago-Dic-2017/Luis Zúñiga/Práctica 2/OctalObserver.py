from Observer import Observer

class OctalObserver(Observer):
     
    def __init__(self,Subject):
        self.subject = Subject
        self.subject.attach(self.subject,self) 
        
    
    def update(self):
        print('String Octal: ' + oct(self.subject.getState(self.subject)))
    
    
