# mtaa-sip-proxy

In this assignment, we were supposed to use any library to create a proxy server that will enable phone calls between two (or more) SIP clients.

I implemented the assignment in Python 3.9. I used the [PySipFullProxy](https://github.com/tirfil/PySipFullProxy) library and the freely available [linphone](https://www.linphone.org) client.

### proxy supports:
- [x] Participant registration
- [x] Dialing, ringing, accepting and ending a call
- [x] Video call
- [x] Redirection
- [x] Conference call
- [x] I also changed some SIP status codes

### pcap files:
- register.pcap -> contains the registration of two clients
- call.pcapng -> contains successful, unsuccessful (Busy here, Decline), does not contain RTP packets
- hovor_rtp.pcapng -> contains a standard call between a device on which there is a proxy, it is a bit confusing, but there are also RTP packets
- videocall.pcapng -> contains a video call between two devices, without RTP
- videocall_rtp.pcapng –> same as call_rtp.pcapng
- forwarding.pcapng -> contains call forwarding
- conference_call.pcapng -> contains a conference call between three participants
