// CN MiniBook Question Bank - 100 Questions with University Syllabus Mapping
const CN_QUIZ_DATA = [
  {
    "id": 1,
    "part": 1,
    "chapter": 1,
    "diff": "Easy",
    "q": "Which of the following is NOT one of the five fundamental components of a data communication system?",
    "options": [
      "Sender",
      "Receiver",
      "Transmission Medium",
      "Router"
    ],
    "ans": 3,
    "exp": "The five fundamental components of any data communication system are: 1. Message, 2. Sender, 3. Receiver, 4. Transmission Medium, and 5. Protocol. A Router is a specific intermediate network device, not a fundamental component of the communication model.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Overview of Networks (Components)",
    "syllabus": "University Core"
  },
  {
    "id": 2,
    "part": 1,
    "chapter": 1,
    "diff": "Easy",
    "q": "A traditional television broadcast transmission is an example of which data flow mode?",
    "options": [
      "Simplex",
      "Half-Duplex",
      "Full-Duplex",
      "Multiplex"
    ],
    "ans": 0,
    "exp": "In Simplex mode, communication is strictly unidirectional: only one entity can transmit, and the other can only receive (like a keyboard, monitor, or TV broadcast). Half-duplex allows bidirectional flow but only one at a time (walkie-talkie). Full-duplex allows simultaneous bidirectional transmission (telephone).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Overview of Networks (Transmission Modes)",
    "syllabus": "University Core"
  },
  {
    "id": 3,
    "part": 1,
    "chapter": 1,
    "diff": "Moderate",
    "q": "The three fundamental criteria that a computer network must satisfy are:",
    "options": [
      "Speed, Cost, and Aesthetics",
      "Performance, Reliability, and Security",
      "Throughput, Bandwidth, and Latency",
      "Modularity, Scalability, and Flexibility"
    ],
    "ans": 1,
    "exp": "According to standard networking literature (Forouzan), the three primary criteria a network must satisfy are Performance (measured by transit time, throughput, latency), Reliability (measured by frequency of failure, MTBF, recovery time), and Security (confidentiality, integrity, availability).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Overview of Networks (Criteria: Performance/Reliability/Security)",
    "syllabus": "University Core"
  },
  {
    "id": 4,
    "part": 1,
    "chapter": 1,
    "diff": "Moderate",
    "q": "A network standard that has not been approved by an official standards organization but has been widely adopted due to market prevalence is known as a:",
    "options": [
      "De Jure Standard",
      "De Facto Standard",
      "RFC Standard",
      "ISO Standard"
    ],
    "ans": 1,
    "exp": "'De Facto' means 'by fact' or 'by convention'\u2014standards that evolved naturally through historical market dominance without formal legislative or committee approval (e.g., QWERTY keyboard layout, early IBM PC architecture). 'De Jure' means 'by law'\u2014standards formally legislated by recognized bodies like ISO or IEEE.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Protocols & Standards (de jure vs de facto)",
    "syllabus": "University Core"
  },
  {
    "id": 5,
    "part": 1,
    "chapter": 1,
    "diff": "Easy",
    "q": "What are the three essential syntactic and operational elements of any network protocol?",
    "options": [
      "Bits, Bytes, and Packets",
      "Syntax, Semantics, and Timing",
      "Addressing, Routing, and Forwarding",
      "Hardware, Software, and Firmware"
    ],
    "ans": 1,
    "exp": "A protocol consists of three core key elements: 1. Syntax (structure or format of data), 2. Semantics (meaning of each section of bits and which action to take), and 3. Timing (when data should be sent and how fast it can be transmitted).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Delay & Latency Components",
    "syllabus": "University Core"
  },
  {
    "id": 6,
    "part": 1,
    "chapter": 2,
    "diff": "Easy",
    "q": "A network spanning across a person's workspace within a range of approximately 10 meters (using Bluetooth or Zigbee) is classified as a:",
    "options": [
      "LAN",
      "MAN",
      "PAN",
      "WAN"
    ],
    "ans": 2,
    "exp": "A PAN (Personal Area Network) covers personal operating space typically within a 10-meter radius around an individual (e.g., connecting a smartwatch, wireless earbuds, and smartphone via Bluetooth).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Types (PAN/LAN/MAN/WAN)",
    "syllabus": "University Core"
  },
  {
    "id": 7,
    "part": 1,
    "chapter": 2,
    "diff": "Moderate",
    "q": "How many physical full-duplex links are required to connect N devices in a fully connected (full-mesh) topology?",
    "options": [
      "N - 1",
      "N(N - 1)",
      "N(N - 1) / 2",
      "2^N"
    ],
    "ans": 2,
    "exp": "In a full mesh topology, every device connects to every other device. Device 1 connects to (N-1) nodes, Device 2 to (N-2), etc. Total dedicated physical duplex links = N(N - 1) / 2.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Architecture (Client-Server vs P2P)",
    "syllabus": "University Core"
  },
  {
    "id": 8,
    "part": 1,
    "chapter": 2,
    "diff": "Moderate",
    "q": "If a network has 8 devices connected in a full mesh topology, how many total physical links and how many I/O ports per device are required?",
    "options": [
      "56 links, 8 ports",
      "28 links, 7 ports",
      "28 links, 8 ports",
      "16 links, 7 ports"
    ],
    "ans": 1,
    "exp": "For N = 8 devices: Links = N(N - 1) / 2 = 8(7) / 2 = 28 links. Each device must connect to the remaining 7 devices, requiring N - 1 = 7 I/O ports per node.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Topologies (Mesh Formula & Complexity)",
    "syllabus": "University Core"
  },
  {
    "id": 9,
    "part": 1,
    "chapter": 2,
    "diff": "Easy",
    "q": "Which network topology suffers from a 'Single Point of Failure' where the failure of the central controller hub brings down the entire network?",
    "options": [
      "Ring Topology",
      "Bus Topology",
      "Star Topology",
      "Mesh Topology"
    ],
    "ans": 2,
    "exp": "In a Star topology, all nodes connect to a central hub or switch. If an individual node's cable fails, only that node goes down. But if the central hub itself fails, the entire network collapses.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Topologies (Star & Single Point of Failure)",
    "syllabus": "University Core"
  },
  {
    "id": 10,
    "part": 1,
    "chapter": 2,
    "diff": "Hard",
    "q": "In a Bus topology, what critical hardware component is installed at both ends of the main backbone cable to absorb electrical reflections?",
    "options": [
      "Attenuator",
      "Amplifier",
      "50-ohm Terminator",
      "BNC T-Connector"
    ],
    "ans": 2,
    "exp": "Terminators (typically 50-ohm resistors matching the characteristic impedance of the coaxial cable) must be attached to both physical cable ends of a bus network to absorb electrical signals and prevent reflections (standing waves) from causing collisions.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Topologies (Ring & Token Passing)",
    "syllabus": "University Core"
  },
  {
    "id": 11,
    "part": 1,
    "chapter": 2,
    "diff": "Moderate",
    "q": "A private corporate network that securely grants access to selected external business partners, vendors, or customers is known as an:",
    "options": [
      "Intranet",
      "Extranet",
      "Internet",
      "Darknet"
    ],
    "ans": 1,
    "exp": "An Intranet is strictly internal to company employees. An Extranet extends part of the internal network securely to authorized external stakeholders (vendors, suppliers, partners). The Internet is publicly open to anyone globally.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Topologies (Bus & Terminating Resistance)",
    "syllabus": "University Core"
  },
  {
    "id": 12,
    "part": 1,
    "chapter": 2,
    "diff": "Moderate",
    "q": "Which peer-to-peer (P2P) network characteristic distinguishes it fundamentally from the Client-Server model?",
    "options": [
      "Centralized database management",
      "Every node acts simultaneously as both client and server (Servent)",
      "Guaranteed 100% uptime through dedicated server hardware",
      "Master-slave hierarchy"
    ],
    "ans": 1,
    "exp": "In P2P architectures, there is no centralized dedicated server; all participating peers share equal responsibility and act as both clients (requesting files) and servers (supplying files to others).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Topologies (Comprehensive Comparison)",
    "syllabus": "University Core"
  },
  {
    "id": 13,
    "part": 1,
    "chapter": 3,
    "diff": "Easy",
    "q": "In the OSI 7-layer reference model, what is the Protocol Data Unit (PDU) at the Transport Layer?",
    "options": [
      "Packet",
      "Frame",
      "Segment",
      "Bit"
    ],
    "ans": 2,
    "exp": "PDUs across OSI layers: Layer 1 (Physical) = Bits; Layer 2 (Data Link) = Frame; Layer 3 (Network) = Packet; Layer 4 (Transport) = Segment (or Datagram for UDP); Layers 5-7 = Data / Message.",
    "uni": true,
    "unit": "Unit I",
    "topic": "OSI Reference Model (7-Layer Architecture)",
    "syllabus": "University Core"
  },
  {
    "id": 14,
    "part": 1,
    "chapter": 3,
    "diff": "Moderate",
    "q": "Which layer of the OSI model is responsible for dialog control, token management, and inserting synchronization checkpoints?",
    "options": [
      "Transport Layer",
      "Session Layer",
      "Presentation Layer",
      "Data Link Layer"
    ],
    "ans": 1,
    "exp": "The Session Layer (Layer 5) establishes, manages, and synchronizes dialogs. It manages tokens (to prevent simultaneous conflicting actions) and inserts checkpoints so that aborted data transfers can resume from the last checkpoint.",
    "uni": true,
    "unit": "Unit I",
    "topic": "OSI Reference Model (Data Link Hop-to-Hop Framing)",
    "syllabus": "University Core"
  },
  {
    "id": 15,
    "part": 1,
    "chapter": 3,
    "diff": "Moderate",
    "q": "The three primary functions associated with the Presentation Layer (Layer 6) are remembered by the acronym T-E-C. What does T-E-C stand for?",
    "options": [
      "Transmission, Error-control, Connection",
      "Translation, Encryption, Compression",
      "Topology, Encapsulation, Checkpointing",
      "Timing, Encoding, Congestion-control"
    ],
    "ans": 1,
    "exp": "The Presentation Layer handles: 1. Translation (character code/endian conversion e.g. ASCII vs EBCDIC), 2. Encryption/Decryption, and 3. Compression/Decompression.",
    "uni": true,
    "unit": "Unit I",
    "topic": "OSI Reference Model (Presentation Syntax & Translation)",
    "syllabus": "University Core"
  },
  {
    "id": 16,
    "part": 1,
    "chapter": 3,
    "diff": "Hard",
    "q": "Which statement correctly distinguishes a 'Service' from a 'Protocol' in layered network design?",
    "options": [
      "A Service is horizontal between peer machines; a Protocol is vertical between adjacent layers.",
      "A Service defines WHAT a layer provides to the layer above it; a Protocol defines HOW peer entities communicate to achieve that service.",
      "Protocols are visible to higher layers, whereas Services are hidden inside the layer.",
      "Services and Protocols are identical synonyms in ISO 7498."
    ],
    "ans": 1,
    "exp": "ISO 7498 defines: A Service is vertical\u2014what Layer N-1 provides across an interface (SAP) to Layer N on the same machine. A Protocol is horizontal\u2014the rules governing communication between peer entities at Layer N on different machines.",
    "uni": true,
    "unit": "Unit I",
    "topic": "TCP/IP Reference Model (Suite Mapping to OSI)",
    "syllabus": "University Core"
  },
  {
    "id": 17,
    "part": 1,
    "chapter": 3,
    "diff": "Moderate",
    "q": "How many layers are defined in the original ARPANET DoD TCP/IP reference model?",
    "options": [
      "7 Layers",
      "4 Layers",
      "5 Layers",
      "3 Layers"
    ],
    "ans": 1,
    "exp": "The original DoD TCP/IP model has 4 layers: 1. Network Access (Host-to-Network), 2. Internet, 3. Host-to-Host (Transport), and 4. Application. (Modern educational textbooks sometimes map it to 5 layers).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Addressing (Physical / MAC 48-bit Address)",
    "syllabus": "University Core"
  },
  {
    "id": 18,
    "part": 1,
    "chapter": 3,
    "diff": "Easy",
    "q": "What is the physical size of a standard MAC address and an IPv4 address, respectively?",
    "options": [
      "32 bits and 48 bits",
      "48 bits and 32 bits",
      "64 bits and 128 bits",
      "48 bits and 128 bits"
    ],
    "ans": 1,
    "exp": "A MAC (Ethernet) address is 48 bits (6 bytes, 12 hexadecimal digits). An IPv4 address is 32 bits (4 bytes, dotted-decimal notation). An IPv6 address is 128 bits.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Addressing (Port Numbers & Transport Multiplexing)",
    "syllabus": "University Core"
  },
  {
    "id": 19,
    "part": 1,
    "chapter": 3,
    "diff": "Hard",
    "q": "When an IP packet travels across three intermediate routers from Host A to Host B, which addresses change at every single hop?",
    "options": [
      "Source IP and Destination IP",
      "Source Port and Destination Port",
      "Source MAC and Destination MAC",
      "All addresses remain constant end-to-end"
    ],
    "ans": 2,
    "exp": "Hop-to-hop physical MAC addresses change at every single router hop because each router strips the old Layer 2 frame and encapsulates the IP packet into a new frame with new source and next-hop MACs. Logical IP and Port addresses remain unchanged end-to-end.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Encapsulation & Decapsulation (PDU Hierarchy)",
    "syllabus": "University Core"
  },
  {
    "id": 20,
    "part": 1,
    "chapter": 4,
    "diff": "Moderate",
    "q": "What is the fundamental difference between an analog Amplifier and a digital Repeater?",
    "options": [
      "Amplifiers boost signal voltage; Repeaters reduce signal voltage.",
      "Amplifiers amplify both the signal AND the accumulated noise; Repeaters regenerate a brand-new noise-free digital waveform.",
      "Repeaters operate at Layer 2; Amplifiers operate at Layer 1.",
      "Amplifiers are bidirectional; Repeaters are strictly simplex."
    ],
    "ans": 1,
    "exp": "An amplifier blindly magnifies whatever waveform enters it, amplifying the noise along with the signal. A repeater is a digital regenerator: it samples incoming pulses, determines whether bits are 0 or 1, discards the noise completely, and transmits clean, pristine new square pulses.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Devices (Hub Layer 1 & Collision Domain)",
    "syllabus": "University Core"
  },
  {
    "id": 21,
    "part": 1,
    "chapter": 4,
    "diff": "Moderate",
    "q": "An 8-port Ethernet Hub creates how many Collision Domains and how many Broadcast Domains?",
    "options": [
      "8 Collision Domains, 8 Broadcast Domains",
      "8 Collision Domains, 1 Broadcast Domain",
      "1 Collision Domain, 1 Broadcast Domain",
      "1 Collision Domain, 8 Broadcast Domains"
    ],
    "ans": 2,
    "exp": "A hub is a multiport Layer 1 repeater that blindly floods electrical signals out all ports. All ports on a hub share 1 single collision domain and 1 broadcast domain.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Devices (Switch Layer 2 & Microsegmentation)",
    "syllabus": "University Core"
  },
  {
    "id": 22,
    "part": 1,
    "chapter": 4,
    "diff": "Moderate",
    "q": "An 8-port standard Layer 2 Ethernet Switch creates how many Collision Domains and how many Broadcast Domains by default?",
    "options": [
      "8 Collision Domains, 1 Broadcast Domain",
      "1 Collision Domain, 8 Broadcast Domains",
      "8 Collision Domains, 8 Broadcast Domains",
      "1 Collision Domain, 1 Broadcast Domain"
    ],
    "ans": 0,
    "exp": "Each port on a switch is its own dedicated collision domain (8 collision domains). However, switches forward broadcast frames to all ports, so all ports share 1 single broadcast domain.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Devices (Router Layer 3 & Broadcast Domain)",
    "syllabus": "University Core"
  },
  {
    "id": 23,
    "part": 1,
    "chapter": 4,
    "diff": "Hard",
    "q": "Which switching method buffers the first 64 bytes of an Ethernet frame before forwarding, specifically to filter out collision runts without waiting for the full frame?",
    "options": [
      "Store-and-Forward",
      "Cut-Through (Fast-Forward)",
      "Fragment-Free (Modified Cut-Through)",
      "Adaptive Switching"
    ],
    "ans": 2,
    "exp": "Fragment-Free switching reads the first 64 bytes (the minimum legal collision slot window in Ethernet). If a collision occurred, the frame runt will be under 64 bytes and will be discarded immediately, avoiding forwarding damaged frames while maintaining much lower latency than Store-and-Forward.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Network Devices (Collision vs Broadcast Domain Calculation)",
    "syllabus": "University Core"
  },
  {
    "id": 24,
    "part": 1,
    "chapter": 4,
    "diff": "Hard",
    "q": "Consider a network containing 1 Router (with 3 active interfaces), 2 Switches (each with 8 ports connected to PCs), and 1 Hub (with 4 PCs). How many Broadcast Domains and Collision Domains exist in this network?",
    "options": [
      "3 Broadcast Domains, 18 Collision Domains",
      "1 Broadcast Domain, 20 Collision Domains",
      "3 Broadcast Domains, 20 Collision Domains",
      "2 Broadcast Domains, 17 Collision Domains"
    ],
    "ans": 0,
    "exp": "Broadcast Domains: Routers separate broadcast domains. 3 active router interfaces = 3 Broadcast Domains. Collision Domains: Each switch port connecting to a PC or router is 1 domain (8 + 8 = 16). The link from the router to the hub is 1 domain, and all 4 PCs on the hub share that 1 domain. 16 + 1 (hub domain) + any remaining router link = 18 total collision domains.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Introduction to SDN (Control & Data Plane Separation)",
    "syllabus": "University Core"
  },
  {
    "id": 25,
    "part": 1,
    "chapter": 4,
    "diff": "Hard",
    "q": "In Software-Defined Networking (SDN), what protocol is the industry standard Southbound API connecting the centralized Controller to the data-plane switches?",
    "options": [
      "BGP",
      "OpenFlow",
      "RESTful JSON",
      "SNMP"
    ],
    "ans": 1,
    "exp": "OpenFlow is the open standard Southbound API defined by the ONF that allows the SDN Controller (Control Plane) to program the flow tables of physical and virtual switches (Data Plane). Northbound APIs connect applications to the Controller.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Introduction to SDN (OpenFlow Protocol & Controllers)",
    "syllabus": "University Core"
  },
  {
    "id": 26,
    "part": 2,
    "chapter": 5,
    "diff": "Easy",
    "q": "What is the relationship between the period (T) and the frequency (f) of a periodic electromagnetic sine wave?",
    "options": [
      "T = 2 * pi * f",
      "T = 1 / f",
      "T = c * f",
      "T = f^2"
    ],
    "ans": 1,
    "exp": "Period (T) is the time required for one complete cycle. Frequency (f) is the number of cycles per second. They are inverse: T = 1 / f, and f = 1 / T.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (Analog vs Digital Signals)",
    "syllabus": "University Core"
  },
  {
    "id": 27,
    "part": 2,
    "chapter": 5,
    "diff": "Moderate",
    "q": "If a signal element carries 3 bits of data, and the transmission system operates at 2400 baud, what is the bit rate?",
    "options": [
      "800 bps",
      "2400 bps",
      "7200 bps",
      "19200 bps"
    ],
    "ans": 2,
    "exp": "Bit Rate = Baud Rate * bits per signal element = 2400 baud * 3 bits/symbol = 7200 bps.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (Harmonics & Bandwidth)",
    "syllabus": "University Core"
  },
  {
    "id": 28,
    "part": 2,
    "chapter": 5,
    "diff": "Moderate",
    "q": "A signal with power 100 mW passes through an attenuating cable and emerges with a power of 10 mW. What is the attenuation in decibels (dB)?",
    "options": [
      "-1 dB",
      "-10 dB",
      "-20 dB",
      "-3 dB"
    ],
    "ans": 1,
    "exp": "dB = 10 * log10(P2 / P1) = 10 * log10(10 mW / 100 mW) = 10 * log10(0.1) = 10 * (-1) = -10 dB.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Impairments (Attenuation in dB)",
    "syllabus": "University Core"
  },
  {
    "id": 29,
    "part": 2,
    "chapter": 5,
    "diff": "Moderate",
    "q": "Thermal noise (also known as Johnson-Nyquist or White Noise) is caused by which physical phenomenon?",
    "options": [
      "External lightning strikes and motor sparks",
      "Random thermal agitation of electrons inside conductor materials",
      "Electromagnetic induction between parallel twisted pairs",
      "Imperfect impedance matching at connectors"
    ],
    "ans": 1,
    "exp": "Thermal noise is generated by the random kinetic motion of electrons in all conductors at temperatures above absolute zero. It is uniformly distributed across all frequencies (white noise) and cannot be eliminated.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Impairments (SNR & Signal Quality)",
    "syllabus": "University Core"
  },
  {
    "id": 30,
    "part": 2,
    "chapter": 5,
    "diff": "Hard",
    "q": "According to Nyquist's theorem, what is the maximum theoretical bit rate of an ideal noiseless channel with bandwidth B = 4 kHz transmitting with L = 16 discrete signal levels?",
    "options": [
      "16 kbps",
      "32 kbps",
      "64 kbps",
      "128 kbps"
    ],
    "ans": 1,
    "exp": "Nyquist Capacity C = 2 * B * log2(L). Here B = 4000 Hz, L = 16 => log2(16) = 4 bits/sample. C = 2 * 4000 * 4 = 32,000 bps = 32 kbps.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Nyquist Bit Rate Formula",
    "syllabus": "University Core"
  },
  {
    "id": 31,
    "part": 2,
    "chapter": 5,
    "diff": "Hard",
    "q": "A noisy communication channel has a bandwidth of 1 MHz and a Signal-to-Noise Ratio (SNR) of 63. What is its theoretical maximum Shannon Capacity?",
    "options": [
      "6 Mbps",
      "63 Mbps",
      "8 Mbps",
      "1 Mbps"
    ],
    "ans": 0,
    "exp": "Shannon Capacity C = B * log2(1 + SNR) = 10^6 * log2(1 + 63) = 10^6 * log2(64). Since 2^6 = 64, log2(64) = 6. C = 6 * 10^6 bps = 6 Mbps.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Shannon Channel Capacity Theorem",
    "syllabus": "University Core"
  },
  {
    "id": 32,
    "part": 2,
    "chapter": 5,
    "diff": "Hard",
    "q": "An engineer is given a channel with SNR_dB = 30 dB. What value of linear SNR must be plugged into Shannon's capacity formula C = B log2(1 + SNR)?",
    "options": [
      "30",
      "300",
      "1000",
      "100"
    ],
    "ans": 2,
    "exp": "SNR_dB = 10 * log10(SNR) => 30 = 10 * log10(SNR) => log10(SNR) = 3 => linear SNR = 10^3 = 1000. Never plug the decibel value directly into Shannon's formula!",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Combined Nyquist & Shannon Limits",
    "syllabus": "University Core"
  },
  {
    "id": 33,
    "part": 2,
    "chapter": 5,
    "diff": "Moderate",
    "q": "Why is impulse noise considered the primary hazard for digital data transmission compared to analog voice?",
    "options": [
      "It has low energy spread over hours.",
      "It consists of high-energy, short-duration spikes that can completely wipe out hundreds of consecutive digital bits in a burst.",
      "It only affects fiber-optic cables.",
      "It shifts the frequency of sine waves without altering voltages."
    ],
    "ans": 1,
    "exp": "Impulse noise comes from lightning or electrical motors. In analog voice it causes an imperceptible click, but in high-speed digital communications a 1 millisecond spike destroys thousands of consecutive bits (burst error).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Bandwidth-Delay Product (BDP)",
    "syllabus": "University Core"
  },
  {
    "id": 34,
    "part": 2,
    "chapter": 5,
    "diff": "Hard",
    "q": "To transmit at 48 kbps over a noiseless channel with a bandwidth of 12 kHz, what is the minimum number of signal levels (L) required?",
    "options": [
      "2 levels",
      "4 levels",
      "8 levels",
      "16 levels"
    ],
    "ans": 1,
    "exp": "Nyquist: C = 2 * B * log2(L) => 48,000 = 2 * 12,000 * log2(L) => 48,000 = 24,000 * log2(L) => log2(L) = 2 => L = 2^2 = 4 signal levels.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Propagation vs Transmission Delay",
    "syllabus": "University Core"
  },
  {
    "id": 35,
    "part": 2,
    "chapter": 5,
    "diff": "Easy",
    "q": "A loss of 3 dB in signal power means that the signal power has been reduced to approximately what fraction of its original value?",
    "options": [
      "One-tenth (10%)",
      "One-half (50%)",
      "One-fourth (25%)",
      "Zero (0%)"
    ],
    "ans": 1,
    "exp": "dB = 10 * log10(0.5) = 10 * (-0.3010) = -3.01 dB. A 3 dB loss represents a halving (50% reduction) of signal power.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Baud Rate vs Bit Rate Modulation",
    "syllabus": "University Core"
  },
  {
    "id": 36,
    "part": 2,
    "chapter": 6,
    "diff": "Easy",
    "q": "Why are copper wire pairs in UTP cables twisted around each other?",
    "options": [
      "To increase tensile strength so the cable does not snap",
      "To ensure both wires are equally exposed to external noise, enabling differential noise cancellation",
      "To reduce cable manufacturing costs",
      "To increase the speed of electrons through the copper"
    ],
    "ans": 1,
    "exp": "Twisting ensures both wires experience identical external electromagnetic interference. The differential receiver measures (V1 - V2), so the equal induced noise (+\u0394V) cancels out completely.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Transmission Media (Twisted Pair & STP/UTP)",
    "syllabus": "University Core"
  },
  {
    "id": 37,
    "part": 2,
    "chapter": 6,
    "diff": "Moderate",
    "q": "What is the characteristic electrical impedance of Baseband coaxial cable used in early Ethernet (10Base5/10Base2)?",
    "options": [
      "75 Ohms",
      "50 Ohms",
      "100 Ohms",
      "120 Ohms"
    ],
    "ans": 1,
    "exp": "Baseband coaxial cable used for digital transmission in early Ethernet is 50 Ohms. Broadband coaxial cable used for analog cable TV (CATV) is 75 Ohms.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Transmission Media (Coaxial Cable Shielding)",
    "syllabus": "University Core"
  },
  {
    "id": 38,
    "part": 2,
    "chapter": 6,
    "diff": "Moderate",
    "q": "For Total Internal Reflection (TIR) to occur in an optical fiber, what two physical conditions must hold?",
    "options": [
      "n_core < n_cladding and angle of incidence < critical angle",
      "n_core > n_cladding and angle of incidence > critical angle",
      "Core and cladding must have identical refractive indices",
      "Light must be polarized horizontally"
    ],
    "ans": 1,
    "exp": "TIR requires: 1. The core must be optically denser than the cladding (n_core > n_cladding), and 2. The angle of incidence \u03b8_i must be greater than the critical angle \u03b8_c (sin \u03b8_c = n2 / n1).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Transmission Media (Fiber Optic & Total Internal Reflection)",
    "syllabus": "University Core"
  },
  {
    "id": 39,
    "part": 2,
    "chapter": 6,
    "diff": "Moderate",
    "q": "Which of the following is a primary characteristic of Single-Mode Fiber (SMF) compared to Multi-Mode Fiber (MMF)?",
    "options": [
      "SMF has a much larger core diameter (50 to 62.5 microns).",
      "SMF uses cheap LED light sources.",
      "SMF has an extremely narrow core (8 to 10 microns), eliminates modal dispersion, and reaches 100+ km.",
      "SMF only supports 10 Mbps speeds."
    ],
    "ans": 2,
    "exp": "Single-Mode Fiber has a microscopic core (8-10 \u03bcm) allowing only one ray/mode of light to propagate axially, eliminating modal dispersion. It uses injection laser diodes (ILD) and travels up to 100 km.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Transmission Media (Single-mode vs Multi-mode Fiber)",
    "syllabus": "University Core"
  },
  {
    "id": 40,
    "part": 2,
    "chapter": 6,
    "diff": "Easy",
    "q": "Which unguided transmission medium cannot penetrate solid walls, making it ideal for indoor remote controls and secure room-confined links?",
    "options": [
      "Radio waves",
      "Microwaves",
      "Infrared",
      "Satellite links"
    ],
    "ans": 2,
    "exp": "Infrared signals (300 GHz to 400 THz) cannot penetrate solid walls or ceilings. This prevents eavesdropping and eliminates regulatory licensing requirements.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Transmission Media (Unguided Wireless Media)",
    "syllabus": "University Core"
  },
  {
    "id": 41,
    "part": 2,
    "chapter": 6,
    "diff": "Moderate",
    "q": "What is the orbital altitude of a Geostationary Earth Orbit (GEO) communications satellite, and what is its typical round-trip propagation latency?",
    "options": [
      "500 km, ~20 ms",
      "20,200 km, ~100 ms",
      "35,786 km, ~250\u2013280 ms",
      "1,000 km, ~5 ms"
    ],
    "ans": 2,
    "exp": "GEO satellites orbit at exactly 35,786 km where their orbital speed matches Earth's rotation (24h period). Round-trip propagation delay to space and back is ~250\u2013280 ms.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (NRZ-L vs NRZ-I Line Coding)",
    "syllabus": "University Core"
  },
  {
    "id": 42,
    "part": 2,
    "chapter": 6,
    "diff": "Hard",
    "q": "In Manchester encoding (IEEE 802.3 standard), how are binary 0 and binary 1 represented?",
    "options": [
      "0 = Low-to-High transition; 1 = High-to-Low transition",
      "0 = High-to-Low transition; 1 = Low-to-High transition",
      "0 = Zero volts; 1 = +5 volts",
      "0 = No transition; 1 = Inversion at start of bit"
    ],
    "ans": 1,
    "exp": "In the official IEEE 802.3 Ethernet standard: Bit 0 is represented by a High-to-Low transition in the middle of the bit period; Bit 1 is represented by a Low-to-High transition.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (Manchester Clock Transition)",
    "syllabus": "University Core"
  },
  {
    "id": 43,
    "part": 2,
    "chapter": 6,
    "diff": "Hard",
    "q": "Why does Manchester encoding require DOUBLE the channel bandwidth compared to NRZ encoding for the exact same bit rate?",
    "options": [
      "Because it transmits 2 bits per symbol",
      "Because there is a guaranteed mid-bit transition in every bit period, doubling the maximum signaling baud rate",
      "Because it carries an extra parity bit per byte",
      "Because it operates at higher voltage levels"
    ],
    "ans": 1,
    "exp": "Manchester encoding enforces a voltage transition in the middle of every bit. For alternating bits, two transitions occur per bit period, requiring twice the baud rate and hence double the minimum channel bandwidth.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (Differential Manchester Inversion)",
    "syllabus": "University Core"
  },
  {
    "id": 44,
    "part": 2,
    "chapter": 6,
    "diff": "Hard",
    "q": "In Differential Manchester encoding (IEEE 802.5 Token Ring), what represents a binary 0?",
    "options": [
      "Absence of transition at the beginning of the bit period",
      "Presence of a transition at the beginning of the bit period",
      "No mid-bit transition",
      "A constant high voltage level"
    ],
    "ans": 1,
    "exp": "In Differential Manchester: A transition in the middle of the bit interval ALWAYS occurs (for clocking). Data is determined at the beginning: Bit 0 = Transition at the beginning; Bit 1 = No transition at the beginning.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (Bipolar AMI & DC Balance)",
    "syllabus": "University Core"
  },
  {
    "id": 45,
    "part": 2,
    "chapter": 6,
    "diff": "Moderate",
    "q": "What major signaling hazard is completely eliminated by Manchester encoding?",
    "options": [
      "Attenuation",
      "DC Component (Direct Current bias) and Loss of Synchronization",
      "Thermal noise",
      "Propagation delay"
    ],
    "ans": 1,
    "exp": "Because Manchester splits every bit into equal high and low halves, the average voltage over time is strictly zero (zero DC component) and the mid-bit transitions provide built-in clock synchronization on every bit.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Signaling (4B/5B Block Encoding)",
    "syllabus": "University Core"
  },
  {
    "id": 46,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "Why can an antenna for 2.4 GHz Wi-Fi be only ~3 cm long, while an antenna for a 3 kHz baseband audio wave would have to be 25 km tall?",
    "options": [
      "Because Wi-Fi has higher power.",
      "Because antenna physical length is proportional to wavelength (lambda / 4 = c / 4f); higher frequencies have dramatically shorter wavelengths.",
      "Because Wi-Fi uses digital modulation.",
      "Because sound waves travel faster than light."
    ],
    "ans": 1,
    "exp": "Antenna length must be roughly \u03bb/4 = c / (4f). For f = 3 kHz, \u03bb/4 = 3*10^8 / (4 * 3000) = 25,000 meters (25 km). For f = 2.4 GHz, \u03bb/4 = 3*10^8 / (4 * 2.4*10^9) = 0.031 meters (3.1 cm).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Modulation & Demodulation (ASK)",
    "syllabus": "University Core"
  },
  {
    "id": 47,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "How many bits per symbol (signal element) are transmitted in a Quadrature Phase Shift Keying (QPSK) system?",
    "options": [
      "1 bit",
      "2 bits",
      "4 bits",
      "8 bits"
    ],
    "ans": 1,
    "exp": "QPSK uses 4 distinct phase shifts (45\u00b0, 135\u00b0, 225\u00b0, 315\u00b0). Since L = 4, each symbol carries log2(4) = 2 bits (a dibit).",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Modulation & Demodulation (FSK)",
    "syllabus": "University Core"
  },
  {
    "id": 48,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "A modern 256-QAM digital cable modem transmits how many bits per constellation symbol?",
    "options": [
      "4 bits",
      "6 bits",
      "8 bits",
      "16 bits"
    ],
    "ans": 2,
    "exp": "In M-QAM, bits per symbol r = log2(M). For 256-QAM, r = log2(256) = 8 bits per symbol.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Modulation & Demodulation (BPSK Phase Shift)",
    "syllabus": "University Core"
  },
  {
    "id": 49,
    "part": 2,
    "chapter": 7,
    "diff": "Easy",
    "q": "In Frequency Division Multiplexing (FDM), what is the purpose of leaving 'Guard Bands' between adjacent subchannels?",
    "options": [
      "To increase data transmission speed",
      "To prevent overlapping frequency spectrums and eliminate inter-channel crosstalk",
      "To store buffered packets during network congestion",
      "To provide power to repeater stations"
    ],
    "ans": 1,
    "exp": "Guard bands are unused narrow slices of frequency spectrum placed between adjacent channels to accommodate practical filter roll-off and prevent overlapping crosstalk.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Modulation & Demodulation (QPSK Multi-bit Symbols)",
    "syllabus": "University Core"
  },
  {
    "id": 50,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "What is the primary inefficiency in Synchronous Time Division Multiplexing (Synchronous TDM)?",
    "options": [
      "Requires complex packet routing tables",
      "Allocated time slots travel completely empty if a connected sender has no data to transmit",
      "Cannot transmit digital signals",
      "Requires expensive optical prisms"
    ],
    "ans": 1,
    "exp": "In Synchronous TDM, time slots are fixed in rigid round-robin fashion. If an input channel is idle, its dedicated slot travels across the wire empty, wasting link capacity. Statistical TDM solves this by dynamic allocation.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Modulation & Demodulation (16-QAM Constellation)",
    "syllabus": "University Core"
  },
  {
    "id": 51,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "What optical technology multiplexes 80 to 160+ independent laser wavelengths onto a single strand of optical fiber?",
    "options": [
      "FDM",
      "T1 Carrier",
      "DWDM (Dense Wavelength Division Multiplexing)",
      "STDM"
    ],
    "ans": 2,
    "exp": "DWDM (Dense Wavelength Division Multiplexing) packs dozens of distinct laser colors spaced closely (0.4 to 0.8 nm apart) into a single fiber strand, achieving terabit-per-second capacities.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Multiplexing (Frequency-Division Multiplexing - FDM)",
    "syllabus": "University Core"
  },
  {
    "id": 52,
    "part": 2,
    "chapter": 7,
    "diff": "Easy",
    "q": "Which switching technique establishes a dedicated physical end-to-end path through three phases (setup, data transfer, teardown) before data transmission?",
    "options": [
      "Packet Switching",
      "Circuit Switching",
      "Message Switching",
      "Datagram Switching"
    ],
    "ans": 1,
    "exp": "Circuit Switching (used in traditional telephone networks) requires a dedicated physical circuit to be established, maintained for the call duration, and torn down upon completion.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Multiplexing (Wavelength-Division Multiplexing - WDM)",
    "syllabus": "University Core"
  },
  {
    "id": 53,
    "part": 2,
    "chapter": 7,
    "diff": "Moderate",
    "q": "In an Internet Datagram Packet-Switched network, how are individual packets treated by intermediate routers?",
    "options": [
      "All packets follow the exact same pre-reserved physical wire.",
      "Each packet is treated as an independent unit and routed dynamically based on current routing tables; packets may arrive out of order.",
      "Routers buffer the entire 1 GB file on hard disk before sending byte 1.",
      "Packets are converted into analog sine waves."
    ],
    "ans": 1,
    "exp": "In a datagram network (like IP), packets are independent datagrams. Each router makes independent forwarding decisions. Packets may take different paths and arrive out of order at the destination.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Multiplexing (Synchronous vs Statistical TDM)",
    "syllabus": "University Core"
  },
  {
    "id": 54,
    "part": 2,
    "chapter": 7,
    "diff": "Hard",
    "q": "Which feature is unique to Virtual Circuit Packet Switching compared to Datagram Packet Switching?",
    "options": [
      "Packets carry full 32-bit source and destination IP addresses in every header.",
      "A pre-established virtual circuit exists, packets carry short Virtual Circuit Identifiers (VCIs), and packets arrive in strict sequence.",
      "Intermediate routers maintain zero connection state memory.",
      "No connection setup phase is needed."
    ],
    "ans": 1,
    "exp": "In Virtual Circuit networks (ATM, Frame Relay, X.25), a logical connection is setup beforehand. Packets carry a small VCI header instead of full global addresses and follow the same pre-established path in order.",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Switching (Circuit Switching & Call Setup)",
    "syllabus": "University Core"
  },
  {
    "id": 55,
    "part": 2,
    "chapter": 7,
    "diff": "Hard",
    "q": "A file of size 1000 bytes is sent across 2 intermediate packet switches (3 hops total). Each link operates at 100 kbps with negligible propagation delay. If the file is sent as a single 1000-byte packet versus ten 100-byte packets, how does pipelined store-and-forward delay compare?",
    "options": [
      "Both take 240 ms.",
      "1 packet takes 240 ms; 10 pipelined packets take 96 ms.",
      "10 packets take 10 times longer than 1 packet.",
      "Pipelining does not reduce transmission time."
    ],
    "ans": 1,
    "exp": "Single packet: T_t = (1000 * 8) / 100,000 = 80 ms per hop. Over 3 hops = 3 * 80 ms = 240 ms. Ten 100-byte packets: Each packet T_t = 8 ms. First packet reaches destination after 3 hops = 24 ms. The remaining 9 packets arrive pipelined 8 ms apart = 9 * 8 ms = 72 ms. Total time = 24 + 72 = 96 ms! Pipelining cuts latency by 60%!",
    "uni": true,
    "unit": "Unit I",
    "topic": "Physical Layer: Switching (Datagram vs Virtual Circuit Packet Switching)",
    "syllabus": "University Core"
  },
  {
    "id": 56,
    "part": 3,
    "chapter": 8,
    "diff": "Easy",
    "q": "What is the primary responsibility of the Data Link Layer?",
    "options": [
      "End-to-end host packet routing across the global Internet",
      "Node-to-node (hop-to-hop) error-free frame delivery over a single physical link",
      "Process-to-process port delivery",
      "Raw bit voltage transmission"
    ],
    "ans": 1,
    "exp": "The Data Link Layer transforms a raw, noisy physical link into an apparently error-free communication facility responsible for node-to-node (hop-to-hop) frame delivery.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Design Issues & Services",
    "syllabus": "University Core"
  },
  {
    "id": 57,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "Why is Character Count framing rarely used as a standalone mechanism in modern networks?",
    "options": [
      "It requires too many check bits.",
      "A single bit error in the count field causes catastrophic loss of frame synchronization that cascades to all subsequent frames.",
      "It cannot be implemented in hardware.",
      "It only works with analog modems."
    ],
    "ans": 1,
    "exp": "If the count byte is corrupted, the receiver reads the wrong number of bytes and mistakes data for the start of the next frame. The receiver completely loses frame synchronization.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Framing (Character Count Fragility)",
    "syllabus": "University Core"
  },
  {
    "id": 58,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "In byte stuffing, if the original data payload contains the sequence: [ A, ESC, FLAG, B ], what is the stuffed sequence transmitted between the frame's boundary FLAG bytes?",
    "options": [
      "[ A, ESC, FLAG, B ]",
      "[ A, ESC, ESC, ESC, FLAG, B ]",
      "[ A, FLAG, ESC, B ]",
      "[ A, ESC, ESC, FLAG, B ]"
    ],
    "ans": 1,
    "exp": "Byte stuffing rules: Insert an ESC before every natural occurrence of FLAG or ESC in the data. For [ A, ESC, FLAG, B ], we stuff an ESC before the ESC -> [ESC, ESC], and an ESC before the FLAG -> [ESC, FLAG]. Result: [ A, ESC, ESC, ESC, FLAG, B ].",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Framing (Byte Stuffing & ESC Delimiters)",
    "syllabus": "University Core"
  },
  {
    "id": 59,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "Under standard HDLC bit stuffing, what bit sequence is transmitted on the wire for the input data string: 01111110111110?",
    "options": [
      "0111110101111100",
      "011111010111110",
      "011111001111100",
      "01111110111110"
    ],
    "ans": 0,
    "exp": "Rule: After EVERY sequence of five consecutive 1s, stuff a 0. Input: 0 1 1 1 1 1 [stuff 0] 1 0 1 1 1 1 1 [stuff 0] 0 -> Transmitted: 0111110101111100.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Framing (Bit Stuffing 01111110 Flag Delimiter)",
    "syllabus": "University Core"
  },
  {
    "id": 60,
    "part": 3,
    "chapter": 8,
    "diff": "Easy",
    "q": "A simple Even Parity check can detect what types of transmission errors?",
    "options": [
      "All double-bit errors",
      "Any odd number of bit errors (1, 3, 5, etc.)",
      "Any even number of bit errors (2, 4, 6, etc.)",
      "All burst errors of length 8"
    ],
    "ans": 1,
    "exp": "Simple parity alters its check state whenever an odd number of bits flip (1, 3, 5). If an even number of bits flip (2, 4, 6), parity remains identical and the error is missed.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (Single-Bit Parity Limit)",
    "syllabus": "University Core"
  },
  {
    "id": 61,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "How can Two-Dimensional (2D) Parity both detect AND correct a single-bit error?",
    "options": [
      "By taking the square root of the matrix",
      "The intersection of the failing Row parity and failing Column parity pinpoints the exact bit that flipped",
      "By re-requesting the frame through ARQ",
      "By converting the data to CRC"
    ],
    "ans": 1,
    "exp": "When 1 bit flips in a 2D matrix, exactly one row parity and one column parity check will fail. Their coordinate intersection identifies the corrupt bit, which is corrected by inverting it.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (Two-Dimensional Parity Matrix)",
    "syllabus": "University Core"
  },
  {
    "id": 62,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "If the generator polynomial for a CRC code is G(x) = x^4 + x + 1, how many check bits (r) will be appended to the data?",
    "options": [
      "5 bits",
      "4 bits",
      "3 bits",
      "1 bit"
    ],
    "ans": 1,
    "exp": "The number of check bits appended in CRC is always equal to the DEGREE of the generator polynomial. Here the highest exponent is 4, so r = 4 check bits (even though the divisor has 5 bits: 10011).",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (Internet 16-bit Checksum)",
    "syllabus": "University Core"
  },
  {
    "id": 63,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "Given data 1010000 and generator polynomial G(x) = x^3 + 1 (binary 1001), what is the remainder obtained from modulo-2 division to be appended as CRC?",
    "options": [
      "011",
      "100",
      "010",
      "110"
    ],
    "ans": 0,
    "exp": "Degree r = 3, append 3 zeros -> 1010000000. Divide by 1001 via XOR: 1010000000 / 1001: 1010 XOR 1001 = 0110; bring down 0 -> 1100 XOR 1001 = 0101; bring down 0 -> 1010 XOR 1001 = 0110; bring down 0 -> 1100 XOR 1001 = 0101; bring down 0 -> 1010 XOR 1001 = 0110; remainder = 011.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (CRC Modulo-2 Arithmetic)",
    "syllabus": "University Core"
  },
  {
    "id": 64,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "At the receiver, a frame protected by CRC is accepted as error-free if and only if:",
    "options": [
      "The quotient of modulo-2 division is all 1s",
      "The remainder of modulo-2 division by G(x) is exactly all 0s",
      "The checksum matches the port number",
      "The remainder equals the generator polynomial"
    ],
    "ans": 1,
    "exp": "The receiver divides the entire received codeword by G(x). If no transmission errors occurred, the remainder must be exactly ZERO.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (CRC Polynomial Divisor Degree)",
    "syllabus": "University Core"
  },
  {
    "id": 65,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "To detect d single-bit errors in any codeword, the minimum Hamming distance (d_min) of the code must be at least:",
    "options": [
      "d",
      "d + 1",
      "2d + 1",
      "2d"
    ],
    "ans": 1,
    "exp": "To detect d errors, d_min >= d + 1 (so that d bit flips cannot reach another valid codeword). To correct t errors, d_min >= 2t + 1.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Detection (CRC Undetected Burst Errors)",
    "syllabus": "University Core"
  },
  {
    "id": 66,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "To correct up to 2 single-bit errors, what is the minimum Hamming distance required?",
    "options": [
      "3",
      "4",
      "5",
      "6"
    ],
    "ans": 2,
    "exp": "Correction formula: d_min >= 2t + 1. For t = 2 errors: d_min >= 2(2) + 1 = 5.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Correction (Hamming Distance Minimum Distance)",
    "syllabus": "University Core"
  },
  {
    "id": 67,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "According to Hamming's redundancy formula 2^r >= m + r + 1, how many parity bits (r) are required to protect m = 4 data bits?",
    "options": [
      "2 bits",
      "3 bits",
      "4 bits",
      "5 bits"
    ],
    "ans": 1,
    "exp": "For m = 4: If r = 2: 2^2 = 4 >= 4 + 2 + 1 = 7 (False). If r = 3: 2^3 = 8 >= 4 + 3 + 1 = 8 (True! 8 >= 8). Thus r = 3 parity bits are required, creating a (7, 4) Hamming code.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Correction (Hamming Inequality 2^p >= m + p + 1)",
    "syllabus": "University Core"
  },
  {
    "id": 68,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "In a 7-bit Hamming code with bit positions 1 to 7, which bit positions are designated as Parity Bits?",
    "options": [
      "Positions 1, 2, and 3",
      "Positions 1, 2, and 4",
      "Positions 5, 6, and 7",
      "Positions 2, 4, and 6"
    ],
    "ans": 1,
    "exp": "In Hamming code, all bit positions that are powers of 2 (2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8...) are reserved exclusively for parity bits. For a 7-bit code, positions 1, 2, and 4 are parity bits.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Correction (Hamming (7,4) Code Parity Matrix)",
    "syllabus": "University Core"
  },
  {
    "id": 69,
    "part": 3,
    "chapter": 8,
    "diff": "Hard",
    "q": "If a receiver calculates a Hamming syndrome value of S_4 S_2 S_1 = 110 (binary 6), what action does the receiver take?",
    "options": [
      "Discards the frame because 6 errors occurred",
      "Inverts the bit at bit position 6 to correct the single-bit error",
      "Requests a full retransmission",
      "Accepts the frame as error-free"
    ],
    "ans": 1,
    "exp": "The non-zero syndrome directly identifies the 1-based bit position of the single-bit error. A syndrome of 110_2 = 6 means bit position 6 was corrupted; the receiver simply flips bit 6 to correct it.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Correction (Syndrome Error Localization)",
    "syllabus": "University Core"
  },
  {
    "id": 70,
    "part": 3,
    "chapter": 8,
    "diff": "Moderate",
    "q": "What type of arithmetic is used by the Internet Checksum in IPv4, TCP, and UDP?",
    "options": [
      "Standard two's complement arithmetic",
      "One's complement addition with end-around carry",
      "CRC polynomial division",
      "Reed-Solomon matrix algebra"
    ],
    "ans": 1,
    "exp": "The Internet Checksum uses 16-bit one's complement addition. Any carry bit emerging from the most significant bit (bit 16) is wrapped around and added to the least significant bit.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Data Link Layer: Error Control (FEC vs ARQ)",
    "syllabus": "University Core"
  },
  {
    "id": 71,
    "part": 3,
    "chapter": 9,
    "diff": "Easy",
    "q": "In Stop-and-Wait ARQ, what sequence numbers are assigned to frames?",
    "options": [
      "0 to 15",
      "Alternating 0 and 1",
      "0 to 255",
      "Random 16-bit numbers"
    ],
    "ans": 1,
    "exp": "Because Stop-and-Wait has only one frame in flight at any time, a 1-bit sequence number alternating between 0 and 1 is sufficient to distinguish new frames from retransmitted duplicates.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Elementary Data Link Protocols (Utopian Simplex Protocol)",
    "syllabus": "University Core"
  },
  {
    "id": 72,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "In Stop-and-Wait ARQ, if an ACK frame sent by the receiver is lost in transit, what happens?",
    "options": [
      "The network enters a permanent deadlock.",
      "The sender's timer expires, it retransmits the frame; the receiver detects the duplicate sequence number, discards the duplicate, and resends the ACK.",
      "The receiver retransmits the data frame.",
      "The network layer aborts the connection."
    ],
    "ans": 1,
    "exp": "The sender's timer expires and it retransmits the frame. The receiver sees a sequence number matching the frame it just processed, realizes the ACK was lost, drops the duplicate payload, and re-acknowledges.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Elementary Data Link Protocols (Stop-and-Wait Flow Control)",
    "syllabus": "University Core"
  },
  {
    "id": 73,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "The efficiency of Stop-and-Wait ARQ is given by eta = 1 / (1 + 2a). What is the parameter 'a'?",
    "options": [
      "a = T_transmission / T_propagation",
      "a = T_propagation / T_transmission",
      "a = Window size / Bandwidth",
      "a = Number of parity bits"
    ],
    "ans": 1,
    "exp": "The parameter 'a' is defined as the ratio of propagation delay to transmission time: a = T_p / T_t = (d / v) / (L / B).",
    "uni": true,
    "unit": "Unit II",
    "topic": "Elementary Data Link Protocols (Stop-and-Wait ARQ Sequence Bits)",
    "syllabus": "University Core"
  },
  {
    "id": 74,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "A channel has T_t = 1 ms and T_p = 49.5 ms. What is the link utilization using Stop-and-Wait ARQ?",
    "options": [
      "1%",
      "2%",
      "10%",
      "50%"
    ],
    "ans": 0,
    "exp": "a = T_p / T_t = 49.5 / 1 = 49.5. Efficiency eta = 1 / (1 + 2a) = 1 / (1 + 2*49.5) = 1 / (1 + 99) = 1 / 100 = 0.01 = 1%.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Elementary Data Link Protocols (Stop-and-Wait Utilization 1/(1+2a))",
    "syllabus": "University Core"
  },
  {
    "id": 75,
    "part": 3,
    "chapter": 9,
    "diff": "Easy",
    "q": "What is the receiver window size (W_r) in the Go-Back-N protocol?",
    "options": [
      "W_r = N",
      "W_r = 1",
      "W_r = 2^n - 1",
      "W_r = 2^(n-1)"
    ],
    "ans": 1,
    "exp": "In Go-Back-N, the receiver window size is strictly 1. The receiver only ever accepts the single frame it is next expecting; any out-of-order frame is discarded.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Pipelining Concept)",
    "syllabus": "University Core"
  },
  {
    "id": 76,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "In Go-Back-N, if Frame 3 is lost in transit while Frames 0, 1, 2, 4, 5 are sent, what happens at the receiver when Frame 4 arrives?",
    "options": [
      "The receiver buffers Frame 4 and waits for Frame 3.",
      "The receiver discards Frame 4 and resends an acknowledgment for Frame 2.",
      "The receiver sends a NAK for Frame 4.",
      "The receiver accepts Frame 4 and forwards it to the Network layer."
    ],
    "ans": 1,
    "exp": "Because W_r = 1, the receiver only wants Frame 3. When Frame 4 arrives out-of-order, it is discarded immediately, and the receiver re-sends ACK 2 (acknowledging the last in-order frame).",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Go-Back-N Sender Window 2^m - 1)",
    "syllabus": "University Core"
  },
  {
    "id": 77,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "If sequence numbers in Go-Back-N are represented using n bits, what is the MAXIMUM allowable sender window size (W_s)?",
    "options": [
      "2^n",
      "2^n - 1",
      "2^(n-1)",
      "n"
    ],
    "ans": 1,
    "exp": "In Go-Back-N, W_s <= 2^n - 1. If W_s = 2^n were permitted and all ACKs were lost, the sender's retransmissions would wrap around and be indistinguishable from brand new frames.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Go-Back-N Receiver Window W_R = 1)",
    "syllabus": "University Core"
  },
  {
    "id": 78,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "What type of acknowledgments are used in Go-Back-N?",
    "options": [
      "Individual ACKs for each frame",
      "Cumulative ACKs (ACK n acknowledges all frames up to n - 1)",
      "Negative acknowledgments only",
      "No ACKs are used"
    ],
    "ans": 1,
    "exp": "Go-Back-N uses Cumulative ACKs: an ACK(n) confirms that all frames with sequence numbers up to n - 1 have been received in order.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Go-Back-N Cumulative ACKs)",
    "syllabus": "University Core"
  },
  {
    "id": 79,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "In Selective Repeat (SR) ARQ, what is the receiver window size (W_r)?",
    "options": [
      "W_r = 1",
      "W_r = W_s (equal to sender window size)",
      "W_r = 2^n",
      "W_r = 0"
    ],
    "ans": 1,
    "exp": "In Selective Repeat, W_r = W_s > 1. The receiver maintains a buffer to store undamaged out-of-order frames within its window.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Go-Back-N Retransmission Overhead)",
    "syllabus": "University Core"
  },
  {
    "id": 80,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "If sequence numbers in Selective Repeat ARQ are represented by n = 4 bits, what is the MAXIMUM allowable sender window size?",
    "options": [
      "16",
      "15",
      "8",
      "4"
    ],
    "ans": 2,
    "exp": "In Selective Repeat: W_s + W_r <= 2^n. Since W_s = W_r, 2*W_s <= 2^n => W_s <= 2^(n-1). For n = 4: W_s <= 2^(4-1) = 2^3 = 8.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Selective Repeat Sender Window 2^(m-1))",
    "syllabus": "University Core"
  },
  {
    "id": 81,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "What happens in Selective Repeat when the sender's retransmission timer for Frame 2 expires?",
    "options": [
      "The sender retransmits all frames starting from Frame 2 up to the window boundary.",
      "The sender retransmits ONLY Frame 2.",
      "The receiver flushes its buffer.",
      "The sender terminates the connection."
    ],
    "ans": 1,
    "exp": "Selective Repeat retransmits ONLY the specific unacknowledged or timed-out frame (Frame 2). Frames 3, 4, 5 that were already buffered by the receiver are NOT retransmitted.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Selective Repeat Receiver Window W_R = W_S)",
    "syllabus": "University Core"
  },
  {
    "id": 82,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "To achieve 100% link utilization (efficiency = 1.0) in a sliding window protocol where a = 14.5, what is the minimum sender window size (N) required?",
    "options": [
      "15",
      "29",
      "30",
      "60"
    ],
    "ans": 2,
    "exp": "For 100% utilization: N >= 1 + 2a = 1 + 2(14.5) = 1 + 29 = 30 frames.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Selective Repeat NAK Handling)",
    "syllabus": "University Core"
  },
  {
    "id": 83,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "What is 'Piggybacking' in bidirectional sliding window protocols?",
    "options": [
      "Sending two identical data frames together for redundancy",
      "Temporarily delaying an outgoing ACK to attach it to the header of the next reverse data frame",
      "Compressing data headers using gzip",
      "Using multiple physical cables simultaneously"
    ],
    "ans": 1,
    "exp": "Piggybacking delays sending an acknowledgment frame so it can be inserted into the ACK field of an outgoing reverse data frame, saving link bandwidth by avoiding dedicated empty ACK frames.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Selective Repeat Buffer Storage)",
    "syllabus": "University Core"
  },
  {
    "id": 84,
    "part": 3,
    "chapter": 9,
    "diff": "Moderate",
    "q": "Between Go-Back-N and Selective Repeat, which protocol requires more memory buffers and complex logic at the RECEIVER?",
    "options": [
      "Go-Back-N",
      "Selective Repeat",
      "Both have identical receiver complexity",
      "Neither requires receiver buffers"
    ],
    "ans": 1,
    "exp": "Selective Repeat requires substantial memory buffers and sorting logic at the receiver to store, track, and resequence out-of-order frames before passing them in-order to the Network layer.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (GBN vs SR Mathematical Utilization)",
    "syllabus": "University Core"
  },
  {
    "id": 85,
    "part": 3,
    "chapter": 9,
    "diff": "Hard",
    "q": "In Go-Back-N with 3-bit sequence numbers, the sender window size is set to the maximum allowed. What is W_s?",
    "options": [
      "8",
      "7",
      "4",
      "3"
    ],
    "ans": 1,
    "exp": "For n = 3 bits: Maximum W_s = 2^n - 1 = 2^3 - 1 = 8 - 1 = 7.",
    "uni": true,
    "unit": "Unit II",
    "topic": "Sliding Window Protocols (Piggybacking Bidirectional ACKs)",
    "syllabus": "University Core"
  },
  {
    "id": 86,
    "part": 3,
    "chapter": 10,
    "diff": "Easy",
    "q": "What is the maximum theoretical channel throughput of Pure ALOHA?",
    "options": [
      "18.4% (1 / 2e)",
      "36.8% (1 / e)",
      "50.0%",
      "100%"
    ],
    "ans": 0,
    "exp": "Pure ALOHA throughput S = G * e^(-2G). Maximum throughput occurs at G = 0.5: S_max = 1 / (2e) \u2248 0.184 = 18.4%.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Pure ALOHA Maximum Throughput 18.4%)",
    "syllabus": "University Core"
  },
  {
    "id": 87,
    "part": 3,
    "chapter": 10,
    "diff": "Easy",
    "q": "What is the maximum theoretical channel throughput of Slotted ALOHA, and how does it compare to Pure ALOHA?",
    "options": [
      "18.4%, identical to Pure ALOHA",
      "36.8% (1 / e), exactly double that of Pure ALOHA",
      "50.0%",
      "73.6%"
    ],
    "ans": 1,
    "exp": "Slotted ALOHA throughput S = G * e^(-G). Maximum throughput occurs at G = 1.0: S_max = 1 / e \u2248 0.368 = 36.8%, exactly doubling Pure ALOHA because the collision window is halved from 2*T_fr to 1*T_fr.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Slotted ALOHA Maximum Throughput 36.8%)",
    "syllabus": "University Core"
  },
  {
    "id": 88,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "In 1-Persistent CSMA, what does a station do when it senses the channel and finds it BUSY?",
    "options": [
      "Transmits immediately with 100% power",
      "Waits a random backoff time before sensing again",
      "Continues listening continuously to the wire and transmits immediately the very instant the channel becomes idle",
      "Sends a Jam signal"
    ],
    "ans": 2,
    "exp": "1-Persistent CSMA is greedy: if busy, it continuously listens to the wire and transmits with probability 1.0 the instant the channel becomes idle.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (ALOHA Vulnerable Period Comparison)",
    "syllabus": "University Core"
  },
  {
    "id": 89,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "In CSMA/CD (Ethernet), why must a transmitting station enforce a MINIMUM frame size?",
    "options": [
      "To prevent preamble drift in transceivers",
      "To ensure the station is still actively transmitting when a collision signal from the farthest node returns, guaranteeing collision detection",
      "To satisfy the IP MTU requirement",
      "To allow enough room for the CRC-32 checksum"
    ],
    "ans": 1,
    "exp": "If a frame is too small (transmission finishes in less than 2*T_p), a collision occurring near the destination will arrive back at the sender AFTER it has stopped transmitting. The sender would falsely believe transmission succeeded!",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA 1-Persistent, Non-Persistent, p-Persistent)",
    "syllabus": "University Core"
  },
  {
    "id": 90,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "A 10 Mbps CSMA/CD Ethernet network has a maximum round-trip propagation delay (2 * T_p) of 51.2 microseconds. What is the minimum frame size?",
    "options": [
      "256 bits (32 bytes)",
      "512 bits (64 bytes)",
      "1024 bits (128 bytes)",
      "1518 bytes"
    ],
    "ans": 1,
    "exp": "L_min = 2 * T_p * Bandwidth = 51.2 * 10^-6 s * 10 * 10^6 bps = 512 bits = 64 bytes. This is the origin of the universal 64-byte minimum Ethernet frame size.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CD Collision Detection Mechanism)",
    "syllabus": "University Core"
  },
  {
    "id": 91,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "In CSMA/CD, what is the purpose of the 32-bit 'Jam Signal' transmitted upon detecting a collision?",
    "options": [
      "To reboot the intermediate switches",
      "To ensure that all other transmitting and receiving stations on the bus detect the collision and abort",
      "To encrypt the damaged packet",
      "To reset the router's routing table"
    ],
    "ans": 1,
    "exp": "When collision is detected, the transmitting node sends a 32-bit Jam Signal of deliberate high-frequency noise to ensure all other stations on the cable detect the collision and discard the fragments.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CD Minimum Frame Size Formula Lmin = 2*Tp*B)",
    "syllabus": "University Core"
  },
  {
    "id": 92,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "Under the Binary Exponential Backoff algorithm in Ethernet, after 3 consecutive collisions, what is the range of random slots k from which the station picks its backoff delay?",
    "options": [
      "0 to 3",
      "0 to 7",
      "0 to 8",
      "0 to 15"
    ],
    "ans": 1,
    "exp": "After i collisions, k is chosen randomly from [0, 2^i - 1]. For i = 3: range is [0, 2^3 - 1] = [0, 8 - 1] = 0 to 7.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CD Binary Exponential Backoff Algorithm)",
    "syllabus": "University Core"
  },
  {
    "id": 93,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "Why is CSMA/CD NOT used in wireless Wi-Fi networks (IEEE 802.11)?",
    "options": [
      "Wireless signals travel too fast for collision detection.",
      "A wireless transmitting antenna radiates high local power that drowns out incoming signals; a station cannot hear collisions while transmitting.",
      "Wi-Fi does not use radio frequencies.",
      "Wireless networks do not have MAC addresses."
    ],
    "ans": 1,
    "exp": "In wireless communications, transmitting energy is thousands of times stronger than incoming received energy. A transmitter cannot hear a weak collision signal while transmitting. Wi-Fi must use Collision Avoidance (CSMA/CA).",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CA Collision Avoidance in 802.11 Wi-Fi)",
    "syllabus": "University Core"
  },
  {
    "id": 94,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "In CSMA/CA, how does the RTS/CTS mechanism resolve the Hidden Terminal problem?",
    "options": [
      "By boosting transmission power to penetrate all walls",
      "The receiving Access Point broadcasts a CTS frame; hidden nodes hear the CTS and defer transmission via their NAV timer",
      "By switching to infrared frequencies",
      "By converting CSMA/CA into CSMA/CD"
    ],
    "ans": 1,
    "exp": "Node A sends RTS to AP. The AP responds with a broadcast CTS. Even though hidden Node C cannot hear Node A, it CAN hear the AP's CTS, reads the NAV duration, and defers its transmission, preventing a collision.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CA Interframe Spaces: DIFS vs SIFS)",
    "syllabus": "University Core"
  },
  {
    "id": 95,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "In CDMA, two chip sequences C1 and C2 are orthogonal if their normalized inner product equals:",
    "options": [
      "1",
      "0",
      "-1",
      "Infinity"
    ],
    "ans": 1,
    "exp": "By definition of mathematical orthogonality, the inner (dot) product of two distinct chip codes C1 . C2 = 0. The inner product of a code with itself is C1 . C1 = 1.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (CSMA/CA RTS/CTS Virtual Carrier Sensing & NAV)",
    "syllabus": "University Core"
  },
  {
    "id": 96,
    "part": 3,
    "chapter": 10,
    "diff": "Easy",
    "q": "What are the minimum and maximum frame sizes of a standard IEEE 802.3 Ethernet frame (excluding preamble and SFD)?",
    "options": [
      "32 bytes and 1024 bytes",
      "64 bytes and 1518 bytes",
      "46 bytes and 1500 bytes",
      "64 bytes and 65535 bytes"
    ],
    "ans": 1,
    "exp": "Minimum Ethernet frame size is 64 bytes (Header 14B + min payload 46B + FCS 4B). Maximum frame size is 1518 bytes (Header 14B + max payload/MTU 1500B + FCS 4B). Preamble (7B) and SFD (1B) are physical framing elements.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Hidden Terminal & Exposed Terminal Problems)",
    "syllabus": "University Core"
  },
  {
    "id": 97,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "If the data payload handed down to the Data Link Layer from IPv4 is only 20 bytes long, what does the Ethernet MAC layer do?",
    "options": [
      "Discards the packet as illegal",
      "Pads the payload with 26 bytes of zeros to meet the minimum 46-byte payload requirement",
      "Transmits the 20-byte packet without padding",
      "Waits for more data from the network layer"
    ],
    "ans": 1,
    "exp": "Ethernet requires a minimum frame of 64 bytes, meaning the payload must be at least 64 - 18 = 46 bytes. If the payload is only 20 bytes, the MAC layer appends 26 bytes of padding zeros.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Controlled Access: Reservation & Polling)",
    "syllabus": "University Core"
  },
  {
    "id": 98,
    "part": 3,
    "chapter": 10,
    "diff": "Moderate",
    "q": "Which of the following is a Controlled Access protocol where a special supervisory frame circulates in a logical ring, and only the holding station may transmit?",
    "options": [
      "Pure ALOHA",
      "Token Passing (IEEE 802.5)",
      "CSMA/CD",
      "FDMA"
    ],
    "ans": 1,
    "exp": "Token Passing (Token Ring IEEE 802.5 and Token Bus IEEE 802.4) circulates a token frame. Only the token holder transmits, eliminating collisions and providing deterministic bounded delay.",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Channelization: CDMA Orthogonal Chip Codes)",
    "syllabus": "University Core"
  },
  {
    "id": 99,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "In a 48-bit MAC address, how can you determine whether the address is a Unicast or a Multicast address?",
    "options": [
      "Check the last bit of the 48-bit address",
      "Check the least significant bit (bit 0) of the first byte: 0 = Unicast, 1 = Multicast",
      "Unicast addresses are always all 0s",
      "Multicast addresses start with 255"
    ],
    "ans": 1,
    "exp": "The least significant bit of the first byte (I/G bit) determines transmission scope: if 0, it is an individual Unicast address; if 1, it is a Group / Multicast address (e.g. 01:00:5E:...).",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (IEEE 802.3 Ethernet Frame Format & 46-1500 MTU)",
    "syllabus": "University Core"
  },
  {
    "id": 100,
    "part": 3,
    "chapter": 10,
    "diff": "Hard",
    "q": "What is the 1-byte Start Frame Delimiter (SFD) bit pattern in an IEEE 802.3 Ethernet frame?",
    "options": [
      "01111110",
      "10101010",
      "10101011",
      "11111111"
    ],
    "ans": 2,
    "exp": "In IEEE 802.3 Ethernet, the 7-byte preamble consists of alternating 10101010 bytes. The 8th byte is the SFD (Start Frame Delimiter), which has the pattern 10101011 (ending with two consecutive 1s to signal the start of destination MAC address bytes).",
    "uni": true,
    "unit": "Unit II",
    "topic": "MAC Protocols (Ethernet Preamble & Start Frame Delimiter SFD)",
    "syllabus": "University Core"
  }
];

if (typeof window !== 'undefined') {
  window.CN_QUIZ_DATA = CN_QUIZ_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CN_QUIZ_DATA;
}
