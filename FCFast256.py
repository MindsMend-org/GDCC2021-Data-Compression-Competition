# GDCC Data Compression Comp 2021 >>Entry 1 Fast256 Bit Reduction
# By Brett Palmer AKA MINCE


#  This Is One step up from Psudo Written For Readerbility

#  Will Optimize in Couple of days Just before Submition. 
#  Written With Only A few Weeks Python Knowledge.

# Notes to self:
# speedups 
#         1) Read all data at once.
#         2) Work on Data held in memory.
#         3) Write in big chunks.
#         4) Bit reduction of value 63 or higher is pointless as not saving any bits.
#         5) Once Data Is Reduced and compacted into 32 byte chunks Further Compress via pattern Match && >64 bit
#         6) Add Commandline Argv with help
#         7) Bugs >Maxsize  >Verbrose


# binary_poem = bytes(open("poem.txt").read(), encoding="utf-8")
# binary_poem[i] = 84


# import sys
import time
import numpy as np
# import argparse
import sys
import os


#Bugs List
#Bug one if file already exists it adds onto rather than write over.


#  File Chk Prefix
#  M_FC_FST256_V1
#  except EOFError:

from array import array

#bin_array = array("B")
#bits = "10111111111111111011110"

#bits = bits + "0" * (32 - len(bits))  # Align bits to 32, i.e. add "0" to tail
#for index in range(0, 32, 8):
#    byte = bits[index:index + 8][::-1]
#    bin_array.append(int(byte, 2))

#with open("test.bnr", "wb") as f:
#    f.write(bytes(bin_array))

#  firstline = f.readline().rstrip()

def WelcombeMessage(MESS):
    print(f'FOLDING CIRCLES , {MESS}')

def ClearFile(Fname):
    f = open(Fname, 'w')
    f.close()


#string = "aAzZ09" #!£$%^&*"

# string with encoding 'utf-8'
#arr = bytes(string, 'utf-8')
#arr2 = bytes(string, 'ascii')

#print(arr, '\n')

# actual bytes in the the string
#for byte in arr:
#   print(byte, end=' ')
#print("\n")
#for byte in arr2:
#    print(byte, end=' ')

print('')







# Args Verbrose 0 Quiet / 1 Info
Verbrose = 1
Lowmemmode = 1

Mode = 0
ArgsFile = ""

# Set Key Size to 1byte
KeySize = 256  # =256

