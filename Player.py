import json
import random
import time
from Deck import *
from Card import *
from tkinter import *
class CardButton(Button):
    __mainText=""
    __subText=""
    def __init__(self, master=None, **kargs):
        super().__init__( master, kargs)
        #if('text' in kargs):
            #self.setMainText(kargs['text'])
    def setMainText(self,txt):
        self.__mainText=txt
        return self
    def setSubText(self,txt):
        self.__subText=txt
        return self
    def switchToMainText(self):
        if(self['text']!=self.__mainText):
            self['text']=self.__mainText
        return self
    def switchToSubText(self):
        if(self['text']!=self.__subText):
            self['text']=self.__subText
        return self
    def swipeText(self):
        if(self['text']==self.__mainText):
            self['text']==self.__subText
        else:
            self['text']==self.__mainText
        return self

class Player:
        
    __hand=None
    __name=""
    __cFrame = None
    def getResponse(self):
        pass
    def delCardFromFrame(self,btn,card,**args):
        
        if(card.isDropable()):
            btn.destroy()
            self.__hand.remove(card)
            del btn,card
        if('rc' in args and args['rc']!=None):
 
            args['rc']()
        if('erpfnc' in args and args['erpfnc']!=None):
            args['erpfnc']()
        print(self.__cFrame.winfo_width())
        
        if('isPublicFrame' in args):
            if(args['isPublicFrame']==False):
                self.__cFrame.winfo_parent().configure(scrollregion = self.__cFrame.winfo_parent().bbox("all"))
            else:
                pass
    __cPublicFrame=None
    __FrameCnfs = {}
    __rootPublicFrameCanvas=None
    __cPublicScroller=None
    __cScroller = None
    def getPublicCardFrame(self,**kargs):
        if('rootCanvas' in kargs and self.__rootFrameCanvas == None):
            __rootPublicFrameCanvas=kargs['rootCanvas']
        rc = None
        erpfnc = None
        if('rankcommand' in self.__FrameCnfs):
            rc = self.__FrameCnfs['rankcommand']
        elif('rankcommand' in kargs):
            rc = kargs['rankcommand']
            self.__FrameCnfs['rankcommand']=kargs['rankcommand']
        if('erpfnc' in self.__FrameCnfs):
            erpfnc=self.__FrameCnfs['erpfnc']
        elif('erpfnc' in kargs):
            erpfnc=kargs['erpfnc']
            self.__FrameCnfs['erpfnc'] =kargs['erpfnc']
        
        if(self.__cPublicFrame != None):
            lst = self.__cPublicFrame.winfo_children()[:]
            for i in lst:
                i.destroy()
        if(self.__cPublicFrame==None and 'parent' in kargs):
            master=kargs['parent']
            self.__cPublicFrame = Frame(master)
            self.__cPublicFrame.pack(fill=X,expand=TRUE)
            self.__cPublicFrame.grid(row=0,column=0,stick="news")
        
        for i in range(len(self.__hand)):
            btn =CardButton(self.__cPublicFrame,text=self.__hand[i].getButtonTextFormat(),wraplength=30,height=8,justify=CENTER).setMainText(self.__hand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToSubText()
            btn.config( command=lambda card=self.__hand[i],btn=btn:self.delCardFromFrame( btn,card,rc=rc,erpfnc=erpfnc,isPublicFrame=True))
            btn.grid(row=0,column=i,rowspan=2,stick=N+S+E+W)
        
                
        return self.__cPublicFrame
        
    __rootFrameCanvas = None
    def getCardFrame(self,**kargs):
        if('rootCanvas' in kargs and self.__rootFrameCanvas == None):
            __rootFrameCanvas=kargs['rootCanvas']
        if('rankcommand' in self.__FrameCnfs):
            rc = self.__FrameCnfs['rankcommand']
        elif('rankcommand' in kargs):
            rc = kargs['rankcommand']
            self.__FrameCnfs['rankcommand']=kargs['rankcommand']
        
        if('erpfnc' in self.__FrameCnfs):
            erpfnc=self.__FrameCnfs['erpfnc']
        elif('erpfnc' in kargs):
            erpfnc=kargs['erpfnc']
            self.__FrameCnfs['erpfnc'] =kargs['erpfnc']
        if(self.__cFrame!=None and len(self.__hand)!= len(self.__cFrame.winfo_children())):
            lst = self.__cFrame.winfo_children()
            for i in lst:
                i.destroy()
            
            for i in range(len(self.__hand)):
                Grid.columnconfigure(self.__cFrame,i,weight=1)
                
                btn =CardButton(self.__cFrame,text=self.__hand[i].getButtonTextFormat(),wraplength=30,height=8).setMainText(self.__hand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToMainText()
                btn.config( command=lambda rc=rc,card=self.__hand[i],btn=btn:self.delCardFromFrame( btn,card,rc=rc,erpfnc=erpfnc,isPublicFrame=False))
                btn.grid(row=0,column=i,rowspan=2,stick=N+S+E+W) #.pack(side=LEFT)
            
        if(self.__cFrame==None and 'parent' in kargs):
            master = kargs['parent']
            self.__cFrame = Frame(master)
            self.__cFrame.pack(fill=X,expand=TRUE)
            leng = len(self.__hand)
            for i in range(len(self.__hand)):
                Grid.columnconfigure(self.__cFrame,i,weight=1)
                btn =CardButton(self.__cFrame,text=self.__hand[i].getButtonTextFormat(),wraplength=30,height=8).setMainText(self.__hand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToMainText()
                btn.config( command=lambda rc=rc,card=self.__hand[i],btn=btn:self.delCardFromFrame( btn,card,rc=rc,erpfnc=erpfnc,isPublicFrame=False))
                btn.grid(row=0,column=i,rowspan=2,stick=N+S+E+W) #.pack(side=LEFT)
            self.__cFrame.grid(row=0,column=0,stick="news")
        
            
        return self.__cFrame
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
            if(card==c  and card.isDropable()):
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