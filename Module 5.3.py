from faker import Faker
faker = Faker()

Person1 = {
    "first_name":faker.first_name(),
    "last_name":faker.last_name(),
    "job":faker.job(),
    "company_name":faker.word(),
    "phone_number":faker.phone_number(),
    "work_number":faker.phone_number(),
    "email":faker.email()
}
Person2 = {
    "first_name":faker.first_name(),
    "last_name":faker.last_name(),
    "job":faker.job(),
    "company_name":faker.word(),
    "phone_number":faker.phone_number(),
    "work_number":faker.phone_number(),
    "email":faker.email()
}
Person3 = {
    "first_name":faker.first_name(),
    "last_name":faker.last_name(),
    "job":faker.job(),
    "company_name":faker.word(),
    "phone_number":faker.phone_number(),
    "work_number":faker.phone_number(),
    "email":faker.email()
}
Person4 = {
    "first_name":faker.first_name(),
    "last_name":faker.last_name(),
    "job":faker.job(),
    "company_name":faker.word(),
    "phone_number":faker.phone_number(),
    "work_number":faker.phone_number(),
    "email":faker.email()
}
Person5 = {
    "first_name":faker.first_name(),
    "last_name":faker.last_name(),
    "job":faker.job(),
    "company_name":faker.word(),
    "phone_number":faker.phone_number(),
    "work_number":faker.phone_number(),
    "email":faker.email()
}

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone_number = phone_number
       self.email = email

       self.label_length = len(self.first_name)+len(self.last_name)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'

class BusinessContact(BaseContact):
    def __init__(self, job, company_name, work_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.job = job
       self.company_name = company_name
       self.work_number = work_number

    def contact(self):
        return f'Wybieram numer {self.work_number} i dzwonię do {self.first_name} {self.last_name}'


P1P = BaseContact(first_name=Person1.get("first_name"), last_name=Person1.get("last_name"), phone_number=Person1.get("phone_number"), email=Person1.get("email"))
P2P = BaseContact(first_name=Person2.get("first_name"), last_name=Person2.get("last_name"), phone_number=Person2.get("phone_number"), email=Person2.get("email"))
P3P = BaseContact(first_name=Person3.get("first_name"), last_name=Person3.get("last_name"), phone_number=Person3.get("phone_number"), email=Person3.get("email"))
P4P = BaseContact(first_name=Person4.get("first_name"), last_name=Person4.get("last_name"), phone_number=Person4.get("phone_number"), email=Person4.get("email"))
P5P = BaseContact(first_name=Person5.get("first_name"), last_name=Person5.get("last_name"), phone_number=Person5.get("phone_number"), email=Person5.get("email"))

P1W = BusinessContact(first_name=Person1.get("first_name"), last_name=Person1.get("last_name"), phone_number=Person1.get("phone_number"), email=Person1.get("email"), job=Person1.get("job"), company_name=Person1.get("company_name"), work_number=Person1.get("work_number"))
P2W = BusinessContact(first_name=Person2.get("first_name"), last_name=Person2.get("last_name"), phone_number=Person2.get("phone_number"), email=Person2.get("email"), job=Person2.get("job"), company_name=Person2.get("company_name"), work_number=Person2.get("work_number"))
P3W = BusinessContact(first_name=Person3.get("first_name"), last_name=Person3.get("last_name"), phone_number=Person3.get("phone_number"), email=Person3.get("email"), job=Person3.get("job"), company_name=Person3.get("company_name"), work_number=Person3.get("work_number"))
P4W = BusinessContact(first_name=Person4.get("first_name"), last_name=Person4.get("last_name"), phone_number=Person4.get("phone_number"), email=Person4.get("email"), job=Person4.get("job"), company_name=Person4.get("company_name"), work_number=Person4.get("work_number"))
P5W = BusinessContact(first_name=Person5.get("first_name"), last_name=Person5.get("last_name"), phone_number=Person5.get("phone_number"), email=Person5.get("email"), job=Person5.get("job"), company_name=Person5.get("company_name"), work_number=Person5.get("work_number"))

y=[]
def create_contacts(type, quantity):
    if type == "base":
        for i in range(0,int(quantity)):
            x=BaseContact(first_name=faker.first_name(), last_name=faker.last_name(), phone_number=faker.phone_number(), email=faker.email())
            y.append(str(x))
    elif type == "business":
        for i in range(0,int(quantity)):
            x=BusinessContact(first_name=faker.first_name(), last_name=faker.last_name(), phone_number=faker.phone_number(), email=faker.email(), job=faker.job(), company_name=faker.word(), work_number=faker.phone_number())
            y.append(str(x))
    else: 
        print("invalid type of contact")


wizytówki = (P1P, P2P, P3P, P4P, P5P)

create_contacts("business", 3)
print(y)