#StartTime = time.time()
if __name__ == '__main__':
    WelcombeMessage('GDCC Data Compression Fast Compression By Brett Palmer.')

    Question = ""
    Question = input("Do You Want To Compress ? (y/n)?: ")

    if Question == "Y" or Question == "y":
        print("Compression Mode Active ref.FC_FST256")
        Question = ""
        print('Test File From GDCC 2021 Test1 = test1_demo.')
        Question = input('Enter File Name')
        if os.path.isfile(Question) != True:
            print('File Not Found Exiting.')
            exit()
        Mode = 1
        ArgsFile = Question
    else:  # Decompression Mode?
        print('Decompression Under Construction.')
        ArgsFile = 'FCOutPut.M256'  # Will Be Args[1] o Direct Imput
        if Verbrose == 1:
            print("Decompression Mode Active...ref..FC_M256")
            print("File is ", ArgsFile)
            if os.path.isfile(ArgsFile) != True:
                print('File Not Found-', ArgsFile, ' Exiting.')
            else:
                ArgsFile = "FCOutPut.M256"  # Decompression File
                if os.path.isfile(ArgsFile) != True:
                    print('File Not Found ', ArgsFile)

                else:
                    ArgsFile = "FCOutPut.M256"  # Default Decompression File
                    #open(ArgsFile, 'a')
                    exit()

        Mode = 2
        ArgsFile = "FCOutPut.M256"  # B-Force to use 1 File Due to DiskSpace

    if Verbrose != 0:
        print("This is the name of the script: ", sys.argv[0])
        print("Number of arguments: ", len(sys.argv))
        print("The arguments are: ", str(sys.argv))

    if Verbrose == 1:
        print('KeyScore>>in Bits.')
        for i in range(KeySize):
            binary_string = '{:0b}'.format(i)
            print(i, ' = ', binary_string)

    if Verbrose == 0:
        print('Running In Silent Mode.')

    #  Note Worthy Values
    NoteWorthy = []

    #  Compression Verbrose
    Update_Rate = 500  # ns
    MaxRep = 100000

    #  Set Read Size
    Read_Size = 1

    #  Make array for keys
    Keys = [0 for i in range(KeySize)]
    if Verbrose == 1:
        print(Keys)

    #  Set Key STD Values
    for i in range(KeySize):
        Keys[i] = i
    if Verbrose == 1:
        print(Keys)

    #  Make array for Score
    Score = np.arange(KeySize)  # [0 for i in range(KeySize)]

    #  Make WriteKey_FromID of Score
    WriteKey = np.arange(KeySize)

    #  Make array for Data For High Mem use ver..
    Data_Byte_Array = [] #  bytearray(b'')  # bytearray('', encoding='ascii')

    print('')
    print('Start the clock..')
    StartTime = time.time()

    if Mode == 1:  # Compress Mode Verbrose 1 and 0
        Read_Size = 1 #To be sure
        if Verbrose == 1:
            #  Read File Data in Bytes And Score
            if os.path.isfile(ArgsFile) != True:
                print('File Not Found ', ArgsFile)
                exit()
            with open(ArgsFile, 'rb') as f:
                byte = f.read(Read_Size)  # read header here!
                #f.seek(0) #To Adjust Read offset after read try  back to start..
                while byte:
                    # Do stuff with byte.
                    byte = f.read(Read_Size)
                    try:
                        index = ord(byte)
                    except:
                        print('End Of Data Stream.')
                    pass
                    #  print (index)
                    #nums = [ord(index) for index in '']
                    #if Verbrose:
                        #print(index)
                    #Data_Byte_Array.append(ord(x) for x in index)  # Store file Data saves ReReading file
                    if not Lowmemmode:
                        Data_Byte_Array.append(index) #  yeah it works!
                    if index:
                        Score[index] += 1

                    if Score[index] > MaxRep:  # NoteWorthy.
                        if index not in NoteWorthy:  # NoteWorthy.
                            NoteWorthy.append(index)
                            #  NoteWorthy.
                            binary_string = '{0:08b}'.format(index)
                            #  print(binary_string)
                            print(index, ' = Score ', Score[index], " = bin ", binary_string)
                            #  MaxRep += MaxRep / 8
        else:  # Silent Mode Verbrose !=1 For Speed Have two seprate versions reduce time by no if statements.
            # Read File Data in Bytes And Score Rep (Multiply By Bit Length To be optimal Convergence)
            with open(ArgsFile, "rb") as f:
                byte = f.read(Read_Size)
                while byte:
                    # Do stuff with byte.
                    byte = f.read(Read_Size)
                    try:
                        index = ord(byte)
                    except:
                        print('End Of Data Stream.')
                    pass
                    # print (index)
                    if index:
                        Score[index] += 1 #  Add Score
                        # if Score[index] > MaxRep:
                        # if index not in NoteWorthy:  # NoteWorthy.
                        # NoteWorthy.append(index)
                        # NoteWorthy.
                        # binary_string = '{0:08b}'.format(index)
                        # print(binary_string)
                        # print(index, '=', Score[index], "=", binary_string)
                        # MaxRep += MaxRep / 8
        if Verbrose:
            print('Verbrose Mode.')
            print('Score Data After Conversion....')
            print(Score)
    #  -------------------------------------------------------------------------------------------------------------------
    #so messy we have rdundents like poss list
        #Score
        #WriteKey
        #NoteWorthy
        #ScoreKeylist = []
        #OrderedScoreKeyMap = np.arange(KeySize)
        #Data_Byte_Array
    #  -------------------------------------------------------------------------------------------------------------------
    #if Mode == 1:  # 1 = Compression   ---bug this is obviosely mode 1!
        print('Make Remap.')

        if Lowmemmode:
            #  GenScoreKeyMap
            # Make array for Score
            OrderedScoreKeyMap = np.arange(KeySize)  # [0 for i in range(KeySize)]
            HS = -1  # 0=0 so set -1 to start
            ID = 0
            ScoreKeylist = []  # Make A List of All Keys(Keysize) #!!!! Fix make this list direct in order from score values
            TargetKeySwaps = KeySize
            KeySwaps = 0
            for i in range(0, KeySize):
                #  Sort KeyMap Remove From ScoreKeyList (((first 63))) =bits-1
                ScoreKeylist.append(i)  # Create A Container For KeyFromScore.
                #ScoreKeylist[i] = -1  # Set To Negative one before Score to ID Done.
                #while KeySwaps and i < TargetKeySwaps:
                for iu in range(KeySize):
                    if Score[iu] >= HS:
                        HS = Score[iu]
                        ID = iu
                        if Verbrose == 2:
                            print('KeySwap Count ', KeySwaps, 'New Key Info..Ammend at Loop ', i, '    KEY ', iu, ' ', ScoreKeylist[i]), '= ID'  # [%d%%\r%i, end=""])
                    # ScoreKeylist[i] #Just do once at end of  loop

                KeySwaps += 1
                ScoreKeylist[i] = ID #  = 1 = 255 2 = 43 ect
                Score[ID] = -1  # Block from Check.
                HS = -1         # Reset Loop HighScore
                ID = 0          # Reset Loop Score Index

                if Verbrose:
                    print('')
                    print('List Size:=', KeySize)
                    print('Key Size =', len(ScoreKeylist))
                    print('')

                if KeySize == KeySwaps:
                    print('Looking Good... KeyLength || KeySwaps || KeySize All Match.')

                #  print(ScoreKeylist[KeySize])
                #  ScoreKeylist[KeySize-i].delete(arr,) #Revers Bits
                #  np.delete(ScoreKeylist, ID)
                #  print('List:=', ScoreKeylist[KeySize-i])

            #  Create Ordermap
            for i in range(KeySize):
                OrderedScoreKeyMap[i] = ScoreKeylist[i]
                if Verbrose:
                    print(OrderedScoreKeyMap[i])


            if Verbrose == 1:
                print('Remap Created.')
                print('ScoreKeyList=')
                print(ScoreKeylist)
                print('OrderedScoreKeyMap=')
                print(OrderedScoreKeyMap)
            #  Done.

            #  Compress Convert Stage!
            #  Read Or Use Data_array?
            if Verbrose == 3:
                print(Data_Byte_Array)  # Data_Byte_Array


            #Write File!
            # Write De-Compressor Key
            # foo = ''.join(foo.split()) # remove white spaces
            cf = ArgsFile[:-3]
            Compressed_ArgsFile_Name = cf + ".M256"

            if Verbrose == 1:
                print('File Out Name =', Compressed_ArgsFile_Name)

            # Write Header & Decompress Key(ScoreKeylist)
            #print('Writing File Header.')
            #print("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)

            #Clear Contents of Mapfile if exista.
            ClearFile(Compressed_ArgsFile_Name)
            FcM256 = open(Compressed_ArgsFile_Name, 'a')  #Mapfile
            #FcM256.writelines("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)
            #for FC_Header_Key_str in ScoreKeylist:
            #FcM256.write(ScoreKeylist[FC_Header_Key_str])
            # file.writelines("%s\n" % item for item in list)


            #Low Mem Mode uses old File rather than a stored version.
            #  Write Through>KeyMp>Conversion Table
            print('Slow Low Mem Use Mode & MAx Compression.')
            print()
            print('Read....', ArgsFile)
            print('Map.....', FcM256)
            print('Zip.....=.Z256')
            print('Writing Map File.')
            FcM256 = open(Compressed_ArgsFile_Name, 'a')  # Out Text
            #FcM256 = open(Compressed_ArgsFile_Name, 'ab')  # Out>File>Binary.
            with open(ArgsFile, "rb") as f: #  In>file
                byte = f.read(Read_Size)  # speedup use size off key as Read_Size = KeySize
                while byte:
                   # byte = f.read(Read_Size) #put at bottum no need to re-seek file start
                    try:
                        index = ord(byte)
                    except:
                        print('End Of Data Stream.')
                    pass
                    #  while byte != b"":
                    #  print (index)
                    #  FcM256 = open('FCOutPut.M256', 'a')
                    #FcM256 = open(Compressed_ArgsFile_Name, 'ab') #  Out>File.
                    for findmap in range(KeySize):  # findmap is the value needed
                        if OrderedScoreKeyMap[findmap] == index:
                            #MapFound
                            _Bytemap = OrderedScoreKeyMap[index]  # OrderedScoreKeyMap[i]
                            break

                        if Verbrose > 2:
                            print(findmap)

                    if Verbrose == 2: #1 ----------
                        #Mybitlength = _Bytemap.bit_length()
                        #OrigBitLength = byte.bit_legth()
                        #print('My=', Mybitlength)
                        ##print('Orig=', OrigBitLength)
                        print('File(int) =', index, 'Remap =', findmap, '=Mem(byte)=', byte, '=(Original)mapped ver=', _Bytemap,'=chr(', chr(_Bytemap), 2)

                    FcM256.write(str(findmap))
                    #file.seek(fil.tell()-1) -rewind 1 place
                    #FcM256.write(_Bytemap)  # Written In Max << Min(SIZE) Bit Order
                    #FcM256.write(bytes(findmap))  #[:-1] Written In Max << Min(SIZE) Bit Order
                    #FcM256.write(str(findmap)+',')
                    #FcM256.write(bytes(byte))
                    #FcM256.write(byte)
                    #FcM256.write(OrderedScoreKeyMap[255-byte])  # reverse 255-byte



                    #FcM256.close()
                    #  --Continue Write Re-Map---
                    byte = f.read(Read_Size)  # Next read! at end!!
            #  Done With open files(end of with)
            FcM256.close()

            #ArgsFile.close()

            print('Bit reduction MapFile Wrote.')

            #-------------------------------------------------------------

            Chunk = 32  #Block Of Maped Bits.
            MaxBits = 0

            OrigSize = 0
            MappedSize = 0

            print('Converting Binary data.')
            Compressed_Bin_ArgsFile_Name = cf + '.B256'

            #Clear file Contents if exist.
            ClearFile(Compressed_Bin_ArgsFile_Name)
            FcB256 = open(Compressed_Bin_ArgsFile_Name, 'a')

            print('Writing Zip File Header.')
            print("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)
            FcB256.writelines('GDCC_Entry_2021_By_Brett Palmer.')
            FcB256.writelines("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)
            # for FC_Header_Key_str in ScoreKeylist:

            print('')
            print('Header Wrote.')
            Zip_seek = FcB256.tell()

            FcB256.close()

            print('Reading Map File,*(', Compressed_ArgsFile_Name, ') & Building Zip*', Compressed_Bin_ArgsFile_Name)


            #Re-Open Bin File in Binary Mode
            FcB256 = open(Compressed_Bin_ArgsFile_Name, 'ab')
            #Move Past Header
            FcB256.seek(Zip_seek)

            #FcM256 = open(Compressed_ArgsFile_Name, 'r')  # Mapfile In>
            with open(Compressed_ArgsFile_Name, "r") as f:  # In>file>MAP
                String_byte = f.read(Read_Size)  # speedup use size off key as Read_Size = KeySize
                while String_byte:
                    # byte = f.read(Read_Size) #put at bottom no need to re-seek file start
                    try:
                        MapValue = int(String_byte)
                    except:
                        print('End Of Map Data.?')
                    pass
                    if Verbrose == 3:
                        print(MapValue)
                        print(MapValue.bit_length())

                    MappedSize += MapValue.bit_length()
                    OrigSize += 8
                    String_byte = f.read(Read_Size)  #Read More
                # End Of Compression! GDCC 3 days to go !!

            #Results
            print('\nResults:')
            added = (OrigSize / 8) / 10
            print('Origanal size =', OrigSize/1024)
            print('Mapped Size   = ', MappedSize/1024)
            print('Added         =  ', added/1024)


            print('Saving ', (OrigSize - (MappedSize + added))/1024, ' Bytes(ish)  Ratio of ', OrigSize / (MappedSize + added) * 100, '%')

            print('Writing Bin FCZipped!')
            FcB256.close()
            print('Complete....')




        else:  # Decompress .M256 File >>>>> Mode !=1
            print('Decompression Of M256 File.')
            #  Chk file exists
            #  read Header
            #  read KeyMap for Read function Real = KeyMap(read(byte))
            #  writefnc(KeyMap(Ral))
            print('File Decompressed')
            print('Header Will Contain Original File Name.')

#if mode==2 = Decompres file enter name of file/read header key/ convert

EndTime = time.time()


#  Show Running Time
print('Time Taken =', EndTime - StartTime)

input("Foundeations All Done(Map To Binary & Decompress To Be finished 48 hours to go..:<) Press Enter to continue...")
