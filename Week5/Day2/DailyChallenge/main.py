class Pagination(alphabetList):
    def __init__(self, items, pageSize):
        self.items = items
        self.page_size = pageSize
        self.items = []
        self.page_size = 10
    
        
    def alphabetList(self):
        self.alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
        
p = Pagination(alphabetList, 4)
