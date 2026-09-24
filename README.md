# 🌐 CN MiniBook — Arpit | DU B.Tech CSE

> **Computer Networks** · University of Delhi · B.Tech CSE
> Complete Interactive Textbook covering Introduction to Networks, Physical Layer, and Data Link Layer + 100-Question Examination Suite.

An interactive study companion and textbook for Computer Networks covering the **complete university syllabus (Units I & II) + GATE** preparation. Built for deep learning, active recall, exam readiness, and offline self-study.

## 🌐 Live Site

Hosted on GitHub Pages → [`malikarpit.github.io/CN-minibook`](https://malikarpit.github.io/CN-minibook/)

## 📚 Curriculum & Content Coverage

| Unit / Part | Chapter | Topics Covered |
|---|---|---|
| **Unit I: Introduction** | **Ch 1: Network Fundamentals** | Definitions, 5 components, communication modes, performance/reliability/security, standards (de jure vs de facto), PDU encapsulation/decapsulation, latency components & formulas |
| **Unit I: Introduction** | **Ch 2: Types & Topologies** | PAN, LAN, MAN, WAN, Internet/Intranet/Extranet, Client-Server vs P2P, 6 Topologies (Bus, Star, Ring, Mesh, Tree, Hybrid) with formulas & matrix |
| **Unit I: Introduction** | **Ch 3: Models & Addressing** | Layering principles, full OSI 7-layer architecture, TCP/IP reference model suite, OSI vs TCP/IP, 4-tier addressing (MAC 48-bit, IP 32/128-bit, Port 16-bit, Specific) |
| **Unit I: Introduction** | **Ch 4: Devices & SDN** | 9 network devices (Hub, Switch, Router, Gateway, Bridge, etc.), collision vs broadcast domains with calculation scenarios, Software-Defined Networking (SDN) 3-tier architecture & OpenFlow |
| **Unit I: Physical Layer** | **Ch 5: Physical Fundamentals** | Data vs Signals, composite signals, harmonics, attenuation/distortion/noise, SNR & decibels, Nyquist Bit Rate, Shannon Channel Capacity theorem, worked numericals |
| **Unit I: Physical Layer** | **Ch 6: Media & Line Coding** | Guided media (Twisted Pair UTP/STP, Coaxial, Fiber Optic TIR physics), unguided media (Radio, Microwave, Infrared), Line coding (NRZ-L, NRZ-I, Manchester, Differential Manchester, 4B/5B) |
| **Unit I: Physical Layer** | **Ch 7: Modulation & Switching** | Digital modulation (ASK, FSK, PSK, QPSK, 16-QAM constellation), Multiplexing (FDM, WDM, Synchronous/Statistical TDM), Switching (Circuit, Packet, Datagram vs Virtual Circuit) |
| **Unit II: Data Link Layer** | **Ch 8: DLL Fundamentals & Error Control** | DLL design issues & services, Framing (character count, byte/bit stuffing), Error Detection (Parity, Checksum, CRC Modulo-2 polynomial division), Error Correction (Hamming distance, (7,4) code) |
| **Unit II: Data Link Layer** | **Ch 9: Protocols & Sliding Window** | Flow & error control, Stop-and-Wait ARQ, Pipelining, Go-Back-N (GBN) ARQ, Selective Repeat (SR) ARQ, window size proofs, mathematical utilization proofs |
| **Unit II: Data Link Layer** | **Ch 10: MAC Protocols & Ethernet** | Random Access (Pure/Slotted ALOHA, 1/p/non-persistent CSMA, CSMA/CD & minimum frame size proof, CSMA/CA & RTS/CTS Wi-Fi, hidden/exposed terminals), CDMA chip codes, IEEE 802.3 Ethernet frame |

## 📝 100 MCQ Examination System

- **Question Bank (`assets/js/quiz-data.js`):** 100 comprehensive questions mapped directly to the University Syllabus (Unit I: 55 Qs, Unit II: 45 Qs).
- **100 MCQ Mock Exam (`exams/mock-exam.html`):** Filterable by Part and University Units, live scoring, timer integration, solution explanations, and exam reset.
- **Custom Quiz Builder (`exams/unit-quiz.html`):** Rapid presets (Unit I & Unit II), individual chapter selection, question count controls, and instant interactive evaluation.

## 🛠️ Interactive Pedagogical Tools

- **Pomodoro Focus Timer:** Integrated study intervals with settings & distraction logging
- **Text-to-Speech (TTS):** Section-by-section and global voice read aloud with speed control
- **Notes & Highlighter:** Persistent in-page text annotations saved to local storage
- **Bookmarking System:** Instant 1-click bookmarks with quick sidebar access
- **Full-Text Search:** Ctrl+K search and command palette
- **Study Mode Toggle:** Filter by University, GATE, Advanced, or All
- **Progress Dashboard:** Scroll depth tracking, stats counter, and JSON backup/restore
- **Offline PWA:** Complete offline caching via Service Worker (`sw.js`)

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+K` | Open Search & Command Palette |
| `T` | Toggle Dark / Light Theme |
| `S` | Toggle Sidebar Navigation |
| `F` | Toggle Reading Focus Mode |
| `Ctrl+P` | Save as Clean PDF / Print |
| `Esc` | Close Active Modal / Popover |

## 🚀 Running Locally

```bash
cd cn
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```
