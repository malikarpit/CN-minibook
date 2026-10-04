"""
Upgrade Chapter 1 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch1_path = '/Users/arpit/minibook/cn/chapters/ch01-fundamentals.html'
with open(ch1_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Network Structural Architecture
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📐</span>
      <span class="diagram-title">Figure 1.1: Structural Network Architecture — End Systems, Intermediary Devices &amp; Links</span>
    </div>
    <span class="diagram-badge">VECTOR TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ch1-1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-ch1-info" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
        <linearGradient id="cloud-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="var(--info)" stop-opacity="0.10"/>
        </linearGradient>
      </defs>

      <!-- Grid Background Subdued -->
      <rect x="10" y="10" width="900" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- HOST A (End Device - Source) -->
      <g transform="translate(30, 40)">
        <rect width="150" height="110" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <rect x="25" y="15" width="100" height="60" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
        <line x1="75" y1="75" x2="75" y2="92" stroke="var(--accent)" stroke-width="2.5"/>
        <line x1="55" y1="92" x2="95" y2="92" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="75" y="42" fill="var(--accent)" font-size="11" font-weight="700" text-anchor="middle" font-family="system-ui">HOST A (Client)</text>
        <text x="75" y="56" fill="var(--tx-muted)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">192.168.1.10</text>
        <text x="75" y="130" fill="var(--tx-primary)" font-size="12" font-weight="700" text-anchor="middle">End Device (Source)</text>
        <text x="75" y="144" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Runs Apps (L1–L7)</text>
      </g>

      <!-- LINK: Host A to Switch A -->
      <path d="M 180 95 L 235 95" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrow-ch1-1)"/>
      <text x="207" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">Cat6 UTP</text>

      <!-- LAYER 2 SWITCH A -->
      <g transform="translate(240, 50)">
        <rect width="130" height="90" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.8"/>
        <rect x="12" y="12" width="106" height="30" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <circle cx="28" cy="27" r="4" fill="var(--success)"/>
        <circle cx="44" cy="27" r="4" fill="var(--success)"/>
        <circle cx="60" cy="27" r="4" fill="var(--success)"/>
        <circle cx="76" cy="27" r="4" fill="var(--success)"/>
        <circle cx="92" cy="27" r="4" fill="var(--tx-muted)"/>
        <text x="65" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Layer-2 Switch</text>
        <text x="65" y="74" fill="var(--info)" font-size="9" text-anchor="middle" font-weight="600">Local MAC Forwarding</text>
        <text x="65" y="106" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Inspects: Layer 2 Only</text>
      </g>

      <!-- LINK: Switch A to Router A -->
      <path d="M 370 95 L 420 95" stroke="var(--info)" stroke-width="2.5" marker-end="url(#arrow-ch1-info)"/>
      <text x="395" y="85" fill="var(--info)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">GbE Fiber</text>

      <!-- ROUTER A (Gateway) -->
      <g transform="translate(425, 45)">
        <circle cx="45" cy="50" r="42" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <path d="M 25 50 L 65 50 M 45 30 L 45 70" stroke="var(--accent)" stroke-width="2"/>
        <path d="M 32 37 L 58 63 M 32 63 L 58 37" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="2,2"/>
        <text x="45" y="105" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Gateway Router R1</text>
        <text x="45" y="119" fill="var(--accent)" font-size="9" font-weight="600" text-anchor="middle">IP Path Selection (L3)</text>
      </g>

      <!-- INTERNET / WAN CLOUD -->
      <g transform="translate(260, 205)">
        <rect width="400" height="95" rx="20" fill="url(#cloud-grad)" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="6,4"/>
        <text x="200" y="32" fill="var(--accent-light)" font-size="13" font-weight="700" text-anchor="middle" letter-spacing="0.05em">WAN / INTERNET BACKBONE CLOUD</text>
        <text x="200" y="50" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">Autonomous Systems • Fiber Optic Trunks • Multi-Hop Routing</text>
        <text x="200" y="68" fill="var(--tx-muted)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">Transit Delay = d_trans + d_prop + d_queue + d_proc</text>
      </g>

      <!-- LINKS to Cloud -->
      <path d="M 470 137 L 470 205" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-ch1-1)"/>
      <path d="M 550 205 L 550 137" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-ch1-1)"/>

      <!-- ROUTER B (Remote Gateway) -->
      <g transform="translate(505, 45)">
        <circle cx="45" cy="50" r="42" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <path d="M 25 50 L 65 50 M 45 30 L 45 70" stroke="var(--accent)" stroke-width="2"/>
        <path d="M 32 37 L 58 63 M 32 63 L 58 37" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="2,2"/>
        <text x="45" y="105" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Gateway Router R2</text>
        <text x="45" y="119" fill="var(--accent)" font-size="9" font-weight="600" text-anchor="middle">Destination Edge</text>
      </g>

      <!-- LINK: Router B to Switch B -->
      <path d="M 595 95 L 645 95" stroke="var(--info)" stroke-width="2.5" marker-end="url(#arrow-ch1-info)"/>
      <text x="620" y="85" fill="var(--info)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">GbE Fiber</text>

      <!-- LAYER 2 SWITCH B -->
      <g transform="translate(650, 50)">
        <rect width="130" height="90" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.8"/>
        <rect x="12" y="12" width="106" height="30" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <circle cx="28" cy="27" r="4" fill="var(--success)"/>
        <circle cx="44" cy="27" r="4" fill="var(--success)"/>
        <circle cx="60" cy="27" r="4" fill="var(--success)"/>
        <circle cx="76" cy="27" r="4" fill="var(--success)"/>
        <circle cx="92" cy="27" r="4" fill="var(--success)"/>
        <text x="65" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Server Switch</text>
        <text x="65" y="74" fill="var(--info)" font-size="9" text-anchor="middle" font-weight="600">VLAN / Rack Aggregation</text>
        <text x="65" y="106" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Inspects: Layer 2 Only</text>
      </g>

      <!-- LINK: Switch B to Host B -->
      <path d="M 780 95 L 825 95" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrow-ch1-1)"/>
      <text x="802" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle" font-family="var(--font-mono)">Cat6A</text>

      <!-- HOST B (End Device - Server) -->
      <g transform="translate(830, 40)">
        <rect width="70" height="110" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <rect x="10" y="15" width="50" height="14" rx="2" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <circle cx="50" cy="22" r="2.5" fill="var(--success)"/>
        <rect x="10" y="35" width="50" height="14" rx="2" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <circle cx="50" cy="42" r="2.5" fill="var(--success)"/>
        <rect x="10" y="55" width="50" height="14" rx="2" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <circle cx="50" cy="62" r="2.5" fill="var(--success)"/>
        <text x="35" y="90" fill="var(--accent)" font-size="10" font-weight="700" text-anchor="middle">SERVER</text>
        <text x="35" y="130" fill="var(--tx-primary)" font-size="12" font-weight="700" text-anchor="middle">Host B</text>
        <text x="35" y="144" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Runs L1–L7</text>
      </g>

      <!-- PROTOCOL ENCAPSULATION BANNER -->
      <rect x="30" y="308" width="860" height="30" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="460" y="328" fill="var(--tx-secondary)" font-size="11" font-weight="600" text-anchor="middle">
        <tspan fill="var(--accent)" font-weight="700">PROTOCOLS IN PLAY:</tspan> Application (HTTP/TLS) ➔ Transport (TCP/UDP) ➔ Network (IP/BGP) ➔ Data Link (Ethernet) ➔ Physical (Bits on Copper/Fiber)
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Key Architectural Demarcation:</strong> End hosts process all 7 layers of the protocol stack. Switches operate exclusively up to <strong>Layer 2</strong> (forwarding frames based on MAC addresses). Routers operate up to <strong>Layer 3</strong> (forwarding packets based on IP addresses and routing tables).
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: The Five Components of Data Communication
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔩</span>
      <span class="diagram-title">Figure 1.2: The Five Components of Data Communication System</span>
    </div>
    <span class="diagram-badge">EXAM BLUEPRINT</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 880 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ch1-2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <linearGradient id="proto-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.2"/>
          <stop offset="50%" stop-color="var(--accent)" stop-opacity="0.35"/>
          <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.2"/>
        </linearGradient>
      </defs>

      <!-- Background frame -->
      <rect x="10" y="10" width="860" height="300" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- COMPONENT 5: PROTOCOL (TOP ENVELOPE) -->
      <g transform="translate(140, 25)">
        <rect width="600" height="60" rx="10" fill="url(#proto-grad)" stroke="var(--accent)" stroke-width="2"/>
        <text x="300" y="28" fill="var(--accent-light)" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.05em">COMPONENT 5: PROTOCOL</text>
        <text x="300" y="48" fill="var(--tx-secondary)" font-size="11" text-anchor="middle">Rules governing Syntax (Format), Semantics (Meaning), and Timing (Speed &amp; Sequencing)</text>
      </g>

      <!-- Protocol Sync Lines down to Sender & Receiver -->
      <path d="M 230 85 L 230 115 L 120 115 L 120 135" stroke="var(--accent)" stroke-width="1.8" stroke-dasharray="4,4" fill="none" marker-end="url(#arrow-ch1-2)"/>
      <path d="M 650 85 L 650 115 L 760 115 L 760 135" stroke="var(--accent)" stroke-width="1.8" stroke-dasharray="4,4" fill="none" marker-end="url(#arrow-ch1-2)"/>

      <!-- COMPONENT 1: SENDER (LEFT) -->
      <g transform="translate(40, 135)">
        <rect width="160" height="135" rx="12" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <circle cx="80" cy="45" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="80" y="50" font-size="20" text-anchor="middle">💻</text>
        <text x="80" y="90" fill="var(--tx-primary)" font-size="13" font-weight="700" text-anchor="middle">1. SENDER</text>
        <text x="80" y="106" fill="var(--accent)" font-size="10" font-weight="600" text-anchor="middle">(Source / Transmitter)</text>
        <text x="80" y="122" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Creates data payload</text>
      </g>

      <!-- COMPONENT 4: TRANSMISSION MEDIUM (CENTER) -->
      <g transform="translate(230, 145)">
        <!-- Channel pipe -->
        <rect width="420" height="85" rx="12" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="2"/>
        <text x="210" y="24" fill="var(--tx-primary)" font-size="12" font-weight="700" text-anchor="middle">4. TRANSMISSION MEDIUM (Channel)</text>
        <text x="210" y="38" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Guided (Twisted Pair, Coaxial, Fiber) or Unguided (Radio RF, Infrared)</text>
        
        <!-- Signal wave path inside channel -->
        <path d="M 20 62 Q 50 48, 80 62 T 140 62 T 200 62 T 260 62 T 320 62 T 380 62 T 400 62" stroke="var(--accent)" stroke-width="2" fill="none" opacity="0.4"/>
        
        <!-- COMPONENT 3: MESSAGE (TRAVELING PACKETS) -->
        <g transform="translate(130, 48)">
          <rect width="160" height="28" rx="6" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
          <text x="80" y="18" fill="#fff" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="0.04em">3. MESSAGE (Payload)</text>
        </g>
      </g>

      <!-- Transmission Flow Arrow -->
      <path d="M 200 190 L 225 190" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-ch1-2)"/>
      <path d="M 650 190 L 675 190" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-ch1-2)"/>

      <!-- COMPONENT 2: RECEIVER (RIGHT) -->
      <g transform="translate(680, 135)">
        <rect width="160" height="135" rx="12" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <circle cx="80" cy="45" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="80" y="50" font-size="20" text-anchor="middle">🖥️</text>
        <text x="80" y="90" fill="var(--tx-primary)" font-size="13" font-weight="700" text-anchor="middle">2. RECEIVER</text>
        <text x="80" y="106" fill="var(--accent)" font-size="10" font-weight="600" text-anchor="middle">(Sink / Destination)</text>
        <text x="80" y="122" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Consumes message data</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University 5-Mark Rule:</strong> A communication system cannot function if any one of the five components is missing. Even if a physical link (Medium) exists between Sender and Receiver with a Message, communication is impossible without a mutually agreed <strong>Protocol</strong>.
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Transmission Modes Comparison (Simplex vs Half-Duplex vs Full-Duplex)
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⇄</span>
      <span class="diagram-title">Figure 1.3: Data Flow Modes — Simplex, Half-Duplex, and Full-Duplex</span>
    </div>
    <span class="diagram-badge">EXAM COMPARISON</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-simp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
        <marker id="arrow-half" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--warning)" />
        </marker>
        <marker id="arrow-full" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <!-- Background Box -->
      <rect x="10" y="10" width="880" height="400" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION 1: SIMPLEX -->
      <g transform="translate(30, 25)">
        <rect width="840" height="110" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        
        <!-- Label Badge -->
        <rect x="15" y="12" width="100" height="24" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="65" y="28" fill="var(--info)" font-size="11" font-weight="700" text-anchor="middle">SIMPLEX</text>
        <text x="125" y="28" fill="var(--tx-muted)" font-size="11">Strictly Unidirectional (One-way only) • 100% Channel capacity dedicated to one direction</text>

        <!-- Device A -->
        <rect x="30" y="48" width="100" height="46" rx="6" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="80" y="70" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Transmitter</text>
        <text x="80" y="84" fill="var(--tx-muted)" font-size="9" text-anchor="middle">e.g. Keyboard</text>

        <!-- Unidirectional Arrow -->
        <path d="M 140 71 L 430 71" stroke="var(--info)" stroke-width="3" marker-end="url(#arrow-simp)"/>
        <rect x="230" y="58" width="130" height="22" rx="4" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1"/>
        <text x="295" y="73" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Only Direction: A ➔ B</text>

        <!-- Device B -->
        <rect x="440" y="48" width="100" height="46" rx="6" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="490" y="70" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Receiver</text>
        <text x="490" y="84" fill="var(--tx-muted)" font-size="9" text-anchor="middle">e.g. Monitor / TV</text>

        <!-- Real life tag -->
        <text x="560" y="72" fill="var(--tx-secondary)" font-size="11" font-weight="600">Examples: TV Broadcast, FM Radio, Keyboard ➔ CPU, GPS Satellites</text>
      </g>

      <!-- SECTION 2: HALF-DUPLEX -->
      <g transform="translate(30, 150)">
        <rect width="840" height="115" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        
        <!-- Label Badge -->
        <rect x="15" y="12" width="120" height="24" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="75" y="28" fill="var(--warning)" font-size="11" font-weight="700" text-anchor="middle">HALF-DUPLEX</text>
        <text x="145" y="28" fill="var(--tx-muted)" font-size="11">Bidirectional, but strictly ONE AT A TIME (Alternate) • Requires Turn-Taking Protocol</text>

        <!-- Station A -->
        <rect x="30" y="50" width="100" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="80" y="72" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Station A</text>
        <text x="80" y="88" fill="var(--warning)" font-size="9" font-weight="600" text-anchor="middle">Tx or Rx</text>

        <!-- Alternating Arrows -->
        <path d="M 140 64 L 430 64" stroke="var(--warning)" stroke-width="2.2" marker-end="url(#arrow-half)"/>
        <text x="285" y="60" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">Time Slot 1: A ➔ B (A Transmits, B Listens)</text>

        <path d="M 430 92 L 140 92" stroke="var(--warning)" stroke-width="2.2" stroke-dasharray="4,4" marker-end="url(#arrow-half)"/>
        <text x="285" y="106" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">Time Slot 2: B ➔ A (B Transmits, A Listens)</text>

        <!-- Station B -->
        <rect x="440" y="50" width="100" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="490" y="72" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Station B</text>
        <text x="490" y="88" fill="var(--warning)" font-size="9" font-weight="600" text-anchor="middle">Tx or Rx</text>

        <!-- Real life tag -->
        <text x="560" y="75" fill="var(--tx-secondary)" font-size="11" font-weight="600">Examples: Walkie-Talkies ("Over"), CSMA/CD Coaxial Ethernet, USB 2.0</text>
      </g>

      <!-- SECTION 3: FULL-DUPLEX -->
      <g transform="translate(30, 280)">
        <rect width="840" height="115" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        
        <!-- Label Badge -->
        <rect x="15" y="12" width="120" height="24" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="75" y="28" fill="var(--success)" font-size="11" font-weight="700" text-anchor="middle">FULL-DUPLEX</text>
        <text x="145" y="28" fill="var(--tx-muted)" font-size="11">SIMULTANEOUS Bidirectional Transmission • Separate Tx/Rx channels or frequency division</text>

        <!-- Station A -->
        <rect x="30" y="50" width="100" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="80" y="72" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Station A</text>
        <text x="80" y="88" fill="var(--success)" font-size="9" font-weight="600" text-anchor="middle">Simultaneous Tx + Rx</text>

        <!-- Concurrent Arrows -->
        <path d="M 140 66 L 430 66" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arrow-full)"/>
        <text x="285" y="61" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">Dedicated Channel 1: A ➔ B (Concurrent)</text>

        <path d="M 430 92 L 140 92" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arrow-full)"/>
        <text x="285" y="106" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">Dedicated Channel 2: B ➔ A (Concurrent)</text>

        <!-- Station B -->
        <rect x="440" y="50" width="100" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="490" y="72" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Station B</text>
        <text x="490" y="88" fill="var(--success)" font-size="9" font-weight="600" text-anchor="middle">Simultaneous Tx + Rx</text>

        <!-- Real life tag -->
        <text x="560" y="75" fill="var(--tx-secondary)" font-size="11" font-weight="600">Examples: Switched Full-Duplex Ethernet (Cat6), Mobile Phone Calls, Fiber Trunks</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Capacity Note:</strong> In Full-Duplex, the link capacity is shared or doubled (e.g. 1 Gbps full-duplex Ethernet supports 1 Gbps send AND 1 Gbps receive simultaneously, yielding 2 Gbps aggregate throughput).
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Network Criteria Triad
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📊</span>
      <span class="diagram-title">Figure 1.4: Network Evaluation Criteria — Performance, Reliability, and Security</span>
    </div>
    <span class="diagram-badge">CRITERIA TRIAD</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 880 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-triad" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <!-- Frame -->
      <rect x="10" y="10" width="860" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- CENTRAL HUB -->
      <g transform="translate(320, 20)">
        <rect width="240" height="50" rx="10" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="120" y="28" fill="var(--accent-light)" font-size="14" font-weight="800" text-anchor="middle">NETWORK CRITERIA</text>
        <text x="120" y="42" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Evaluation &amp; SLA Benchmarks</text>
      </g>

      <!-- Connecting vectors -->
      <path d="M 370 70 L 170 115" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-triad)"/>
      <path d="M 440 70 L 440 115" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-triad)"/>
      <path d="M 510 70 L 710 115" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-triad)"/>

      <!-- PILLAR 1: PERFORMANCE -->
      <g transform="translate(30, 120)">
        <rect width="250" height="190" rx="12" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="15" y="12" width="220" height="28" rx="6" fill="var(--info-dim)"/>
        <text x="125" y="31" fill="var(--info)" font-size="13" font-weight="800" text-anchor="middle">1. PERFORMANCE</text>
        <text x="25" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700">• Transit Time &amp; Response Time</text>
        <text x="25" y="85" fill="var(--tx-secondary)" font-size="10">• Throughput ($T \le B$): Useful bps</text>
        <text x="25" y="105" fill="var(--tx-secondary)" font-size="10">• Bandwidth ($R$): Link capacity</text>
        <text x="25" y="125" fill="var(--tx-secondary)" font-size="10">• Latency ($D = d_{\\text{trans}} + d_{\\text{prop}} + d_{\\text{q}} + d_{\\text{p}}$)</text>
        <text x="25" y="145" fill="var(--tx-secondary)" font-size="10">• Jitter: Packet delay variation</text>
        <text x="25" y="165" fill="var(--tx-muted)" font-size="9">Governed by: load, hardware, protocol</text>
      </g>

      <!-- PILLAR 2: RELIABILITY -->
      <g transform="translate(315, 120)">
        <rect width="250" height="190" rx="12" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="15" y="12" width="220" height="28" rx="6" fill="var(--warning-dim)"/>
        <text x="125" y="31" fill="var(--warning)" font-size="13" font-weight="800" text-anchor="middle">2. RELIABILITY</text>
        <text x="25" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700">• Failure Frequency (MTTF)</text>
        <text x="25" y="85" fill="var(--tx-secondary)" font-size="10">• Recovery Time (MTTR)</text>
        <text x="25" y="105" fill="var(--tx-secondary)" font-size="10">• Availability ($A = \\frac{\\text{MTTF}}{\\text{MTTF}+\\text{MTTR}}$)</text>
        <text x="25" y="125" fill="var(--tx-secondary)" font-size="10">• Catastrophe Resilience</text>
        <text x="25" y="145" fill="var(--tx-secondary)" font-size="10">• Redundant Links &amp; Failover</text>
        <text x="25" y="165" fill="var(--tx-muted)" font-size="9">Standard: "Five Nines" (99.999% uptime)</text>
      </g>

      <!-- PILLAR 3: SECURITY -->
      <g transform="translate(600, 120)">
        <rect width="250" height="190" rx="12" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.8"/>
        <rect x="15" y="12" width="220" height="28" rx="6" fill="var(--danger-dim)"/>
        <text x="125" y="31" fill="var(--danger)" font-size="13" font-weight="800" text-anchor="middle">3. SECURITY (CIA)</text>
        <text x="25" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700">• Confidentiality: Encryption (TLS/AES)</text>
        <text x="25" y="85" fill="var(--tx-secondary)" font-size="10">• Integrity: Tamper detection (HMAC)</text>
        <text x="25" y="105" fill="var(--tx-secondary)" font-size="10">• Availability: Defense vs DDoS</text>
        <text x="25" y="125" fill="var(--tx-secondary)" font-size="10">• Access Control &amp; Firewalls</text>
        <text x="25" y="145" fill="var(--tx-secondary)" font-size="10">• Disaster Recovery Policies</text>
        <text x="25" y="165" fill="var(--tx-muted)" font-size="9">Protects against breaches &amp; data loss</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Engineering Trade-Off:</strong> High security (deep packet inspection, heavy cryptographic handshakes) inherently increases processing latency ($d_{\\text{proc}}$), demonstrating the direct engineering trade-off between Security and Performance.
  </div>
</div>'''

# ==========================================
# 5. DIAGRAM 5: PDU Encapsulation & Decapsulation Stack
# ==========================================
svg_diagram_5 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📦</span>
      <span class="diagram-title">Figure 1.5: PDU Encapsulation &amp; Decapsulation Across the Protocol Stack</span>
    </div>
    <span class="diagram-badge">CORE EXAM CONCEPT</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 460" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-encap" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-decap" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
      </defs>

      <!-- Frame -->
      <rect x="10" y="10" width="920" height="440" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SENDER HEADER (Host A) -->
      <text x="140" y="38" fill="var(--accent)" font-size="14" font-weight="800" text-anchor="middle">SENDER: ENCAPSULATION ⬇</text>
      <path d="M 140 46 L 140 70" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-encap)"/>

      <!-- RECEIVER HEADER (Host B) -->
      <text x="800" y="38" fill="var(--info)" font-size="14" font-weight="800" text-anchor="middle">⬆ DECAPSULATION : RECEIVER</text>
      <path d="M 800 70 L 800 46" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-decap)"/>

      <!-- LAYER 5 / APPLICATION: DATA -->
      <g transform="translate(60, 75)">
        <rect width="820" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="25" y="32" fill="var(--accent)" font-size="12" font-weight="800">L7 / L5: APPLICATION</text>
        <text x="25" y="46" fill="var(--tx-muted)" font-size="10">PDU: Data / Message</text>
        
        <!-- PDU Block -->
        <rect x="230" y="12" width="460" height="32" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="460" y="32" fill="var(--accent-light)" font-size="12" font-weight="700" text-anchor="middle">APPLICATION USER DATA (HTTP Payload, JSON, Image)</text>
      </g>

      <!-- ENCAPSULATION ARROW 1 -->
      <path d="M 140 135 L 140 155" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-encap)"/>
      <path d="M 800 155 L 800 135" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-decap)"/>

      <!-- LAYER 4: TRANSPORT (SEGMENT) -->
      <g transform="translate(60, 160)">
        <rect width="820" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="25" y="32" fill="var(--info)" font-size="12" font-weight="800">L4: TRANSPORT</text>
        <text x="25" y="46" fill="var(--tx-muted)" font-size="10">PDU: Segment (TCP) / Datagram</text>

        <!-- PDU Block: Header + Data -->
        <rect x="180" y="12" width="120" height="32" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="240" y="32" fill="var(--info)" font-size="11" font-weight="700" text-anchor="middle">H4: TCP Header</text>
        <rect x="305" y="12" width="385" height="32" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="497" y="32" fill="var(--accent-light)" font-size="11" font-weight="600" text-anchor="middle">Application User Data</text>
      </g>

      <!-- ENCAPSULATION ARROW 2 -->
      <path d="M 140 220 L 140 240" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-encap)"/>
      <path d="M 800 240 L 800 220" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-decap)"/>

      <!-- LAYER 3: NETWORK (PACKET) -->
      <g transform="translate(60, 245)">
        <rect width="820" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="25" y="32" fill="var(--warning)" font-size="12" font-weight="800">L3: NETWORK</text>
        <text x="25" y="46" fill="var(--tx-muted)" font-size="10">PDU: Packet / Datagram</text>

        <!-- PDU Block: H3 + H4 + Data -->
        <rect x="140" y="12" width="110" height="32" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="195" y="32" fill="var(--warning)" font-size="11" font-weight="700" text-anchor="middle">H3: IP Header</text>
        <rect x="255" y="12" width="105" height="32" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="307" y="32" fill="var(--info)" font-size="11" font-weight="700" text-anchor="middle">H4: TCP</text>
        <rect x="365" y="12" width="325" height="32" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="527" y="32" fill="var(--accent-light)" font-size="11" font-weight="600" text-anchor="middle">Application User Data</text>
      </g>

      <!-- ENCAPSULATION ARROW 3 -->
      <path d="M 140 305 L 140 325" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-encap)"/>
      <path d="M 800 325 L 800 305" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-decap)"/>

      <!-- LAYER 2: DATA LINK (FRAME - HEADER + TRAILER) -->
      <g transform="translate(60, 330)">
        <rect width="820" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="25" y="32" fill="var(--success)" font-size="12" font-weight="800">L2: DATA LINK</text>
        <text x="25" y="46" fill="var(--tx-muted)" font-size="10">PDU: Frame (H2 + Data + T2)</text>

        <!-- Frame Block -->
        <rect x="110" y="12" width="115" height="32" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="167" y="32" fill="var(--success)" font-size="11" font-weight="700" text-anchor="middle">H2: MAC Header</text>
        <rect x="230" y="12" width="95" height="32" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="277" y="32" fill="var(--warning)" font-size="11" font-weight="700" text-anchor="middle">H3: IP</text>
        <rect x="330" y="12" width="90" height="32" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="375" y="32" fill="var(--info)" font-size="11" font-weight="700" text-anchor="middle">H4: TCP</text>
        <rect x="425" y="12" width="225" height="32" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="537" y="32" fill="var(--accent-light)" font-size="11" font-weight="600" text-anchor="middle">Application Data</text>
        
        <!-- TRAILER (FCS / CRC) -->
        <rect x="655" y="12" width="105" height="32" rx="6" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="707" y="32" fill="var(--danger)" font-size="11" font-weight="800" text-anchor="middle">T2: CRC Trailer</text>
      </g>

      <!-- LAYER 1: PHYSICAL (BITS OVER MEDIA) -->
      <g transform="translate(60, 400)">
        <rect width="820" height="34" rx="6" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="470" y="22" fill="var(--accent)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.2em">
          L1 PHYSICAL: 0 1 1 0 1 0 0 1 1 1 0 1 0 0 0 1 1 0 1 1 0 1 0 1 1 1 0 (Signals over Link)
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Why Data Link Layer Adds a Trailer (FCS):</strong> Computing a 32-bit Cyclic Redundancy Check (CRC) requires examining all preceding bits (header + payload) as they stream out through the network interface card (NIC). The checksum is calculated on-the-fly and appended at the tail as Trailer $T_2$ without buffering the entire frame first.
  </div>
</div>'''

# ==========================================
# 6. DIAGRAM 6: Latency Components & BDP Pipe (Section 1.6)
# ==========================================
svg_diagram_6 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⏱️</span>
      <span class="diagram-title">Figure 1.6: Packet Latency Timeline &amp; The Bandwidth-Delay Product (BDP) Pipe</span>
    </div>
    <span class="diagram-badge">MATHEMATICAL MODEL</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-lat" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <linearGradient id="pipe-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="var(--info)" stop-opacity="0.15"/>
        </linearGradient>
      </defs>

      <!-- Frame -->
      <rect x="10" y="10" width="900" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: THE 4 DELAY COMPONENTS -->
      <g transform="translate(30, 25)">
        <text x="10" y="20" fill="var(--accent)" font-size="13" font-weight="800">A. THE 4 DELAY COMPONENTS OF PACKET LATENCY</text>
        <text x="10" y="38" fill="var(--tx-muted)" font-size="10">End-to-End Delay Equation: D_total = d_trans + d_prop + d_queue + d_proc</text>

        <!-- Delay Block 1: d_trans -->
        <g transform="translate(10, 52)">
          <rect width="200" height="85" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
          <text x="100" y="24" fill="var(--accent)" font-size="12" font-weight="700" text-anchor="middle">Transmission Delay</text>
          <text x="100" y="44" fill="var(--tx-primary)" font-size="14" font-weight="800" text-anchor="middle" font-family="var(--font-mono)">d_trans = L / R</text>
          <text x="100" y="62" fill="var(--tx-muted)" font-size="9" text-anchor="middle">L = Packet size (bits)</text>
          <text x="100" y="75" fill="var(--tx-muted)" font-size="9" text-anchor="middle">R = Bandwidth (bps)</text>
        </g>

        <!-- Plus 1 -->
        <text x="222" y="100" fill="var(--tx-muted)" font-size="20" font-weight="700">+</text>

        <!-- Delay Block 2: d_prop -->
        <g transform="translate(240, 52)">
          <rect width="200" height="85" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
          <text x="100" y="24" fill="var(--info)" font-size="12" font-weight="700" text-anchor="middle">Propagation Delay</text>
          <text x="100" y="44" fill="var(--tx-primary)" font-size="14" font-weight="800" text-anchor="middle" font-family="var(--font-mono)">d_prop = d / s</text>
          <text x="100" y="62" fill="var(--tx-muted)" font-size="9" text-anchor="middle">d = Distance (meters)</text>
          <text x="100" y="75" fill="var(--tx-muted)" font-size="9" text-anchor="middle">s = Wave speed (~2x10^8 m/s)</text>
        </g>

        <!-- Plus 2 -->
        <text x="452" y="100" fill="var(--tx-muted)" font-size="20" font-weight="700">+</text>

        <!-- Delay Block 3: d_queue -->
        <g transform="translate(470, 52)">
          <rect width="185" height="85" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
          <text x="92" y="24" fill="var(--warning)" font-size="12" font-weight="700" text-anchor="middle">Queuing Delay</text>
          <text x="92" y="44" fill="var(--tx-primary)" font-size="14" font-weight="800" text-anchor="middle" font-family="var(--font-mono)">d_queue</text>
          <text x="92" y="62" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Buffer wait time</text>
          <text x="92" y="75" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Congestion dependent</text>
        </g>

        <!-- Plus 3 -->
        <text x="667" y="100" fill="var(--tx-muted)" font-size="20" font-weight="700">+</text>

        <!-- Delay Block 4: d_proc -->
        <g transform="translate(685, 52)">
          <rect width="165" height="85" rx="8" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.8"/>
          <text x="82" y="24" fill="var(--danger)" font-size="12" font-weight="700" text-anchor="middle">Processing Delay</text>
          <text x="82" y="44" fill="var(--tx-primary)" font-size="14" font-weight="800" text-anchor="middle" font-family="var(--font-mono)">d_proc</text>
          <text x="82" y="62" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Header lookup / CRC</text>
          <text x="82" y="75" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Microseconds scale</text>
        </g>
      </g>

      <!-- SECTION B: BANDWIDTH-DELAY PRODUCT (BDP) PIPE -->
      <g transform="translate(30, 195)">
        <text x="10" y="20" fill="var(--accent)" font-size="13" font-weight="800">B. BANDWIDTH-DELAY PRODUCT (BDP) — "BITS IN FLIGHT"</text>
        <text x="10" y="36" fill="var(--tx-muted)" font-size="10">Physical pipe analogy: Volume = Cross-Section (Bandwidth R) × Length (Propagation Delay d_prop)</text>

        <!-- Cylinder 3D Pipe -->
        <g transform="translate(40, 50)">
          <!-- Main Pipe Body -->
          <rect x="40" y="10" width="680" height="70" fill="url(#pipe-grad)" stroke="var(--accent)" stroke-width="2"/>
          
          <!-- Left Ellipse (Cross Section) -->
          <ellipse cx="40" cy="45" rx="25" ry="35" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          
          <!-- Right Ellipse (End of Pipe) -->
          <ellipse cx="720" cy="45" rx="25" ry="35" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>

          <!-- Flying Bits inside pipe -->
          <g fill="var(--accent-light)" font-family="var(--font-mono)" font-size="11" font-weight="700">
            <circle cx="120" cy="35" r="5" fill="var(--accent)"/>
            <circle cx="180" cy="55" r="5" fill="var(--accent)"/>
            <circle cx="240" cy="30" r="5" fill="var(--accent)"/>
            <circle cx="310" cy="50" r="5" fill="var(--accent)"/>
            <circle cx="380" cy="38" r="5" fill="var(--accent)"/>
            <circle cx="450" cy="58" r="5" fill="var(--accent)"/>
            <circle cx="530" cy="32" r="5" fill="var(--accent)"/>
            <circle cx="610" cy="48" r="5" fill="var(--accent)"/>
            <circle cx="670" cy="35" r="5" fill="var(--accent)"/>
          </g>

          <!-- Annotations -->
          <line x1="15" y1="10" x2="15" y2="80" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="8" y="48" fill="var(--accent)" font-size="10" font-weight="700" text-anchor="end">Bandwidth (R)</text>

          <line x1="40" y1="95" x2="720" y2="95" stroke="var(--info)" stroke-width="1.5" marker-end="url(#arrow-lat)"/>
          <text x="380" y="112" fill="var(--info)" font-size="11" font-weight="700" text-anchor="middle">Propagation Delay: d_prop = d / s</text>

          <!-- BDP Formula box -->
          <g transform="translate(760, 15)">
            <rect width="90" height="60" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
            <text x="45" y="24" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Pipe Capacity</text>
            <text x="45" y="42" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">BDP = R × d_prop</text>
          </g>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Toll-Booth Intuition:</strong> Think of <em>Transmission Delay</em> as the time it takes for a toll booth to service all cars in a caravan and release them onto the highway ($L/R$). Think of <em>Propagation Delay</em> as the time required for a car to drive at speed $s$ across the highway distance $d$ ($d/s$). A wider highway does NOT speed up the cars!
  </div>
</div>'''

# ==========================================
# 7. ADD 10-MARK UNIVERSITY MODEL ANSWERS & TRAPS
# ==========================================
uni_blueprint_html = '''
    <!-- 7. 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Comprehensive Network Fundamentals, Delay Derivations, and Media Modes</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define a Computer Network. State and explain the five foundational components of a data communication system with a neat schematic diagram. [4 Marks]<br>
          (b) Differentiate between Simplex, Half-Duplex, and Full-Duplex transmission modes with suitable circuit diagrams, bandwidth utilization comparisons, and practical real-world examples. [3 Marks]<br>
          (c) Derive the mathematical equation for total end-to-end packet latency across a path with $N$ point-to-point links and $N-1$ store-and-forward routers. Calculate the transmission and propagation delay for a 1,500-byte frame transmitted over a 10 Mbps link of length 2,500 km ($s = 2 \\times 10^8\\text{ m/s}$). [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Definition &amp; 5 Foundational Components</h4>
          <p><strong>Definition:</strong> An autonomous interconnection of geographically distributed computing systems (nodes) linked by physical or wireless communication channels to facilitate resource sharing, data transfer, and collaborative computing governed by standardized protocols.</p>
          <p><strong>The Five Components (Refer to Figure 1.2):</strong></p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Sender (Source):</strong> The terminal device that originates the information (e.g., workstation, mobile phone, sensor).</li>
            <li><strong>Receiver (Sink):</strong> The designated endpoint intended to consume the message (e.g., web server, network printer).</li>
            <li><strong>Message (Payload):</strong> The digital information being communicated (text, multimedia stream, binary telemetry).</li>
            <li><strong>Transmission Medium:</strong> The physical channel (guided Cat6, coaxial, optical fiber, or unguided radio waves) through which signals propagate.</li>
            <li><strong>Protocol:</strong> The governing set of technical rules specifying syntax, semantics, and synchronization timing required for meaningful communication.</li>
          </ol>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Transmission Modes Comparative Matrix</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Simplex</th>
                <th>Half-Duplex</th>
                <th>Full-Duplex</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Data Direction</strong></td>
                <td>Strictly unidirectional ($A \\rightarrow B$)</td>
                <td>Bidirectional, alternating ($A \\leftrightarrow B$ non-simultaneous)</td>
                <td>Simultaneous bidirectional ($A \\rightleftharpoons B$)</td>
              </tr>
              <tr>
                <td><strong>Channel Allocation</strong></td>
                <td>100% capacity in one fixed direction</td>
                <td>Shared single channel, time-divided</td>
                <td>Dual physical paths or frequency division</td>
              </tr>
              <tr>
                <td><strong>Hardware Cost</strong></td>
                <td>Lowest (single transmitter/receiver pair)</td>
                <td>Moderate (turn-around switching circuitry)</td>
                <td>Highest (duplicate transceivers and dedicated lines)</td>
              </tr>
              <tr>
                <td><strong>Standard Examples</strong></td>
                <td>Keyboard to CPU, Television Broadcast, GPS</td>
                <td>Walkie-Talkie, Coaxial Ethernet (10BASE2), USB 2.0</td>
                <td>Switched Ethernet (1000BASE-T), Mobile phones, Fiber links</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Latency Derivation &amp; Solved Numerical</h4>
          <p><strong>End-to-End Latency Derivation for $N$ Identical Links &amp; $N-1$ Intermediate Store-and-Forward Routers:</strong></p>
          <p>At each link, a packet experiences transmission delay $d_{\\text{trans}} = \\frac{L}{R}$ and propagation delay $d_{\\text{prop}} = \\frac{d}{s}$. Because routers operate on a <em>store-and-forward</em> basis, the complete packet must be received before it can be transmitted onto the next outbound link. Thus, across $N$ links:</p>
          $$D_{\\text{total}} = N \\cdot \\left( \\frac{L}{R} + \\frac{d}{s} \\right) + \\sum_{i=1}^{N-1} d_{\\text{proc}}^{(i)} + \\sum_{i=1}^{N-1} d_{\\text{queue}}^{(i)}$$
          
          <p><strong>Numerical Calculation:</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li>Packet Size: $L = 1,500\\text{ bytes} = 1,500 \\times 8 = 12,000\\text{ bits}$</li>
            <li>Link Bandwidth: $R = 10\\text{ Mbps} = 10 \\times 10^6\\text{ bps}$</li>
            <li>Distance: $d = 2,500\\text{ km} = 2.5 \\times 10^6\\text{ meters}$</li>
            <li>Propagation Speed: $s = 2 \\times 10^8\\text{ m/s}$</li>
          </ul>
          
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 10px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Step 1: Transmission Delay:</strong><br>
              $$d_{\\text{trans}} = \\frac{L}{R} = \\frac{12,000\\text{ bits}}{10 \\times 10^6\\text{ bps}} = 1.2 \\times 10^{-3}\\text{ s} = \\mathbf{1.2\\text{ ms}}$$<br>
              <strong>Step 2: Propagation Delay:</strong><br>
              $$d_{\\text{prop}} = \\frac{d}{s} = \\frac{2.5 \\times 10^6\\text{ m}}{2 \\times 10^8\\text{ m/s}} = 1.25 \\times 10^{-2}\\text{ s} = \\mathbf{12.5\\text{ ms}}$$<br>
              <strong>Step 3: Total Point-to-Point Latency (assuming negligible queuing and processing):</strong><br>
              $$D_{\\text{total}} = d_{\\text{trans}} + d_{\\text{prop}} = 1.2\\text{ ms} + 12.5\\text{ ms} = \\mathbf{13.7\\text{ ms}}$$
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 1
# ==========================================

# Replace Match 1 (Diagram 1)
m1_target = re.search(r'<h3>Structural Architecture Diagram</h3>\s*<div class="code-block">.*?</div>', content, flags=re.DOTALL)
if m1_target:
    content = content[:m1_target.start()] + '<h3>Structural Architecture Diagram</h3>\n' + svg_diagram_1 + content[m1_target.end():]
    print('Replaced Diagram 1')

# Replace Match 2 (Diagram 2)
m2_target = re.search(r'<h3>Data Communication Model</h3>\s*<div class="code-block">.*?</div>', content, flags=re.DOTALL)
if m2_target:
    content = content[:m2_target.start()] + '<h3>Data Communication Model</h3>\n' + svg_diagram_2 + content[m2_target.end():]
    print('Replaced Diagram 2')

# Replace Match 3 (Diagram 3)
m3_target = re.search(r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Transmission Modes: Signal Direction Comparison</span></div>.*?</div>', content, flags=re.DOTALL)
if m3_target:
    content = content[:m3_target.start()] + svg_diagram_3 + content[m3_target.end():]
    print('Replaced Diagram 3')

# Replace Match 4 (Diagram 4)
m4_target = re.search(r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Network Criteria Triangle</span></div>.*?</div>', content, flags=re.DOTALL)
if m4_target:
    content = content[:m4_target.start()] + svg_diagram_4 + content[m4_target.end():]
    print('Replaced Diagram 4')

# Replace Match 5 (Diagram 5)
m5_target = re.search(r'<h3>Encapsulation &amp; Decapsulation Flow Diagram</h3>\s*<div class="code-block">.*?</div>', content, flags=re.DOTALL)
if m5_target:
    content = content[:m5_target.start()] + '<h3>Encapsulation &amp; Decapsulation Flow Diagram</h3>\n' + svg_diagram_5 + content[m5_target.end():]
    print('Replaced Diagram 5')

# Insert Diagram 6 and 10-Mark Blueprint into Section 1.6
# Look for Worked Example or before Section Summary in Section 1.6
sec16_target = re.search(r'<!-- 3\. LATENCY & THE 4 DELAY COMPONENTS -->.*?<h3>3\. Total Packet Latency', content, flags=re.DOTALL)
if sec16_target:
    content = content[:sec16_target.start()] + '<!-- 3. LATENCY & THE 4 DELAY COMPONENTS -->\n' + svg_diagram_6 + '\n' + content[sec16_target.start():]
    print('Inserted Diagram 6 in Section 1.6')

# Insert 10-Mark Blueprint right before the chapter review / summary or at end of Section 1.6
summary_target = re.search(r'<div class="section-summary">', content)
if summary_target:
    content = content[:summary_target.start()] + uni_blueprint_html + '\n\n' + content[summary_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 1')

with open(ch1_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 1 successfully updated!')
