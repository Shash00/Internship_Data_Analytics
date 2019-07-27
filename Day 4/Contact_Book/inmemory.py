from contact import Contact
from beautifultable import BeautifulTable


class InMemoryImpl:
    contact_list = []

    @classmethod
    def addContact(cls):
        name = input('Enter Name:')
        email = input('Enter Email:')
        mobile = input('Enter Mobile:')
        address = input('Enter Address:')
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"Contact is added successfully with name:{name}")
    
    @classmethod
    def deleteContact(cls):
        name = input('Enter name to delete:')
        c = cls.get_contact_by_name(name)
        if c:
            cls.contact_list.remove(c)
            print('Contact deleted successfully')
            InMemoryImpl._paint(cls.contact_list)
        
        else:
            print('No record found')


    @classmethod
    def viewContacts(cls):
        InMemoryImpl._paint(cls.contact_list)
    
    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0:
            key = input('Enter name to search:')
            s_list = list(filter(lambda x: key.lower() in x.get__name().lower(), cls.contact_list ))
            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print('Search failed')
        else:
            print('No contacts')

    @classmethod
    def updateContact(cls):
        if len(cls.contact_list) > 0:
            name1 = input('Enter name to update:')
            contact = cls.get_contact_by_name(name1)
            if contact:
                print('1.Name 2.Email 3.Mobile 4.Address')
                ch = int(input('Enter choice:'))
                if ch == 1:
                    print(f'Old name:{contact.get__name()}')
                    name = input('Enter name to update:')
                    if name:
                        contact.set__name(name)
                        InMemoryImpl._paint(cls.contact_list)

                elif ch == 2:
                    print(f"Old email:{contact.get__email()}")
                    email = input('Enter email to update')
                    if email:
                        contact.set__email(email)
                        InMemoryImpl._paint(cls.contact_list)
                    
                elif ch == 3:
                    print(f"Old mobile:{contact.get__mobile()}")
                    mobile = input('Enter mobile to update')
                    if mobile:
                        contact.set__mobile(mobile)
                        InMemoryImpl._paint(cls.contact_list)
                
                elif ch == 4:
                    print(f"Old address:{contact.get__address()}")
                    address = input('Enter address to update')
                    if address:
                        contact.set__addresss(address)
                        InMemoryImpl._paint(cls.contact_list)

        else:
            print('No contacts to update')
    
    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ['Name', 'Email', 'Mobile', 'Address']
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print("Contact book is empty")

    @classmethod
    def get_contact_by_name(cls, name):
        if len(cls.contact_list) > 0:
            c = list(filter(lambda x: x.get__name().lower() == name.lower(), cls.contact_list))
            
            return c[0] if c else None

    