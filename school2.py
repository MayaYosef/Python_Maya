#Maya Yosef

def make_dict():
#Exit claim: The func returns a dictionary which contains: key = x, value = x**2, 
#from x = 0 until x = 4
    dict = {}
    for x in range(5):
        dict[x] = x**2
    return dict    
        
def main():
    new_dict = make_dict()
    print("Dictionaty:", new_dict)
    
    
if __name__ == "__main__": 
    main() 
