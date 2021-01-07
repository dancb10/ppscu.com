import os

def add_word(word, word_hash):
    if word in word_hash:
        word_hash[word] += 1
    else:
        word_hash[word] = 1

def read_file(text_file ,text_offset, text_chunk):

    with open(text_file) as f:
        f.seek(text_offset)
        tempword = ""
        word_hash = {}
        while(True):
            f.tell()
            if f.tell() - text_offset < text_chunk:
                tmpchar = f.read(1)
                if tmpchar.isalpha():
                    tempword += tmpchar
                else:
                    add_word(tempword, word_hash)
                    tempword = ""
            else:
                while(True):
                    tmpchar = f.read(1)
                    if not tmpchar.isspace():
                        if tmpchar.isalpha():
                            tempword += tmpchar
                        else:
                            add_word(tempword, word_hash)
                            tempword = ""
                    else:
                        print(word_hash)
                        return f.tell()

# print(read_file(, 0, 1024))
file_end = os.path.getsize('input.txt')
offset = 0;
chunk = 1024;
while(True):
    if offset < file_end:
        offset = read_file('input.txt', offset, chunk)
    else:
        break


