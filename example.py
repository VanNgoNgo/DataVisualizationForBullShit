import Visualization as V

def main():
    #Create main variables
    '''
    {"Category for bullshit" : (no. of of BS, no. of debunked BS)}
    '''
    categories = {
        "Facebook": (5,3),
        "Youtube": (2,1),
        "News": (1,0),
        "Chat": (3,3),
        "Family": (1,0),
        "Debates": (3,3)
    }
    V.drawGraph(categories)
               
main()
