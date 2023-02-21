# thisslices the email into a particular username domain/extension
# steps
# collect email from user
# split the email using the @, the first part as the user name, the second part is the domain
# split the domain using the .

def mailslicer():

    email_input = input('Enter your email address: ')

# Storing the two parts in descriptive variables
    (username, domain) = email_input.split("@")

# splitting the domain and storing it in two descriptive variables
    (domain, extension) = domain.split('.')

# output
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
# for the user to coninuosly do this or even quit
while True:
    print('What would you like to do?')
    print('')
    print("A. Email slicer")
    print("B. Exit")

    print('')
    choice = input("Enter your choice: ")
    print('')

    if choice=='a' or choice == 'A':
        print('Welcome to the email slicer')
        mailslicer()
        print("")

    elif choice=='b' or choice == 'B':
        quit()
