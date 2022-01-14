import pickle
#unpickle file if exists otherwise start with empty dictionary
try:
    contacts = pickle.load( open( "contact_list", 'rb') )
except:
    contacts = {}
option = 0
while option != 'x':
    print('Choose an option:', '1:Look up email address', '2:add new contact','3:change email address','4:delete contact','x: exit program', sep="\n")
    option = input()
    #check which option was selected
    if option == '1':
        #only load if input is in contacts
        search = input('Search for contact: ')
        if search in contacts:
            print(contacts[search])
        else:
            print('contact not found')
    elif option == '2':
        #add new key value pair
        k = input('Contact name: ')
        v = input('Email: ')
        contacts[k] = v
    elif option == '3':
        #display current email and change
        search = input('Which contact? ')
        print('current email address: '+ contacts[search])
        new = input('new email address: ')
        contacts[search] = new
    elif option == '4':
        #delete by key
        search = input('Which contact? ')
        del contacts[search]
    elif option =='x':
        #exit
        print('Bye!')
    else:
        print('invalid option')
#write to file
file = open('contact_list', 'ab') 
pickle.dump(contacts, file)
file.close
input()
