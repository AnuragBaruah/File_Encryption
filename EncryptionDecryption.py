#imports
from base64 import b64encode, b64decode
from random import randint
from os import system

#Function for encryption
def Encrypt(content, extension):
    while True:
        sp=randint(-20,20)
        r=randint(-20,20)
        if sp*r!=0 and sp!=r:
            break
        
    va = 2*randint(13, 50)
    vd = 2*randint(1, 6)
    
    ca = 2*randint(13, 50) + 1
    cd = 2*randint(1,6)

    copy = content.lower()
    encrypt = []
    for f in range(len(copy)):
        i = copy[f]
        if not i.isalnum():
            p = '?' + str(sp + ord(i))
        else:
            let = chr(randint(97, 97+25))
            if i.isdigit():
                p = let.upper() + str(int(i) + r)
            else:
                if i in 'aeiou':
                    p = str(va + vd*(ord(i) - 96 - 1))
                    if content[f].isupper():
                        p = let + p
                else:
                    p = str(ca + cd*(ord(i) - 96 - 1))
                    if content[f].isupper():
                        p = let + p
        encrypt.append(p)
    encrypt = '.'.join(encrypt)
        
    rawInfo = '{} {} {} {} {} {}'.format(sp, r, va, vd, ca, cd) + " " + extension + " "
    info = ''
    for j in rawInfo:
        info += chr(ord(j) - 5)

    final = info + '_sep_' + encrypt
    return final

#Function for decryption
def Decrypt(content):
    try:
        info, encrypt=content.split('_sep_')    
        rawInfo=[]
        x=''
        for i in info:
            if i!=chr(27):
                x+=chr(ord(i)+5)
            else:
                rawInfo.append(x)
                x=''
                
        sp,r,va,vd,ca,cd,ext=rawInfo
        sp,r,va,vd,ca,cd=int(sp),int(r),int(va),int(vd),int(ca),int(cd)
        contentList=encrypt.split('.')
        decrypt=[]
        for i in contentList:
            if i[0]=='?':
                a=int(i[1:])
                p=chr(a-sp)
            else:
                if i[0].isupper():
                    a=int(i[1:])
                    p=str(a-r)
                else:
                    if i[0].isalpha():
                        a=int(i[1:])
                        if a%2==0:
                            p=chr(((a-va)//vd)+97).upper()
                        else:
                            p=chr(((a-ca)//cd)+97).upper()
                    else:
                        a=int(i)
                        if a%2==0:
                            p=chr(((a-va)//vd)+97)
                        else:
                            p=chr(((a-ca)//cd)+97)
        
            decrypt.append(p)
        decrypt = ''.join(decrypt)
        extension='.'+ext
    except:
        decrypt = '#'
        extension = '#'
        print('\nEXCEPTION: The file is corrupted. Cannot decrypt\n')
    return decrypt, extension

#Function for taking necessary input from user
def Input():
    pathinput='''\nPlease enter the path of the file with the extension and use'\\\\' instead of '\\'
Example:-
C:\\\\Users\\\\Home\\\\Desktop\\\\Hello World.txt'''
    cmdinput='''\nPlease enter whether you want to encrypt(enter e) or decrypt(enter d) the file'''

    q = True
    while q:
        a = True
        b = True
        while a:
            try:
                print(pathinput)
                path = input()
                path.strip()
                f = open(path, 'r')
                f.close()
                print('File Located')

                #Finding the file type once file is located
                i = -1
                ext = ''
                while 1:
                    if path[i] == '.':
                        break
                    else:
                        ext += path[i]
                        i -= 1
                ext = ext[::-1]
                a = False
            except:
                print('ERROR: Invalid Path!\nTry Again')
                
        while b:
            print(cmdinput)
            cmd = input()
            cmd.strip().lower()
            if cmd in 'ed':
                b = False
                print('Command Detected')
                if cmd=='e':
                    print('\nPlease wait...')
                    print('Your file is being encrypted')
                    q = False
                elif ext != 'txt':
                    print('\nERROR: Command and File Type Mismatch!\nOnly the files encrypted by this program can be decrypted.\n\
An encrypted file with extension \'.txt\' was expected.\nGot a file with extension \'.{}\''.format(ext))
                else:
                    print('\nPlease wait...')
                    print('Your file is being decrypted')
                    q = False
            else:
                print('ERROR: Command was not detected')
                cmdinput = 'Only "e" or "d" expected\nPlease enter again'
    return path, cmd, ext

#Function for creating New File (encrypted or decrypted)
def CreateFile(Path, fileExtension, oldExt, task):
    L = list(Path.rstrip(oldExt))
    L.reverse()
    d = ''
    d2 = ''
    for i in L:
        d += i
        if i == " ":
            break
    d = list(d)
    d.reverse()
    for i in d:
        d2 += i
    if not ('DECRYPTED' in d2 or 'ENCRYPTED' in d2):
        d2 = ''
    if task == 'ENCRYPTED':
        d2 = ''
    nPath = Path.rstrip(d2 + oldExt) + ' ' + task
    try:
        f = open(nPath+fileExtension, 'r')
        f.close()
        c = True
    except:
        newPath = nPath+fileExtension
        c = False
    x = 0
    while c:
        x += 1
        try:
            newPath = nPath + '(' + str(x) + ')' + fileExtension
            f = open(newPath)
            f.close()
        except:
            c = False
    return newPath
            


#MAIN CODE STARTS:
while True:
    system('cls')
    #starting message
    print("\nEncryption Decryption Program")

    #input from the user:
    path, cmd, ext = Input()

    #getting the file content in strings form
    if ext == 'txt':
        file = open(path, 'r')
        data = file.read()
        file.close()
    else:
        file = open(path, 'rb')
        data = b64encode(file.read())
        data = str(data)
        data = data.lstrip("b'").rstrip("'")
        file.close()

    #Encryption
    if cmd == 'e':
        encryptedData = Encrypt(data, ext)                                 
        newPath = CreateFile(path, '.txt', '.'+ext, 'ENCRYPTED')
        newFile = open(newPath, 'w')                                          
        newFile.write(encryptedData)                                         
        print('\nEncrypted file formed.\n\nPath of encrypted file is::')
        print(newPath)
        newFile.close()

    #Decryption
    else:
        decryptedData, fileExtension = Decrypt(data)
        if not decryptedData == fileExtension == '#':
            newPath = CreateFile(path, fileExtension, '.txt', 'DECRYPTED')
            if fileExtension == '.txt':
                newFile = open(newPath, 'w')
                newFile.write(decryptedData)
            else:
                newFile = open(newPath, 'wb')
                newFile.write(b64decode(decryptedData))                                         
            newFile.close()
            print('\nDecrypted file formed.\n\nPath of decrypted file is::')
            print(newPath)
        else:
            print('Program Terminated due to exception')

    #Continue Encrypting/Decrypting
    if input('Press enter to continue\nenter \'x\' to exit program\n') in ['x', 'X']:
        break
