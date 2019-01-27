import numpy as np

which_file = 'Creative Commons Attribution-ShareAlike 3.0 Unported.txt'

#open() r=read-oly
# license_file = open(which_file, mode='r')
# license_name = license_file.readline()

# print(license_name)

# license = license_file.read()
# print(license)

# license_file.close()

#utilizando with não precisamos lembrar de usar close file.
with open(which_file, 'r') as text_file:
  print(text_file.read())


#importando arquivos de texto usando numpy
sample_array = np.array([0,0,7])
print(type(sample_array))
print(dir(sample_array))

badges_saved_np = np.loadtxt('badges-five-numpy.txt')
print(badges_saved_np)
print(badges_saved_np.size)
print(badges_saved_np.shape) #para consultar a dimensao

badges_comma = np.loadtxt('badges-five.txt', delimiter=',')
print(badges_comma)

badges_header = np.loadtxt('badges-five-header.txt', delimiter=',', skiprows=1)
print(badges_header)

print(badges_header.dtype)

#para mudar o tipo do arquivo
badges_uint = np.loadtxt('badges-five-header.txt', delimiter=',', skiprows=1, dtype=np.uint)
print(badges_uint.dtype)

def increase(the_id):
  return int(the_id) + 1000

#especificamos qual coluna queremos aplicar uma funcao especifica
badges_increased = np.loadtxt('badges-five.txt', delimiter=',', dtype=int, converters={0: increase})

print(badges_increased)

#loading textData with missing values
badges_missing_value = np.genfromtxt('badges-five-missing-value.txt', delimiter=',', skip_header=1)
print(badges_missing_value)