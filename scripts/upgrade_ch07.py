"""
Upgrade Chapter 7 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch7_path = '/Users/arpit/minibook/cn/chapters/ch07-modulation-switching.html'
with open(ch7_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Digital Modulation & Constellation Diagrams (ASK, FSK, QPSK, 16-QAM)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📡</span>
      <span class="diagram-title">Figure 7.1: Digital Modulation Schemes &amp; I/Q Constellation Diagrams (ASK, FSK, QPSK, 16-QAM)</span>
    </div>
    <span class="diagram-badge">MODULATION &amp; CONSTELLATION</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: WAVEFORMS (ASK, FSK, BPSK) -->
      <g transform="translate(30, 25)">
        <rect width="420" height="315" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.8"/>
        <text x="210" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          A. DIGITAL MODULATION CARRIER WAVEFORMS
        </text>

        <!-- Test Bit Pattern: 1, 0, 1 -->
        <text x="70" y="50" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Bit 1</text>
        <text x="210" y="50" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Bit 0</text>
        <text x="350" y="50" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Bit 1</text>
        <line x1="140" y1="40" x2="140" y2="290" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="280" y1="40" x2="280" y2="290" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>

        <!-- 1. ASK (Amplitude Shift Keying) -->
        <g transform="translate(20, 65)">
          <text x="0" y="22" fill="var(--info)" font-size="10" font-weight="700">ASK: 1 = +A, 0 = 0</text>
          <!-- Bit 1: Sine active -->
          <path d="M 0 35 Q 25 10, 50 35 T 100 35" stroke="var(--info)" stroke-width="2" fill="none"/>
          <!-- Bit 0: Flat line 0V -->
          <line x1="120" y1="35" x2="240" y2="35" stroke="var(--info)" stroke-width="2"/>
          <!-- Bit 1: Sine active -->
          <path d="M 260 35 Q 285 10, 310 35 T 360 35" stroke="var(--info)" stroke-width="2" fill="none"/>
        </g>

        <!-- 2. FSK (Frequency Shift Keying) -->
        <g transform="translate(20, 145)">
          <text x="0" y="22" fill="var(--warning)" font-size="10" font-weight="700">FSK: 1 = High f₁, 0 = Low f₀</text>
          <!-- Bit 1: High freq -->
          <path d="M 0 35 Q 15 15, 30 35 T 60 35 T 90 35 T 120 35" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <!-- Bit 0: Low freq -->
          <path d="M 120 35 Q 150 15, 180 35 T 240 35" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <!-- Bit 1: High freq -->
          <path d="M 240 35 Q 255 15, 270 35 T 300 35 T 330 35 T 360 35" stroke="var(--warning)" stroke-width="2" fill="none"/>
        </g>

        <!-- 3. BPSK (Phase Shift Keying) -->
        <g transform="translate(20, 225)">
          <text x="0" y="22" fill="var(--success)" font-size="10" font-weight="700">BPSK: 1 = 0°, 0 = 180° Inversion</text>
          <!-- Bit 1: Starts upward -->
          <path d="M 0 35 Q 25 15, 50 35 T 100 35 T 120 35" stroke="var(--success)" stroke-width="2" fill="none"/>
          <!-- 180 deg phase jump at 120 -->
          <!-- Bit 0: Starts downward -->
          <path d="M 120 35 Q 145 55, 170 35 T 220 35 T 240 35" stroke="var(--success)" stroke-width="2" fill="none"/>
          <!-- 180 deg phase jump at 240 -->
          <!-- Bit 1: Starts upward -->
          <path d="M 240 35 Q 265 15, 290 35 T 340 35 T 360 35" stroke="var(--success)" stroke-width="2" fill="none"/>
        </g>
      </g>

      <!-- SECTION B: CONSTELLATION DIAGRAMS (QPSK & 16-QAM) -->
      <g transform="translate(480, 25)">
        <rect width="430" height="315" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="215" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          B. I/Q CONSTELLATION DIAGRAMS (QPSK &amp; 16-QAM)
        </text>

        <!-- SUBPANEL 1: QPSK (4 STATES, 2 BITS/SYMBOL) -->
        <g transform="translate(30, 45)">
          <rect width="170" height="230" rx="8" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="85" y="22" fill="var(--accent)" font-size="11" font-weight="800" text-anchor="middle">QPSK (4-PSK)</text>
          <text x="85" y="38" fill="var(--tx-muted)" font-size="9" text-anchor="middle">2 bits/baud ($r = 2$)</text>

          <!-- Axes -->
          <line x1="20" y1="125" x2="150" y2="125" stroke="var(--border)" stroke-width="1"/>
          <line x1="85" y1="60" x2="85" y2="190" stroke="var(--border)" stroke-width="1"/>
          <text x="145" y="120" fill="var(--tx-muted)" font-size="8">I</text>
          <text x="90" y="70" fill="var(--tx-muted)" font-size="8">Q</text>

          <!-- 4 Constellation Points -->
          <circle cx="120" cy="90" r="5" fill="var(--accent)"/>
          <text x="122" y="82" fill="var(--accent-light)" font-size="9" font-weight="700">00</text>

          <circle cx="50" cy="90" r="5" fill="var(--accent)"/>
          <text x="45" y="82" fill="var(--accent-light)" font-size="9" font-weight="700">01</text>

          <circle cx="50" cy="160" r="5" fill="var(--accent)"/>
          <text x="45" y="175" fill="var(--accent-light)" font-size="9" font-weight="700">11</text>

          <circle cx="120" cy="160" r="5" fill="var(--accent)"/>
          <text x="122" y="175" fill="var(--accent-light)" font-size="9" font-weight="700">10</text>

          <text x="85" y="210" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">4 Phases, Constant Amp</text>
        </g>

        <!-- SUBPANEL 2: 16-QAM (16 STATES, 4 BITS/SYMBOL) -->
        <g transform="translate(230, 45)">
          <rect width="170" height="230" rx="8" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="85" y="22" fill="#c084fc" font-size="11" font-weight="800" text-anchor="middle">16-QAM</text>
          <text x="85" y="38" fill="var(--tx-muted)" font-size="9" text-anchor="middle">4 bits/baud ($r = 4$)</text>

          <!-- Axes -->
          <line x1="20" y1="125" x2="150" y2="125" stroke="var(--border)" stroke-width="1"/>
          <line x1="85" y1="60" x2="85" y2="190" stroke="var(--border)" stroke-width="1"/>

          <!-- 16 Dots Grid in 4x4 -->
          <!-- Row 1 -->
          <circle cx="45" cy="80" r="3" fill="#c084fc"/>
          <circle cx="70" cy="80" r="3" fill="#c084fc"/>
          <circle cx="100" cy="80" r="3" fill="#c084fc"/>
          <circle cx="125" cy="80" r="3" fill="#c084fc"/>

          <!-- Row 2 -->
          <circle cx="45" cy="105" r="3" fill="#c084fc"/>
          <circle cx="70" cy="105" r="3" fill="#c084fc"/>
          <circle cx="100" cy="105" r="3" fill="#c084fc"/>
          <circle cx="125" cy="105" r="3" fill="#c084fc"/>

          <!-- Row 3 -->
          <circle cx="45" cy="145" r="3" fill="#c084fc"/>
          <circle cx="70" cy="145" r="3" fill="#c084fc"/>
          <circle cx="100" cy="145" r="3" fill="#c084fc"/>
          <circle cx="125" cy="145" r="3" fill="#c084fc"/>

          <!-- Row 4 -->
          <circle cx="45" cy="170" r="3" fill="#c084fc"/>
          <circle cx="70" cy="170" r="3" fill="#c084fc"/>
          <circle cx="100" cy="170" r="3" fill="#c084fc"/>
          <circle cx="125" cy="170" r="3" fill="#c084fc"/>

          <text x="85" y="210" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">3 Amplitudes + 12 Phases</text>
        </g>

        <!-- Bandwidth Efficiency Footer -->
        <text x="215" y="295" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">
          ★ Spectral Efficiency: 16-QAM transmits 4× more data than BPSK in the exact same channel bandwidth!
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Constellation Mathematics:</strong> In an In-Phase / Quadrature ($I/Q$) constellation diagram, the distance of a point from the origin represents its <em>peak amplitude</em>, and the angle with the horizontal axis represents its <em>phase shift</em>. QPSK packs 2 bits per symbol ($\log_2 4 = 2$); 16-QAM packs 4 bits per symbol ($\log_2 16 = 4$); modern Wi-Fi 7 uses 4096-QAM (12 bits/symbol!).
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Multiplexing Comparison (FDM vs TDM vs WDM)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔀</span>
      <span class="diagram-title">Figure 7.2: Multiplexing Comparison — Frequency (FDM), Time (TDM), and Wavelength (WDM)</span>
    </div>
    <span class="diagram-badge">BANDWIDTH AGGREGATION</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- FDM PANEL -->
      <g transform="translate(30, 25)">
        <rect width="260" height="300" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="15" y="15" width="230" height="28" rx="6" fill="var(--info-dim)"/>
        <text x="130" y="34" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">1. FDM (Frequency)</text>

        <!-- Frequency Spectrum with Guard Bands -->
        <g transform="translate(25, 60)">
          <!-- Channel 1 -->
          <rect y="0" width="210" height="32" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="105" y="20" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Channel 1 (Carrier f₁)</text>

          <!-- Guard Band 1 -->
          <rect y="35" width="210" height="12" fill="var(--danger-dim)"/>
          <text x="105" y="44" fill="var(--danger)" font-size="8" font-weight="800" text-anchor="middle">GUARD BAND (No Overlap)</text>

          <!-- Channel 2 -->
          <rect y="50" width="210" height="32" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="105" y="70" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Channel 2 (Carrier f₂)</text>

          <!-- Guard Band 2 -->
          <rect y="85" width="210" height="12" fill="var(--danger-dim)"/>
          <text x="105" y="94" fill="var(--danger)" font-size="8" font-weight="800" text-anchor="middle">GUARD BAND</text>

          <!-- Channel 3 -->
          <rect y="100" width="210" height="32" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="105" y="120" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Channel 3 (Carrier f₃)</text>
        </g>

        <text x="25" y="215" fill="var(--tx-primary)" font-size="10" font-weight="700">Analog Multiplexing:</text>
        <text x="25" y="232" fill="var(--tx-secondary)" font-size="9">• Divides continuous bandwidth</text>
        <text x="25" y="248" fill="var(--tx-secondary)" font-size="9">• Guard bands prevent crosstalk</text>
        <text x="25" y="275" fill="var(--info)" font-size="10" font-weight="700">Radio, FM Broadcast, Cable TV</text>
      </g>

      <!-- TDM PANEL -->
      <g transform="translate(320, 25)">
        <rect width="270" height="300" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="15" y="15" width="240" height="28" rx="6" fill="var(--warning-dim)"/>
        <text x="135" y="34" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">2. TDM (Time)</text>

        <!-- Time Slots in Frames -->
        <g transform="translate(25, 60)">
          <!-- Frame 1 -->
          <text x="0" y="15" fill="var(--warning)" font-size="9" font-weight="700">Frame 1 (Time t₁):</text>
          <g transform="translate(0, 22)">
            <rect x="0" y="0" width="65" height="35" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
            <text x="32" y="22" fill="var(--accent-light)" font-size="9" font-weight="800" text-anchor="middle">Slot A₁</text>

            <rect x="70" y="0" width="65" height="35" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
            <text x="102" y="22" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">Slot B₁</text>

            <rect x="140" y="0" width="65" height="35" rx="3" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
            <text x="172" y="22" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">Slot C₁</text>
          </g>

          <!-- Frame 2 -->
          <text x="0" y="80" fill="var(--warning)" font-size="9" font-weight="700">Frame 2 (Time t₂):</text>
          <g transform="translate(0, 87)">
            <rect x="0" y="0" width="65" height="35" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
            <text x="32" y="22" fill="var(--accent-light)" font-size="9" font-weight="800" text-anchor="middle">Slot A₂</text>

            <rect x="70" y="0" width="65" height="35" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
            <text x="102" y="22" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">Slot B₂</text>

            <rect x="140" y="0" width="65" height="35" rx="3" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
            <text x="172" y="22" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">Slot C₂</text>
          </g>
        </g>

        <text x="25" y="215" fill="var(--tx-primary)" font-size="10" font-weight="700">Digital Multiplexing:</text>
        <text x="25" y="232" fill="var(--tx-secondary)" font-size="9">• Entire channel bandwidth used</text>
        <text x="25" y="248" fill="var(--tx-secondary)" font-size="9">• Synchronous vs Statistical (STDM)</text>
        <text x="25" y="275" fill="var(--warning)" font-size="10" font-weight="700">T1 Carrier (1.544M), SONET</text>
      </g>

      <!-- WDM PANEL -->
      <g transform="translate(620, 25)">
        <rect width="270" height="300" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <rect x="15" y="15" width="240" height="28" rx="6" fill="var(--accent-dim)"/>
        <text x="135" y="34" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">3. WDM (Wavelength)</text>

        <!-- Optical Prism Combiner -->
        <g transform="translate(25, 60)">
          <!-- 3 Colored Light Beams -->
          <line x1="0" y1="20" x2="90" y2="60" stroke="#f87171" stroke-width="3"/>
          <text x="5" y="14" fill="#f87171" font-size="8" font-weight="700">λ₁ = 1310 nm</text>

          <line x1="0" y1="60" x2="90" y2="60" stroke="#34d399" stroke-width="3"/>
          <text x="5" y="54" fill="#34d399" font-size="8" font-weight="700">λ₂ = 1550 nm</text>

          <line x1="0" y1="100" x2="90" y2="60" stroke="#60a5fa" stroke-width="3"/>
          <text x="5" y="94" fill="#60a5fa" font-size="8" font-weight="700">λ₃ = 1625 nm</text>

          <!-- Optical Multiplexer Prism -->
          <polygon points="90,30 140,60 90,90" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="105" y="64" fill="var(--accent)" font-size="8" font-weight="800">MUX</text>

          <!-- Single Composite Fiber Output -->
          <line x1="140" y1="60" x2="220" y2="60" stroke="#fff" stroke-width="5"/>
          <text x="180" y="80" fill="var(--tx-primary)" font-size="8" font-weight="800" text-anchor="middle">Single Fiber</text>
        </g>

        <text x="25" y="215" fill="var(--tx-primary)" font-size="10" font-weight="700">Optical Domain Multiplexing:</text>
        <text x="25" y="232" fill="var(--tx-secondary)" font-size="9">• Multiple distinct laser wavelengths</text>
        <text x="25" y="248" fill="var(--tx-secondary)" font-size="9">• DWDM: 80+ channels on one strand</text>
        <text x="25" y="275" fill="var(--success)" font-size="10" font-weight="700">★ Terabit Backbone Infrastructure</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Architectural Analogy:</strong> <em>FDM</em> is like a highway divided into separate parallel lanes (frequencies) where all cars drive simultaneously. <em>TDM</em> is like a single high-speed lane where cars take turns entering in rapid alternating time slots. <em>WDM</em> is FDM implemented in the optical light domain using distinct photon wavelengths ($\lambda$).
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Switching Paradigms Sequence Timelines
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⏱️</span>
      <span class="diagram-title">Figure 7.3: Switching Sequence Timelines — Circuit Switching vs. Packet Switching</span>
    </div>
    <span class="diagram-badge">SWITCHING ENGINE TIMELINES</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-sw-seq" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: CIRCUIT SWITCHING TIMELINE -->
      <g transform="translate(30, 25)">
        <rect width="410" height="315" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <text x="205" y="24" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">
          1. CIRCUIT SWITCHING (3 Distinct Phases)
        </text>

        <!-- Vertical Timeline Nodes: Host A, Switch 1, Host B -->
        <g transform="translate(40, 45)">
          <line x1="40" y1="20" x2="40" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="40" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Host A</text>

          <line x1="165" y1="20" x2="165" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="165" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Switch</text>

          <line x1="290" y1="20" x2="290" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="290" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Host B</text>

          <!-- PHASE 1: SETUP -->
          <line x1="40" y1="35" x2="165" y2="60" stroke="var(--warning)" stroke-width="1.8" marker-end="url(#arrow-sw-seq)"/>
          <line x1="165" y1="60" x2="290" y2="85" stroke="var(--warning)" stroke-width="1.8" marker-end="url(#arrow-sw-seq)"/>
          <line x1="290" y1="95" x2="165" y2="120" stroke="var(--warning)" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrow-sw-seq)"/>
          <line x1="165" y1="120" x2="40" y2="145" stroke="var(--warning)" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrow-sw-seq)"/>
          <text x="5" y="90" fill="var(--warning)" font-size="9" font-weight="800">1. Setup Delay</text>

          <!-- PHASE 2: CONTINUOUS DATA STREAM -->
          <rect x="40" y="155" width="250" height="40" fill="rgba(126, 196, 184, 0.18)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="165" y="180" fill="var(--accent-light)" font-size="10" font-weight="800" text-anchor="middle">
            2. Continuous Data Stream (Zero Queuing Delay!)
          </text>

          <!-- PHASE 3: TEARDOWN -->
          <line x1="40" y1="210" x2="290" y2="235" stroke="var(--danger)" stroke-width="1.8" marker-end="url(#arrow-sw-seq)"/>
          <text x="5" y="225" fill="var(--danger)" font-size="9" font-weight="800">3. Teardown</text>
        </g>
      </g>

      <!-- RIGHT: PACKET SWITCHING (STORE-AND-FORWARD PIPELINING) -->
      <g transform="translate(480, 25)">
        <rect width="410" height="315" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="205" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          2. PACKET SWITCHING (Pipelined Store-and-Forward)
        </text>

        <!-- Vertical Timeline Nodes -->
        <g transform="translate(40, 45)">
          <line x1="40" y1="20" x2="40" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="40" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Host A</text>

          <line x1="165" y1="20" x2="165" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="165" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Router R1</text>

          <line x1="290" y1="20" x2="290" y2="250" stroke="var(--border)" stroke-width="1.5"/>
          <text x="290" y="12" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Host B</text>

          <!-- Packet 1 Transmission -->
          <line x1="40" y1="35" x2="165" y2="60" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <line x1="165" y1="65" x2="290" y2="90" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <text x="100" y="42" fill="var(--accent)" font-size="8" font-weight="700">Pkt 1</text>
          <text x="225" y="72" fill="var(--accent)" font-size="8" font-weight="700">Pkt 1</text>

          <!-- Packet 2 Transmission (Pipelined concurrently!) -->
          <line x1="40" y1="65" x2="165" y2="90" stroke="var(--info)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <line x1="165" y1="95" x2="290" y2="120" stroke="var(--info)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <text x="100" y="72" fill="var(--info)" font-size="8" font-weight="700">Pkt 2</text>
          <text x="225" y="102" fill="var(--info)" font-size="8" font-weight="700">Pkt 2</text>

          <!-- Packet 3 Transmission -->
          <line x1="40" y1="95" x2="165" y2="120" stroke="var(--warning)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <line x1="165" y1="125" x2="290" y2="150" stroke="var(--warning)" stroke-width="2.5" marker-end="url(#arrow-sw-seq)"/>
          <text x="100" y="102" fill="var(--warning)" font-size="8" font-weight="700">Pkt 3</text>
          <text x="225" y="132" fill="var(--warning)" font-size="8" font-weight="700">Pkt 3</text>

          <!-- PIPELINING CALLOUT -->
          <rect x="15" y="170" width="300" height="65" rx="6" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="1"/>
          <text x="165" y="190" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">
            ★ Pipelining Gain:
          </text>
          <text x="165" y="208" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">
            While R1 forwards Pkt 1 to Host B, Host A transmits Pkt 2 to R1.
          </text>
          <text x="165" y="222" fill="var(--tx-muted)" font-size="8" text-anchor="middle">
            Links operate concurrently in parallel!
          </text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Exam Comparison:</strong> Circuit switching incurs high initial connection setup delay ($t_{\text{setup}}$) but offers zero queuing delay once established (ideal for traditional voice). Packet switching eliminates setup delay and achieves dramatic throughput gains via store-and-forward <em>pipelining</em> across intermediate router links.
  </div>
</div>'''

# ==========================================
# 4. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 7
# ==========================================
ch7_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Multiplexing Techniques &amp; Circuit vs. Packet Switching Pipelining Derivation</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define Multiplexing. Differentiate between Frequency Division Multiplexing (FDM), Synchronous Time Division Multiplexing (STDM), and Wavelength Division Multiplexing (WDM) with neat structural diagrams. [3 Marks]<br>
          (b) Compare Circuit Switching and Packet Switching across: Call setup requirement, Resource reservation, Bandwidth efficiency, Latency characteristics, and Fault tolerance. [3 Marks]<br>
          (c) A file of size $F = 1\\text{ Megabyte } (10^6\\text{ bytes})$ is to be transmitted from Source Host A to Destination Host B across a path with $3$ point-to-point links and $2$ intermediate store-and-forward routers. Each link has a transmission rate $R = 10\\text{ Mbps}$ and a propagation delay $d_{\\text{prop}} = 5\\text{ ms}$. Assume negligible queuing and processing delays.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(i) Calculate total transfer time under <strong>Circuit Switching</strong> assuming connection setup requires $t_{\\text{setup}} = 300\\text{ ms}$ and teardown requires $50\\text{ ms}$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(ii) Calculate total transfer time under <strong>Packet Switching</strong> if the file is broken into packets of size $L = 1,000\\text{ bytes}$ (each having a 40-byte header included).<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(iii) Explain the physical origin of the pipelining advantage. [4 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Multiplexing Taxonomy</h4>
          <p><strong>Definition:</strong> The set of technical techniques that allow the simultaneous transmission of multiple information signals across a single shared physical data link to maximize channel utilization.</p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>FDM (Frequency Division Multiplexing):</strong> An analog technique where the total channel bandwidth is partitioned into non-overlapping frequency bands. Each user modulates a unique carrier frequency ($f_1, f_2, \\dots$). Guard bands (unused frequency strips) are inserted between channels to prevent inter-channel crosstalk.</li>
            <li><strong>STDM (Synchronous TDM):</strong> A digital technique where multiple digital streams interleave time slots onto a single high-speed line. Time slots are pre-allocated periodically regardless of whether a source has data to send (wasted slots if idle).</li>
            <li><strong>WDM (Wavelength Division Multiplexing):</strong> Analog multiplexing implemented in the optical domain. Multiple laser beams of distinct light wavelengths (colors: $\\lambda_1, \\lambda_2, \\dots$, typically in the $1550\\text{ nm}$ low-loss fiber window) are combined into a single optical fiber strand via a prism/diffraction multiplexer.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Circuit vs. Packet Switching</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Circuit Switching</th>
                <th>Packet Switching</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Call Setup Phase</strong></td>
                <td>Mandatory physical reservation before data transfer</td>
                <td>None (Connectionless datagram forwarding)</td>
              </tr>
              <tr>
                <td><strong>Resource Reservation</strong></td>
                <td>Dedicated end-to-end bandwidth allocated</td>
                <td>On-demand statistical multiplexing (shared buffers)</td>
              </tr>
              <tr>
                <td><strong>Bandwidth Utilization</strong></td>
                <td>Inefficient (silent pauses waste reserved capacity)</td>
                <td>Optimal (idle capacity absorbed by active users)</td>
              </tr>
              <tr>
                <td><strong>Congestion Effect</strong></td>
                <td>Call blocking at setup (busy signal)</td>
                <td>Packet queuing delay, buffer jitter, packet loss</td>
              </tr>
              <tr>
                <td><strong>Fault Tolerance</strong></td>
                <td>If any switch fails, the entire call terminates</td>
                <td>Dynamic rerouting of subsequent packets around failures</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Numerical Calculation &amp; Pipelining Proof</h4>
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 8px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Given Parameters:</strong><br>
              • File Size: $F = 1\\text{ MB} = 10^6\\text{ bytes} = 8 \\times 10^6\\text{ bits}$<br>
              • Link Rate: $R = 10\\text{ Mbps} = 10^7\\text{ bps}$<br>
              • Links: $N = 3$, Routers: $N - 1 = 2$<br>
              • Propagation Delay per link: $d_{\\text{prop}} = 5\\text{ ms} = 0.005\\text{ s}$<br>
              • Total 3-link Propagation: $3 \\times 5\\text{ ms} = 15\\text{ ms}$<br><br>

              <strong>(i) Circuit Switching Total Time:</strong><br>
              Once the circuit is established, bits flow continuously as a single unbroken stream from Host A to Host B without store-and-forward queuing delay at intermediate switches:<br>
              $$t_{\\text{trans}} = \\frac{F}{R} = \\frac{8 \\times 10^6\\text{ bits}}{10^7\\text{ bps}} = 0.8\\text{ seconds} = 800\\text{ ms}$$<br>
              $$T_{\\text{circuit}} = t_{\\text{setup}} + t_{\\text{trans}} + \\text{Total } d_{\\text{prop}} + t_{\\text{teardown}}$$<br>
              $$T_{\\text{circuit}} = 300\\text{ ms} + 800\\text{ ms} + 15\\text{ ms} + 50\\text{ ms} = \\mathbf{1,165\\text{ ms}} = \\mathbf{1.165\\text{ s}}$$<br><br>

              <strong>(ii) Packet Switching Total Time:</strong><br>
              • Number of packets: $P = \\frac{10^6\\text{ bytes}}{1,000\\text{ bytes}} = 1,000\\text{ packets}$<br>
              • Packet transmission delay: $$t_p = \\frac{L}{R} = \\frac{1,000 \\times 8\\text{ bits}}{10^7\\text{ bps}} = \\frac{8,000}{10,000,000} = 0.8\\text{ ms}$$<br>
              • Host A transmits all $P = 1,000$ packets in: $1,000 \\times 0.8\\text{ ms} = 800\\text{ ms}$.<br>
              • While Host A was transmitting, intermediate routers pipelined the preceding packets forward concurrently! Only the very last packet must traverse the remaining $(N-1) = 2$ router hops:<br>
              $$T_{\\text{packet}} = (P + N - 1) \\cdot t_p + N \\cdot d_{\\text{prop}}$$<br>
              $$T_{\\text{packet}} = (1,000 + 3 - 1) \\times 0.8\\text{ ms} + (3 \\times 5\\text{ ms})$$<br>
              $$T_{\\text{packet}} = (1,002 \\times 0.8\\text{ ms}) + 15\\text{ ms} = 801.6\\text{ ms} + 15\\text{ ms} = \\mathbf{816.6\\text{ ms}} = \\mathbf{0.817\\text{ s}}$$<br><br>

              <strong>(iii) Physical Origin of Pipelining Advantage:</strong><br>
              In packet switching, packet transmission overlaps across consecutive hops. While Router R1 is forwarding Packet 1 to Router R2, Host A is simultaneously transmitting Packet 2 to Router R1. All links operate in parallel, eliminating the 300 ms call setup overhead and reducing total transfer time from 1,165 ms to 816.6 ms!
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 7
# ==========================================
# Insert Diagram 1 into Section 7.5 (QPSK/QAM)
s5_target = re.search(r'<section id="s-qpsk"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s5_target:
    content = content[:s5_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s5_target.end():]
    print('Inserted Diagram 1 in Section 7.5')

# Insert Diagram 2 into Section 7.12 (Mux compare)
s12_target = re.search(r'<section id="s-mux-compare"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s12_target:
    content = content[:s12_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s12_target.end():]
    print('Inserted Diagram 2 in Section 7.12')

# Insert Diagram 3 into Section 7.18 (Switch compare)
s18_target = re.search(r'<section id="s-switch-compare"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s18_target:
    content = content[:s18_target.end()] + '\n' + svg_diagram_3 + '\n' + content[s18_target.end():]
    print('Inserted Diagram 3 in Section 7.18')

# Insert 10-Mark Blueprint into Chapter 7 before study-resources in s-summary-ch7
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch7_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 7!')

with open(ch7_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 7 upgrade completed!')
