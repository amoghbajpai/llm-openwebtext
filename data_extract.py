import os
import lzma
from tqdm import tqdm

def xz_files_in_dir(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

#folder_path= "C://Users/amogh/openwebtext.tar.xz/openwebtext" 
folder_path= r"C:\Users\amogh\openwebtext\openwebtext"
output_file_train= "output_train.txt"
output_file_val= "output_val.txt"
vocab_file= "vocab.txt" #Where the vocabulary will be stored

files= xz_files_in_dir(folder_path)
total_files= len(files)

split_index = int(total_files * 0.80) 
files_train = files[:split_index]
files_val = files[split_index:]



vocab= set() #to store vocabulary, this shall go into the vocab file

#for training

with open(output_file_train, "w", encoding= "utf-8") as outfile:
        for count, filename in enumerate(tqdm(files_train, total= len(files_train))):
            file_path= os.path.join(folder_path, filename)
            with lzma.open(file_path, "rt", encoding= "utf-8") as infile:
                text= infile.read()
                outfile.write(text)
                characters= set(text)
                vocab.update(characters)
     

#for validation, same set of operations
with open(output_file_val, "w", encoding= "utf-8") as outfile:
        for count, filename in enumerate(tqdm(files_val, total= len(files_val))):
            file_path= os.path.join(folder_path, filename)
            with lzma.open(file_path, "rt", encoding= "utf-8") as infile:
                text= infile.read()
                outfile.write(text)
                characters= set(text)
                vocab.update(characters)
    

with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')
