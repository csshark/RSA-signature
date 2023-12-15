#ENG

########################################################
##################ELECTRONIC-SIGNATURE##################
########################################################
A program in Python, using cryptographic libraries for electronic signature
electronic signature and its verification with a graphical interface. 2023

Author Robert Strzoda (https://github.com/JustTypin)


DESCRIPTION OF FUNCTIONALITY:

The program consists of two buttons:
-File Signing
-Verifying file

Pressing the button located under the caption "Signature"
will cause a function to be called that generates the signature itself,
Which is hashed before completing this process. 
The hash is then signed with a private key. 
In memory, this value is stored in the file "Signature.txt".
At the same time, the generation of the 
public key, which in our program finds
used in verifying the integrity of the document. 
All the rules of character formatting are preserved, so
when verifying, the signature is decoded from ASCII text
to binary data (base64). The public key as well as the private key,
are stored in the program's memory, thanks to the library
cryptography.hazmat. The project is for illustrative purposes and is 
intended only to reproduce the way electronic signatures work in a considerable simplification
electronic signature in considerable simplification. 

Signed file: c:/Path/To/Program/Signature.txt

Note: This is a newly created file that is signed. The 
source file stays in place and can still be used. 

########################################################
########################################################
########################################################

#PL

########################################################
##################PODPIS ELEKTRONICZNY##################
########################################################
Program w Pythonie, wykorzystujący biblioteki kryptograficzne do podpisu
elektronicznego i jego weryfikacji z interfejsem graficznym. 2023

Autorzy: Robert Strzoda (https://github.com/JustTypin)

OPIS FUNKCJONALNOŚCI:

Program składa się z dwóch przycisków:
-Podpisującego plik
-Weryfikującego plik

Wciśnięcie przycisku znajdującego się pod napisem "Podpis"
sprawi, że zostanie wywołana funkcja generująca sam podpis,
który jest haszowany przed zakończeniem tego procesu. 
Następnie skrót jest podpisywany kluczem prywatnym. 
W pamięci ta wartość jest przechowywana w pliku "Podpis.txt".
Jednocześnie w tym samym czasie realizowane jest generowanie 
klucza publicznego, który w naszym programie znajduje
zastosowanie przy weryfikowaniu integralności dokumentu. 
Zachowane zostały wszystkie zasady formatowania znaków, więc
przy weryfikacji następuje dekodowanie podpisu z tekstu ASCII
do danych binarnych (base64). Klucz publiczny jak i prywatny,
są przechowywane w pamięci programu, dzięki bibliotece
cryptography.hazmat. Projekt ma charakter poglądowy i jest 
przeznaczony jedynie do odtworzenia sposobu działania podpisu
elektronicznego w sporym uproszczeniu. 

Podpisany plik: c:/Ścieżka/Do/Programu/Podpis.txt

Uwaga: Jest to nowo utworzony plik, który jest podpisany. Plik 
źródłowy zostaje na miejscu i wciąż można z niego korzystać. 

########################################################
########################################################
########################################################
