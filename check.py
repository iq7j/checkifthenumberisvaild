                               
import phonenumbers



print ("""    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'


                   """)
                           

print("programmer:yahya")
print("instagram:iq4.p") 


number = input("enter your number:")
sym = input("enter number country symbol:")


check = phonenumbers.parse(f'{number}', f'{sym}')


print("is the number vaild?:")
print(phonenumbers.is_valid_number(check))

                                                                    
                                                                                                                                                                  