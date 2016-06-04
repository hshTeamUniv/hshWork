import json
import random
import time
from Deck import *
from Card import *

class Player:
    __hand=None
    __name=""
    def getResponse(self):
        
    @property
    def name(self):
        return self.__name
    def __init__(self,name):
        self.__hand = Deck.getEmptyDeck();
        self.setName(name)
    def popTwoCards(self,cards):
       for card in cards:
           self.__hand.remove(card)
       if(cards!=()):
            del cards
        
    def popOneCard(self,card):
        for c in self.__hand:
            if(card==c  ):
                self.__hand.remove(c)
                break
    def selectPlayerCard(self,player,card,waitMode=False):
        pdeck = player.getDeck()
        responseIdx = 0#impl this
        return pdeck[responseIdx]
    
    def exportCard(self,exportingIdx):
        result = self.__hand[exportingIdx].cloneCard()
        del self.__hand[exportingIdx]
        return  result
    def importCard(self,card):
        self.__hand.append(card)

    def setName(self,Name):
        self.__name = Name
        return self
    def getName(self):
        return self.__name
    def setHand(self,hand):
        d = hand
        if(type(hand) == Deck):
            d= d.getCloneDeck()
        else:
            d = Deck.getEmptyDeck()
            d.extend(hand)
        self.__hand = d
    def setDeck(self,hand):
        return self.setHand(hand)
    def pushCards(self,cards):
        self.__hand += cards
        return self.__hand
    def pushCard(self,card):
        self.__hand.append(card)
        return self.__hand
    def getHand(self):
        return self.__hand
    def getDeck(self):
        return self.__hand
    def fromJson(self,Json,returnObject=True):
        data = json.loads()
        handData = data['hand']
        nameData = data['name']
        self.__hand.clear()
        for card in handData:
            self.__hand.append(Card.createFromJson(card))
        self.__name = nameData
        if(returnObject):
            return self
    def toJson(self):
        handj = []
        for c in self.__hand:
            handj.add(c.toJson());
        result = {"hand":handj,"name":name}
        result = json.dumps(result)
        return result
class Computer(Player):
    def __init__(self,pname="Computer"):
        super().__init__(pname)
            
    def popTwoCards(self,selectedIndexes):
        card1 = None
        card2 = None
        levelList = Card.Levels()
        for _ in range(len(levelList)-1):
            pass
        while(type(card1) == JokerCard or type(card2) == JokerCard):
             pass
        super().popTwoCards(selectedIndexes)
    
    def selectPlayerCard(self,player,card,waitMode=True):
        
        pdeck = player.getDeck()
        
        idx = random.randrange(0, len(player.getDeck()))
        result = player.getDeck()[idx].clone()
        if(waitMode):
            time.sleep(random.randrange(0,31)/10)
        self.importCard(result)
        player.exportCard(idx)
        return result