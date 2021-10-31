#  GDCC Comp 2021 By Brett Palmer
#  Written With Only A few Weeks Python Knowledge.

#'line 430 480 verbose >1 write Mapfile ,csd

#688-write zip errors int?str?
__author__ = "Brett Palmer"
__license__ = "Mince @ FoldingCircles(C)2021-2030)"
__version__ = "1.0090"
__status__ = "Development Pre Alpha"
__email__ = "mindsmend@gmail.com/brettpalmerakamince@hotmail.com"
__url__ = "https://github.com/MindsMend-org"

#from bitstream import BitStream
import math

from bitarray import bitarray
from bitstring import BitArray
import io
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
import sys


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

def print_at(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def WelcombeMessage(MESS):
    print(f'             FOLDING CIRCLES                 2021                Brett Palmer\n\n  {MESS}')

def ClearFile(Fname):
    f = open(Fname, 'w')
    f.close()

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


print('')



# Args Verbrose 0 = Quiet / 1 = Info
Verbose = 1
Lowmemmode = 0
Ratio = 100
Mode = 0
ArgsFile = ""

# Set Key Size to 1byte
KeySize = 256  # =256

#StartTime = time.time()
if __name__ == '__main__':
    WelcombeMessage('                            GDCC Global Data Compression Comp.\n\n '
                    'Entry (1).........................256 Mapped Bit Compression.\n')
    print('GUI Mode No Arguments; FCzip -h for help.')
    print('')

    #Question = ""
    Question = input("Do You Want To Compress ? (y/n)?: ")

    if Question == "Y" or Question == "y":
        print("Compression Mode Active ref.FC_FST256")
        Question = ""
        print('Test File From GDCC 2021 Test1 = test1_demo.')
        Question = input('Enter File Name ')
        if os.path.isfile(Question) != True:
            print('File Not Found Exiting.')
            exit()
        Mode = 1
        ArgsFile = Question
    else:  # Decompression Mode?
        print('Decompression Under Construction.')
        ArgsFile = 'FCOutPut.M256'  # Will Be Args[1] o Direct Imput
        if Verbose == 1:
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

    if Verbose != 0:
        print("This is the name of the script: ", sys.argv[0])
        print("Number of arguments: ", len(sys.argv))
        print("The arguments are: ", str(sys.argv))


    #Create bin representation strings
    MaskBitReducedString = []
    print('Build Mask(KeyScore>>in Bits).')
    for i in range(KeySize):
        binary_string = '{:0b}'.format(i)
        MaskBitReducedString.append(binary_string)

        # Show InnerWorkings Build Mask List.
        if Verbose > 1:
            print(i, ' = ', binary_string)

    # Show Bit Mask List.
    if Verbose > 0:
        print(MaskBitReducedString)
        print(MaskBitReducedString[0], '-', MaskBitReducedString[i])

    if Verbose == 0:
        print('Running In Silent Mode.')

    #  Note Worthy Values
    NoteWorthy = []

    #  Compression Verbrose
    Update_Rate = 500  # ns
    MaxRep = 100000

    #  Set Read Size
    Read_Size = 1  # 1024

    #  Make array for keys
    Keys = [0 for i in range(KeySize)]
    if Verbose > 0:
        print(Keys)

    #  Set Key STD Values
    for i in range(KeySize):
        Keys[i] = i
    if Verbose > 0:
        print(Keys)

    #  Make array for Score
    Score = np.arange(KeySize)  # [0 for i in range(KeySize)]

    #  Make WriteKey_FromID of Score
    WriteKey = np.arange(KeySize)

    #  Make array for Data For High Mem use ver..
    Data_Byte_Array = bytearray(b"")  #  bytearray(b'')  # bytearray('', encoding='ascii')

    print('')
    print('Start the clock..')
    StartTime = time.time()

    if Mode == 1:  # Compress Mode Verbrose 1 and 0
        #Read_Size = 1 #To be sure its 1  early dayz go slooooooooooooooo
        if Verbose == 1:
            if Lowmemmode == 1:
                #  Read File Data in Bytes And Score
                if os.path.isfile(ArgsFile) != True:
                    print('File Not Found ', ArgsFile)
                    exit()
                with open(ArgsFile, 'rb') as f:
                    byte = f.read(Read_Size)  # read header here!
                    #f.seek(0) #To Adjust Read offset after read try  back to start..
                    while byte:
                        try:
                            index = ord(byte)
                        except:
                            print('End Of Data Stream.')
                        pass
                        # FIX
                        # if Ratio <100 % Count Bytes read and use seek to files end once Ratio Met.
                        #  print (index)
                        #nums = [ord(index) for index in '']
                        #if Verbrose:
                            #print(index)
                        #Data_Byte_Array.append(ord(x) for x in index)  # Store file Data saves ReReading file
                        #Data_Byte_Array = bytearray(f) # Load in one go!

                        #LowMem>
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

                                # Do stuff with byte.
                        byte = f.read(Read_Size)

            else:  # HighMemMode
                if not Lowmemmode:  # Do All in One HIMem

                    print('High Memory Mode:Load all.')
                    f = open(ArgsFile, 'rb')
                    Data_Byte_Array = bytearray(f.read())  # Load in one go!

                    # High Mem
                    pos = 0
                    for i in Data_Byte_Array:
                        pos += 1
                        if i:
                            Score[i] += len(bin(i))

                        if Score[i] > MaxRep:  # NoteWorthy.
                            if i not in NoteWorthy:  # NoteWorthy.
                                NoteWorthy.append(i)
                                #  NoteWorthy.
                                binary_string = '{0:08b}'.format(i)
                                #  print(binary_string)
                                print(pos, ' ', i, " = bin ", binary_string, 'Found>', len(NoteWorthy))
                                #  MaxRep += MaxRep / 8
                        if len(NoteWorthy) > 70:
                            break

                    #f.seek(i)  # exit loop

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
                        Score[index] += len(bin(index))  #  Add Score
                        # if Score[index] > MaxRep:
                        # if index not in NoteWorthy:  # NoteWorthy.
                        # NoteWorthy.append(index)
                        # NoteWorthy.
                        # binary_string = '{0:08b}'.format(index)
                        # print(binary_string)
                        # print(index, '=', Score[index], "=", binary_string)
                        # MaxRep += MaxRep / 8

        if Verbose:
            print('Verbrose Mode.')
            print('Score Data After Conversion....')
            print(Score)
    #  ----------------------------------------------------------------------------------------------------------------
    #  ----------------------------------------------------------------------------------------------------------------
    #if Mode == 1:  # 1 = Compression   ---bug this is obviosely mode 1!
        print('Make Remap. Mode:', Mode, '       Mem:', Lowmemmode)

        if Lowmemmode == 0:
            #  GenScoreKeyMap
            # Make array for Score
            OrderedScoreKeyMap = np.arange(KeySize)  # [0 for i in range(KeySize)]
            HS = -1  # 0=0 so set -1 to start
            ID = 0
            ScoreKeylist = []  # Make A List of All Keys(Keysize) #!!!!
            ## Fix make this list direct in order from score values
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
                        if Verbose == 1:
                            print('id=', iu, ': Score=', Score[iu])

                        if Verbose == 2:
                            print('KeySwap Count ', KeySwaps, 'New Key Info..Ammend at Loop ', i, '    KEY ', iu, ' ', ScoreKeylist[i]), '= ID'  # [%d%%\r%i, end=""])
                    # ScoreKeylist[i] #Just do once at end of  loop

                KeySwaps += 1
                ScoreKeylist[i] = ID #  = 1 = 255 2 = 43 ect
                Score[ID] = -1  # Block from Check.
                HS = -1         # Reset Loop HighScore
                ID = 0          # Reset Loop Score Index

                if Verbose > 1:
                    print('')
                    print('List Size:=', KeySize)
                    print('Key Size =', len(ScoreKeylist))
                    print('')

                if KeySize == KeySwaps:
                    print('Looking Good... KeyLength || KeySwaps || KeySize All Match.')

                #  print(ScoreKeylist[KeySize])
                #  ScoreKeylist[KeySize-i].delete(arr,) #Reverse Bits
                #  np.delete(ScoreKeylist, ID)
                #  print('List:=', ScoreKeylist[KeySize-i])

            #  Create Ordermap
            for i in range(KeySize):
                OrderedScoreKeyMap[i] = ScoreKeylist[i]
                if Verbose:
                    print(OrderedScoreKeyMap[i])

            if Verbose == 1:
                print('Remap Created.')
                print('ScoreKeyList=')
                print(ScoreKeylist)
                print('OrderedScoreKeyMap=')
                print(OrderedScoreKeyMap)
            #  Done.

            #  Compress Convert Stage!
            #  Read Or Use Data_array?
            if Verbose == 3:
                print(Data_Byte_Array)  # Data_Byte_Array

            #Write File!
            # Write De-Compressor Key
            # foo = ''.join(foo.split()) # remove white spaces
            cf = ArgsFile[:-3]
            Compressed_ArgsFile_Name = cf + ".M256"  # fix split .

            if Verbose == 1:
                print('File Out Name =', Compressed_ArgsFile_Name)

            # Write Header & Decompress Key(ScoreKeylist)
            #print('Writing File Header.')
            #print("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)

            #Clear Contents of Mapfile if exista.
            ClearFile(Compressed_ArgsFile_Name)
            FcM256 = open(Compressed_ArgsFile_Name, 'a')  # Mapfile
            #FcM256.writelines("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)
            #for FC_Header_Key_str in ScoreKeylist:
            #FcM256.write(ScoreKeylist[FC_Header_Key_str])
            # file.writelines("%s\n" % item for item in list)

            # Fix Compression Speed Control mainly governed by how much data read and scored
            # Also could do runlength scan and alter scored data  to increase the run length if
            # possible by shifting the value of the run block especially if its only one number stopping the run.

            #Low Mem Mode uses old File rather than a stored version.
            #  Write Through>KeyMp>Conversion Table
            _Modetxt = ""
            if Mode == 1:
                _Modetxt = "Compression"
            else:
                _Modetxt = "Un-Pack."

            _MemModetxt = ''
            if Lowmemmode:
                _MemModetxt = 'Low Memory Mode'
            else:
                _MemModetxt = 'High Mem Mode'

            print(_MemModetxt, ' & ', _Modetxt)
            print()
            print('Read....', ArgsFile)
            print('Map.....', ArgsFile[:3] + 'M256')  # FcM256)
            print('Zip.....=', ArgsFile[:3] + 'Z256')  # if lowmem mode. in-fact map low mem will be removed
            print('Building Map.')  # map Will be removed

            # Open file in mode a
            FcM256 = open(Compressed_ArgsFile_Name, 'a')  # Out Text

            # init temp map array
            _fstMapstringarray = []

            #FcM256 = open(Compressed_ArgsFile_Name, 'ab')  # Out>File>Binary.
            f = open(ArgsFile, 'rb')
            Data_Byte_Array = bytearray(f.read())  # Load in one go!

            for z in Data_Byte_Array:
                index = z
                #print(index)
                for findmap in range(KeySize):  # findmap is the value needed
                    if OrderedScoreKeyMap[findmap] == index:
                        #MapFound
                        _Bytemap = OrderedScoreKeyMap[index]  # OrderedScoreKeyMap[i]
                        if Verbose > 1:
                            print(findmap)
                        break


                if Verbose > 1: #1 ----------
                    #Mybitlength = _Bytemap.bit_length()
                    #OrigBitLength = byte.bit_legth()
                    #print('My=', Mybitlength)
                    ##print('Orig=', OrigBitLength)
                    print('File(int) =', index, 'Remap =', findmap, '=Mem(byte)=', byte, '=(Original)mapped ver=', _Bytemap,'=chr(', chr(_Bytemap), 2)

                # update map data write every 64000 entries
                ##FcM256.write(str(findmap))
                _fstMapstringarray.append(findmap)
                if len(_fstMapstringarray) > 63999:

                    print('.', end='')

                    for mapv in range(len(_fstMapstringarray)):
                        if Verbose > 0: #<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>Map file not needed in final release<<<<
                            FcM256.write(str(_fstMapstringarray[mapv]))
                            ##FcM256.write(',')##csv setup for readability

                    for mapv in range(len(_fstMapstringarray)):
                        _fstMapstringarray.pop(0)

                #FcM256.close()
                #  --Continue Write Re-Map---

            #write last data held in _fstMapstringarray
            for mapv in range(len(_fstMapstringarray)):
                if Verbose > 0:  #<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>Map file not needed in final release<<<<
                    FcM256.write(str(_fstMapstringarray[mapv]))

            for mapv in range(len(_fstMapstringarray)):
                _fstMapstringarray.pop(0)

            #  Done With open files(end of with)
            FcM256.close()

            #ArgsFile.close()

            print('Bit reduction MapFile Wrote.')

            # -------------------------------------------------------------
            # -------------------MAGIC BIT---------------------------------
            # -------------------------------------------------------------

            # Setup Array to write in one shot.
            bin_stream = io.BytesIO()  # binary_stream = io.BytesIO()

            # Setup WriteBlock
            BinWriteBlock = []

            # Set Chunk Size(WriteBlockSize)
            Chunk = 32  # Block Of Mapped Bits.

            # BitsHolder
            bits = ""

            # Counter Bit Count
            MaxBits = 0
            BitCountThisBloc = 0

            # Counter Current Map Index Pos
            PositionInMap = 1
            # Stats
            OrigSize = 0
            MappedSize = 0

            print('Converting Binary data.')
            Compressed_Bin_ArgsFile_Name = cf + '.B256'

            # Clear file Contents if exist.(Create New File)
            ClearFile(Compressed_Bin_ArgsFile_Name)
            FcB256 = open(Compressed_Bin_ArgsFile_Name, 'a')

            print('Writing Zip File Header.')
            print("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)
            #FcB256.writelines('FCzip GDCC_Entry_2021_By_Brett Palmer.')
            FcB256.writelines("%s\n" % FC_Header_Key_str for FC_Header_Key_str in ScoreKeylist)  # write key
            # for FC_Header_Key_str in ScoreKeylist:

            print('Header Wrote.')
            Zip_seek = FcB256.tell() #//function
            # Temp Close write mode change.
            FcB256.close()

            print('Reading Map File,*(', Compressed_ArgsFile_Name, ') & Building Zip*', Compressed_Bin_ArgsFile_Name)

            # fix use memory stored data rather than reading from file!
            #Re-Open Bin File in Binary Mode
            FcB256 = open(Compressed_Bin_ArgsFile_Name, 'ab')

            #Move Past Header  zipseek holds location  to move to.
            FcB256.seek(Zip_seek)

            # Fix To Use Data_Byte_Array(Copy Of File Compressing or the map)(High-Mem)
            #FcM256 = open(Compressed_ArgsFile_Name, 'r')  # Mapfile In>

            #Keep eye on BitSize Changes
            LastMaxbits = 0
            countsamesize = 0
        print('Building Binary File.')
        with open(Compressed_ArgsFile_Name, "r") as f:  # In>file>MAP
            String_byte = f.read(Read_Size)  # speedup use size off key as Read_Size = KeySize#Pull from Data_Byte_Array
            while String_byte:
                # byte = f.read(Read_Size) #put at bottom no need to re-seek file start
                try:
                    MapValue = int(String_byte)
                    ###print('String_byte', String_byte, ':mapval:', MapValue)
                except:
                    print('End Of Map Data.?')
                pass
                # Progress info
                #print('.', end='') #Data_Byte_Array in 1 data
                ##print(len(Data_Byte_Array) - f.tell(), end='')
                ##print_at(1, 10, len(Data_Byte_Array) - f.tell())
                _plength = len(Data_Byte_Array)
                _pcent = math.floor(len(Data_Byte_Array) / f.tell())
                ##print(f.tell()) #debug show file read position
                progress(100 - _pcent, 30)
                # Debug show read value
                ##print('MapValue:', MapValue)

                # Update File Block
                BinWriteBlock.append(MaskBitReducedString[MapValue])
                _tmpval = len(BinWriteBlock) - 1
                ##print('Block-Index_tmpval:', _tmpval)
                ##print('BinWriteBlock:', BinWriteBlock[_tmpval])

                # Update PositionInMap
                PositionInMap += BitCountThisBloc  # start -1
                BitCountThisBloc = len(MaskBitReducedString[MapValue])

                #Bitsize Info Debug
                if Verbose > 4:
                    print(len(MaskBitReducedString[MapValue]))
                    print('Last Size =', LastMaxbits)
                    if len(MaskBitReducedString[MapValue]) != LastMaxbits:
                        LastMaxbits = len(MaskBitReducedString[MapValue])
                        countsamesize = 0
                    else:
                        countsamesize += 1
                        print(countsamesize)

                # get bit count of data
                if len(MaskBitReducedString[MapValue]) > MaxBits:
                    MaxBits = len(MaskBitReducedString[MapValue])

                # Data Was Not Caught. bin array ln=475
                if PositionInMap > Chunk:
                    if Verbose > 1:
                        print('Data Withheld But Construction Data Lost !!')  ######bin_array 475 linenum########<<Fix<
                        print('bits+1=', PositionInMap+1)
                        print('BinWriteBlockSize=', len(BinWriteBlock))
                        print('Max Index=', len(BinWriteBlock))
                        print('PosInMap=', PositionInMap+1)
                        print('BWB_val=', BinWriteBlock)
                        print('')

                    # Remove MaskBitReducedString[0 - PositionInMap]
                    _StrToBin = BitArray()
                    ##print('BinWriteBlock=', BinWriteBlock)
                    for CreateBin in range(len(BinWriteBlock)):

                        bits = BinWriteBlock[CreateBin]
                        byte = bits[CreateBin:CreateBin + len(BinWriteBlock)][::-1]

                        ##print('byte len =', len(byte), '   Pos:', PositionInMap)

                        # check for limit to chunk<store<rewind<read
                        if PositionInMap + len(byte) > Chunk:
                            ##Zip_seek = FcB256.tell() - (len(BinWriteBlock) - CreateBin)##bug with relocation of read
                            ##f.seek(Zip_seek)
                            # Reset Pos & block info
                            MaxBits = 0
                            PositionInMap = 0
                            BitCountThisBloc = 0
                            # remove block data(reset)
                            for RemoveMem in range(len(BinWriteBlock)):
                                # Remove BinWriteBlocks from memory
                                BinWriteBlock.pop(0)

                            String_byte = f.read(Read_Size)  # Read More  String_byte = f.read(Read_Size)
                            ##ValueError: invalid literal for int() with base 10: ',' Coz the csv setup!!y
                            ##MapValue = int(String_byte)##check csc comma,seperarred,vaules
                            break

                        _StrToBin.join(BitArray(uint=x, length=len(BinWriteBlock)) for x in BinWriteBlock)
                        #bin_array.append(int(byte, 2))
                        #_StrToBin.append(int(byte, 2))
                        # Construct Array Data.
                        #bytes(_StrToBin, 'utf-16')
                        ##print('_StrToBin', _StrToBin)
                        # _StrToBin = bytearray(BinWriteBlock[CreateBin], 'ascii')
                        #_StrToBin = bitstring_to_bytes(BinWriteBlock[CreateBin])
                        #print(_StrToBin)
                        
                        #bin_stream.write(BinWriteBlock[CreateBin].encode('ascii'))  # binary_stream.write
                        bin_stream.write(bytes(BinWriteBlock[CreateBin].encode('ascii')))

                        if Verbose > 1:
                            print('#', CreateBin, '   ', BinWriteBlock[CreateBin], bin_stream)
                        # Write to Zip Reduced Bytes
                        #FcB256.write(bytes(bin_stream))  # fix Write at end.
                        #print('FileData', bytes(bin_stream))

                    for RemoveMem in range(len(BinWriteBlock)):
                        # Remove BinWriteBlocks from memory
                        BinWriteBlock.pop(0)

                    # Reset Pos & block info
                    MaxBits = 0
                    PositionInMap = 0
                    BitCountThisBloc = 0

                if PositionInMap == Chunk:
                    ##print(Chunk, "  bits")
                    _StrToBin = BitArray()
                    bits = ""
                    byte = None
                    if Verbose > 1:#--
                        print('bits=', PositionInMap+1)
                        print('BinWriteBlockSize=', len(BinWriteBlock))
                        print('Max Index=', len(BinWriteBlock))
                        print('PosInMap=', PositionInMap+1)
                        print('BWB_val=', BinWriteBlock)
                        print('')

                    # Remove MaskBitReducedString[0 - PositionInMap]
                    for CreateBin in range(len(BinWriteBlock)):
                        #byte = bits[index:index + 8][::-1]
                        #bin_array.append(int(byte, 2))
                        #bits = BinWriteBlock[CreateBin]
                        #byte = bits[CreateBin:CreateBin + len(BinWriteBlock)][::-1]
                        #_StrToBin.join(BitArray(uint=x, length=len(BinWriteBlock)) for x in BinWriteBlock)

                        # Construct Array Data.
                        bits.join(BinWriteBlock[CreateBin])
                        #print('Bits = ', bits)
                        byte = bits[CreateBin:CreateBin + len(BinWriteBlock)][::-1]
                        #print('Byte = ', byte)
                        #bin_array.append(int(byte, 2))
                        #_StrToBin.append(int(byte, 2))#///////////////////////////////////here
                        # Construct Array Data.
                        #bytes(_StrToBin, 'utf-16')
                        #print('created int value from byte=', _StrToBin)
                        bin_stream.write(BinWriteBlock[CreateBin].encode('ascii')) #binary_stream.write

                        if Verbose > 1:
                            print('#', CreateBin, '   ', BinWriteBlock[CreateBin], bin_stream)
                        # Write to Zip Reduced Bytes
                        #FcB256.write(bytes(bin_stream))  # fix Write at end.
                        #print('FileData', bytes(bin_stream))

                    for RemoveMem in range(len(BinWriteBlock)):
                        # Remove BinWriteBlock from memory
                        BinWriteBlock.pop(0)

                    # Reset Pos & block info
                    MaxBits = 0
                    PositionInMap = 0
                    BitCountThisBloc = 0

                # Stats
                if Verbose > 2:
                    print(MapValue)
                    print(MapValue.bit_length())

                MappedSize += MapValue.bit_length()
                OrigSize += 8
                String_byte = f.read(Read_Size)  #Read More

            if Verbose == 4:
                print('')
                print('Compression Data:')
                print('MaxBitSize =', MaxBits)
                print('PositionInMap', PositionInMap)
                print('')

            # Write to Zip Reduced Bytes
            print('')
            print('Writing Zip: Write In One...')
            #bin_array.append(int(BinWriteBlock[0]))
            #FcB256.write(bin_stream)  # fix Write at end.
            bin_stream.seek(0)
            #FcB256.write(bin_stream.read())
            #print(bin_stream.read())
            B = bitarray()
            B.frombytes(bin_stream.read())
            B.tofile(FcB256)  # true bin

            # Memory Cleanup
            #bin_stream.close() # save close till end
            # End Of Compression! GDCC days to go !!

        #File-data-zipped
        bin_stream.seek(0)
        print((bin_stream.read()))

        #Results
        print('\nResults:')
        added = (OrigSize / 8) / 10
        os_Z_fsize = os.stat(Compressed_Bin_ArgsFile_Name)
        os_fsize = os.stat(ArgsFile)
        if MappedSize == 0:
            MappedSize = 1

        print('File Size On Disc =', os_fsize.st_size)
        print(' ZIP Size On Disc =', os_Z_fsize.st_size)
        print('    Original size =', OrigSize/1024)
        print('    Mapped Size   = ', MappedSize/1024)
        print('    Added         =  ', added/1024)

        print('Saving ', (OrigSize - (MappedSize + added))/1024, ' Bytes(ish)  Ratio of ', OrigSize / (MappedSize + added) * 100, '%')

        print('Writing Bin FCZipped!')

        # Close Open Files.
        FcB256.close()
        bin_stream.close()

        print('Complete....')
    if Lowmemmode == 1:
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
                        if Verbose == 2:
                            print('KeySwap Count ', KeySwaps, 'New Key Info..Ammend at Loop ', i, '    KEY ', iu, ' ', ScoreKeylist[i]), '= ID'  # [%d%%\r%i, end=""])
                    # ScoreKeylist[i] #Just do once at end of  loop

                KeySwaps += 1
                ScoreKeylist[i] = ID #  = 1 = 255 2 = 43 ect
                Score[ID] = -1  # Block from Check.
                HS = -1         # Reset Loop HighScore
                ID = 0          # Reset Loop Score Index

                if Verbose:
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
                if Verbose:
                    print(OrderedScoreKeyMap[i])


            if Verbose == 1:
                print('Remap Created.')
                print('ScoreKeyList=')
                print(ScoreKeylist)
                print('OrderedScoreKeyMap=')
                print(OrderedScoreKeyMap)
            #  Done.

            #  Compress Convert Stage!
            #  Read Or Use Data_array?
            if Verbose == 3:
                print(Data_Byte_Array)  # Data_Byte_Array

            #Write File!
            # Write De-Compressor Key
            # foo = ''.join(foo.split()) # remove white spaces
            cf = ArgsFile[:-3]
            Compressed_ArgsFile_Name = cf + ".M256"

            if Verbose == 1:
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

                            if Verbose > 0:
                                print(findmap)
                            break



                    if Verbose == 2: #1 ----------
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

            # -------------------------------------------------------------
            # -------------------MAGIC BIT---------------------------------
            # -------------------------------------------------------------

            # Setup Array to write in one shot.
            bin_stream = array("B")

            # Setup WriteBlock
            BinWriteBlock = []

            # Set Chunk Size(WriteBlockSize)
            Chunk = 32 - 1  #Block Of Maped Bits. pos 0 = 1

            # BitsHolder
            bits = ""

            # Counter Bit Count
            MaxBits = 0
            BitCountThisBloc = 0

            # Counter Current Map Index Pos
            PositionInMap = 0

            # Stats
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

            # Fix To Use Data_Byte_Array(Copy Of File Compressing or the map)(High-Mem)
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
                    # Update Block
                    BinWriteBlock.append(MaskBitReducedString[MapValue])

                    # Update PositionInMap
                    PositionInMap += 1
                    BitCountThisBloc += len(MaskBitReducedString[MapValue])  # Check if larger than Chunk

                    # Stats
                    MappedSize += MapValue.bit_length()
                    OrigSize += 8
                    String_byte = f.read(Read_Size)  #Read More

                if Verbose:
                    print('')
                    print('Compression Data:')
                    print('MaxBitSize =', MaxBits)
                    print('PositionInMap', PositionInMap)
                    print('')

                print('Writing Zip: Write In One...')

                # Write to Zip Reduced Bytes
                #bin_array.append(int(BinWriteBlock[0]))
                FcB256.write(bytes(bin_stream))  # fix Write at end.

                # Memory Cleanup
                bin_stream = 0
                # End Of Compression! GDCC 3 days to go !!

            #Results
            print('\nResults:')
            added = (OrigSize / 8) / 10
            os_Z_fsize = os.stat(Compressed_Bin_ArgsFile_Name)
            os_fsize = os.stat(ArgsFile)
            print('File Size On Disc =', os_fsize.st_size)
            print(' ZIP Size On Disc =', os_Z_fsize.st_size)
            print('    Original size =', OrigSize/1024)
            print('    Mapped Size   = ', MappedSize/1024)
            print('    Added         =  ', added/1024)
            print('Saving ', (OrigSize - (MappedSize + added))/1024, ' Bytes(ish)  Ratio of ', OrigSize / (MappedSize + added) * 100, '%')

            print('Writing Bin FCZipped!')
            FcB256.close()
            print('Complete....')

    else:  # Decompress .M256 File >>>>> Mode !=1
        if Mode == 2:  # Decompress
            print('Decompression Of M256 File.')
            #  Chk file exists
            #  read Header
            #  read KeyMap for Read function Real = KeyMap(read(byte))
            #  writefnc(KeyMap(Ral))
            print('File Decompressed')
            print('Header Will Contain Original File Name.')
# ----------------------------------------------------------------------------------------------
#-------------------------------end-------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#if mode==2 = Decompres file enter name of file/read header key/ convert
EndTime = time.time()


#  Show Running Time
print('Time Taken =', EndTime - StartTime)
input(" :<) Press Enter to continue... ")

exit()
