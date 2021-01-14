class Node_Data:
    def __init__(self,key:int,pos:tuple):
        self.__key=key
        self.w=0
        self.tag=0
        self.info=""
        self.__postion=pos
        self.in_e=0
        self.out_e=0
    def getk(self) -> int:
        return self.__key

    def getPos(self) -> tuple:
        return self.__postion

    def setPos(self,pos:tuple) -> tuple:
        self.__postion = pos

    def __repr__(self):
        return "%s: |edges out| %s |edges in| %s"%(self.__key,self.out_e,self.in_e)

    def __lt__(self, other):
        selfPriority = (self.w, self.getk())
        otherPriority = (other.w, other.getk())
        return selfPriority < otherPriority