from pymonad.either import Left, Right
from datetime import *

class Agent:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.response = ""

    def issueTicket(self):
        return True

    def __repr__(self):
        return self.name

class Flight:
    def __init__(self, flightNumber, datetime):
        self.flightNumber = flightNumber
        self.datetime = datetime
    
    def __repr__(self):
        return self.flightNumber

    def seatAvailable(self):
        seats = ['i1-r','w2-l','w3-r']
        return seats

class Customer:
    def __init__(self, name, ssn, card):
        self.name = name
        self.ssn = ssn
        self.card = card

    def __repr__(self):
        return self.name

    def checkCredit(self):
        return self.card.valid()
    
    def paymentDone(self):
        return True

class CreditCard:
    def __init__(self, cardname, expiration):
        self.cardname = cardname
        self.expiration = expiration

    def valid(self):
        today = date.today()
        return self.expiration > today 

def authorize(agent):
    if agent.id >10 and agent.id <20:
        return True
    return False

def seatAvailable(flight):
    return len(flight.seatAvailable()) > 0
    
def agentAuthorization(party):
    agent = party[0]
    if authorize(agent):
        agent.response = {'status':'success', 'message':'Valid agent.', 'agent_id':f'{agent.id}'}
        return Right(party)
    agent.response = {'status':'failed', 'message':'Invalid agent.'}
    return Left(party)

def seatAvailability(party):
    flight = party[2]
    agent = party[0]
    if seatAvailable(flight):
        agent.response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(party)
    agent.response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(party)

def checkCustomerCredit(party):
    customer = party[1]
    agent = party[0]
    if customer.checkCredit():
        agent.response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(party)
    agent.response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(party)

def paymentProcess(party):
    customer = party[1]
    agent = party[0]
    if customer.paymentDone():
        agent.response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(party)
    agent.response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(party)

def issueTicket(party):
    agent = party[0]
    if agent.issueTicket():
        agent.response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(party)
    agent.response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(party)

if __name__ == '__main__':
    expire = date(2022,12,31)
    card = CreditCard("VISA",expire)
    customer = Customer("John","111-11-1111", card)
    flight = Flight("CO102", date.today())
    agent = Agent("David",15)
    party = (agent, customer, flight)
    process = agentAuthorization(party) \
        .bind(seatAvailability)         \
        .bind(checkCustomerCredit)      \
        .bind(paymentProcess)           \
        .bind(issueTicket)

    print(process) # get boxed values
    print(process.value) # open box
    print(process.value[0].response)