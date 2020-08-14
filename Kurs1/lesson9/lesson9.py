from abc import ABC, abstractmethod

class Tag(ABC):
    TAG_NAME = None
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_html(self):
        return ''

class Image(Tag):
    TAG_NAME = "img"
    def __init__(self, scr, alt=''):   
        self.scr = scr
        self.alt = alt

    def get_html(self):
        return '<{} scr="{}" alt={}'.format(self.TAG_NAME, self.scr, self.alt)


class Input(Tag):
    TAG_NAME = "input"
    def __init__(self):
        super().__init__()
        
    def get_html(self):
         return '<{}></{}>'.format(self.TAG_NAME, self.TAG_NAME)  

class Text(Tag):
    TAG_NAME = "p"
    def __init__(self):
        super().__init__()

    def get_html(self):
        return '<{}></{}>'.format(self.TAG_NAME, self.TAG_NAME)

class Link(Tag):
    TAG_NAME = "a"
    def __init__(self, href):
        self.href = href

    def get_html(self):
        return '<{} href="{}"></{}>'.format(self.TAG_NAME, self.href, self.TAG_NAME)   


class TagFactory:
    TAG_LIST = (Image, Input, Text, Link)

    @staticmethod
    def creat_tag(name, **kwargs):
        for tag in TagFactory.TAG_LIST:
            if tag.TAG_NAME.lower() == name.lower():
                return tag(**kwargs)
        return None        
      


factory = TagFactory()
image = factory.creat_tag('img', scr='scr', alt='image')
print(image.get_html())
input = factory.creat_tag('input')
print(input.get_html())
text = factory.creat_tag('p')
print(text.get_html())
link = factory.creat_tag('a', href="")
print(link.get_html())





                         





