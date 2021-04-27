# Opracowanie pytań z egzaminu z CPS.

### 1. Cel i podstawowe zastosowania przetwarzania sygnałów. Podać przykłady

Celem przetwarzania sygnału jest przetworzenie sygnału w inną postać, będacą bardziej pożądaną od pierwotnej postaci.

Na przykład można stosować przekształcenia w celu: rozdzielania dwóch sygnałów nałożonych w
jakiś sposób na siebie (tłumienie szumu).

Zastosowania:
- Techniczna i medyczna diagnostyka.
- Rozpoznawanie mowy i obrazów.
- Transmisja i kompresja danych.
- Radary i sonary.
- Systemy Sterowania
- Telewizja Cyfrowa.
- Grafika Komputerowa.
- Radary sonary

### 2. Definicja sygnału. Ciągłe analogowe i cyfrowe układy przetwarzania sygnałów.

- Sygnał jest funkcją przynajmniej jednej zmiennej, gdzie wszystkie zmienne są od siebie niezależne. Sygnał przenosi informacje o stanie lub zachowaniu pewnego układu fizycznego lub zjawiska.
 Informacja ta jest zawarta w postaci jakichś zmian w czasie lub przestrzeni.

- Sygnał analogowy opisywany jest funkcją ciągłą x<sub>a</sub>(t). Przy czym zmienna t jest ograniczona przedziałem trwania sygnału.
- Sygnał dyskretny jest ciągiem liczb rzeczywistych lub zespolonych. x(nT), n = 0,+-1,+-2,... . n może przyjmować tylko wartości dyskretne. Poszczególne wartości funkcji nazywamy próbkami sygnału dyskretnego. Wartość T jest to okres próbkowania, przy przejściu z sygnału analogowego do dyskretnego.
- Sygnał cyfrowy = jest otrzymywany poprzez kwantyzację sygnału dyskretnego. Kwantowanie polega na przydzielaniu wartości kolejnych próbek do jednego z 2<sup>m</sup> przedziałów kwantowania.

### 3. Elementarne sygnały (ciąg impulsowy i skokowy, rzeczywisty ciąg wykładniczy, ciąg sinusoidalny).
- Sygnał elementarny jest to sygnał całkowicie opisywany małą liczbą parametrów - 1,2. 
- Ciąg impulsowy delta(n), inaczej impuls przyjmuje wartość 1 dla n = 0 lub wartość 0 dla n != 0. Sygnał przyjmuje jeden parametr, którym jest n.
- Ciąg skokowy u(n) przyjmuje wartość 1 dla n >= 0 lub wartość 0 dla n < 0. Sygnał przyjmuje jeden parametr, którym jest n.
- Rzeczywisty sygnał wykładniczy x(n) = a<sup>n</sup>, przyjmuje jeden parametr a, który jest liczbą rzeczywistą. 
- Ciąg sinusoidalny x(n) = A*cos(omega<sub>0</sub>n + fi) * e<sup>(a + j omega)n</sup>. Sygnał pobiera 3 parametry A - amplituda, 
  omega<sub>0</sub> - częstotliwość, fi - faza.

### 4. Okresowe sygnały. Zespolony ciąg wykładniczy.

- Sygnał x(t) jest okresowym sygnałem o okresie T, gdy dla każdego t zachodzi równość x(t) = x(t + T),
to znaczy wartości sygnału powtarzają się co czas równy okresowi T. 

- x(n) = e<sup>(a + j * (omega, czytaj w)) * n</sup>
- - Gdzie j = sqrt(-1), n = ... -2,-1,0,1,2 ... Zespolony ciąg wykładniczy zawiera dwa rzeczywiste parametry a i omega.

# Sprawdzić zespolony ciąg wykładniczy w nagraniu!


### 5. Wartość chwilowa, wartość bezwzględna, energia sygnału.

- Wartość chwilowa sygnału x(n) dla chwili czasu n<sub>0</sub> 
  jest to wartość zmiennej zależnej x(n<sub>0</sub>), czyli jest to wartość sygnału dla danej chwili n<sub>0</sub>
  
