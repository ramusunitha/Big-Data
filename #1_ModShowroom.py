class cls1:
    class_attrib=100 #class attribute or member variable
    #self - default object of a class. Self is not a mandatory keyword - SELF can be mentioned as X or sunitha also
    def funct1(self,a,b): #member function of cls1
        return a+b+self.class_attrib
    def funct2(self, a, b): #member function of cls1
        return a+b-self.class_attrib

class cls2:
    class_attrib=100 #class attribute or member variable
    #self - default object of a class. Self is not a mandatory keyword - SELF can be mentioned as X or sunitha also
    def funct1(self,a,b): #member function of cls1
        return a+b
    def funct2(self, a, b): #member function of cls1
        return a+b