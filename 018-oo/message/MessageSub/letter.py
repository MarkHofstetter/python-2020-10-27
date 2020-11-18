from ..Message import *


class Letter(Message):
    
    @Message.content.setter
    def content(self, value):
        if (len(value) > 10):
            raise AttributeError('content too long')
        Message.content.fset(self, value)
    
    @Message.to.getter
    def to(self):
        return "letter: " + Message.to.fget(self)
        