"""
Upgrade Chapter 10 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch10_path = '/Users/arpit/minibook/cn/chapters/ch10-mac-ethernet.html'
with open(ch10_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: ALOHA Vulnerability Windows & Throughput Curves
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📊</span>
      <span class="diagram-title">Figure 10.1: Random Access Protocols — Pure vs. Slotted ALOHA Vulnerability Windows &amp; Throughput Curves</span>
    </div>
    <span class="diagram-badge">MAC PROTOCOL ANALYSIS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: PURE ALOHA VULNERABLE PERIOD = 2 * T_fr -->
      <g transform="translate(30, 25)">
        <rect width="420" height="155" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <text x="210" y="24" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">
          A. PURE ALOHA: VULNERABLE TIME = 2 · T_fr
        </text>

        <!-- Timeline axis -->
        <g transform="translate(30, 50)">
          <line x1="20" y1="50" x2="350" y2="50" stroke="var(--border)" stroke-width="1.5"/>
          
          <!-- Vulnerable Time Span Bracket: [t0 - Tfr, t0 + Tfr] -->
          <rect x="60" y="10" width="240" height="70" rx="4" fill="rgba(248, 113, 113, 0.12)" stroke="var(--danger)" stroke-width="1.5" stroke-dasharray="4,2"/>
          <text x="180" y="24" fill="var(--danger)" font-size="9" font-weight="800" text-anchor="middle">
            VULNERABLE PERIOD = 2 · T_fr (Collision if any frame begins here!)
          </text>

          <!-- Frame Target: [t0, t0 + Tfr] -->
          <rect x="180" y="32" width="120" height="35" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="240" y="54" fill="var(--accent-light)" font-size="10" font-weight="800" text-anchor="middle">Target Frame</text>

          <!-- Time markers -->
          <line x1="60" y1="45" x2="60" y2="55" stroke="var(--tx-muted)" stroke-width="2"/>
          <text x="60" y="70" fill="var(--tx-muted)" font-size="8" text-anchor="middle">t₀ - T_fr</text>

          <line x1="180" y1="45" x2="180" y2="55" stroke="var(--tx-muted)" stroke-width="2"/>
          <text x="180" y="70" fill="var(--tx-muted)" font-size="8" text-anchor="middle">t₀</text>

          <line x1="300" y1="45" x2="300" y2="55" stroke="var(--tx-muted)" stroke-width="2"/>
          <text x="300" y="70" fill="var(--tx-muted)" font-size="8" text-anchor="middle">t₀ + T_fr</text>
        </g>

        <text x="210" y="142" fill="var(--warning)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">
          S = G · e^(-2G) ➔ Maximum S = 1 / (2e) ≈ 18.4% (at G = 0.5)
        </text>
      </g>

      <!-- SECTION B: SLOTTED ALOHA VULNERABLE PERIOD = T_fr -->
      <g transform="translate(480, 25)">
        <rect width="430" height="155" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="215" y="24" fill="var(--success)" font-size="12" font-weight="800" text-anchor="middle">
          B. SLOTTED ALOHA: VULNERABLE TIME = T_fr
        </text>

        <!-- Discrete Clock Slots -->
        <g transform="translate(30, 50)">
          <!-- Slots boundaries -->
          <line x1="20" y1="10" x2="20" y2="70" stroke="var(--border)" stroke-width="1.5"/>
          <line x1="130" y1="10" x2="130" y2="70" stroke="var(--border)" stroke-width="1.5"/>
          <line x1="240" y1="10" x2="240" y2="70" stroke="var(--border)" stroke-width="1.5"/>
          <line x1="350" y1="10" x2="350" y2="70" stroke="var(--border)" stroke-width="1.5"/>

          <text x="75" y="24" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Slot k - 1</text>
          
          <!-- Active Slot k -->
          <rect x="130" y="10" width="110" height="60" fill="rgba(52, 211, 153, 0.12)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="185" y="24" fill="var(--success)" font-size="9" font-weight="800" text-anchor="middle">Slot k (Vulnerable)</text>

          <rect x="140" y="32" width="90" height="30" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="185" y="52" fill="var(--accent-light)" font-size="9" font-weight="800" text-anchor="middle">Target Frame</text>

          <text x="295" y="24" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Slot k + 1</text>
        </g>

        <text x="215" y="142" fill="var(--success)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">
          S = G · e^(-G) ➔ Maximum S = 1 / e ≈ 36.8% (at G = 1.0)
        </text>
      </g>

      <!-- SECTION C: THROUGHPUT CURVES COMPARISON GRAPH -->
      <g transform="translate(30, 195)">
        <rect width="880" height="150" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="25" y="24" fill="var(--accent)" font-size="11" font-weight="800">
          C. THROUGHPUT (S) VS. OFFERED TRAFFIC LOAD (G) CURVES
        </text>

        <!-- Graph Axes -->
        <g transform="translate(180, 25)">
          <line x1="50" y1="95" x2="600" y2="95" stroke="var(--border)" stroke-width="1.5"/>
          <line x1="50" y1="20" x2="50" y2="95" stroke="var(--border)" stroke-width="1.5"/>
          <text x="600" y="90" fill="var(--tx-muted)" font-size="9">Offered Load (G)</text>
          <text x="45" y="18" fill="var(--tx-muted)" font-size="9" text-anchor="end">S</text>

          <!-- Slotted ALOHA Curve (Peaks at 0.368 at G=1) -->
          <path d="M 50 95 Q 120 20, 190 20 Q 280 20, 550 95" stroke="var(--success)" stroke-width="3" fill="none"/>
          <circle cx="190" cy="20" r="5" fill="var(--success)"/>
          <text x="200" y="18" fill="var(--success)" font-size="10" font-weight="800">Slotted: S_max = 36.8% (G = 1.0)</text>

          <!-- Pure ALOHA Curve (Peaks at 0.184 at G=0.5) -->
          <path d="M 50 95 Q 90 55, 120 55 Q 180 55, 450 95" stroke="var(--warning)" stroke-width="2.5" fill="none"/>
          <circle cx="120" cy="55" r="5" fill="var(--warning)"/>
          <text x="130" y="52" fill="var(--warning)" font-size="10" font-weight="800">Pure: S_max = 18.4% (G = 0.5)</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>ALOHA Performance Halving:</strong> Pure ALOHA permits unconstrained asynchronous transmission at any microsecond, resulting in an overlap vulnerability window of $2 T_{\text{fr}}$. By synchronizing transmissions to clock slot boundaries, Slotted ALOHA eliminates partial collisions, halving the vulnerable time to $T_{\text{fr}}$ and exactly doubling capacity from 18.4% to 36.8%.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: CSMA/CD Minimum Frame Size Spatio-Temporal Proof
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">💥</span>
      <span class="diagram-title">Figure 10.2: CSMA/CD Worst-Case Collision Detection &amp; Minimum Frame Size Derivation ($L_{\min} = 2 R d_{\text{prop}}$)</span>
    </div>
    <span class="diagram-badge">ETHERNET CSMA/CD PROOF</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-cd" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-jam" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP CABLE LAYOUT: HOST A AT x=0, HOST B AT x=d -->
      <g transform="translate(60, 25)">
        <line x1="80" y1="25" x2="740" y2="25" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>
        
        <!-- Station A -->
        <g transform="translate(30, 0)">
          <rect width="65" height="45" rx="6" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
          <text x="32" y="24" font-size="12" text-anchor="middle">💻</text>
          <text x="32" y="38" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">Host A (x=0)</text>
        </g>

        <!-- Station B -->
        <g transform="translate(730, 0)">
          <rect width="65" height="45" rx="6" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
          <text x="32" y="24" font-size="12" text-anchor="middle">💻</text>
          <text x="32" y="38" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">Host B (x=d)</text>
        </g>
        <text x="410" y="16" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Physical Distance d (Propagation Time τ = d / s)</text>
      </g>

      <!-- SPATIO-TEMPORAL COLLISION TIMELINE -->
      <g transform="translate(80, 85)">
        <!-- Vertical Time Axis -->
        <line x1="60" y1="20" x2="60" y2="230" stroke="var(--border)" stroke-width="1.5"/>
        <line x1="760" y1="20" x2="760" y2="230" stroke="var(--border)" stroke-width="1.5"/>

        <!-- Event 1: t = 0 (Host A starts transmitting) -->
        <circle cx="60" cy="20" r="4" fill="var(--accent)"/>
        <text x="45" y="24" fill="var(--accent)" font-size="10" font-weight="700" text-anchor="end">t = 0:</text>
        <text x="70" y="24" fill="var(--tx-primary)" font-size="10">Host A starts pushing frame bits onto wire</text>

        <!-- Waveform travels from A towards B -->
        <line x1="60" y1="20" x2="730" y2="110" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-cd)"/>

        <!-- Event 2: t = τ - ε (Host B senses channel idle just before wavefront arrives!) -->
        <circle cx="760" cy="110" r="4" fill="var(--warning)"/>
        <text x="775" y="105" fill="var(--warning)" font-size="10" font-weight="800">t = τ - ε: Host B senses idle &amp; transmits!</text>

        <!-- Event 3: t = τ (Collision occurs right at B's tap!) -->
        <circle cx="740" cy="118" r="14" fill="var(--danger)"/>
        <text x="740" y="123" fill="#fff" font-size="12" font-weight="900" text-anchor="middle">💥</text>
        <text x="775" y="128" fill="var(--danger)" font-size="10" font-weight="800">t = τ: Collision Occurs</text>

        <!-- Collision Corrupted Energy propagates BACK to A -->
        <line x1="740" y1="120" x2="60" y2="210" stroke="var(--danger)" stroke-width="2.5" stroke-dasharray="4,2" marker-end="url(#arrow-jam)"/>

        <!-- Event 4: t = 2τ (Host A finally detects the collision!) -->
        <circle cx="60" cy="210" r="5" fill="var(--danger)"/>
        <text x="45" y="214" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="end">t = 2τ:</text>
        <text x="70" y="214" fill="var(--danger)" font-size="11" font-weight="800">
          Collision runt reaches Host A (Worst-Case Time: 2 · d_prop)
        </text>
      </g>

      <!-- MATHEMATICAL CONCLUSION BANNER -->
      <g transform="translate(60, 310)">
        <rect width="820" height="42" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="410" y="26" fill="var(--accent-light)" font-size="12" font-weight="800" text-anchor="middle">
          ★ MANDATORY CONDITION: d_trans ≥ 2 · d_prop ➔ (L / R) ≥ 2τ ➔ <tspan fill="var(--warning)" font-size="14">L_min = 2 · R · d_prop</tspan>
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>The 64-Byte Ethernet Rule:</strong> If a station sends a tiny frame (e.g. 20 bytes) and finishes transmitting <em>before</em> the collision runt returns at $t = 2\tau$, its transceiver will assume the frame was delivered safely, corrupting the protocol! To guarantee that the sender is STILL transmitting when the worst-case collision arrives, Ethernet mandates $L_{\min} = 64\text{ bytes}$ (512 bit-times).
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: IEEE 802.3 Ethernet Frame Bitfield Structure
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧱</span>
      <span class="diagram-title">Figure 10.3: IEEE 802.3 Ethernet Frame Structure &amp; Header Bitfields</span>
    </div>
    <span class="diagram-badge">FRAME BITFIELDS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- ETHERNET FRAME TILES -->
      <g transform="translate(30, 40)">
        <!-- 1. Preamble (7 Bytes) -->
        <g transform="translate(0, 0)">
          <rect width="100" height="75" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="50" y="24" fill="var(--tx-muted)" font-size="10" font-weight="800" text-anchor="middle">PREAMBLE</text>
          <text x="50" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">7 Bytes</text>
          <text x="50" y="60" fill="var(--tx-muted)" font-size="8" text-anchor="middle">10101010... (Sync)</text>
        </g>

        <!-- 2. SFD (1 Byte) -->
        <g transform="translate(105, 0)">
          <rect width="65" height="75" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="32" y="24" fill="var(--warning)" font-size="10" font-weight="800" text-anchor="middle">SFD</text>
          <text x="32" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">1 Byte</text>
          <text x="32" y="60" fill="var(--warning)" font-size="8" text-anchor="middle">10101011</text>
        </g>

        <!-- 3. Destination MAC (6 Bytes) -->
        <g transform="translate(175, 0)">
          <rect width="115" height="75" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="57" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">DEST MAC</text>
          <text x="57" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">6 Bytes</text>
          <text x="57" y="60" fill="var(--info)" font-size="8" text-anchor="middle">48-bit Hardware</text>
        </g>

        <!-- 4. Source MAC (6 Bytes) -->
        <g transform="translate(295, 0)">
          <rect width="115" height="75" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="57" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">SOURCE MAC</text>
          <text x="57" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">6 Bytes</text>
          <text x="57" y="60" fill="var(--info)" font-size="8" text-anchor="middle">48-bit Hardware</text>
        </g>

        <!-- 5. EtherType / Length (2 Bytes) -->
        <g transform="translate(415, 0)">
          <rect width="80" height="75" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="40" y="24" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">TYPE/LEN</text>
          <text x="40" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">2 Bytes</text>
          <text x="40" y="60" fill="var(--accent)" font-size="8" text-anchor="middle">0x0800 (IPv4)</text>
        </g>

        <!-- 6. Payload Data (46 to 1500 Bytes) -->
        <g transform="translate(500, 0)">
          <rect width="260" height="75" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
          <text x="130" y="24" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">PAYLOAD DATA (+ PAD)</text>
          <text x="130" y="44" fill="var(--tx-primary)" font-size="13" font-weight="900" text-anchor="middle">46 to 1,500 Bytes (MTU)</text>
          <text x="130" y="60" fill="var(--success)" font-size="8" text-anchor="middle">Padded if data &lt; 46B to satisfy 64B min</text>
        </g>

        <!-- 7. FCS / CRC-32 (4 Bytes) -->
        <g transform="translate(765, 0)">
          <rect width="95" height="75" rx="6" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="2"/>
          <text x="47" y="24" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="middle">CRC / FCS</text>
          <text x="47" y="44" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">4 Bytes</text>
          <text x="47" y="60" fill="var(--danger)" font-size="8" text-anchor="middle">32-bit Checksum</text>
        </g>
      </g>

      <!-- TOTAL FRAME SIZE BRACKET -->
      <g transform="translate(205, 140)">
        <line x1="0" y1="10" x2="685" y2="10" stroke="var(--accent)" stroke-width="2"/>
        <text x="342" y="28" fill="var(--accent-light)" font-size="11" font-weight="800" text-anchor="middle">
          TOTAL ETHERNET FRAME SIZE = 64 to 1,518 BYTES (Excluding Preamble &amp; SFD)
        </text>
      </g>

      <!-- DETAILS GRID -->
      <g transform="translate(30, 185)">
        <rect width="860" height="110" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="25" fill="var(--tx-primary)" font-size="11" font-weight="700">Detailed Field Breakdown:</text>
        <text x="25" y="45" fill="var(--tx-secondary)" font-size="10">• <strong>Preamble + SFD (8B):</strong> Allows receiver physical layer to synchronize clock and detect frame start bit (11).</text>
        <text x="25" y="65" fill="var(--tx-secondary)" font-size="10">• <strong>Destination &amp; Source MAC (12B):</strong> Burned-in IEEE 802 addresses. Dest MAC can be Unicast, Multicast, or Broadcast (FF:FF:FF:FF:FF:FF).</text>
        <text x="25" y="85" fill="var(--tx-secondary)" font-size="10">• <strong>Pad Field:</strong> If upper layer packet is smaller than 46 bytes (e.g. 28-byte ARP packet), padding zeros are added to reach 64B.</text>
        <text x="25" y="102" fill="var(--tx-secondary)" font-size="10">• <strong>FCS (4B):</strong> 32-bit Cyclic Redundancy Check (CRC-32) computed over Destination MAC through Pad field.</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>MTU vs. Frame Size:</strong> The Maximum Transmission Unit (MTU) of standard Ethernet is <strong>1,500 bytes</strong> (the maximum size of the IP payload). The entire Ethernet frame with its 14-byte header and 4-byte CRC is $14 + 1500 + 4 = \mathbf{1,518\text{ bytes}}$ ($1,522$ bytes if an 802.1Q VLAN tag is present).
  </div>
</div>'''

# ==========================================
# 4. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 10
# ==========================================
ch10_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: CSMA/CD Operation, Minimum Frame Size Derivation &amp; Backoff Probability</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Explain the Carrier Sense Multiple Access with Collision Detection (CSMA/CD) protocol. With a neat space-time diagram, derive the mathematical formula for minimum frame length: $L_{\\min} = 2 \\times R \\times d_{\\text{prop}}$. Why does classic Ethernet enforce a 64-byte minimum frame size? [4 Marks]<br>
          (b) Describe the Binary Exponential Backoff (BEB) algorithm used in CSMA/CD. What is the capture effect? [3 Marks]<br>
          (c) Two hosts A and B are situated at the extreme opposite ends of a $2\\text{ km}$ coaxial cable running 100 Mbps Fast Ethernet ($R = 100\\text{ Mbps}$). The signal propagation speed in coaxial cable is $s = 2 \\times 10^8\\text{ m/s}$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(i) Calculate the round-trip propagation time ($2\\tau$).<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(ii) Compute the absolute minimum frame size $L_{\\min}$ in bits and bytes to ensure proper collision detection.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(iii) If Stations A and B collide on their first attempt, calculate the probability that they will collide again on their immediate next retransmission attempt under Binary Exponential Backoff. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: CSMA/CD Operation &amp; $L_{\\min}$ Proof</h4>
          <p><strong>CSMA/CD Protocol Rules:</strong> (1) <em>Carrier Sense:</em> Listen before transmitting. If channel is busy, defer transmission per persistence algorithm; (2) <em>Multiple Access:</em> Any station may transmit when medium is idle; (3) <em>Collision Detection:</em> Listen while transmitting. If voltage amplitude exceeds normal threshold, collision is detected; (4) <em>Jam Signal:</em> Transmit a 32-to-48 bit jam signal so all stations recognize the collision, abort transmission, and enter Binary Exponential Backoff.</p>

          <p><strong>Mathematical Derivation of $L_{\\min}$ (Refer to Figure 10.2):</strong></p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li>Let the physical distance between the two farthest stations A and B be $d$, and wave velocity be $s$. One-way propagation delay is $\\tau = d / s$.</li>
            <li>Station A begins transmitting a frame at time $t = 0$.</li>
            <li>The signal arrives at Station B at time $t = \\tau - \\epsilon$ (just a microsecond before arriving). Station B senses the line idle and begins transmitting its own frame.</li>
            <li>A collision occurs immediately near Station B at time $t = \\tau$.</li>
            <li>The collision runt (corrupted electrical energy) must now propagate all the way back across the entire cable length $d$ to reach Station A.</li>
            <li>The collision signal reaches Station A at time $t = 2\\tau = 2 \\cdot d_{\\text{prop}}$ (the Round-Trip Time).</li>
            <li>For Station A to detect this collision while it is still responsible for the frame, Station A <strong>must still be transmitting</strong> when the collision signal arrives at $t = 2\\tau$:</li>
          </ol>
          $$d_{\\text{trans}} \\ge 2 \\cdot d_{\\text{prop}} \\implies \\frac{L}{R} \\ge 2\\tau \\implies \\mathbf{L_{\\min} = 2 \\cdot R \\cdot d_{\\text{prop}}}$$
          <p><strong>Why Ethernet Mandates 64 Bytes:</strong> In original 10 Mbps Ethernet over maximum specification (2.5 km with 4 repeaters), round-trip time was $2\\tau \\approx 51.2\\ \\mu\\text{s}$. Transmitting at 10 Mbps for $51.2\\ \\mu\\text{s}$ yields $10 \\times 10^6 \\times 51.2 \\times 10^{-6} = 512\\text{ bits} = \\mathbf{64\\text{ bytes}}$. Any frame smaller than 64 bytes is padded with zeros.</p>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Binary Exponential Backoff (BEB) Algorithm</h4>
          <p>After a collision, stations wait a random backoff time $T_{\\text{backoff}} = K \\times 2\\tau$ (where $2\\tau$ is the slot time = 512 bit times):</p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li>After collision $i$ (where $1 \\le i \\le 10$), choose integer $K$ uniformly at random from the set: $$K \\in \\{0, 1, 2, \\dots, 2^i - 1\\}$$</li>
            <li>For $11 \\le i \\le 15$, the maximum range freezes at $K \\in \\{0, \\dots, 1023\\}$ ($2^{10} - 1$).</li>
            <li>After $i = 16$ consecutive collisions, the station aborts transmission entirely and reports a permanent network failure to upper layers.</li>
            <li><strong>Capture Effect:</strong> A station that has collided fewer times has a narrower backoff window (e.g., $\{0, 1\}$) compared to a station that has collided multiple times (e.g., $\{0, \\dots, 15\}$). The favored station repeatedly "captures" the channel, causing temporary starvation of other nodes.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Step-by-Step Solved Numerical</h4>
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 8px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Given:</strong> Distance $d = 2\\text{ km} = 2,000\\text{ m}$, Speed $s = 2 \\times 10^8\\text{ m/s}$, Rate $R = 100\\text{ Mbps} = 10^8\\text{ bps}$.<br><br>
              <strong>(i) Calculate Round-Trip Propagation Delay:</strong><br>
              $$d_{\\text{prop}} = \\frac{d}{s} = \\frac{2,000\\text{ m}}{2 \\times 10^8\\text{ m/s}} = 10^{-5}\\text{ s} = 10\\ \\mu\\text{s}$$<br>
              $$\\text{Round-Trip Time } (2\\tau) = 2 \\times 10\\ \\mu\\text{s} = \\mathbf{20\\ \\mu\\text{s}}$$<br><br>
              <strong>(ii) Calculate Minimum Frame Size:</strong><br>
              $$L_{\\min} = 2 \\cdot R \\cdot d_{\\text{prop}} = 2 \\times (10^8\\text{ bps}) \\times (10 \\times 10^{-6}\\text{ s})$$<br>
              $$L_{\\min} = 2,000\\text{ bits} = \\frac{2,000}{8} = \\mathbf{250\\text{ bytes}}$$<br>
              <em>(Notice: Because rate $R$ increased by $10\\times$ from 10M to 100M, minimum frame size increases proportionally from 25 bytes to 250 bytes!)</em><br><br>
              <strong>(iii) Probability of Recollision on Next Attempt:</strong><br>
              After the 1st collision ($i = 1$), each station chooses $K \\in \\{0, 1\\}$ with equal probability ($P(K=0) = 0.5$, $P(K=1) = 0.5$).<br>
              Possible combinations for $(K_A, K_B)$: $\\{(0,0), (0,1), (1,0), (1,1)\\}$. Total outcomes = $4$.<br>
              Recollision occurs if both pick the same slot: $(0,0)$ or $(1,1)$ (2 favorable outcomes).<br>
              $$P(\\text{Collision}) = \\frac{2}{4} = \\mathbf{0.5 \\text{ (or } 50\\%)}$$
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 10
# ==========================================
# Insert Diagram 1 into Section 10.3 (Slotted aloha)
s3_target = re.search(r'<section id="s-slotted-aloha"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s3_target:
    content = content[:s3_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s3_target.end():]
    print('Inserted Diagram 1 in Section 10.3')

# Insert Diagram 2 into Section 10.8 (CSMA/CD)
s8_target = re.search(r'<section id="s-csma-cd"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s8_target:
    content = content[:s8_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s8_target.end():]
    print('Inserted Diagram 2 in Section 10.8')

# Insert Diagram 3 into Section 10.16 (Ethernet frame)
s16_target = re.search(r'<section id="s-ethernet-frame"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s16_target:
    content = content[:s16_target.end()] + '\n' + svg_diagram_3 + '\n' + content[s16_target.end():]
    print('Inserted Diagram 3 in Section 10.16')

# Insert 10-Mark Blueprint into Chapter 10 before study-resources in s-summary-ch10
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch10_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 10!')

with open(ch10_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 10 upgrade completed!')
