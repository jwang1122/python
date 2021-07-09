class Website:
    def __init__(self,title, urlAddress):
        self.title = title
        self.__urlAddress = urlAddress

    def showTitle(self):
        print(self.title)

    def getUrlAddress(self):
        return self.__urlAddress

obj = Website('Python Basics', 'https://python.org/pythonbasics')
obj.showTitle()
print(obj.getUrlAddress())