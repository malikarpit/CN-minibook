"""
Upgrade Chapter 4 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch4_path = '/Users/arpit/minibook/cn/chapters/ch04-devices-sdn.html'
with open(ch4_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Amplifier vs Repeater
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📶</span>
      <span class="diagram-title">Figure 4.1: Signal Restoration — Analog Amplifier vs. Digital Regenerative Repeater</span>
    </div>
    <span class="diagram-badge">PHYSICAL LAYER RESTORATION</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-amp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
        <marker id="arrow-rep" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="300" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP HALF: ANALOG AMPLIFIER (NOISE BOOST) -->
      <g transform="translate(30, 25)">
        <rect width="840" height="125" rx="10" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="20" y="24" fill="var(--danger)" font-size="12" font-weight="800">1. ANALOG AMPLIFIER (Indiscriminate Gain)</text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">Boosts both weakened signal AND cumulative channel noise</text>

        <!-- Input Attenuated + Noisy Wave -->
        <g transform="translate(30, 55)">
          <path d="M 0 30 Q 25 15, 50 30 T 100 30 T 150 30" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <path d="M 0 30 L 150 30" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="75" y="55" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Attenuated + Noisy Input</text>
        </g>

        <!-- Amplifier Symbol -->
        <path d="M 230 85 L 280 85" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-amp)"/>
        <g transform="translate(290, 50)">
          <polygon points="0,0 60,35 0,70" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="2"/>
          <text x="20" y="40" fill="var(--danger)" font-size="12" font-weight="800">AMP</text>
        </g>
        <path d="M 360 85 L 410 85" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-amp)"/>

        <!-- Output: Amplified Signal AND Amplified Noise -->
        <g transform="translate(430, 45)">
          <path d="M 0 40 Q 30 5, 60 40 T 120 40 T 180 40 T 240 40" stroke="var(--danger)" stroke-width="3" fill="none"/>
          <path d="M 0 40 L 240 40" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="120" y="70" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">
            ❌ Amplified Signal + AMPLIFIED NOISE (SNR degrades!)
          </text>
        </g>
      </g>

      <!-- BOTTOM HALF: DIGITAL REPEATER (REGENERATION) -->
      <g transform="translate(30, 165)">
        <rect width="840" height="130" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="20" y="24" fill="var(--success)" font-size="12" font-weight="800">2. DIGITAL REPEATER (Regenerative Reconstruction)</text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">Samples incoming pulses, thresholds 0/1 bits, and outputs brand-new pristine square waves</text>

        <!-- Input Distorted Digital Pulses -->
        <g transform="translate(30, 55)">
          <path d="M 0 40 L 20 20 L 40 22 L 50 40 L 80 40 L 95 18 L 120 24 L 135 40" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <path d="M 0 40 L 140 40" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="70" y="60" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Distorted / Rounded Pulses</text>
        </g>

        <!-- Repeater Symbol -->
        <path d="M 230 90 L 280 90" stroke="var(--success)" stroke-width="2" marker-end="url(#arrow-rep)"/>
        <g transform="translate(290, 60)">
          <rect width="80" height="55" rx="8" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
          <text x="40" y="25" fill="var(--success)" font-size="10" font-weight="800" text-anchor="middle">REPEATER</text>
          <text x="40" y="42" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Retiming Core</text>
        </g>
        <path d="M 380 90 L 430 90" stroke="var(--success)" stroke-width="2" marker-end="url(#arrow-rep)"/>

        <!-- Output: Pristine Clean Square Wave -->
        <g transform="translate(450, 55)">
          <path d="M 0 40 L 0 10 L 40 10 L 40 40 L 80 40 L 80 10 L 120 10 L 120 40 L 160 40 L 160 10 L 200 10 L 200 40" stroke="var(--success)" stroke-width="2.5" fill="none"/>
          <path d="M 0 40 L 210 40" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="105" y="60" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">
            ✓ Pristine Reconstructed Digital Bitstream (Noise Eliminated!)
          </text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University Exam Distinction:</strong> An <em>Amplifier</em> is a purely linear analog circuit that boosts the amplitude of whatever enters it, amplifying noise alongside the signal. A <em>Repeater</em> is an intelligent Layer-1 device that decodes the bits, strips all physical noise, and regenerates brand new, full-power square pulses at the original transmitter voltage.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Hub Architecture (Star Wiring, Logical Bus)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔌</span>
      <span class="diagram-title">Figure 4.2: Hub Internal Architecture — Physical Star Wiring, Logical Shared Bus</span>
    </div>
    <span class="diagram-badge">LAYER 1 MULTIPORT REPEATER</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-hub" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
        <marker id="arrow-hub-in" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- HUB CHASSIS -->
      <g transform="translate(200, 40)">
        <rect width="500" height="170" rx="12" fill="var(--bg-card)" stroke="var(--border)" stroke-width="2"/>
        <text x="250" y="30" fill="var(--tx-primary)" font-size="13" font-weight="800" text-anchor="middle">
          INTERNAL MULTIPORT REPEATER HUB (Layer 1)
        </text>

        <!-- INTERNAL SHARED ELECTRICAL BUS (YELLOW) -->
        <rect x="40" y="55" width="420" height="24" rx="4" fill="rgba(251, 191, 36, 0.2)" stroke="var(--warning)" stroke-width="2"/>
        <text x="250" y="72" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">
          INTERNAL SHARED BACKPLANE BUS (Single Shared Collision Domain)
        </text>

        <!-- 4 PORTS -->
        <!-- Port 1 (Ingress) -->
        <g transform="translate(60, 110)">
          <rect width="60" height="35" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="30" y="22" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Port 1</text>
          <line x1="30" y1="0" x2="30" y2="-31" stroke="var(--accent)" stroke-width="2.5"/>
        </g>

        <!-- Port 2 (Flooded) -->
        <g transform="translate(170, 110)">
          <rect width="60" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="30" y="22" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">Port 2</text>
          <line x1="30" y1="0" x2="30" y2="-31" stroke="var(--danger)" stroke-width="2"/>
        </g>

        <!-- Port 3 (Flooded) -->
        <g transform="translate(280, 110)">
          <rect width="60" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="30" y="22" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">Port 3</text>
          <line x1="30" y1="0" x2="30" y2="-31" stroke="var(--danger)" stroke-width="2"/>
        </g>

        <!-- Port 4 (Flooded) -->
        <g transform="translate(390, 110)">
          <rect width="60" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="30" y="22" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">Port 4</text>
          <line x1="30" y1="0" x2="30" y2="-31" stroke="var(--danger)" stroke-width="2"/>
        </g>
      </g>

      <!-- HOST 1 (SENDER) -->
      <g transform="translate(50, 230)">
        <rect width="110" height="55" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="55" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="55" y="44" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Host A (Sender)</text>
      </g>
      <!-- Link Host 1 to Port 1 -->
      <path d="M 105 230 L 105 185 L 290 185" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-hub-in)"/>
      <text x="180" y="178" fill="var(--accent)" font-size="9" font-weight="700">Packet In</text>

      <!-- FLOODING TO HOSTS 2, 3, 4 -->
      <!-- Host 2 -->
      <g transform="translate(350, 240)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="45" y="24" font-size="12" text-anchor="middle">💻</text>
        <text x="45" y="40" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Host B</text>
      </g>
      <path d="M 400 185 L 395 240" stroke="var(--danger)" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrow-hub)"/>

      <!-- Host 3 -->
      <g transform="translate(500, 240)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="45" y="24" font-size="12" text-anchor="middle">💻</text>
        <text x="45" y="40" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Host C</text>
      </g>
      <path d="M 510 185 L 545 240" stroke="var(--danger)" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrow-hub)"/>

      <!-- Host 4 -->
      <g transform="translate(680, 240)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="45" y="24" font-size="12" text-anchor="middle">💻</text>
        <text x="45" y="40" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Host D</text>
      </g>
      <path d="M 620 185 L 725 240" stroke="var(--danger)" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrow-hub)"/>

      <!-- BOTTOM WARNING CALLOUT -->
      <rect x="30" y="295" width="840" height="22" rx="4" fill="var(--bg-elevated)"/>
      <text x="450" y="310" fill="var(--danger)" font-size="9" font-weight="700" text-anchor="middle">
        ⚠️ HUB BEHAVIOR: Bits entering ANY port are blindly copied and broadcast out of ALL other ports. Only 1 device can talk at a time.
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>"Dumb" Hub Mechanism:</strong> A Hub has zero intelligence—it contains no MAC address table and cannot parse headers. It is literally a multiport repeater with an internal shared bus. Connecting 24 computers to a hub yields <strong>1 single collision domain</strong> and <strong>1 broadcast domain</strong> running in half-duplex CSMA/CD.
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Switch MAC Learning & Forwarding Logic
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧠</span>
      <span class="diagram-title">Figure 4.3: Switch CAM Table Learning &amp; Forwarding Decision Engine</span>
    </div>
    <span class="diagram-badge">TRANSPARENT BRIDGING</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-sw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-sw-succ" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
        <marker id="arrow-sw-warn" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--warning)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- STEP 1: FRAME ARRIVAL -->
      <g transform="translate(30, 30)">
        <rect width="260" height="70" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="130" y="24" fill="var(--accent)" font-size="11" font-weight="800" text-anchor="middle">STEP 1: INGRESS FRAME</text>
        <text x="130" y="44" fill="var(--tx-primary)" font-size="10" font-family="var(--font-mono)" text-anchor="middle">Frame arrives on Port P</text>
        <text x="130" y="58" fill="var(--tx-muted)" font-size="9" text-anchor="middle">[Src MAC = S, Dst MAC = D]</text>
      </g>

      <path d="M 160 100 L 160 135" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-sw)"/>

      <!-- STEP 2: SOURCE MAC LEARNING -->
      <g transform="translate(30, 140)">
        <rect width="260" height="95" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <text x="130" y="24" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">STEP 2: CAM TABLE LEARNING</text>
        <text x="130" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Record / Update Entry:</text>
        <rect x="25" y="52" width="210" height="30" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="130" y="72" fill="var(--info)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">
          CAM[Src MAC S] ➔ Port P
        </text>
      </g>

      <path d="M 290 185 L 350 185" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-sw)"/>

      <!-- STEP 3: DESTINATION LOOKUP DECISION DIAMOND -->
      <g transform="translate(360, 110)">
        <polygon points="120,0 240,75 120,150 0,75" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <text x="120" y="65" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">Is Dst MAC 'D'</text>
        <text x="120" y="80" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">in CAM Table?</text>
      </g>

      <!-- BRANCH 1: YES (KNOWN UNICAST) -->
      <path d="M 600 185 L 670 185" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arrow-sw-succ)"/>
      <text x="635" y="175" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">YES</text>

      <g transform="translate(680, 120)">
        <rect width="210" height="120" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <text x="105" y="24" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">KNOWN UNICAST</text>
        <text x="105" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Check Destination Port:</text>
        
        <rect x="15" y="52" width="180" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="105" y="69" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">If Dest Port == Ingress: FILTER</text>

        <rect x="15" y="82" width="180" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="105" y="99" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">If Dest Port != Ingress: FORWARD</text>
      </g>

      <!-- BRANCH 2: NO (UNKNOWN UNICAST / BROADCAST) -->
      <path d="M 480 260 L 480 290 L 670 290" stroke="var(--warning)" stroke-width="2.5" fill="none" marker-end="url(#arrow-sw-warn)"/>
      <text x="495" y="280" fill="var(--warning)" font-size="11" font-weight="800">NO / BROADCAST</text>

      <g transform="translate(680, 260)">
        <rect width="210" height="65" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <text x="105" y="24" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">FLOOD / BROADCAST</text>
        <text x="105" y="44" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Forward out ALL ports</text>
        <text x="105" y="56" fill="var(--tx-muted)" font-size="9" text-anchor="middle">EXCEPT the ingress port P</text>
      </g>

      <!-- CAM TABLE AGING NOTE -->
      <rect x="30" y="270" width="300" height="55" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="40" y="290" fill="var(--accent)" font-size="10" font-weight="700">⏱️ CAM Table Aging Timer (Default 300s):</text>
      <text x="40" y="306" fill="var(--tx-muted)" font-size="9">Inactive MAC entries are purged to handle device moves.</text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Transparent Bridging Rule:</strong> <em>Switches learn on Source MAC and forward on Destination MAC.</em> If a destination MAC is not yet in the CAM table (unknown unicast), the switch floods the frame out of all ports except the arrival port. As soon as the target responds, its port is learned, converting future transmissions into private unicasts.
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Switching Methods (Cut-Through vs Store-and-Forward)
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚡</span>
      <span class="diagram-title">Figure 4.4: Ethernet Switching Modes — Store-and-Forward vs. Cut-Through vs. Fragment-Free</span>
    </div>
    <span class="diagram-badge">SWITCH FORWARDING MODES</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- FRAME STRUCTURE TOP BAR -->
      <g transform="translate(30, 25)">
        <text x="10" y="20" fill="var(--accent)" font-size="11" font-weight="800">STANDARD ETHERNET FRAME STRUCTURE (64 to 1518 Bytes):</text>
        <g transform="translate(0, 30)">
          <rect width="80" height="32" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="40" y="20" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Dst MAC (6B)</text>

          <rect x="85" y="0" width="80" height="32" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="125" y="20" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Src MAC (6B)</text>

          <rect x="170" y="0" width="60" height="32" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="200" y="20" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Type (2B)</text>

          <rect x="235" y="0" width="510" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="490" y="20" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">IP Payload Data (46 – 1500 Bytes)</text>

          <rect x="750" y="0" width="90" height="32" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.2"/>
          <text x="795" y="20" fill="var(--danger)" font-size="9" font-weight="700" text-anchor="middle">FCS / CRC (4B)</text>
        </g>
      </g>

      <!-- MODE 1: CUT-THROUGH (FASTEST) -->
      <g transform="translate(30, 110)">
        <rect width="840" height="60" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="15" y="25" fill="var(--accent)" font-size="11" font-weight="800">1. CUT-THROUGH SWITCHING</text>
        <text x="15" y="44" fill="var(--tx-muted)" font-size="9">Forwarding begins after reading first 6 Bytes (Dst MAC) • Lowest Latency (~microseconds) • Forwards corrupted frames!</text>
        
        <line x1="280" y1="10" x2="280" y2="50" stroke="var(--accent)" stroke-width="2"/>
        <text x="290" y="34" fill="var(--accent)" font-size="10" font-weight="800">Forwarding Starts ➔</text>
      </g>

      <!-- MODE 2: FRAGMENT-FREE (COMPROMISE) -->
      <g transform="translate(30, 180)">
        <rect width="840" height="60" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="15" y="25" fill="var(--warning)" font-size="11" font-weight="800">2. FRAGMENT-FREE SWITCHING</text>
        <text x="15" y="44" fill="var(--tx-muted)" font-size="9">Buffers first 64 Bytes (Ethernet Collision Window) • Filters out collision runts (&lt;64B) • Moderate latency</text>

        <line x1="420" y1="10" x2="420" y2="50" stroke="var(--warning)" stroke-width="2"/>
        <text x="430" y="34" fill="var(--warning)" font-size="10" font-weight="800">Forwarding Starts ➔</text>
      </g>

      <!-- MODE 3: STORE-AND-FORWARD (SAFEST) -->
      <g transform="translate(30, 250)">
        <rect width="840" height="60" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <text x="15" y="25" fill="var(--success)" font-size="11" font-weight="800">3. STORE-AND-FORWARD SWITCHING (Modern Enterprise Standard)</text>
        <text x="15" y="44" fill="var(--tx-muted)" font-size="9">Buffers entire frame (up to 1518B), computes CRC-32 checksum, drops all corrupt frames • Required for mixed port speeds</text>

        <line x1="770" y1="10" x2="770" y2="50" stroke="var(--success)" stroke-width="2"/>
        <text x="630" y="34" fill="var(--success)" font-size="10" font-weight="800">Forwarding Starts ONLY After CRC Check ➔</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Speed vs. Integrity Trade-Off:</strong> Cut-Through achieves ultra-low latency for high-frequency trading (HFT) but blindly propagates corrupt frames across the network. Store-and-Forward guarantees zero bad frames propagate into downstream switches and is mandatory whenever ingress and egress ports run at different speeds (e.g., 10G to 1G).
  </div>
</div>'''

# ==========================================
# 5. DIAGRAM 5: Collision vs Broadcast Domains Master Topology
# ==========================================
svg_diagram_5 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🌐</span>
      <span class="diagram-title">Figure 4.5: Master Domain Demarcation — Collision Domains vs. Broadcast Domains</span>
    </div>
    <span class="diagram-badge">CRUCIAL EXAM DIAGRAM</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bcast1-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--info)" stop-opacity="0.12"/>
          <stop offset="100%" stop-color="var(--info)" stop-opacity="0.04"/>
        </linearGradient>
        <linearGradient id="bcast2-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--success)" stop-opacity="0.12"/>
          <stop offset="100%" stop-color="var(--success)" stop-opacity="0.04"/>
        </linearGradient>
      </defs>

      <rect x="10" y="10" width="920" height="380" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- BROADCAST DOMAIN 1 (LEFT HALF: BLUE OUTLINE) -->
      <rect x="25" y="25" width="415" height="350" rx="16" fill="url(#bcast1-grad)" stroke="var(--info)" stroke-width="2" stroke-dasharray="6,4"/>
      <rect x="40" y="35" width="220" height="24" rx="4" fill="var(--info-dim)"/>
      <text x="150" y="51" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">
        BROADCAST DOMAIN 1 (Subnet A)
      </text>

      <!-- BROADCAST DOMAIN 2 (RIGHT HALF: GREEN OUTLINE) -->
      <rect x="500" y="25" width="415" height="350" rx="16" fill="url(#bcast2-grad)" stroke="var(--success)" stroke-width="2" stroke-dasharray="6,4"/>
      <rect x="515" y="35" width="220" height="24" rx="4" fill="var(--success-dim)"/>
      <text x="625" y="51" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">
        BROADCAST DOMAIN 2 (Subnet B)
      </text>

      <!-- CENTRAL ROUTER (LAYER 3 BOUNDARY) -->
      <g transform="translate(425, 140)">
        <circle cx="45" cy="50" r="40" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="3"/>
        <text x="45" y="44" font-size="18" text-anchor="middle">🧭</text>
        <text x="45" y="62" fill="var(--warning)" font-size="10" font-weight="800" text-anchor="middle">ROUTER</text>
        <text x="45" y="74" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Breaks Broadcast</text>
      </g>

      <!-- LEFT SIDE HARDWARE (SWITCH 1 + HUB) -->
      <!-- Switch 1 -->
      <g transform="translate(180, 80)">
        <rect width="110" height="60" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <text x="55" y="28" font-size="14" text-anchor="middle">🔀</text>
        <text x="55" y="48" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">SWITCH 1</text>
      </g>

      <!-- Hub -->
      <g transform="translate(80, 220)">
        <rect width="100" height="50" rx="6" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.8"/>
        <text x="50" y="24" font-size="12" text-anchor="middle">🔌</text>
        <text x="50" y="40" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="middle">HUB 1</text>
      </g>

      <!-- Computers on Left -->
      <!-- PC 1 (Direct on Switch Port) -->
      <rect x="300" y="220" width="80" height="45" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="340" y="240" font-size="12" text-anchor="middle">💻</text>
      <text x="340" y="256" fill="var(--tx-primary)" font-size="9" text-anchor="middle">PC 1</text>

      <!-- PC 2 & PC 3 on Hub -->
      <rect x="40" y="300" width="70" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="75" y="325" fill="var(--tx-primary)" font-size="9" text-anchor="middle">PC 2</text>

      <rect x="130" y="300" width="70" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="165" y="325" fill="var(--tx-primary)" font-size="9" text-anchor="middle">PC 3</text>

      <!-- Collision Domain Badges on Left -->
      <line x1="290" y1="110" x2="425" y2="170" stroke="var(--info)" stroke-width="2"/>
      <circle cx="350" cy="135" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="350" y="139" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD1</text>

      <line x1="250" y1="140" x2="330" y2="220" stroke="var(--info)" stroke-width="2"/>
      <circle cx="300" cy="180" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="300" y="184" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD2</text>

      <line x1="200" y1="140" x2="140" y2="220" stroke="var(--info)" stroke-width="2"/>
      <circle cx="165" cy="175" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="165" y="179" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD3</text>

      <!-- Hub Shared Collision Domain -->
      <line x1="100" y1="270" x2="75" y2="300" stroke="var(--danger)" stroke-width="1.5"/>
      <line x1="140" y1="270" x2="165" y2="300" stroke="var(--danger)" stroke-width="1.5"/>
      <rect x="40" y="348" width="160" height="18" rx="4" fill="var(--danger-dim)"/>
      <text x="120" y="360" fill="var(--danger)" font-size="8" font-weight="800" text-anchor="middle">
        All PCs on Hub share CD3!
      </text>

      <!-- RIGHT SIDE HARDWARE (SWITCH 2 + HOSTS) -->
      <g transform="translate(650, 110)">
        <rect width="110" height="60" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <text x="55" y="28" font-size="14" text-anchor="middle">🔀</text>
        <text x="55" y="48" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">SWITCH 2</text>
      </g>
      <line x1="515" y1="170" x2="650" y2="140" stroke="var(--success)" stroke-width="2"/>
      <circle cx="580" cy="150" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="580" y="154" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD4</text>

      <rect x="580" y="240" width="80" height="45" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="620" y="265" fill="var(--tx-primary)" font-size="9" text-anchor="middle">PC 4</text>
      <line x1="680" y1="170" x2="630" y2="240" stroke="var(--success)" stroke-width="2"/>
      <circle cx="650" cy="210" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="650" y="214" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD5</text>

      <rect x="740" y="240" width="80" height="45" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="780" y="265" fill="var(--tx-primary)" font-size="9" text-anchor="middle">PC 5</text>
      <line x1="720" y1="170" x2="770" y2="240" stroke="var(--success)" stroke-width="2"/>
      <circle cx="750" cy="210" r="10" fill="var(--accent)" stroke="#fff" stroke-width="1"/>
      <text x="750" y="214" fill="#000" font-size="9" font-weight="900" text-anchor="middle">CD6</text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University Exam Gold Standard:</strong> <em>Collision Domains:</em> Every active port of a Switch or Router is an independent collision domain (here = 6 CDs). A Hub does NOT break collision domains. <em>Broadcast Domains:</em> Only Routers break broadcast domains (here = 2 BDs, one per router interface). Switches and Hubs forward broadcasts to all ports.
  </div>
</div>'''

# ==========================================
# 6. DIAGRAM 6: SDN 3-Tier Architecture
# ==========================================
svg_diagram_6 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🤖</span>
      <span class="diagram-title">Figure 4.6: Software-Defined Networking (SDN) 3-Tier Plane Architecture</span>
    </div>
    <span class="diagram-badge">NEXT-GEN NETWORKING</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-sdn" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TIER 1: APPLICATION PLANE -->
      <g transform="translate(40, 25)">
        <rect width="840" height="70" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="25" y="26" fill="var(--accent)" font-size="12" font-weight="800">1. APPLICATION PLANE (Network Services &amp; Business Logic)</text>
        
        <rect x="30" y="34" width="180" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="120" y="51" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">Load Balancing App</text>

        <rect x="230" y="34" width="180" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="320" y="51" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">Firewall / Security IDS</text>

        <rect x="430" y="34" width="180" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="520" y="51" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">QoS / Traffic Engineering</text>

        <rect x="630" y="34" width="180" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="720" y="51" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">VPN Orchestration</text>
      </g>

      <!-- NORTHBOUND API CONNECTOR -->
      <g transform="translate(360, 100)">
        <path d="M 100 0 L 100 30" stroke="var(--info)" stroke-width="3" marker-end="url(#arrow-sdn)"/>
        <text x="115" y="18" fill="var(--info)" font-size="10" font-weight="800">NORTHBOUND APIs (RESTful / JSON / gRPC)</text>
      </g>

      <!-- TIER 2: CONTROL PLANE (SDN CONTROLLER) -->
      <g transform="translate(40, 135)">
        <rect width="840" height="85" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
        <text x="25" y="26" fill="var(--info)" font-size="13" font-weight="900">
          2. CONTROL PLANE (Centralized SDN Controller / Network Operating System)
        </text>
        <text x="25" y="44" fill="var(--tx-muted)" font-size="10">
          Global Topology Map • Path Computation (Dijkstra) • Flow Table Programming • State Synchronization
        </text>

        <!-- Controller Engines -->
        <rect x="30" y="52" width="240" height="24" rx="4" fill="var(--info-dim)"/>
        <text x="150" y="68" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">OpenDaylight / ONOS Controller</text>

        <rect x="290" y="52" width="240" height="24" rx="4" fill="var(--info-dim)"/>
        <text x="410" y="68" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Central Routing Logic</text>

        <rect x="550" y="52" width="260" height="24" rx="4" fill="var(--info-dim)"/>
        <text x="680" y="68" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">East-West API (Multi-controller Federation)</text>
      </g>

      <!-- SOUTHBOUND API CONNECTOR -->
      <g transform="translate(360, 225)">
        <path d="M 100 0 L 100 30" stroke="var(--warning)" stroke-width="3" marker-end="url(#arrow-sdn)"/>
        <text x="115" y="18" fill="var(--warning)" font-size="10" font-weight="800">SOUTHBOUND APIs (OpenFlow / P4 / NETCONF)</text>
      </g>

      <!-- TIER 3: DATA PLANE (FORWARDING SWITCHES) -->
      <g transform="translate(40, 260)">
        <rect width="840" height="85" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <text x="25" y="24" fill="var(--warning)" font-size="12" font-weight="800">
          3. DATA PLANE (Infrastructure / Dumb Whitebox Packet Forwarders)
        </text>
        <text x="25" y="40" fill="var(--tx-muted)" font-size="9">
          No routing decisions • Executes flow tables pushed by controller • High-speed ASIC line-rate forwarding
        </text>

        <!-- Whitebox Forwarders -->
        <g transform="translate(40, 48)">
          <rect width="160" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
          <text x="80" y="18" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">OpenFlow Switch 1</text>
        </g>
        <g transform="translate(240, 48)">
          <rect width="160" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
          <text x="80" y="18" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">OpenFlow Switch 2</text>
        </g>
        <g transform="translate(440, 48)">
          <rect width="160" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
          <text x="80" y="18" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">OpenFlow Switch 3</text>
        </g>
        <g transform="translate(640, 48)">
          <rect width="160" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
          <text x="80" y="18" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">OpenFlow Switch 4</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Traditional vs. SDN Paradigm Shift:</strong> In traditional routers, the Control Plane (routing decision) and Data Plane (packet forwarding) are tightly bundled together inside each proprietary vendor box. SDN completely decouples them, moving all control intelligence to a centralized software controller, leaving hardware switches as cheap, fast packet executioners programmed via OpenFlow.
  </div>
</div>'''

# ==========================================
# 7. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 4
# ==========================================
ch4_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Network Interconnection Devices, Domain Calculations &amp; SDN Paradigm</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Tabulate the fundamental differences between a Repeater, Hub, Switch, Router, and Gateway with respect to: Operating OSI Layer, PDU processed, Hardware addressing inspected, and Forwarding decision logic. [4 Marks]<br>
          (b) Consider an enterprise network consisting of 1 Router (with 2 active LAN interfaces), 2 Switches (each having 8 ports), and 1 Hub (4 ports). If Switch 1 connects to one router interface and has 4 PCs and the Hub connected to it (with 3 PCs on the hub), and Switch 2 connects to the other router interface with 5 PCs, calculate: (i) Total number of Collision Domains, and (ii) Total number of Broadcast Domains. Show your step-by-step reasoning. [3 Marks]<br>
          (c) What is Software-Defined Networking (SDN)? Contrast traditional distributed routing with the centralized SDN architecture. Sketch and explain the 3-tier SDN plane model, highlighting the role of Northbound and Southbound APIs. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Network Devices Comparative Master Catalog</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Device</th>
                <th>OSI Layer</th>
                <th>PDU</th>
                <th>Address Inspected</th>
                <th>Forwarding Decision Logic</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Repeater / Hub</strong></td>
                <td>Layer 1 (Physical)</td>
                <td>Bits</td>
                <td>None (Blind signal regeneration)</td>
                <td>Copies input electrical signals to all other ports. Single shared collision domain.</td>
              </tr>
              <tr>
                <td><strong>Bridge / Switch</strong></td>
                <td>Layer 2 (Data Link)</td>
                <td>Frame</td>
                <td>48-bit MAC Address</td>
                <td>Inspects Destination MAC; consults CAM table. Unicast to target port or floods if unknown.</td>
              </tr>
              <tr>
                <td><strong>Router</strong></td>
                <td>Layer 3 (Network)</td>
                <td>Packet</td>
                <td>32-bit IPv4 / 128-bit IPv6</td>
                <td>Consults IP routing table using Longest Prefix Match (LPM). Breaks broadcast domains.</td>
              </tr>
              <tr>
                <td><strong>Gateway</strong></td>
                <td>All Layers (L1–L7)</td>
                <td>Application Data</td>
                <td>Full protocol headers</td>
                <td>Translates between incompatible protocol suites (e.g., IPv4 to IPv6, SMTP to SMS).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Domain Calculation &amp; Step-by-Step Proof</h4>
          <p><strong>Fundamental Axioms:</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Axiom 1:</strong> Every active point-to-point link on a Switch or Router forms an independent <strong>Collision Domain</strong>. Hubs do NOT break collision domains (all devices plugged into a hub share 1 collision domain with the switch port feeding it).</li>
            <li><strong>Axiom 2:</strong> Only Layer-3 Routers (or VLAN boundaries) break <strong>Broadcast Domains</strong>. Neither Switches nor Hubs break broadcast domains.</li>
          </ul>

          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin: 8px 0 14px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Step 1: Broadcast Domain Calculation:</strong><br>
              The router has 2 active LAN interfaces. Routers do not forward Layer-2 broadcast frames.<br>
              • Subnet A (fed by Router Interface 1 ➔ Switch 1): 1 Broadcast Domain<br>
              • Subnet B (fed by Router Interface 2 ➔ Switch 2): 1 Broadcast Domain<br>
              ➔ <strong>TOTAL BROADCAST DOMAINS = 2</strong><br><br>
              <strong>Step 2: Collision Domain Calculation:</strong><br>
              • <em>On Switch 1:</em><br>
              &nbsp;&nbsp;- Link between Router Interface 1 and Switch 1 = 1 CD<br>
              &nbsp;&nbsp;- 4 dedicated links to the 4 PCs = 4 CDs<br>
              &nbsp;&nbsp;- Link to Hub 1 = 1 CD (the Hub and all its 3 PCs share this single collision domain!)<br>
              &nbsp;&nbsp;Subtotal for Subnet A = 1 + 4 + 1 = <strong>6 Collision Domains</strong><br><br>
              • <em>On Switch 2:</em><br>
              &nbsp;&nbsp;- Link between Router Interface 2 and Switch 2 = 1 CD<br>
              &nbsp;&nbsp;- 5 dedicated links to the 5 PCs = 5 CDs<br>
              &nbsp;&nbsp;Subtotal for Subnet B = 1 + 5 = <strong>6 Collision Domains</strong><br><br>
              ➔ <strong>TOTAL COLLISION DOMAINS = 6 + 6 = 12</strong>
            </p>
          </div>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: SDN Principles &amp; Plane Architecture</h4>
          <p><strong>Software-Defined Networking (SDN) Definition:</strong> An architectural framework that decouples the network control plane (decision-making logic) from the underlying data plane (packet forwarding infrastructure), centralizing network state in a software-based controller.</p>
          
          <p><strong>Traditional vs. SDN Comparison:</strong> In traditional networks, each router independently computes shortest paths (using OSPF/BGP) and manages its own forwarding table—leading to decentralized, complex configuration and slow protocol convergence. In SDN, switches are simplified "whitebox" forwarding elements whose Flow Tables are directly programmed by a logically centralized SDN controller.</p>

          <p><strong>The Three Planes &amp; Interfaces (Refer to Figure 4.6):</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Application Plane:</strong> High-level business software specifying networking requirements (e.g., dynamic QoS for video calls, firewall rules, automated DDoS mitigation).</li>
            <li><strong>Northbound APIs:</strong> Programmatic RESTful/JSON interfaces allowing application developers to request network behavior directly from the SDN controller without understanding hardware specifics.</li>
            <li><strong>Control Plane (The Brain):</strong> The centralized Network Operating System (e.g., OpenDaylight, ONOS) that maintains a global topology map and installs flow rules.</li>
            <li><strong>Southbound APIs (OpenFlow):</strong> Standardized protocols (OpenFlow, P4, NETCONF) through which the controller writes flow matching entries into the ternary content-addressable memory (TCAM) of physical data plane switches.</li>
            <li><strong>Data Plane:</strong> High-speed hardware switches that match incoming packet headers against flow entries and execute actions (forward, drop, rewrite, meter).</li>
          </ul>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 4
# ==========================================
replacements = [
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Amplifier \(Boosts Noise\) vs\. Repeater \(Regenerates Pristine Signal\)</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_1),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Hub Internal Architecture: Physical Star, Logical Bus</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_2),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Transparent Bridge Learning Flowchart</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_3),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Visual Comparison: When Does Forwarding Begin\?</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_4),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Topology 1 Layout</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_5),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">The Complete 3-Tier SDN Model &amp; Interfaces</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_6),
]

for pattern, repl in replacements:
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + repl + content[match.end():]
        print(f'Successfully replaced pattern: {pattern[:40]}...')
    else:
        print(f'FAILED to match pattern: {pattern[:40]}...')

# Insert 10-Mark Blueprint into Chapter 4 before study-resources in s-summary-ch4
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch4_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 4!')

with open(ch4_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 4 upgrade completed!')
