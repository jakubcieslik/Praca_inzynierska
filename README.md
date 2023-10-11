# Praca_inzynierska
Wykorzystanie n-krotnego ekstraktora von Neumanna do generowania liczb losowych

Celem pracy jest zaimplementowanie i testy n-krotnego ekstraktora von Neumanna wybielającego ciąg bitów pozyskanych z przetwornika ADC, na mikrokontrolerze STM32.

Po stronie STM32 powinno powstać proste oprogramowanie w C. Powinno ono:

a) pozyskiwać bity z ADC,
b) wybielać je zgodnie z algorytmem n-krotnie, dla n=0 (brak wybielania), n=1 i n=2
c) bity zebrane w bajty przesyłać do komputera PC

Ciągi otrzymanych wartości mają być zapisane w plikach na PC albo RPi w celu ich dalszej analizy.

Należy przetestować i porównać jakość uzyskanej losowości dla różnych n, stosując histogramy i metodę zmiennych opóźnionych lub lepszą.
