from abc import ABCMeta, abstractmethod

class ICompositor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def compose(self): raise NotImplementedError

class SimpleCompositor(ICompositor):

    def compose(self):
        print("SimpleCompositor implements a simple strategy that determines"+ 
            "linebreaks one at a time.")

class ArrayCompositor(ICompositor):
    
    def compose(self):
        print("ArrayCompositor implements a strategy that selects breaks so that each row"+
            "has a fixed number of items.  It's useful for breaking a collection"+ 
            "of icons into rows, for example.")
        

class Composition(object):

    def __init__(self,compositor):
        self.compositor = compositor

    def compose(self):
        self.compositor.compose()

Composition(ArrayCompositor()).compose()
Composition(SimpleCompositor()).compose()