- Wartość bezwzględna sygnału x(n) dla chwili czasu n<sub>0</sub> jest to moduł wartości chwilowej |x(n<sub>0</sub>)|

- Energia sygnału x(n) okeślona jest jako suma kwadratów wartości chwilowych E = sum od -inf do +inf x(n)<sup>2</sup>

### 6. Operacje na sygnałach (dodawanie, odejmowanie, mnożenie, dzielenie, opóźnienie, przyspieszenie).

Sygnały dyskretne – ciągi liczb x(n) wygodnie jest opisywać jako wektory o skończonej liczbie elementów N. 
Zakładamy, że n zmienia się od 0 do N - 1. 
Wtedy operacje arytmetyczne wykonane są na sygnałach analogicznie do operacji na macierzach i wektorach lub ciągach o jednakowej długości.

- Suma / różnica. Suma lub różnicą dwu sygnałów x(n) i y(n) jest sygnał z(n), którego każdy element
 równa się sumie / różnicy opowiednich elementów. 
  
- Wynik dzielenia / mnożenia. Iloczynem lub ilorazem dwu sygnałów x(n) i y(n) jest sygnał z(n), którego każdy element
  równa się iloczynowi / ilorazowi opowiednich elementów. Gdy nastąpi dzielenie przez 0 to należy przyjąć arbitralną liczbę.
  
# Poprawić opóźnienie i przyśpeszenie, narazie nwm.

- Opóźnienie sygnału. W ogóle opóźnienie sygnału o skończonej długości o m elementów zwiększa jego długość o m elementów.
 Fizycznie operację opóźnienie nieokresowego skończonego sygnału można interpretować jako dopełnienie wartościami, które były w przeszłości.

- Operacja przyspieszenia wykorzystuje się rzadziej, bo niema ona “dobrej” fizycznej interpretacji. Przyspieszenie
  nieokresowego sygnału oznacza, że z góry są znane wartości elementów z przyszłości, a jest to niemożliwie (jest
  możliwie tylko dla okresowych modeli sygnałów).


### 7. Układy liniowe. Układ liniowy niezmienny względem przesunięcia. Podać przykład.

- Układ liniowy jest układem należący do klasy układów, które są określane zasadą superpozycji. 
  # wideło

- Układ liniowy niezmienny względem przesunięcia jest układem charakteryzującym się poprzez własność, że jeśli y(n) jest odpowiedzą 
  na pobudzenie x(n), to y(n - k)jest odpowiedzą na pobudzenie x(n - k), gdzie k jest dodatnią lub ujemną liczbą całkowitą.
  
- Przykłady
#Wideło


### 8. Odpowiedź impulsowa układu.
- Odpowiedź impulsowa układu jest to sposób wyrażenia sygnału poprzez sumę opóźnionych i pomnożonych ciągów impulsowych. Odpowiedź impulsowa 
  w połączeniu z właściwością stacjonarności pozwala w pełni scharakteryzować sygnał.  
  # nie jestem pewna :(

### 9. Równanie splotu
- Równanie splotu ciągów x(n) i h(n): y(n) = x(n) kropka h(n) = h(n) kropka x(n) gdzie n przyjmuje wartości całkowite. Kolejność ciągów w zbiorze nie ma znaczenia. 


### 10. Stabilność i przyczynowość układu.

- Układ stabilny definiujemy jako układ, w którym każde (dowolne) ograniczone pobudzenie powoduje ograniczoną odpowiedź.
- Układ przyczynowy jest to układ, w którym zmiany na wyjściu nie poprzedzają zmian na wejściu.
  Oznacza to, że dla układów przyczynowych istnieje właściwość: jeśli x<sub>1</sub>(n) = x<sub>2</sub>(n),
  n < n<sub>0</sub>, to y<sub>1</sub>(n) = y<sub>2</sub>(n), n < n<sub>0</sub>.\
- Dokladne wzory koniec wykladu 1-2.

### 11. 



### 12. Filtracja sygnałów za pomocą splotu (liniowa i okresowa)
















