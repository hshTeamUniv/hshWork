class Util:
    @staticmethod
    def moveListOrder(listv):
        if(type(listv) == list and listv!=[]):
            listv = listv[1:]+[listv[0]]