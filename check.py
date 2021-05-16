                               
import phonenumbers



print ("""
                             /^\/^\
                             \----|
                         _---'---~~~~-_
                          ~~~|~~L~|~~~~
                             (/_  /~~--
                           \~ \  /  /~
                         __~\  ~ /   ~~----,
                         \    | |       /  \
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \\---'
                      //_- |  |          \
                     //   |____|\______\__\
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\            """)
                           

print("programmer:yahya")
print("instagram:iq4.p") 


number = input("enter your number:")
sym = input("enter number country symbol:")


check = phonenumbers.parse(f'{number}', f'{sym}')


print("is the number vaild?:")
print(phonenumbers.is_valid_number(check))

                                                                    
                                                                                                                                                                  