/**
 * ⚡ Arpit | glossary.js — CN MiniBook 2026
 * GlossaryManager: Auto-detects Computer Networking terms on page and shows tooltip definitions
 */
'use strict';

const GlossaryManager = (() => {
  const TERMS = {
    'PDU': 'Protocol Data Unit — the formal name for a unit of data transferred at a specific layer (Bits at L1, Frame at L2, Packet at L3, Segment at L4).',
    'SDU': 'Service Data Unit — the raw user data passed down from Layer N+1 across an interface (SAP) to Layer N before headers are attached.',
    'SAP': 'Service Access Point — the conceptual boundary port where an upper layer accesses the services of the layer beneath it (e.g., TSAP = Port number).',
    'MAC address': 'Media Access Control Address — a unique 48-bit (6-byte) physical hardware address burned into every Network Interface Card (NIC).',
    'IP address': 'Internet Protocol Address — a logical, hierarchical address (32-bit IPv4 or 128-bit IPv6) used to route packets globally across internetworks.',
    'port number': 'A 16-bit integer (0 to 65535) used at the Transport Layer to identify a specific application process running on a host.',
    'socket address': 'The combination of an IP address and a port number (e.g., 192.168.1.100:8080) uniquely defining an endpoint worldwide.',
    'simplex': 'Unidirectional communication mode where one device can only transmit and the other can only receive (e.g., TV broadcast).',
    'half-duplex': 'Bidirectional communication mode where both devices can transmit and receive, but only one at a time (e.g., walkie-talkie).',
    'full-duplex': 'Simultaneous bidirectional communication where both devices can transmit and receive concurrently (e.g., telephone call).',
    'repeater': 'A Layer 1 physical regenerator that receives an attenuated digital signal, cleans and reshapes it, and retransmits it at full voltage.',
    'hub': 'A Layer 1 multiport repeater that blindly floods electrical signals out all ports, creating 1 collision domain and 1 broadcast domain.',
    'bridge': 'A Layer 2 hardware/software device that inspects 48-bit MAC addresses, maintains a CAM table, and separates collision domains.',
    'switch': 'A high-speed Layer 2 multiport bridge using ASIC hardware switching; every single port forms an independent collision domain.',
    'router': 'An intelligent Layer 3 internetworking device that inspects logical IP addresses, routes packets, and breaks broadcast domains.',
    'gateway': 'A protocol converter operating across Layers 1–7 connecting radically incompatible network architectures (e.g., SNA to TCP/IP).',
    'modem': 'Modulator-Demodulator — converts digital binary computer signals to analog carrier waves and vice-versa.',
    'collision domain': 'A physical network segment where simultaneous transmissions by two or more devices will collide and garble each other.',
    'broadcast domain': 'The logical boundary of a network within which any broadcast frame (FF:FF:FF:FF:FF:FF) will be received by all nodes.',
    'attenuation': 'The progressive loss of signal energy and amplitude as it propagates through a transmission medium, measured in decibels (dB).',
    'distortion': 'The alteration of signal waveform shape caused by different frequency components traveling at different phase velocities.',
    'thermal noise': 'White noise caused by the random kinetic agitation of electrons in conductors; proportional to temperature and bandwidth (kTB).',
    'crosstalk': 'Electromagnetic interference caused by inductive coupling between adjacent parallel wire pairs inside a cable conduit.',
    'SNR': 'Signal-to-Noise Ratio — average signal power divided by average noise power. SNR_dB = 10 * log10(SNR).',
    'Nyquist theorem': 'C = 2B log2(L) — defines the maximum theoretical bit rate of an ideal noiseless channel with bandwidth B and L signal levels.',
    'Shannon capacity': 'C = B log2(1 + SNR) — establishes the absolute physical upper bound on the data rate of any noisy channel with thermal noise.',
    'UTP': 'Unshielded Twisted Pair — common 8-wire copper LAN cable where twisting cancels external electromagnetic interference via differential signaling.',
    'optical fiber': 'Glass transmission medium carrying data as pulses of light via Total Internal Reflection (TIR) when n_core > n_cladding.',
    'single-mode fiber': 'Optical fiber with an 8–10 μm core carrying a single axial ray of laser light; eliminates modal dispersion and reaches 100+ km.',
    'multi-mode fiber': 'Optical fiber with a 50–62.5 μm core where multiple light rays bounce at angles; limited to ~2 km by modal dispersion.',
    'Manchester encoding': 'Line coding with a mandatory mid-bit transition (Low-to-High = 1, High-to-Low = 0); self-clocking, zero DC, but uses 2x bandwidth.',
    'Differential Manchester': 'Line coding with mid-bit transition always; bit 0 has a transition at the start, bit 1 has no transition at start (Token Ring).',
    'ASK': 'Amplitude Shift Keying — digital modulation where carrier amplitude represents bits; sensitive to noise (used in fiber OOK).',
    'FSK': 'Frequency Shift Keying — digital modulation where carrier shifts between two frequencies (mark and space); higher noise immunity.',
    'PSK': 'Phase Shift Keying — digital modulation where carrier phase shifts (e.g., BPSK flips 180°; QPSK shifts 90° carrying 2 bits/symbol).',
    'QAM': 'Quadrature Amplitude Modulation — combines ASK and PSK into a 2D constellation grid (e.g., 256-QAM carries 8 bits per symbol).',
    'FDM': 'Frequency Division Multiplexing — analog technique dividing total link bandwidth into subcarrier bands separated by guard bands.',
    'TDM': 'Time Division Multiplexing — digital technique interleaving time slots (Synchronous TDM has fixed slots; Statistical TDM allocates on-demand).',
    'DWDM': 'Dense Wavelength Division Multiplexing — multiplexes 80–160+ laser wavelengths onto a single optical fiber strand, achieving terabit throughput.',
    'circuit switching': 'Switching that establishes a dedicated physical end-to-end circuit via 3 phases (setup, transfer, teardown); guaranteed bandwidth.',
    'packet switching': 'Switching where data is divided into packets that travel across intermediate switches using store-and-forward pipelining.',
    'virtual circuit': 'Connection-oriented packet switching where packets follow a pre-established logical route tagged with short VCI numbers.',
    'datagram': 'Connectionless packet switching where each packet is routed independently by intermediate routers based on destination IP.',
    'framing': 'Data Link Layer mechanism dividing the raw physical bit stream into discrete frames using count fields or delimiter flags.',
    'byte stuffing': 'Framing technique inserting an Escape (ESC) byte before naturally occurring FLAG or ESC bytes in the data payload.',
    'bit stuffing': 'Framing technique inserting a 0 bit after every five consecutive 1s in the data stream to prevent false FLAG (01111110) patterns.',
    'parity': 'Appends 1 bit to make the count of 1s even or odd; detects any odd number of bit errors, but misses even numbers of errors.',
    'checksum': 'Error detection method summing 16-bit words using one\'s complement arithmetic and inverting the sum (used in TCP/IP).',
    'CRC': 'Cyclic Redundancy Check — powerful polynomial modulo-2 binary division error detection code (CRC-32 used in Ethernet frames).',
    'Hamming distance': 'The number of bit positions in which two binary codewords differ. To detect d errors: d_min >= d+1; to correct t errors: d_min >= 2t+1.',
    'Hamming code': 'Forward Error Correcting (FEC) code with parity bits at positions 2^k (1, 2, 4, 8) capable of single-bit error correction.',
    'Stop-and-Wait': 'Elementary ARQ protocol where sender transmits 1 frame and waits for an ACK before sending the next; low efficiency on high-delay links.',
    'Go-Back-N': 'Sliding window ARQ with W_s = 2^n - 1, W_r = 1, cumulative ACKs; on timeout, sender retransmits all N outstanding frames.',
    'Selective Repeat': 'Sliding window ARQ with W_s = W_r = 2^(n-1), individual ACKs, receiver buffer; on timeout, sender retransmits ONLY the lost frame.',
    'pipelining': 'Transmitting multiple consecutive frames back-to-back before waiting for ACKs to keep the transmission channel full.',
    'piggybacking': 'Attaching an outgoing acknowledgment number into the header of a reverse-direction data frame to conserve channel bandwidth.',
    'Pure ALOHA': 'Random access protocol where stations transmit anytime without sensing; maximum throughput is 18.4% (1 / 2e).',
    'Slotted ALOHA': 'Random access protocol where stations transmit only at the start of synchronized time slots; maximum throughput is 36.8% (1 / e).',
    'CSMA': 'Carrier Sense Multiple Access — "listen before talk" protocol where stations sense carrier before transmitting.',
    'CSMA/CD': 'Carrier Sense Multiple Access with Collision Detection (Ethernet 802.3) — listens while transmitting, aborts on collision with Jam signal.',
    'CSMA/CA': 'Carrier Sense Multiple Access with Collision Avoidance (Wi-Fi 802.11) — uses IFS gaps, contention backoff, RTS/CTS, and NAV timers.',
    'hidden terminal': 'Wireless scenario where two stations cannot hear each other but both reach the same AP; simultaneous sends collide; resolved by RTS/CTS.',
    'exposed terminal': 'Wireless scenario where a station needlessly defers transmission because it hears an adjacent node transmitting to a different receiver.',
    'CDMA': 'Code Division Multiple Access — channelization technique allowing all stations to transmit simultaneously using orthogonal chip codes.',
    'SDN': 'Software-Defined Networking — decouples the Control Plane (centralized controller) from the Data Plane (forwarding switches) via OpenFlow.'
  };

  function init() {
    highlightTerms();
  }

  function highlightTerms() {
    const content = document.querySelector('.content-inner');
    if (!content) return;

    // Build regex from terms, case-insensitive
    const keys = Object.keys(TERMS).sort((a, b) => b.length - a.length);
    const regex = new RegExp(`\\b(${keys.map(k => escapeRegExp(k)).join('|')})\\b`, 'gi');

    // Walk text nodes, skipping pre, code, heading, script, style tags
    walkTextNodes(content, node => {
      const parent = node.parentNode;
      if (!parent) return;
      const tag = parent.tagName ? parent.tagName.toLowerCase() : '';
      if (['pre', 'code', 'h1', 'h2', 'h3', 'h4', 'script', 'style', 'button', 'a'].includes(tag)) return;
      if (parent.classList && parent.classList.contains('glossary-term')) return;

      const text = node.nodeValue;
      if (!regex.test(text)) return;

      regex.lastIndex = 0;
      const fragment = document.createDocumentFragment();
      let lastIdx = 0;
      let match;

      while ((match = regex.exec(text)) !== null) {
        const matchedTerm = match[0];
        const canonicalKey = keys.find(k => k.toLowerCase() === matchedTerm.toLowerCase());
        const definition = TERMS[canonicalKey];

        // Text before match
        if (match.index > lastIdx) {
          fragment.appendChild(document.createTextNode(text.substring(lastIdx, match.index)));
        }

        // Glossary wrapper
        const span = document.createElement('span');
        span.className = 'glossary-term';
        span.textContent = matchedTerm;
        span.title = definition;
        span.setAttribute('data-def', definition);
        span.onclick = (e) => {
          e.stopPropagation();
          showTooltip(span, matchedTerm, definition);
        };

        fragment.appendChild(span);
        lastIdx = regex.lastIndex;
      }

      if (lastIdx < text.length) {
        fragment.appendChild(document.createTextNode(text.substring(lastIdx)));
      }

      parent.replaceChild(fragment, node);
    });
  }

  function walkTextNodes(element, callback) {
    for (let child of Array.from(element.childNodes)) {
      if (child.nodeType === Node.TEXT_NODE) {
        callback(child);
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        walkTextNodes(child, callback);
      }
    }
  }

  function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  let tooltipEl = null;

  function showTooltip(target, term, definition) {
    removeTooltip();

    tooltipEl = document.createElement('div');
    tooltipEl.className = 'glossary-tooltip';
    tooltipEl.innerHTML = `<strong>${term}</strong><p style="margin:4px 0 0;font-size:0.85rem;color:var(--tx-secondary);">${definition}</p>`;
    document.body.appendChild(tooltipEl);

    const rect = target.getBoundingClientRect();
    const tooltipRect = tooltipEl.getBoundingClientRect();

    let top = rect.top - tooltipRect.height - 8;
    let left = rect.left + (rect.width / 2) - (tooltipRect.width / 2);

    if (top < 10) top = rect.bottom + 8;
    if (left < 10) left = 10;
    if (left + tooltipRect.width > window.innerWidth - 10) {
      left = window.innerWidth - tooltipRect.width - 10;
    }

    tooltipEl.style.top = `${top + window.scrollY}px`;
    tooltipEl.style.left = `${left + window.scrollX}px`;

    setTimeout(() => {
      document.addEventListener('click', removeTooltip, { once: true });
    }, 10);
  }

  function removeTooltip() {
    if (tooltipEl) {
      tooltipEl.remove();
      tooltipEl = null;
    }
  }

  return { init, highlightTerms };
})();

document.addEventListener('DOMContentLoaded', () => {
  GlossaryManager.init();
});
