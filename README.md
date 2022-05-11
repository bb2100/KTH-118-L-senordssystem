# KTH lösenordssystem

## Description


This program is written in python. It is a account creator and log in system made to simulate a working account creator with the function to track who has tried to log onto your account. Since it has no form of security it is not recommended to use in a serious matter.

## Technology/Languages/Built with (Teknologier/Språk/Byggt med - välj en)

***Här kan du beskriva vilka språk som driver vilka delar av projektet, exempelvis att du skrivit frontend med JavaScript och Python för backend. Det kan även vara nyttigt att berätta vilka ramverk eller bibliotek du använt här för de olika delarna. För exemplena givna är React (för JS) och Flask (Python) bra att nämna. Utelämna add-ons eller plugins, lämna dessa till Acknowledgements.***

- Python - The whole program
- Markdown - This description file

## Requirements/Prerequisites (Krav)

***Vad krävs för att köra ditt program? Lista bara kraven.***

- Python 3.9+

## Installation

***För att köra programmet listar du här vad som behövs och hur det installeras. Exempel:***

Exempel 1: 

1. Klona repot
```cmd
    git clone https://github.com/ditt_anv/reponamn
```
2. Installera Flask
```cmd
pip install Flask
```
3. Installera pygame
```cmd
pip install pygame
```

Exempel 2:

Detta projekt är testat på Python 3.7+. För att installera Python kan du besöka (https://www.python.org/downloads/)[följande länk för senaste versionen.]

Programmet kräver även att biblioteket Flask samt pygame är installerade. För att installera krävs python 3.7+ installerat, följt av att följande kodrader skrivs i terminalen: 

```cmd
pip install Flask
pip install pygame
```

## Code conventions (Kodkonvention)

***Detta är överkurs, men här kan du lista exempelvis hur filerna ska vara strukturerade, hur namngivning och kommentarer skrivs och massvis av annat. (Kan vara bra att förtydliga att PEP8 efterföljs.)***
File structure does not matter, the important thing is the filenames. The logging file should be named "log.txt" and the user file should be named "users.txt". If this were to be changed, it has to be changed everywhere it is used in the code too. The program is written following PEP8.

## Hur det fungerar (Usage)

***Använd detta utrymme för att visa användbara exempel av hur projektet kan användas. Skärmdumpar, kodexempel och demos passar in här. Du kan också länka till fler resurser, exempelvis en dokumentation.***

Users are saved as username/password in the "users.txt" file
![](Screenshots/users.png)
It is possible to have the same username as someone else as you could see on the screenshot. This is a problem, but it does not matter for this purpose.

Log is saved like this (see screenshot below) in the "log.txt" file
![](Screenshots/log.png)

This is how easy it is to change password:
![](Screenshots/Passwordchanging.png)

## Example (exempelkörning)

***Visa gärna, genom ett kodblock från din konsol, eller en bild, hur en exempelkörning kan gå till.***

## To do/Roadmap (Att göra/Plan)

***Det kan vara nyttigt att få andra som läser om projektet att få veta vad du saknar just nu i programmet. Gör detta gärna genom en lista där färdiga saker strukits över.***
Exempel:

- [x] Påbörja exempelreadme
- [ ] Hitta fler exempelrubriker
- [ ] Kom på bättre exempel
- [ ] Ge exempel på projekt med fullständig readme
- [ ] Ytterligare språk
- [x] Svenska
- [ ] Engelska

## Changelog

***Det kan vara rimligt att inkludera vad som har förändrats genom de olika iterationerna som ditt projekt gått igenom. Detta kan antingen göras i din README eller så kan du inkludera en CHANGELOG.md.***

***I changelogen ska varje rubrik vara en version. Under varje version bör du inkludera vad du lagt till eller ändrat på (added or changed) under en rubrik samt vad du tagit bort (removed) under en annan. Exempel: ***

### Version 1.0.1

#### Tillagt eller ändrat

- La till avsnitt om changelog
- La till avsnitt om kodkonventioner

#### Borttaget

- Tog bort tidigare rubriker som inte såg bra ut.
- Tog bort felaktig rubrik om innehållsförteckning

## Att bidra (Contribution)

***Inom programmeringsvärlden är det ofta populärt att man vill utveckla andras projekt och bidra till förbättring. För att underlätta detta är det bra om det i READMEn förklaras om det är tillåtet, och om det är det hur en går till väga för att kunna göra det. Detta avsnitt skulle se ut som följande:*** 

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  

Vid större förändringar önskar jag att en issue öppnas för diskussion om vad som ska förändras.

## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)

## Contact (Kontakt)

***Skriv här hur du blir kontaktad ifall det finns frågor om projektet***

Ditt Namn - @din_twitter (eller discord? annan plattform?) - email@example.com

Projektlänk: https://github.com/ditt_anv/reponamn

## Erkännanden (Acknowledgments)

***Här kan du lista resurser eller personer som har hjälpt dig med projektet. Det kan vara länkar till tutorials eller dokumentation, eller bara någon annans profil som du vill uppmärksamma. Har du inget som behöver tas här så kan du strunta i rubriken. ***

- Mamma och Pappa
- [En jättebra låt](https://www.youtube.com/watch?v=cvh0nX08nRw)
- Dan Hermansson
