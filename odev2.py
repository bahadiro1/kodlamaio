
students=[]

#listeye öğrenci ekleme

def addStudent():
    name_surname=input("Eklemek istediğiniz öğrencinin adı ve soyadı : ")
    students.append(name_surname)
    print(f"{name_surname} eklendi.")

addStudent()    

#listeden öğrenci silme

def deleteStudent():
    name_surname=input("Silmek istedğiniz öğrencicin adı ve soyadı : ")
    students.remove(name_surname)
    print(f"{name_surname} silindi.")

deleteStudent()    
   

#listeye birden fazla öğrenci ekleme

def addMultipleStudent():
    numberOfStudents = int(input("Kaç öğrenci ekleyeceksiniz? "))
    newStudents = []
    for i in range(numberOfStudents):
        name_surname=input(f"{i+1}. Öğrencinin adını ve soyadını giriniz : ")
        newStudents.append(f"{name_surname}")
    students.extend(newStudents)    
    print(f"{numberOfStudents} öğrenci listeye eklendi.")

addMultipleStudent()    

#listedeki öğrencileri tek tek yazdırma

def listOfStudents():
    for name_surname in students:
        print(name_surname)    
        
listOfStudents()   

#index no = öğrenci no

def studentNumber():
    name_surname=input("Öğrencinin adı ve soyadını giriniz : ")
    if name_surname in students:
        number=students.index(name_surname)
        print(f"{name_surname} öğrencisinin numarası : ")
    else:
        print("Listede böyle bir öğrenci yok")    

studentNumber()        

#döngü kullanarak listeden birden fazla öğrenci silme

ogrencisayisi=input("Kaç öğrenci silmek istiyorsunuz ? : ")

i=0


while i<int(ogrencisayisi):
    students.remove(students[i])
    i+=1

print(students)    


    
