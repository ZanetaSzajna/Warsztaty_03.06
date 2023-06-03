# Generator e-mail 
Program powstał podczas drugich  warsztatów  będacych częścią Kursu Python od Podstaw.

## Opis 

Skrypt generuje wiadomosć e-mail do uczniów z inforomacją ilu zadań jeszcze nie wysłał do nauczyciela, wraz z obecną oceną.
Plik informuje również ucznia  jaką ocenę otrzyma jeżeli dośle brakujące zadania oraz  jaki jest ostateczny termin.
W folderze znajdują się 3 pliki. 

### Geerator_email_etapI :

Skrypt ten to najprostrzy generator e-mail, pobiera następujące dane od uzytkownika:
* Imię ucznia
* Nazwisko ucznia
* Ilosć brakujacych zadań 
* Ocena 

Dane zamieniane są na listy a następnie za pomocą pętli oraz f-string generowany jest email z paarametrem, gdzie podstawianie są zmienne wprowadzone przez użytkownika


### Generator_email_etap III:

Skrypt odczytuje dane z pliku CSV i rozdziela je odpowiednio na 3 listy:
* name_surname - imię i nazwisko ucznia
* missing_tasks - ilość brakujacych zadań 
* grades - obecna ocena

Po stworzeniu list za pomocą pętli for oraz f-string generowany jest e-mail z podstawieniem odpowiednio danych

### Generator_email_etap_IV:

Skrypt ma wbudowane dwie funkcje: 
* generata_email której zadaniem jest pobieranie szablony email z pliiku txt. i dla każdej pozycji z listy uczniów generuje wiadomość email i zapisuje ją w txt
* main zadaniem jest odczytanie pliku csv,  zapisanie danych w listach a nastęnie wywołuje funckje generata_email
