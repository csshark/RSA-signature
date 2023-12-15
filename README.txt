########################################################
##################PODPIS ELEKTRONICZNY##################
########################################################
Program w Pythonie, wykorzystujący biblioteki kryptograficzne do podpisu
elektronicznego i jego weryfikacji z interfejsem graficznym. 2023

Autorzy: Robert Strzoda s10048 (https://github.com/JustTypin)
         Alan Kasperczak s10044

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