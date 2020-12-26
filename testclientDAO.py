from clientDao import clientDao

client = {
    
    'Names': 'John',
    'Surname': 'Kennedy',
    'Price': 60,

}
client2 = {
    'ClientID': 2,
    'Names': 'Mary',
    'Surname': 'Smith',
    'Price': 60,

}
client3 = {
    'ClientID': 3,
    'Names': 'Louise',
    'Surname': 'See',
    'Price': 60,

}
client8 = {
    'Names': 'Lineo',
    'Surname': 'Seed',
    'Price': 60,

}

client7 = {
    'Names': 'Lorene',
    'Surname': 'Bernard',
    'Price': 200,
}


#returnValue = clientDao.create(client)
#print(returnValue)

#latestid = clientDao.create(client7)
returnValue = clientDao.findById(2)
print("find By Id")
print(returnValue)


#returnValue = clientDao.getAll()
#print(returnValue)

#returnValue = clientDao.findById(client2['ClientID'])
#print("find By Id")
#print(returnValue)

#returnValue = clientDao.update(client3)
#print(returnValue)


#returnValue = clientDao.findById(client2['ClientID'])
#print(returnValue)

#returnValue = clientDao.delete(client6['ClientID'])
#print(returnValue)

#returnValue = clientDao.getAll()
#print(returnValue)


