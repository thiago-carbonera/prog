'''
2. Escreva um programa que imprime a tabela ASC com valores em decimal (%03d), hexadecimal
(%03X) e o caractere (%c). Imprima apenas os caracteres 33 ao 125, separados em 3 colunas
(cada uma conterá 31 elementos), similar ao seguinte exemplo:
DEC HEX CHR DEC HEX CHR DEC HEX CHR
033 021  !  064 040  @  095 061  _
034 022  "  065 041  A  096 062  `
035 023  #  066 042  B  097 063  a
036 024  $  067 043  C  098 064  b
...           ...        ...
061 03D  =  092 05C  \  123 07D  {
062 03E  >  093 05D  ]  124 07E  |
063 03F  ?  094 05E  ^  125 07F  }
'''
print("DEC HEX CHR - DEC HEX CHR - DEC HEX CHR")

for i in range(1,32):
    print(f" {1+32} {hex(i+32)} {chr(i+32)}  -  {1+63} {hex(i+63)} {chr(i+63)}  -  {1+94} {hex(i+94)} {chr(i+94)}")




