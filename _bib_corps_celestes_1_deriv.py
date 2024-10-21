#####################
###### IMPORTS ######
#####################


import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm



def cos(x):
    return math.cos(math.radians(x))

def sin(x):
    return math.sin(math.radians(x))

def produit(k,u):
    return (k*u[0] , k*u[1])
    
def somme(u,v):
    return (u[0]+v[0], u[1] + v[1])

def calcul_vecteur_u(theta):
    return ( cos(theta) , sin(theta) ) # Compléter cette ligne

def force(m1,m2,r,theta):
    u = calcul_vecteur_u(theta)
    G = 6.7 * 10**(-11)
    return produit(G*m1*m2/r**2,u) # Compléter cette ligne

def dessin_vecteur(fction_calcul):
    v = fction_calcul(45)
    
    print("Test pour theta = 45 degrés")
    
    plt.close('all')
    fig, ax = plt.subplots()
    
    # Add the vector V to the plot
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')

    # Set the x-limits and y-limits of the plot
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    # Show the plot along with the grid
    
    plt.grid()
    plt.show()

def dessin_somme_vecteurs(fonction_somme):
    u = (1,1)
    v = (-1,2)
    s = fonction_somme(u,v)
    print('Test de votre somme de vecteurs : (1 ; 1) + (-1 ; 2), le premier en rouge, le second en bleu et la somme en vert')
    
    plt.close('all')

    fig, ax = plt.subplots()

    # Add vectors V and W to the plot
    ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax.quiver(u[0], u[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax.quiver(0,0, s[0], s[1], angles='xy', scale_units='xy', scale=1, color='g')
    
    ax.set_xlim([-.5, 1.5])
    ax.set_ylim([-.5, 3.5])
    plt.grid()
    plt.show()
    
def dessin_produit_vecteurs(fonction_produit):
    u = (1,1)
    v = fonction_produit(2,u)
    print('Test du produit de (1 ; 1) par 2. (1;1) en rouge et le résultat en bleu')
    plt.close('all')

    fig, ax = plt.subplots()

    # Add vectors V and W to the plot
    ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax.quiver(0,1, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b')
    
    ax.set_xlim([-.5, 2.5])
    ax.set_ylim([-.5, 3.5])
    
    plt.grid()
    plt.show()
    
def calcul_theta(v):
    u  = (1,0)
    cosTh = np.dot(u,v)
    sinTh = np.cross(u,v)
    return (np.rad2deg(np.arctan2(sinTh,cosTh)))   
#---------------------------------------

def simulation(A1,A2,v1,v2,m1,m2,T,nombrePas,calcul_position,calcul_vitesse, option = False):
    posA1 = [A1]
    posA2 = [A2]
    
    
    for i in range(nombrePas):
        A1A2 = somme( A2, produit(-1,A1))
       
        theta = calcul_theta( A1A2)
      
        r = np.linalg.norm(A1A2)
       
        F1 = force(m1,m2,r,theta)
        F2 = produit(-1,F1)
       
        v1 = calcul_vitesse(v1, produit(1/m1,F1),T)
        v2 = calcul_vitesse(v2, produit(1/m2,F2),T)
       
        A1 = calcul_position(A1,v1,T)
        A2 = calcul_position(A2,v2,T)
        
        posA1.append(A1)
        posA2.append(A2)

    xA1 = [ u[0] for u in posA1]
    yA1 = [ u[1] for u in posA1]

    xA2 = [ u[0] for u in posA2]
    yA2 = [ u[1] for u in posA2]

    plt.close('all')
    plt.figure()
    if option == True:
        plt.scatter( 0 , 0 , s = 1000 , color ='y')
        plt.text(-0.5*10**10,-1.4*10**10,'soleil')
        plt.plot(xA1,yA1,'y',label="Trajectoire Soleil")
        plt.plot(xA2,yA2,'b',label="Trajectoire Terre")
    else :
        plt.plot(xA1,yA1,'y',label="Trajectoire A1")
        plt.plot(xA2,yA2,'b',label="Trajectoire A2")
    plt.legend()
    plt.title('Trajectoire de deux corps')

    plt.show()



def simulation3corps(A1,A2,A3,v1,v2,v3,m1,m2,m3,T,nombrePas,calcul_position, calcul_vitesse, option = False):

    posA1 = [A1]
    posA2 = [A2]
    posA3 = [A3]
    
    for i in range(nombrePas):
        #print("____________ \nPas Suivant \n ____________")    
        A1A2 = somme( A2, produit(-1,A1))
        A1A3 = somme( A3, produit(-1,A1))
        A2A3 = somme( A3, produit(-1,A2))
        A2A1 = somme( A1, produit(-1,A2))
        A3A1 = somme( A1, produit(-1,A3))
        A3A2 = somme( A2, produit(-1,A3))
        
        theta12 = calcul_theta( A1A2)
        theta13 = calcul_theta( A1A3)
        theta21 = calcul_theta( A2A1)
        theta23 = calcul_theta( A2A3)
        theta31 = calcul_theta( A3A1)
        theta32 = calcul_theta( A3A2)
        
        
        r12 = np.linalg.norm(A1A2)
        r13 = np.linalg.norm(A1A3)
        r23 = np.linalg.norm(A2A3)
        
        F1 = force(m1,m2,m3,r12,r13,theta12,theta13)
        F2 = force(m2,m1,m3,r12,r23,theta21,theta23)
        F3 = force(m3,m1,m2,r13,r23,theta31,theta32)
        
        v1 = calcul_vitesse(v1, produit(1/m1,F1),T)
        v2 = calcul_vitesse(v2, produit(1/m2,F2),T)
        v3 = calcul_vitesse(v3, produit(1/m3,F3),T)
        
        A1 = calcul_position(A1,v1,T)
        A2 = calcul_position(A2,v2,T)
        A3 = calcul_position(A3,v3,T)
        
        posA1.append(A1)
        posA2.append(A2)
        posA3.append(A3)

    xA1 = [ u[0] for u in posA1]
    yA1 = [ u[1] for u in posA1]

    xA2 = [ u[0] for u in posA2]
    yA2 = [ u[1] for u in posA2]

    xA3 = [ u[0] for u in posA3]
    yA3 = [ u[1] for u in posA3]
    
    plt.close('all')
    plt.figure()
    
    if option == True:
        plt.scatter( 0 , 0 , s = 1000 , color ='y')
        plt.text(-0.5*10**10,-0.7*10**10,'soleil')
        plt.plot(xA1,yA1,'y',label="Trajectoire Soleil")
        plt.plot(xA2,yA2,'b',label="Trajectoire Terre")
        plt.plot(xA3,yA3,'gray',label="Trajectoire Lune")
    else :
        plt.plot(xA1,yA1,'y',label="Trajectoire A1")
        plt.plot(xA2,yA2,'b',label="Trajectoire A2")
        plt.plot(xA3,yA3,'gray',label="Trajectoire A3")
    plt.legend()
    plt.title('Trajectoire de trois corps')

    plt.show()