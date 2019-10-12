#Maya Yosef

def make_dict():
#Exit claim: The func returns a dict which contains 3 input objects
#(key = string, value = integer)"""
    dict = {}
    for x in range(3):
        key = input("please type a string for the dictionary: ")
        value = int(input("please type an integer for the dictionary: "))
        dict[key] = value
#   print(dict)   #just to check 
    return dict    

def is_string_key_in_dict(dict):
#Entrance claim: The func gets a dict which contains 3 input objects 
#(key = string, value = integer)
#Exit claim: The func prints "yes" if the input string it inputs is a key in dict,
#and "no" otherwise
    input_string = input("please type a string: ")
    if input_string in dict:
        print("yes")
    else:
        print("no")

def main():
    dict = make_dict()
    is_string_key_in_dict(dict)

if __name__ == "__main__": 
    main() 