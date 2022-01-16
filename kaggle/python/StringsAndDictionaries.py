#1
#There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." 
# Let's see if you can write a function to help clean US zip code data. 
# Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
#HINT: str has a method that will be useful here. Use help(str) to review a list of string methods.

def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

#print([is_valid_zip('12345')
#    ,is_valid_zip('1234x')
#    ,is_valid_zip('1234')
#    ,is_valid_zip('123456')
#    ,is_valid_zip('')
#    ,is_valid_zip('/n')])



#2
#A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

#Your function should meet the following criteria:

#Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
#She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
#Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.

def word_search(doc_list, keyword):
    i=0
    result = []
    for i, row in enumerate(doc_list):  
        words = row.split() 
        formated_words = [el.strip('.,').lower() for el in words]
        if keyword.lower() in formated_words:
            result.append(i)
        i+=1
    return result

#doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#print(word_search(doc_list, 'casino'))


#3
#Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

#(You're encouraged to use the word_search function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - and it saves typing!)
def multi_word_search(doc_list, keywords):
    result = dict()
    for el in keywords:
        a = word_search(doc_list, el)
        result[el] = a
    return result
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
multi_word_search(doc_list, keywords)