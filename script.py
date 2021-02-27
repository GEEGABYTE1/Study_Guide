import time 
from os import system


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size 
        self.array = [None for i in range(self.array_size)]

    def hash(self, key, collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size 

    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return 

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]

        number_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                self.array[new_array_index] = [key, value]
                return 
            if new_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return 

            number_collisions += 1
        return 

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value == None:
            return 'That subject is not defined!'

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieve_collisions = 1
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieve_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                return 'That subject is not defined'

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieve_collisions += 1
        return 

    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        for i in self.array:
            if i[0] == key:
                self.array.remove(i)
                break
            else:
                continue

class Gameplay:
    def __init__(self, name):
        self.name = name
        prompt1 = input("This is your study guide. To help you memorize certain concepts, please type the amount of concepts you want to review!: ")
        hash_map = HashMap(int(prompt1))

        
        
        for i in range(int(prompt1)):
            prompt2 = input("Please enter a conept: ")
            prompt3 = input("Please enter it's response: ")

            hash_map.setter(str(prompt2), str(prompt3))
        
        print("Now you have set all your concepts, let us begin practicing!")
        time.sleep(1)
        clear = lambda: system('clear')
        clear()
        playing = True
        while len(hash_map.array) != 0:
            time.sleep(0.5)
            print(hash_map.array)
            prompt_subject = input("Please type in a concept: ")
            
            for i in hash_map.array:
                if prompt_subject == i[0]:
                    prompt_answer = input('Please type in your answer: ')
                    
                    correct_letters = [] 
                    count = 0
                    for i in hash_map.retrieve(prompt_subject):
                        correct_letters.append(i)

                    answer = []
                    for i in prompt_answer:
                        answer.append(i)
                    
                    results = zip(answer, correct_letters)

                    for i in list(results):
                        if i[0] == i[1]:
                            count += 1
                        else:
                            continue

                    
                    percentage = count / (len(correct_letters) - 1) * 100
                    if percentage > 65 and percentage < 75:
                        print("You have gotten it partially correct")
                        hash_map.delete(prompt_subject)
                        clear = lambda: system('clear')
                        clear()
                        break
                    elif percentage > 75 and percentage < 85:
                        print('You have got the main concept correct')
                        hash_map.delete(promp_subject)
                        clear = lambda: system('clear')
                        clear()
                        break
                    elif percentage > 85:
                        print('You have gotten the whole concept correct')
                        hash_map.delete(prompt_subject)
                        clear = lambda: system('clear')
                        clear()
                        break
                    else:
                        print("Looks like this is an incorrect answer, please try again")
                        clear = lambda: system('clear')
                        clear()

                
            
                else:
                    print("That concept is not defined or has been answered already!")
                    break
                
        print('You have completed your study guide?')
        playing_again = input("Would you like to practice again?")
        if playing_again == "yes" or playing_again == "Yes":
            print(prompt1)

        else:
            break   

            

gameplay = Gameplay("Jaival")


print(gameplay)
            
            

    