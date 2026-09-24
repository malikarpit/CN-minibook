#!/usr/bin/env python3
"""
apply_uni_filter.py
Minibook-wide University Syllabus Filter & Section Requirement Mapper
Maps every section across all 10 chapters strictly within section boundaries.
"""

import os
import re

BASE_DIR = '/Users/arpit/minibook/cn'

MAPPINGS = {
    "chapters/ch01-fundamentals.html": {
        "s-definition": (True, "Overview of computer networks and their importance"),
        "s-components": (True, "Overview of computer networks (5 Components of Data Communication)"),
        "s-criteria": (True, "Overview of computer networks (Performance, Reliability, Security Criteria)"),
        "s-protocols": (True, "Overview of computer networks (Protocols, De Facto & De Jure Standards)"),
        "s-encapsulation": (True, "Overview of computer networks (Protocol Data Units & Encapsulation)"),
        "s-terminology": (True, "Overview of computer networks (Bandwidth, Throughput, Latency, Jitter, RTT)"),
    },
    "chapters/ch02-types-topologies.html": {
        "s-network-types": (True, "Network types (PAN, LAN, MAN, WAN, WLAN)"),
        "s-internet-intranet": (True, "Network types (Internet, Intranet, and Extranet)"),
        "s-client-server": (True, "Network models (Client-Server vs Peer-to-Peer Models)"),
        "s-topology-intro": (True, "Network topologies (Physical vs Logical Topologies Overview)"),
        "s-bus": (True, "Network topologies (Bus Topology)"),
        "s-star": (True, "Network topologies (Star Topology)"),
        "s-ring": (True, "Network topologies (Ring Topology)"),
        "s-mesh": (True, "Network topologies (Mesh Topology & Link Calculation n(n-1)/2)"),
        "s-tree": (True, "Network topologies (Tree / Hierarchical Topology)"),
        "s-hybrid": (True, "Network topologies (Hybrid & Point-to-Point / Multipoint)"),
        "s-topology-compare": (True, "Network topologies (Grand Comparison & Selection Matrix)"),
    },
    "chapters/ch03-models-addressing.html": {
        "s-layering": (True, "OSI Reference Model & TCP/IP (Layered Architecture Principles)"),
        "s-terminology-layers": (True, "OSI Reference Model (Services, Protocols, Interfaces & SAPs)"),
        "s-osi-overview": (True, "OSI Reference Model (The 7-Layer Architecture Overview)"),
        "s-osi-physical": (True, "OSI Reference Model (Layer 1 — Physical Layer)"),
        "s-osi-datalink": (True, "OSI Reference Model (Layer 2 — Data Link Layer)"),
        "s-osi-network": (True, "OSI Reference Model (Layer 3 — Network Layer)"),
        "s-osi-transport": (True, "OSI Reference Model (Layer 4 — Transport Layer)"),
        "s-osi-session": (True, "OSI Reference Model (Layer 5 — Session Layer)"),
        "s-osi-presentation": (True, "OSI Reference Model (Layer 6 — Presentation Layer)"),
        "s-osi-application": (True, "OSI Reference Model (Layer 7 — Application Layer)"),
        "s-encap-detail": (True, "OSI Reference Model (7-Layer Encapsulation & Headers)"),
        "s-tcpip": (True, "TCP/IP reference model (The 4/5-Layer Architecture & Protocols)"),
        "s-osi-vs-tcpip": (True, "OSI Reference Model vs TCP/IP reference model (Grand Comparison)"),
        "s-addressing": (True, "Addressing (Physical MAC, Logical IP, Port & Specific Addresses)"),
        "s-summary-ch3": (True, "OSI Reference Model & Addressing (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch04-devices-sdn.html": {
        "s-repeater": (True, "Network Devices (Repeater — Layer 1 Signal Regeneration)"),
        "s-hub": (True, "Network Devices (Hub — Multiport Repeater, Collision Domains)"),
        "s-bridge": (True, "Network Devices (Bridge — Layer 2 Transparent Learning)"),
        "s-switch": (True, "Network Devices (Switch — Layer 2 Multiport Store-and-Forward)"),
        "s-router": (True, "Network Devices (Router — Layer 3 Path Determination & IP Forwarding)"),
        "s-gateway": (True, "Network Devices (Gateway — Higher-Layer Protocol Translation)"),
        "s-modem": (True, "Network Devices (Modem — Modulation & Demodulation)"),
        "s-ap": (True, "Network Devices (Access Point — 802.11 Wireless AP)"),
        "s-firewall": (True, "Network Devices (Firewall — Layer 3/4/7 Filtering & Network Security Device)"),
        "s-device-compare": (True, "Network Devices (Grand 8-Device Comparison Matrix)"),
        "s-collision-broadcast": (True, "Network Devices (Collision Domains vs Broadcast Domains)"),
        "s-sdn-intro": (True, "Introduction to software-defined networking (SDN: Decoupled Control & Data Planes)"),
        "s-sdn-arch": (True, "Introduction to software-defined networking (SDN Three-Tier Architecture & OpenFlow)"),
        "s-summary-ch4": (True, "Network Devices & SDN (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch05-physical-fundamentals.html": {
        "s-phy-purpose": (True, "Physical layer: signaling (Physical Layer Functions & Specs)"),
        "s-data-signals": (True, "Physical layer: signaling (Analog vs Digital Data and Signals)"),
        "s-periodic": (True, "Physical layer: signaling (Periodic vs Non-Periodic & Composite Signals)"),
        "s-sine-wave": (True, "Physical layer: signaling (Sine Wave: Amplitude, Frequency, Phase)"),
        "s-bitrate-baud": (True, "Physical layer: signaling (Bit Rate vs Baud Rate Formulation)"),
        "s-attenuation": (True, "Physical layer: signaling (Transmission Impairment 1: Attenuation & Decibels)"),
        "s-distortion": (True, "Physical layer: signaling (Transmission Impairment 2: Distortion & Dispersion)"),
        "s-noise": (True, "Physical layer: signaling (Transmission Impairment 3: Thermal & Induced Noise)"),
        "s-snr": (True, "Physical layer: signaling (Signal-to-Noise Ratio & SNR_dB)"),
        "s-nyquist": (True, "Physical layer: signaling (Nyquist Bit Rate Theorem for Noiseless Channels)"),
        "s-shannon": (True, "Physical layer: signaling (Shannon Capacity Theorem for Noisy Channels)"),
        "s-numerical-practice": (True, "Physical layer: signaling (Worked Numerical Problems on Capacity)"),
        "s-summary-ch5": (True, "Physical layer: signaling (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch06-media-signaling.html": {
        "s-media-overview": (True, "Physical layer: transmission media (Guided vs Unguided Classification)"),
        "s-twisted-pair": (True, "Physical layer: transmission media (Twisted Pair Cable: UTP vs STP, Categories)"),
        "s-coaxial": (True, "Physical layer: transmission media (Coaxial Cable: Baseband vs Broadband)"),
        "s-fiber": (True, "Physical layer: transmission media (Optical Fiber Cable: Total Internal Reflection)"),
        "s-radio": (True, "Physical layer: transmission media (Unguided Media: Radio Waves 3 kHz to 1 GHz)"),
        "s-microwave": (True, "Physical layer: transmission media (Unguided Media: Terrestrial & Satellite Microwaves)"),
        "s-infrared": (True, "Physical layer: transmission media (Unguided Media: Infrared Line-of-Sight)"),
        "s-satellite": (True, "Physical layer: transmission media (Unguided Media: Satellite Communication GEO/MEO/LEO)"),
        "s-media-compare": (True, "Physical layer: transmission media (Master Media Comparison Table)"),
        "s-line-coding-intro": (True, "Physical layer: signaling (Digital-to-Digital Line Coding Fundamentals)"),
        "s-nrz": (True, "Physical layer: signaling (NRZ-L & NRZ-I Line Coding)"),
        "s-manchester": (True, "Physical layer: signaling (Manchester Encoding — IEEE 802.3 Standard)"),
        "s-diff-manchester": (True, "Physical layer: signaling (Differential Manchester Encoding — Token Ring)"),
        "s-line-compare": (True, "Physical layer: signaling (Line Coding Schemes Comparison Matrix)"),
        "s-summary-ch6": (True, "Physical layer: transmission media & signaling (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch07-modulation-switching.html": {
        "s-mod-need": (True, "Physical layer: modulation and demodulation (Baseband vs Passband Need)"),
        "s-ask": (True, "Physical layer: modulation and demodulation (Amplitude Shift Keying — ASK & OOK)"),
        "s-fsk": (True, "Physical layer: modulation and demodulation (Frequency Shift Keying — FSK)"),
        "s-psk": (True, "Physical layer: modulation and demodulation (Phase Shift Keying — PSK & BPSK)"),
        "s-qpsk": (True, "Physical layer: modulation and demodulation (Quadrature Phase Shift Keying — QPSK)"),
        "s-qam": (True, "Physical layer: modulation and demodulation (Quadrature Amplitude Modulation — QAM)"),
        "s-mod-compare": (True, "Physical layer: modulation and demodulation (Digital Modulation Comparison Table)"),
        "s-multiplex-intro": (True, "Physical layer: signaling (Channel Multiplexing Concepts & Efficiency)"),
        "s-fdm": (True, "Physical layer: signaling & modulation (Frequency Division Multiplexing — FDM)"),
        "s-tdm": (True, "Physical layer: signaling & modulation (Time Division Multiplexing — Synchronous & Statistical TDM)"),
        "s-wdm": (True, "Physical layer: transmission media (Wavelength Division Multiplexing — WDM)"),
        "s-mux-compare": (True, "Physical layer: signaling (Multiplexing Techniques Comparison Matrix)"),
        "s-switching-intro": (True, "Physical layer: switching (Overview of Switching Methodologies)"),
        "s-circuit-switching": (True, "Physical layer: switching (Circuit Switching: Setup, Transfer, Teardown)"),
        "s-packet-switching": (True, "Physical layer: switching (Packet Switching: Store-and-Forward)"),
        "s-datagram-vc": (True, "Physical layer: switching (Datagram vs Virtual Circuit Approaches)"),
        "s-message-switching": (True, "Physical layer: switching (Message Switching: Store-and-Forward Principle)"),
        "s-switch-compare": (True, "Physical layer: switching (Grand Switching Comparison Matrix)"),
        "s-summary-ch7": (True, "Physical layer: modulation & switching (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch08-dll-fundamentals.html": {
        "s-dll-role": (True, "UNIT II Data link layer (Position, Functions & LLC/MAC Sublayers)"),
        "s-dll-services": (True, "UNIT II Data link layer (Services Provided to the Network Layer)"),
        "s-dll-design": (True, "UNIT II Data link layer: design issues (Framing, Flow Control, Error Control)"),
        "s-framing-intro": (True, "UNIT II Data link layer: framing (The Frame Delimiting Problem)"),
        "s-char-count": (True, "UNIT II Data link layer: framing (Character Count Method)"),
        "s-byte-stuffing": (True, "UNIT II Data link layer: framing (Byte / Character Stuffing)"),
        "s-bit-stuffing": (True, "UNIT II Data link layer: framing (Bit Stuffing & 01111110 Flag)"),
        "s-framing-compare": (True, "UNIT II Data link layer: framing (Master Framing Techniques Comparison)"),
        "s-error-types": (True, "UNIT II Data link layer: error detection and correction (Single-bit vs Burst Errors)"),
        "s-detect-vs-correct": (True, "UNIT II Data link layer: error detection and correction (Detection vs Correction Trade-Offs)"),
        "s-parity": (True, "UNIT II Data link layer: error detection and correction (Simple Parity Check)"),
        "s-2d-parity": (True, "UNIT II Data link layer: error detection and correction (Two-Dimensional Parity)"),
        "s-checksum": (True, "UNIT II Data link layer: error detection and correction (Internet Checksum Algorithm)"),
        "s-crc-theory": (True, "UNIT II Data link layer: error detection and correction (Cyclic Redundancy Check — CRC Theory & Polynomials)"),
        "s-crc-step": (True, "UNIT II Data link layer: error detection and correction (CRC Sender Step-by-Step XOR Division)"),
        "s-crc-verify": (True, "UNIT II Data link layer: error detection and correction (CRC Receiver Verification Process)"),
        "s-crc-mcq": (True, "UNIT II Data link layer: error detection and correction (CRC Exam Traps & Properties)"),
        "s-hamming-intro": (True, "UNIT II Data link layer: error detection and correction (Hamming Distance & Code Principles)"),
        "s-hamming-code": (True, "UNIT II Data link layer: error detection and correction (Hamming Code Construction 2^r >= m + r + 1)"),
        "s-hamming-detect": (True, "UNIT II Data link layer: error detection and correction (Hamming Single-Bit Error Correction Walkthrough)"),
        "s-error-compare": (True, "UNIT II Data link layer: error detection and correction (Master Error Handling Comparison)"),
        "s-summary-ch8": (True, "UNIT II Data link layer: design issues, framing & error control (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch09-protocols-sliding.html": {
        "s-why-protocols": (True, "UNIT II Data link layer: Elementary data link protocols (Flow & Error Control Need)"),
        "s-simplex-unrest": (True, "UNIT II Data link layer: Elementary data link protocols (Protocol 1: Unrestricted Simplex Protocol)"),
        "s-stop-wait-simple": (True, "UNIT II Data link layer: Elementary data link protocols (Protocol 2: Simplex Stop-and-Wait Protocol)"),
        "s-stop-wait-arq": (True, "UNIT II Data link layer: Elementary data link protocols (Protocol 3: Stop-and-Wait ARQ Protocol)"),
        "s-sw-arq-detail": (True, "UNIT II Data link layer: Elementary data link protocols (Stop-and-Wait ARQ Failure Scenarios Walkthrough)"),
        "s-sw-problems": (True, "UNIT II Data link layer: Sliding window protocols (Stop-and-Wait Inefficiency & Pipelining Motivation)"),
        "s-pipeline-intro": (True, "UNIT II Data link layer: Sliding window protocols (Concept of Pipelined Transmission)"),
        "s-sliding-window": (True, "UNIT II Data link layer: Sliding window protocols (Sliding Window Mechanics & Sequence Numbers)"),
        "s-gbn-working": (True, "UNIT II Data link layer: Sliding window protocols (Go-Back-N ARQ Protocol Working & Window Rules)"),
        "s-gbn-scenarios": (True, "UNIT II Data link layer: Sliding window protocols (Go-Back-N ARQ Failure Scenarios Walkthrough)"),
        "s-gbn-window": (True, "UNIT II Data link layer: Sliding window protocols (Go-Back-N Window Size Proof: W_s <= 2^n - 1)"),
        "s-sr-working": (True, "UNIT II Data link layer: Sliding window protocols (Selective Repeat ARQ Protocol Working & Individual ACKs)"),
        "s-sr-scenarios": (True, "UNIT II Data link layer: Sliding window protocols (Selective Repeat ARQ Failure Scenarios Walkthrough)"),
        "s-sr-window": (True, "UNIT II Data link layer: Sliding window protocols (Selective Repeat Window Size Proof: W_s <= 2^(n-1))"),
        "s-protocol-compare": (True, "UNIT II Data link layer: Elementary & Sliding window protocols (Grand Protocol Comparison)"),
        "s-throughput": (True, "UNIT II Data link layer: Sliding window protocols (Efficiency & Throughput Calculations)"),
        "s-piggybacking": (True, "UNIT II Data link layer: Elementary data link protocols (Piggybacking ACKs on Data Frames)"),
        "s-summary-ch9": (True, "UNIT II Data link layer: Elementary & Sliding window protocols (Chapter Revision & Exam Traps)"),
    },
    "chapters/ch10-mac-ethernet.html": {
        "s-mac-need": (True, "UNIT II Data link layer: MAC Protocols (The MAC Sublayer & Channel Allocation Problem)"),
        "s-pure-aloha": (True, "UNIT II Data link layer: MAC Protocols (Pure ALOHA Protocol & 18.4% Throughput Analysis)"),
        "s-slotted-aloha": (True, "UNIT II Data link layer: MAC Protocols (Slotted ALOHA Protocol & 36.8% Throughput Analysis)"),
        "s-csma-intro": (True, "UNIT II Data link layer: MAC Protocols (Carrier Sense Multiple Access — CSMA Fundamentals)"),
        "s-1-persistent": (True, "UNIT II Data link layer: MAC Protocols (1-Persistent CSMA)"),
        "s-non-persistent": (True, "UNIT II Data link layer: MAC Protocols (Non-Persistent CSMA)"),
        "s-p-persistent": (True, "UNIT II Data link layer: MAC Protocols (p-Persistent CSMA)"),
        "s-csma-cd": (True, "UNIT II Data link layer: MAC Protocols (CSMA/CD — Collision Detection & IEEE 802.3 Ethernet)"),
        "s-csma-ca": (True, "UNIT II Data link layer: MAC Protocols (CSMA/CA — Collision Avoidance & IEEE 802.11 Wi-Fi)"),
        "s-hidden-exposed": (True, "UNIT II Data link layer: MAC Protocols (Hidden & Exposed Terminal Problems in Wireless MAC)"),
        "s-cd-vs-ca": (True, "UNIT II Data link layer: MAC Protocols (Master Comparison: CSMA/CD vs CSMA/CA)"),
        "s-controlled-access": (True, "UNIT II Data link layer: MAC Protocols (Controlled Access Protocols — Reservation, Polling & Token Passing)"),
        "s-channelization": (True, "UNIT II Data link layer: MAC Protocols (Channelization Protocols — FDMA, TDMA, CDMA)"),
        "s-ethernet-basics": (True, "UNIT II Data link layer: MAC Protocols (Ethernet Standards: 10Base-T, Fast Ethernet, Gigabit Ethernet)"),
        "s-mac-address": (True, "UNIT II Data link layer: MAC Protocols (Physical MAC 48-bit Addressing & OUI Architecture)"),
        "s-ethernet-frame": (True, "UNIT II Data link layer: MAC Protocols (IEEE 802.3 Ethernet Frame Structure & Fields)"),
        "s-summary-ch10": (True, "UNIT II Data link layer: MAC Protocols (Chapter Revision & Exam Traps)"),
    },
}

TOGGLE_CARD_HTML = """  <!-- UNIVERSITY SYLLABUS FILTER SWITCH -->
  <div class="uni-mode-toggle-card">
    <div>
      <div style="font-weight:700; font-size:0.95rem; color:var(--tx-primary); display:flex; align-items:center; gap:0.4rem;">
        <span>🎓</span> University Exam Focus Filter
      </div>
      <div style="font-size:0.8rem; color:var(--tx-muted); margin-top:0.2rem;">
        Toggle between full textbook depth and core University Exam syllabus mode.
      </div>
    </div>
    <div class="uni-filter-switch">
      <button class="uni-toggle-btn active" id="filter-all-btn" data-mode="all" onclick="ModeManager.apply('all')">📚 Show All Content</button>
      <button class="uni-toggle-btn" id="filter-uni-btn" data-mode="uni" onclick="ModeManager.apply('uni')">🎓 Focus Uni Syllabus Only</button>
    </div>
  </div>
"""

def process_file(rel_path, sec_dict):
    filepath = os.path.join(BASE_DIR, rel_path)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert TOGGLE CARD if not present
    if 'uni-mode-toggle-card' not in content:
        if '<!-- TABLE OF CONTENTS -->' in content:
            content = content.replace('<!-- TABLE OF CONTENTS -->', TOGGLE_CARD_HTML + '\n  <!-- TABLE OF CONTENTS -->')
        elif '<div class="toc-card' in content:
            idx = content.find('<div class="toc-card')
            content = content[:idx] + TOGGLE_CARD_HTML + '\n  ' + content[idx:]

    # 2. Clean and update TOC items
    for sec_id, (is_uni, topic_name) in sec_dict.items():
        pattern = rf'(<a\s+href=[\"\']#{sec_id}[\"\']\s+class=[\"\']toc-item)([^\"\']*)([\"\'][^>]*>)(.*?)(</a>)'
        def replace_toc(m):
            prefix = m.group(1)
            extra_classes = m.group(2)
            suffix = m.group(3)
            inner = m.group(4)
            closing = m.group(5)

            # Strip any old uni or supp tag
            inner_clean = re.sub(r'<span class=[\"\']toc-(?:uni|supp)-tag[\"\']>.*?</span>', '', inner).strip()

            classes = extra_classes.split()
            classes = [c for c in classes if c not in ('in-uni', 'not-in-uni')]
            classes.append('in-uni')
            tag = '<span class="toc-uni-tag">🎓 Uni Core</span>'

            class_str = (' ' + ' '.join(classes)) if classes else ''
            return f'{prefix}{class_str}{suffix}{inner_clean} {tag}{closing}'

        content = re.sub(pattern, replace_toc, content, flags=re.DOTALL)

    # 3. Update sections (class and banner strictly scoped within each section)
    for sec_id, (is_uni, topic_name) in sec_dict.items():
        # Match <section id="sec_id" ...>
        m_sec = re.search(rf'(<section\b[^>]*\bid=[\"\']{sec_id}[\"\'][^>]*>)', content)
        if not m_sec:
            continue

        sec_start = m_sec.start()
        # Find closing </section>
        sec_end = content.find('</section>', sec_start)
        if sec_end == -1:
            sec_end = len(content)

        sec_chunk = content[sec_start:sec_end]

        # Fix section opening class
        open_tag = m_sec.group(1)
        open_tag_new = re.sub(r'\b(section-in-uni|section-not-in-uni)\b', '', open_tag)
        open_tag_new = re.sub(r'\s+', ' ', open_tag_new)

        if 'class="' in open_tag_new:
            open_tag_new = open_tag_new.replace('class="', 'class="section-in-uni ')
        elif "class='" in open_tag_new:
            open_tag_new = open_tag_new.replace("class='", "class='section-in-uni ")
        else:
            open_tag_new = open_tag_new[:-1] + ' class="section-in-uni">'

        sec_chunk = open_tag_new + sec_chunk[len(open_tag):]

        banner_html = f'''  <div class="uni-req-banner">
    <span class="uni-req-badge">🎓 Uni Required</span>
    <span>Required for syllabus topic: <strong>{topic_name}</strong></span>
  </div>'''

        # If non-uni banner exists, replace it
        if '<div class="non-uni-req-banner">' in sec_chunk:
            sec_chunk = re.sub(r'<div class="non-uni-req-banner">.*?</div>', banner_html.strip(), sec_chunk, count=1, flags=re.DOTALL)
        elif '<div class="uni-req-banner">' in sec_chunk:
            sec_chunk = re.sub(r'<div class="uni-req-banner">.*?</div>', banner_html.strip(), sec_chunk, count=1, flags=re.DOTALL)
        else:
            # Insert after header
            h2_idx = sec_chunk.find('</h2>')
            if h2_idx != -1:
                close_div = sec_chunk.find('</div>', h2_idx)
                if close_div != -1:
                    insert_pos = close_div + len('</div>')
                    sec_chunk = sec_chunk[:insert_pos] + '\n' + banner_html + '\n' + sec_chunk[insert_pos:]
                else:
                    insert_pos = h2_idx + len('</h2>')
                    sec_chunk = sec_chunk[:insert_pos] + '\n' + banner_html + '\n' + sec_chunk[insert_pos:]

        content = content[:sec_start] + sec_chunk + content[sec_end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Successfully processed {rel_path}")

def main():
    for rel_path, sec_dict in MAPPINGS.items():
        process_file(rel_path, sec_dict)
    print("✨ All university syllabus requirements applied flawlessly across all chapters!")

if __name__ == '__main__':
    main()
