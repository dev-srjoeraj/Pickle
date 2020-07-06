# Pickle make it simple to write and read binary files much easier.
# Syntax
# To write / dump file :
# pickle.dump(content_to_be_dumped, file_in_which_to_be_dumped)

#fetch content / load content
# pickle.load(filename)



import pickle

imelda = ( 'More Mayhem',
           'Imelda May',
          '2011',
           ((1, "Pulling the Rug"),
           (2, "Psyco"),
            (3, "Mayhem"),
            (4, "Kentish Town Waltz")))

even = range(0,11,2)
odd = range(1,11,2)

with open("imelda.pickle" , "wb") as imelda_file:

    #dump contents to the file "imedla.pickle"
    pickle.dump(imelda, imelda_file)
    pickle.dump(even, imelda_file)
    pickle.dump(odd, imelda_file)
    pickle.dump(123, imelda_file)

with open ("imelda.pickle" , "rb") as imelda_file:

    #Assigning content of the imelda.pickle to variables
    #Make sure the sequence of dump and load are maintained if the content
    #is hetrogenous in nature
    imelda = pickle.load(imelda_file)
    even_list = pickle.load(imelda_file)
    odd_list = pickle.load(imelda_file)
    number = pickle.load(imelda_file)

artist , album , year , tracklist = imelda

print(artist)
print(album)
print(year)

for track in tracklist:
    tracknumber , trackname = track
    print("{0} : {1}".format(tracknumber, trackname))

print("-" * 20)


for i in even_list:
    print(i)

print("-" * 20)


for i in odd_list:
    print(i)


print("-" * 20)

print(number)


