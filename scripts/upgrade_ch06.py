"""
Upgrade Chapter 6 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch6_path = '/Users/arpit/minibook/cn/chapters/ch06-media-signaling.html'
with open(ch6_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Transmission Media Cross-Sections & Optical Fiber TIR
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔬</span>
      <span class="diagram-title">Figure 6.1: Physical Cross-Sections of Guided Media &amp; Optical Fiber TIR Physics</span>
    </div>
    <span class="diagram-badge">CABLE ARCHITECTURE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: UTP TWISTED PAIR -->
      <g transform="translate(30, 25)">
        <rect width="260" height="300" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="130" y="24" fill="var(--accent)" font-size="11" font-weight="800" text-anchor="middle">
          1. TWISTED PAIR (Cat6 UTP)
        </text>

        <!-- Circular Cross Section -->
        <g transform="translate(130, 95)">
          <circle cx="0" cy="0" r="55" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="2"/>
          <circle cx="0" cy="0" r="50" fill="var(--bg-surface)"/>
          
          <!-- Central Spline Cross -->
          <line x1="-35" y1="0" x2="35" y2="0" stroke="var(--border)" stroke-width="3"/>
          <line x1="0" y1="-35" x2="0" y2="35" stroke="var(--border)" stroke-width="3"/>

          <!-- 4 Pairs (Blue, Orange, Green, Brown) -->
          <circle cx="-20" cy="-20" r="10" fill="var(--info)" stroke="#fff" stroke-width="1"/>
          <circle cx="-25" cy="-10" r="10" fill="#fff" stroke="var(--info)" stroke-width="1"/>

          <circle cx="20" cy="-20" r="10" fill="var(--warning)" stroke="#fff" stroke-width="1"/>
          <circle cx="25" cy="-10" r="10" fill="#fff" stroke="var(--warning)" stroke-width="1"/>

          <circle cx="-20" cy="20" r="10" fill="var(--success)" stroke="#fff" stroke-width="1"/>
          <circle cx="-25" cy="10" r="10" fill="#fff" stroke="var(--success)" stroke-width="1"/>

          <circle cx="20" cy="20" r="10" fill="#a855f7" stroke="#fff" stroke-width="1"/>
          <circle cx="25" cy="10" r="10" fill="#fff" stroke="#a855f7" stroke-width="1"/>
        </g>

        <text x="20" y="175" fill="var(--tx-primary)" font-size="11" font-weight="700">Engineering Physics:</text>
        <text x="20" y="195" fill="var(--tx-secondary)" font-size="10">• Twisting cancels electromagnetic</text>
        <text x="20" y="210" fill="var(--tx-secondary)" font-size="10">&nbsp;&nbsp;interference (differential signaling)</text>
        <text x="20" y="228" fill="var(--tx-secondary)" font-size="10">• Plastic spline isolates pairs</text>
        <text x="20" y="246" fill="var(--tx-secondary)" font-size="10">• Standard: RJ-45 (100 m limit)</text>
        <text x="20" y="275" fill="var(--accent)" font-size="10" font-weight="700">Bandwidth: Up to 10 Gbps (Cat6A)</text>
      </g>

      <!-- SECTION B: COAXIAL CABLE -->
      <g transform="translate(310, 25)">
        <rect width="260" height="300" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="130" y="24" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">
          2. COAXIAL CABLE (RG-6 / RG-58)
        </text>

        <!-- Concentric Cylinder Cross Section -->
        <g transform="translate(130, 95)">
          <!-- Outer Jacket -->
          <circle cx="0" cy="0" r="55" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="2"/>
          <!-- Braided Shield -->
          <circle cx="0" cy="0" r="44" fill="none" stroke="var(--tx-muted)" stroke-width="3" stroke-dasharray="3,2"/>
          <!-- Foil Shield -->
          <circle cx="0" cy="0" r="38" fill="none" stroke="var(--info)" stroke-width="1.5"/>
          <!-- Dielectric Insulator -->
          <circle cx="0" cy="0" r="32" fill="var(--bg-surface)"/>
          <!-- Inner Copper Conductor -->
          <circle cx="0" cy="0" r="12" fill="var(--warning)" stroke="#fff" stroke-width="1.5"/>
        </g>

        <text x="20" y="175" fill="var(--tx-primary)" font-size="11" font-weight="700">Concentric Architecture:</text>
        <text x="20" y="195" fill="var(--tx-secondary)" font-size="10">• Inner core carries signal</text>
        <text x="20" y="210" fill="var(--tx-secondary)" font-size="10">• Braided mesh shields from EMI</text>
        <text x="20" y="228" fill="var(--tx-secondary)" font-size="10">• High noise immunity vs UTP</text>
        <text x="20" y="246" fill="var(--tx-secondary)" font-size="10">• Standard: BNC / F-Type connectors</text>
        <text x="20" y="275" fill="var(--info)" font-size="10" font-weight="700">Cable TV, Broadband DOCSIS, CCTV</text>
      </g>

      <!-- SECTION C: OPTICAL FIBER TIR -->
      <g transform="translate(590, 25)">
        <rect width="300" height="300" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <text x="150" y="24" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">
          3. OPTICAL FIBER &amp; SNELL'S LAW (TIR)
        </text>

        <!-- Fiber Core / Cladding Longitudinal View -->
        <g transform="translate(20, 45)">
          <!-- Cladding Upper (n2) -->
          <rect width="260" height="28" fill="rgba(251, 191, 36, 0.15)" stroke="var(--warning)" stroke-width="1"/>
          <text x="130" y="18" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">
            Cladding (Refractive Index n₂ = 1.46)
          </text>

          <!-- Core (n1 > n2) -->
          <rect y="28" width="260" height="50" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="130" y="58" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">
            Glass Core (n₁ = 1.48 &gt; n₂)
          </text>

          <!-- Light Ray Bouncing via TIR -->
          <path d="M 10 70 L 60 30 L 120 70 L 180 30 L 240 70" stroke="var(--danger)" stroke-width="2.5" fill="none" marker-end="url(#arrow-ray)"/>

          <!-- Cladding Lower (n2) -->
          <rect y="78" width="260" height="28" fill="rgba(251, 191, 36, 0.15)" stroke="var(--warning)" stroke-width="1"/>
          <text x="130" y="96" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">
            Cladding (Refractive Index n₂ = 1.46)
          </text>
        </g>

        <!-- TIR Mathematical Law -->
        <rect x="15" y="165" width="270" height="60" rx="6" fill="var(--bg-elevated)" stroke="var(--warning)" stroke-width="1"/>
        <text x="25" y="184" fill="var(--warning)" font-size="10" font-weight="800">Critical Angle Equation (Snell's Law):</text>
        <text x="25" y="204" fill="var(--tx-primary)" font-family="var(--font-mono)" font-size="11">
          θ_c = arcsin(n₂ / n₁)
        </text>
        <text x="25" y="218" fill="var(--tx-muted)" font-size="9">If angle of incidence θ &gt; θ_c: 100% Light Reflected!</text>

        <text x="20" y="245" fill="var(--tx-secondary)" font-size="10">• Immune to electromagnetic noise (RFI/EMI)</text>
        <text x="20" y="260" fill="var(--tx-secondary)" font-size="10">• Attenuation &lt; 0.2 dB/km at 1550 nm</text>
        <text x="20" y="278" fill="var(--success)" font-size="10" font-weight="700">★ Terabits/sec over submarine trunks</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Total Internal Reflection (TIR) Condition:</strong> Light is entirely guided within the glass core without escaping if and only if two conditions are met: (1) Core refractive index is strictly greater than cladding ($n_1 > n_2$), and (2) The angle of incidence at the core-cladding boundary exceeds the critical angle ($\theta > \theta_c$).
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Master Line Coding Comparison (NRZ-L, NRZ-I, Manchester, Diff Manchester, AMI)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📊</span>
      <span class="diagram-title">Figure 6.2: Master Line Coding Waveforms — NRZ-L, NRZ-I, Manchester, Diff Manchester &amp; AMI</span>
    </div>
    <span class="diagram-badge">SIGNAL ENCODING MATRIX</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="420" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- BIT STREAM HEADER: [ 0, 1, 0, 0, 1, 1, 0, 1 ] -->
      <!-- 8 bit intervals, width = 85 each, start = 180 -->
      <!-- Bit 1: 180-265 (0) -->
      <!-- Bit 2: 265-350 (1) -->
      <!-- Bit 3: 350-435 (0) -->
      <!-- Bit 4: 435-520 (0) -->
      <!-- Bit 5: 520-605 (1) -->
      <!-- Bit 6: 605-690 (1) -->
      <!-- Bit 7: 690-775 (0) -->
      <!-- Bit 8: 775-860 (1) -->

      <g transform="translate(180, 20)">
        <!-- Vertical Guidelines -->
        <line x1="0" y1="25" x2="0" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="85" y1="25" x2="85" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="170" y1="25" x2="170" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="255" y1="25" x2="255" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="340" y1="25" x2="340" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="425" y1="25" x2="425" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="510" y1="25" x2="510" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="595" y1="25" x2="595" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="680" y1="25" x2="680" y2="390" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>

        <!-- Bit Labels -->
        <text x="42" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">0</text>
        <text x="127" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">1</text>
        <text x="212" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">0</text>
        <text x="297" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">0</text>
        <text x="382" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">1</text>
        <text x="467" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">1</text>
        <text x="552" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">0</text>
        <text x="637" y="15" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">1</text>
      </g>

      <!-- ROW 1: NRZ-L (0 = +V, 1 = -V) -->
      <g transform="translate(30, 55)">
        <text x="0" y="30" fill="var(--info)" font-size="11" font-weight="800">1. Polar NRZ-L</text>
        <text x="0" y="44" fill="var(--tx-muted)" font-size="8">0 = +V, 1 = -V</text>
        <!-- Trace (y=15 for +V, y=45 for -V) -->
        <path d="M 150 15 L 235 15 L 235 45 L 320 45 L 320 15 L 490 15 L 490 45 L 660 45 L 660 15 L 745 15 L 745 45 L 830 45" stroke="var(--info)" stroke-width="2.5" fill="none"/>
      </g>

      <!-- ROW 2: NRZ-I (Transition on 1, No transition on 0) -->
      <g transform="translate(30, 125)">
        <text x="0" y="30" fill="var(--accent)" font-size="11" font-weight="800">2. Polar NRZ-I</text>
        <text x="0" y="44" fill="var(--tx-muted)" font-size="8">Transition on 1</text>
        <!-- Initial state assumed -V (y=45) -->
        <!-- Bit 1 (0): stays -V (150-235) -->
        <!-- Bit 2 (1): trans to +V (235-320) -->
        <!-- Bit 3 (0): stays +V (320-405) -->
        <!-- Bit 4 (0): stays +V (405-490) -->
        <!-- Bit 5 (1): trans to -V (490-575) -->
        <!-- Bit 6 (1): trans to +V (575-660) -->
        <!-- Bit 7 (0): stays +V (660-745) -->
        <!-- Bit 8 (1): trans to -V (745-830) -->
        <path d="M 150 45 L 235 45 L 235 15 L 490 15 L 490 45 L 575 45 L 575 15 L 745 15 L 745 45 L 830 45" stroke="var(--accent)" stroke-width="2.5" fill="none"/>
      </g>

      <!-- ROW 3: BIPOLAR AMI (0 = 0V, 1 = Alternating +V/-V) -->
      <g transform="translate(30, 195)">
        <text x="0" y="30" fill="var(--warning)" font-size="11" font-weight="800">3. Bipolar AMI</text>
        <text x="0" y="44" fill="var(--tx-muted)" font-size="8">0=0V, 1=Alt +/-V</text>
        <!-- y=15 (+V), y=30 (0V), y=45 (-V) -->
        <path d="M 150 30 L 235 30 L 235 15 L 320 15 L 320 30 L 490 30 L 490 45 L 575 45 L 575 15 L 660 15 L 660 30 L 745 30 L 745 45 L 830 45" stroke="var(--warning)" stroke-width="2.5" fill="none"/>
      </g>

      <!-- ROW 4: MANCHESTER (IEEE 802.3: 0 = Low-to-High, 1 = High-to-Low) -->
      <g transform="translate(30, 265)">
        <text x="0" y="30" fill="var(--success)" font-size="11" font-weight="800">4. Manchester</text>
        <text x="0" y="44" fill="var(--tx-muted)" font-size="8">Mid-bit: 0=L➔H, 1=H➔L</text>
        <!-- Bit 1 (0): 150-192.5 at 45, 192.5-235 at 15 -->
        <!-- Bit 2 (1): 235-277.5 at 15, 277.5-320 at 45 -->
        <!-- Bit 3 (0): 320-362.5 at 45, 362.5-405 at 15 -->
        <!-- Bit 4 (0): 405-447.5 at 45, 447.5-490 at 15 -->
        <!-- Bit 5 (1): 490-532.5 at 15, 532.5-575 at 45 -->
        <!-- Bit 6 (1): 575-617.5 at 15, 617.5-660 at 45 -->
        <!-- Bit 7 (0): 660-702.5 at 45, 702.5-745 at 15 -->
        <!-- Bit 8 (1): 745-787.5 at 15, 787.5-830 at 45 -->
        <path d="M 150 45 L 192.5 45 L 192.5 15 L 277.5 15 L 277.5 45 L 362.5 45 L 362.5 15 L 405 15 L 405 45 L 447.5 45 L 447.5 15 L 490 15 L 532.5 15 L 532.5 45 L 575 45 L 575 15 L 617.5 15 L 617.5 45 L 702.5 45 L 702.5 15 L 745 15 L 787.5 15 L 787.5 45 L 830 45" stroke="var(--success)" stroke-width="2.5" fill="none"/>
      </g>

      <!-- ROW 5: DIFFERENTIAL MANCHESTER (Transition at start = 0, None = 1) -->
      <g transform="translate(30, 335)">
        <text x="0" y="30" fill="#c084fc" font-size="11" font-weight="800">5. Diff Manchester</text>
        <text x="0" y="44" fill="var(--tx-muted)" font-size="8">Trans at start = 0</text>
        <path d="M 150 15 L 192.5 15 L 192.5 45 L 277.5 45 L 277.5 15 L 320 15 L 320 45 L 362.5 45 L 362.5 15 L 405 15 L 405 45 L 447.5 45 L 447.5 15 L 532.5 15 L 532.5 45 L 617.5 45 L 617.5 15 L 660 15 L 660 45 L 702.5 45 L 702.5 15 L 787.5 15 L 787.5 45 L 830 45" stroke="#c084fc" stroke-width="2.5" fill="none"/>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Line Coding Evaluation Criteria:</strong> <em>Self-Synchronization:</em> Manchester and Differential Manchester feature guaranteed transitions at the center of every bit, providing the receiver with an integrated clock signal (eliminating baseline wander and DC component). However, this doubles signal baud rate ($\text{Baud} = 2 \times \text{Bit Rate}$), requiring double the channel bandwidth.
  </div>
</div>'''

# ==========================================
# 3. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 6
# ==========================================
ch6_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Transmission Media Comparison, Optical Fiber TIR Physics &amp; Line Coding Waveforms</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Compare Twisted Pair, Coaxial Cable, and Optical Fiber across: Physical transmission mechanism, Maximum segment distance, Data rate capability, Electromagnetic noise immunity, and Relative installation cost. [3 Marks]<br>
          (b) Explain the physics of light propagation through optical fibers based on Snell's Law and Total Internal Reflection (TIR). Derive the mathematical expression for the Critical Angle ($\\theta_c$) and Acceptance Angle (Numerical Aperture, $\\text{NA}$). [3 Marks]<br>
          (c) For the digital bit sequence <code>0 1 0 0 1 1 1 0</code>, sketch the corresponding signal waveforms for: (i) Polar NRZ-L, (ii) Polar NRZ-I, (iii) Bipolar AMI, (iv) Manchester (IEEE 802.3), and (v) Differential Manchester. Explain why Manchester coding requires twice the bandwidth of NRZ-L. [4 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Guided Transmission Media Comparative Matrix</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Parameter</th>
                <th>Twisted Pair (Cat6)</th>
                <th>Coaxial Cable (RG-6)</th>
                <th>Optical Fiber (Single-Mode)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Signal Carrier</strong></td>
                <td>Electrical differential voltages</td>
                <td>Electrical RF current</td>
                <td>Infrared/visible light pulses (photons)</td>
              </tr>
              <tr>
                <td><strong>Max Segment Distance</strong></td>
                <td>100 meters (Ethernet standard)</td>
                <td>185 m (Thinnet) – 500 m (Thicknet)</td>
                <td>40 km – 100 km (without repeaters)</td>
              </tr>
              <tr>
                <td><strong>Data Rate</strong></td>
                <td>Up to 10 Gbps (10GBASE-T)</td>
                <td>10–100 Mbps (legacy), 1 Gbps (DOCSIS)</td>
                <td>100 Gbps – Terabits/sec (DWDM)</td>
              </tr>
              <tr>
                <td><strong>EMI / RFI Immunity</strong></td>
                <td>Low to Moderate (vulnerable to crosstalk)</td>
                <td>High (braided metal copper shield)</td>
                <td>Absolute 100% Immunity (dielectric glass)</td>
              </tr>
              <tr>
                <td><strong>Relative Cost</strong></td>
                <td>Lowest (cheap copper &amp; RJ45 crimping)</td>
                <td>Moderate</td>
                <td>Highest (fusion splicing &amp; transceivers)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Optical Fiber Total Internal Reflection Derivation</h4>
          <p><strong>Snell's Law:</strong> $$n_1 \\sin(\\theta_1) = n_2 \\sin(\\theta_2)$$ where $n_1$ is the core refractive index and $n_2$ is the cladding refractive index ($n_1 > n_2$).</p>
          <p><strong>Critical Angle ($\\theta_c$):</strong> As the angle of incidence $\\theta_1$ increases, the refracted angle $\\theta_2$ in the cladding reaches $90^\\circ$. Substituting $\\theta_2 = 90^\\circ$ into Snell's Law:</p>
          $$n_1 \\sin(\\theta_c) = n_2 \\sin(90^\\circ) = n_2 \\implies \\sin(\\theta_c) = \\frac{n_2}{n_1} \\implies \\mathbf{\\theta_c = \\arcsin\\left(\\frac{n_2}{n_1}\\right)}$$
          <p>If the incident light ray strikes the core-cladding boundary at an angle $\\theta_1 > \\theta_c$, zero light refracts into the cladding; 100% of light power is reflected back into the core via <strong>Total Internal Reflection (TIR)</strong>.</p>
          <p><strong>Numerical Aperture ($\\text{NA}$):</strong> Measures the light-gathering ability of the fiber face from air ($n_0 = 1$):</p>
          $$\\text{NA} = \\sin(\\theta_{\\text{max}}) = \\sqrt{n_1^2 - n_2^2}$$
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Line Coding Waveforms &amp; Bandwidth Analysis</h4>
          <p><strong>Waveform Definitions for Bit Pattern <code>0 1 0 0 1 1 1 0</code> (Refer to Figure 6.2):</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Polar NRZ-L (Level):</strong> Bit <code>0</code> = $+V$, Bit <code>1</code> = $-V$. (Waveform: $+V, -V, +V, +V, -V, -V, -V, +V$).</li>
            <li><strong>Polar NRZ-I (Invert on 1):</strong> Invert signal level at the start of bit <code>1</code>; keep level unchanged for bit <code>0</code>.</li>
            <li><strong>Bipolar AMI:</strong> Bit <code>0</code> = $0\\text{ V}$, Bit <code>1</code> = alternating $+V$ and $-V$. Eliminates DC component.</li>
            <li><strong>Manchester (IEEE 802.3):</strong> Bit <code>0</code> = Low-to-High transition at mid-bit; Bit <code>1</code> = High-to-Low transition at mid-bit.</li>
            <li><strong>Differential Manchester:</strong> Transition at the start of bit interval signifies <code>0</code>; absence of transition at start signifies <code>1</code>. Mid-bit transition always occurs to provide clock synchronization.</li>
          </ul>

          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 10px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Why Manchester Requires Twice the Bandwidth of NRZ:</strong><br>
              In NRZ, each bit interval contains at most 1 signal level transition (worst-case bit pattern <code>010101</code> produces frequency $f = R / 2\\text{ Hz}$).<br>
              In Manchester coding, there is <strong>guaranteed to be at least one transition at the center of EVERY bit</strong>. In the worst-case (consecutive zeros or consecutive ones), there are 2 transitions per bit interval, yielding a fundamental frequency $f = R\\text{ Hz}$.<br>
              Therefore, the <strong>minimum Nyquist bandwidth required for Manchester is $B_{\\text{min}} = R\\text{ Hz}$</strong> (exactly double that of NRZ $B_{\\text{min}} = R/2\\text{ Hz}$). The penalty of doubling bandwidth is paid to achieve perfect clock synchronization and zero DC component.
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 6
# ==========================================
# Insert Diagram 1 into Section 6.4 (Fiber)
s4_target = re.search(r'<section id="s-fiber"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s4_target:
    content = content[:s4_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s4_target.end():]
    print('Inserted Diagram 1 in Section 6.4')

# Insert Diagram 2 into Section 6.14 (Line compare)
s14_target = re.search(r'<section id="s-line-compare"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s14_target:
    content = content[:s14_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s14_target.end():]
    print('Inserted Diagram 2 in Section 6.14')

# Insert 10-Mark Blueprint into Chapter 6 before study-resources in s-summary-ch6
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch6_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 6!')

with open(ch6_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 6 upgrade completed!')
