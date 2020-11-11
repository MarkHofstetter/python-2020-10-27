# ein "To" property
# bei der Ausgabe soll 
# bei SMS "phone: $o->to"
# bei Email "email: $o->to" 

from abc import ABCMeta, abstractmethod


class Message(metaclass = ABCMeta):
    __content = None
    __to      = None

    def __init__(self):
        print("neues Object")
        self.__to = None

    def send(self):
        print(self.content)
        print(self.to)
	
    # getter
    @property
    def content(self):
        return "content: " + self.__content
        
    # setter
    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def to(self):
        return self.__to
        
    @to.setter
    def to(self, value):
        self.__to = value
    
    
class SMS(Message):
    
    @Message.content.setter
    def content(self, value):
        if (len(value) > 10):
            raise AttributeError('content too long')
        Message.content.fset(self, value)
    
    @Message.to.getter
    def to(self):
        return "phone: " + Message.to.fget(self)

class Email(Message):
    subject = None
    
    '''
    def __init__(self):
        super().__init__()
    ''' 
    
    @Message.to.getter
    def to(self):
        return "email: " + Message.to.fget(self)
    
    
    def send(self):
        super().send()
        print(self.subject)
        
        