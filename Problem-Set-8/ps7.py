# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        return random.random() < self.clearProb

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if random.random() < self.maxBirthProb*(1 - popDensity):
            return SimpleVirus( self.maxBirthProb, self.clearProb )
        raise NoChildException()
        



class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        survivedViruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                survivedViruses.append(virus)

        self.viruses = survivedViruses
        popDensity = len(self.viruses)/float(self.maxPop)

        childViruses = []
        for virus in self.viruses:
            try : childViruses.append( virus.reproduce(popDensity) )
            except : pass
            
        self.viruses += childViruses
                   
        return self.getTotalPop() 



#
# PROBLEM 2
#
def runSimulation(numViruses,maxPop, maxBirthProb, clearProb):
    
    viruses = []
    timeStep = 0
    total = []
    totalTimeSteps = 300
    
    for i in xrange (numViruses):
        viruses.append( SimpleVirus(maxBirthProb, clearProb) )

    patient = SimplePatient( viruses, 1000)

    while timeStep < totalTimeSteps :
        k = patient.update()
        total.append(k)
        timeStep += 1

    return total

def simulationWithoutDrug(numTrials, numViruses=100, maxPop=1000,
                          maxBirthProb=0.1, clearProb=0.05):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    finalResult = None

    for i in xrange(numTrials):
        print 'running trial:', i+1
        results = runSimulation(numViruses,maxPop, maxBirthProb, clearProb)
        if finalResult == None :
            finalResult = results
        else :
            for i in  xrange(len(finalResult)):
                finalResult[i] += results[i]

    for i in  xrange(len(finalResult)):
        finalResult[i] /= float(numTrials)

        
    pylab.figure(1)
    pylab.title('Population v/s Time')
    pylab.xlabel('Time')
    pylab.ylabel('Population')
    pylab.plot(finalResult)
    pylab.show()
        
