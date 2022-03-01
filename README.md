# mtaa-sip-proxy
## Jakub Povinec

V tomto zadaní sme mali pomocou ľubovoľnej knižnice vytvoriť proxy server, ktorý umožní telefonovanie medzi dvomi (alebo viacerými) SIP klientami. 

Zadanie som implementoval v jazyku Python 3.9.7. Použil som knižnicu [PySipFullProxy](https://github.com/tirfil/PySipFullProxy) a voľne dostupný klient [linphone](https://www.linphone.org). 

Proxy podporuje:
- [x] Registráciu účastníka
- [x] Vytáčanie, zvonenie, prijatie a ukončenie hovoru
- [x] Videohovor
- [x] Presmerovanie 
- [x] Konferenčný hovor
- [x] Taktiež som zmenil niektoré SIP stavové kódy

### pcap súbory
- register.pcap -> obsahuje registráciu dvoch klientov
- hovor.pcapng -> obsahuje úspešný, neúspešný (Busy here, Decline), neobsahuje RTP packety
- hovor_rtp.pcapng -> obsahuje štandardný hovor medzi zariadením na ktorom je proxy, je to trochu neprehľadné ale sú tam aj RTP packety
- videohovor.pcapng -> obsahuje videohovor medzi dvomi zariadeniami, bez RTP
- videohovor_rtp.pcapng –> rovnako ako hovor_rtp.pcapng
- presmerovanie.pcapng -> obsahuje presmerovanie hovoru
- konferencny_hovor.pcapng -> obsahuje konferenčný hovor medzi tromi učastníkmi

