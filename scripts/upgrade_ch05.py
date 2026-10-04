"""
Upgrade Chapter 5 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch5_path = '/Users/arpit/minibook/cn/chapters/ch05-physical-fundamentals.html'
with open(ch5_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Sine Wave Anatomy & Fourier Harmonic Synthesis
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">〰️</span>
      <span class="diagram-title">Figure 5.1: Sine Wave Parameters &amp; Fourier Harmonic Approximation of Digital Pulses</span>
    </div>
    <span class="diagram-badge">SIGNAL MATHEMATICS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ch5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT PANEL: SINE WAVE ANATOMY -->
      <g transform="translate(30, 25)">
        <rect width="400" height="300" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="200" y="26" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          A. ANALOG SINE WAVE ANATOMY: s(t) = A · sin(2πft + φ)
        </text>

        <!-- Coordinate axes -->
        <line x1="50" y1="160" x2="370" y2="160" stroke="var(--border)" stroke-width="1.5"/>
        <line x1="70" y1="50" x2="70" y2="270" stroke="var(--border)" stroke-width="1.5"/>
        <text x="370" y="155" fill="var(--tx-muted)" font-size="10">Time (t)</text>
        <text x="65" y="45" fill="var(--tx-muted)" font-size="10" text-anchor="end">Voltage (V)</text>

        <!-- Sine Wave Curve -->
        <path d="M 70 160 Q 120 70, 170 160 T 270 160 T 370 160" stroke="var(--accent)" stroke-width="3" fill="none"/>

        <!-- Amplitude Annotation -->
        <line x1="120" y1="160" x2="120" y2="70" stroke="var(--info)" stroke-width="1.8" stroke-dasharray="3,3"/>
        <circle cx="120" cy="70" r="4" fill="var(--info)"/>
        <text x="130" y="115" fill="var(--info)" font-size="11" font-weight="800">Peak Amplitude (A)</text>

        <!-- Period T Annotation -->
        <line x1="70" y1="230" x2="270" y2="230" stroke="var(--warning)" stroke-width="1.5" marker-end="url(#arrow-ch5)"/>
        <line x1="70" y1="160" x2="70" y2="240" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="270" y1="160" x2="270" y2="240" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
        <text x="170" y="248" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">
          Period T = 1 / f (seconds)
        </text>

        <text x="200" y="282" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">
          Frequency f = 1/T (Hz) • Phase φ = offset in radians/degrees
        </text>
      </g>

      <!-- RIGHT PANEL: FOURIER HARMONIC SYNTHESIS -->
      <g transform="translate(460, 25)">
        <rect width="430" height="300" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="215" y="26" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">
          B. FOURIER SYNTHESIS: SQUARE WAVE FROM SINE HARMONICS
        </text>

        <!-- Formula display -->
        <rect x="20" y="40" width="390" height="30" rx="4" fill="var(--info-dim)"/>
        <text x="215" y="60" fill="var(--info)" font-family="var(--font-mono)" font-size="10" font-weight="700" text-anchor="middle">
          s(t) = (4A/π) · [ sin(2πft) + (1/3)sin(6πft) + (1/5)sin(10πft) + ... ]
        </text>

        <!-- Waveform traces -->
        <!-- Trace 1: Fundamental alone (f) -->
        <g transform="translate(30, 85)">
          <path d="M 0 30 Q 40 5, 80 30 T 160 30 T 240 30 T 320 30 T 360 30" stroke="var(--tx-muted)" stroke-width="1.5" fill="none"/>
          <text x="365" y="32" fill="var(--tx-muted)" font-size="9">1 Harmonic (f)</text>
        </g>

        <!-- Trace 2: Fundamental + 3rd Harmonic -->
        <g transform="translate(30, 145)">
          <path d="M 0 30 Q 20 12, 40 18 Q 60 24, 80 30 Q 100 48, 120 42 Q 140 36, 160 30 Q 180 12, 200 18 Q 220 24, 240 30 Q 260 48, 280 42 Q 300 36, 320 30" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <text x="365" y="32" fill="var(--warning)" font-size="9">3 Harmonics (f + 3f)</text>
        </g>

        <!-- Trace 3: Many harmonics approaching sharp square pulse -->
        <g transform="translate(30, 205)">
          <path d="M 0 30 L 5 5 L 75 5 L 85 55 L 155 55 L 165 5 L 235 5 L 245 55 L 315 55 L 320 30" stroke="var(--success)" stroke-width="2.5" fill="none"/>
          <text x="365" y="32" fill="var(--success)" font-size="9">Infinite (Square Wave)</text>
        </g>

        <text x="215" y="285" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">
          ★ Physical channels act as Low-Pass Filters: truncating higher harmonics rounds square pulses!
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Fourier Insight for Networking:</strong> A pristine digital square bit (0 or 1) requires <em>infinite bandwidth</em> containing all odd harmonics. When a transmission channel limits bandwidth, higher harmonics are chopped off, causing sharp square pulses to distort and spread across adjacent bit intervals (Inter-Symbol Interference).
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Transmission Impairments (Attenuation, Distortion, Noise)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚠️</span>
      <span class="diagram-title">Figure 5.2: The Three Transmission Impairments — Attenuation, Distortion, and Noise</span>
    </div>
    <span class="diagram-badge">PHYSICAL IMPAIRMENTS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- IMPAIRMENT 1: ATTENUATION -->
      <g transform="translate(30, 25)">
        <rect width="260" height="295" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="15" y="15" width="230" height="28" rx="6" fill="var(--info-dim)"/>
        <text x="130" y="34" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">1. ATTENUATION (Loss)</text>

        <!-- Attenuation waveform trace -->
        <g transform="translate(20, 60)">
          <!-- Original -->
          <path d="M 0 35 Q 25 5, 50 35 T 100 35" stroke="var(--accent)" stroke-width="2.5" fill="none"/>
          <text x="50" y="55" fill="var(--accent)" font-size="9" text-anchor="middle">Transmitted Signal</text>

          <text x="110" y="38" fill="var(--tx-muted)" font-size="16">➔</text>

          <!-- Attenuated -->
          <path d="M 125 35 Q 150 24, 175 35 T 225 35" stroke="var(--info)" stroke-width="2" fill="none"/>
          <text x="175" y="55" fill="var(--info)" font-size="9" text-anchor="middle">Attenuated (Distance)</text>
        </g>

        <text x="25" y="145" fill="var(--tx-primary)" font-size="11" font-weight="700">Physical Cause:</text>
        <text x="25" y="165" fill="var(--tx-secondary)" font-size="10">• Electrical resistance of copper</text>
        <text x="25" y="182" fill="var(--tx-secondary)" font-size="10">• Absorption &amp; scattering in fiber</text>
        <text x="25" y="199" fill="var(--tx-secondary)" font-size="10">• Energy converted to heat</text>

        <rect x="15" y="215" width="230" height="65" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="235" fill="var(--info)" font-size="10" font-weight="800">Decibel Formula:</text>
        <text x="25" y="255" fill="var(--tx-primary)" font-family="var(--font-mono)" font-size="11">dB = 10 · log₁₀(P₂ / P₁)</text>
        <text x="25" y="270" fill="var(--tx-muted)" font-size="9">Countered by: Amplifiers &amp; Repeaters</text>
      </g>

      <!-- IMPAIRMENT 2: DISTORTION -->
      <g transform="translate(320, 25)">
        <rect width="270" height="295" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="15" y="15" width="240" height="28" rx="6" fill="var(--warning-dim)"/>
        <text x="135" y="34" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">2. DISTORTION (Phase Shift)</text>

        <!-- Distortion waveform trace -->
        <g transform="translate(20, 60)">
          <!-- Original Composite -->
          <path d="M 0 35 L 20 15 L 40 15 L 60 55 L 80 55 L 100 35" stroke="var(--accent)" stroke-width="2" fill="none"/>
          <text x="50" y="70" fill="var(--accent)" font-size="9" text-anchor="middle">Composite Shape</text>

          <text x="110" y="38" fill="var(--tx-muted)" font-size="16">➔</text>

          <!-- Distorted -->
          <path d="M 125 35 Q 145 5, 165 45 T 205 25 T 225 35" stroke="var(--warning)" stroke-width="2" fill="none"/>
          <text x="175" y="70" fill="var(--warning)" font-size="9" text-anchor="middle">Distorted / Warped</text>
        </g>

        <text x="25" y="145" fill="var(--tx-primary)" font-size="11" font-weight="700">Physical Cause:</text>
        <text x="25" y="165" fill="var(--tx-secondary)" font-size="10">• Different frequencies propagate</text>
        <text x="25" y="182" fill="var(--tx-secondary)" font-size="10">&nbsp;&nbsp;at different phase velocities</text>
        <text x="25" y="199" fill="var(--tx-secondary)" font-size="10">• Modal dispersion in optical fiber</text>

        <rect x="15" y="215" width="240" height="65" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="235" fill="var(--warning)" font-size="10" font-weight="800">Consequence:</text>
        <text x="25" y="255" fill="var(--tx-primary)" font-size="10">Inter-Symbol Interference (ISI)</text>
        <text x="25" y="270" fill="var(--tx-muted)" font-size="9">Countered by: Equalizers &amp; Dispersion Fibers</text>
      </g>

      <!-- IMPAIRMENT 3: NOISE -->
      <g transform="translate(620, 25)">
        <rect width="270" height="295" rx="10" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.8"/>
        <rect x="15" y="15" width="240" height="28" rx="6" fill="var(--danger-dim)"/>
        <text x="135" y="34" fill="var(--danger)" font-size="12" font-weight="800" text-anchor="middle">3. NOISE (External Contamination)</text>

        <!-- Noise waveform trace -->
        <g transform="translate(20, 60)">
          <!-- Pure Signal + Noise -->
          <path d="M 0 35 Q 25 15, 50 35 T 100 35" stroke="var(--accent)" stroke-width="2" fill="none"/>
          <text x="50" y="70" fill="var(--accent)" font-size="9" text-anchor="middle">Signal s(t)</text>

          <text x="110" y="38" fill="var(--tx-muted)" font-size="16">+</text>

          <!-- Noise Spikes -->
          <path d="M 125 35 L 140 10 L 155 45 L 170 20 L 190 50 L 210 25 L 225 35" stroke="var(--danger)" stroke-width="2" fill="none"/>
          <text x="175" y="70" fill="var(--danger)" font-size="9" text-anchor="middle">Noise Spike n(t)</text>
        </g>

        <text x="25" y="145" fill="var(--tx-primary)" font-size="11" font-weight="700">4 Types of Noise:</text>
        <text x="25" y="165" fill="var(--tx-secondary)" font-size="10">• Thermal (Johnson) Noise: k·T·B</text>
        <text x="25" y="182" fill="var(--tx-secondary)" font-size="10">• Induced Noise: Motors / fluorescent</text>
        <text x="25" y="199" fill="var(--tx-secondary)" font-size="10">• Crosstalk &amp; Impulse Spikes</text>

        <rect x="15" y="215" width="240" height="65" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="235" fill="var(--danger)" font-size="10" font-weight="800">Signal-to-Noise Ratio:</text>
        <text x="25" y="255" fill="var(--tx-primary)" font-family="var(--font-mono)" font-size="11">SNR_dB = 10 · log₁₀(SNR)</text>
        <text x="25" y="270" fill="var(--tx-muted)" font-size="9">Governed by: Shannon Capacity Limit</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University Exam Triad:</strong> <em>Attenuation</em> reduces signal strength (handled by repeaters). <em>Distortion</em> alters signal shape due to differing harmonic velocities (handled by equalizers). <em>Noise</em> adds external unwanted energy onto the channel (limits maximum channel capacity per Shannon).
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Nyquist vs Shannon Engineering Decision Flow
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚖️</span>
      <span class="diagram-title">Figure 5.3: Theoretical Channel Capacity — Nyquist Limit vs. Shannon Capacity Workflow</span>
    </div>
    <span class="diagram-badge">COMMUNICATIONS THEOREM</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-th" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: SHANNON CAPACITY (REALISTIC NOISY CHANNEL) -->
      <g transform="translate(30, 25)">
        <rect width="400" height="295" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <rect x="15" y="15" width="370" height="30" rx="6" fill="var(--warning-dim)"/>
        <text x="200" y="35" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">
          SHANNON'S THEOREM (Noisy Channel Physical Bound)
        </text>

        <rect x="25" y="60" width="350" height="50" rx="8" fill="var(--bg-elevated)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="200" y="90" fill="var(--warning)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">
          C = B · log₂(1 + SNR) &nbsp;(bps)
        </text>

        <text x="25" y="135" fill="var(--tx-primary)" font-size="11" font-weight="700">Key Parameters:</text>
        <text x="25" y="155" fill="var(--tx-secondary)" font-size="10">• $B$ = Analog bandwidth of transmission channel (Hz)</text>
        <text x="25" y="175" fill="var(--tx-secondary)" font-size="10">• $SNR$ = Signal-to-Noise Ratio (Linear power ratio, NOT dB!)</text>
        <text x="25" y="195" fill="var(--tx-secondary)" font-size="10">• $C$ = Absolute physical theoretical ceiling on bit rate</text>

        <line x1="25" y1="215" x2="375" y2="215" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="240" fill="var(--danger)" font-size="11" font-weight="700">CRITICAL PHYSICAL REALITY:</text>
        <text x="25" y="260" fill="var(--tx-muted)" font-size="10">
          No engineering technique, error-correcting code, or signal modulation can ever exceed Shannon's capacity $C$ for a given $B$ and $SNR$.
        </text>
      </g>

      <!-- CENTER BRIDGE ARROW -->
      <path d="M 440 170 L 480 170" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-th)"/>
      <text x="460" y="155" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">EQUATE</text>

      <!-- RIGHT: NYQUIST BIT RATE (MODULATION DESIGN) -->
      <g transform="translate(490, 25)">
        <rect width="400" height="295" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <rect x="15" y="15" width="370" height="30" rx="6" fill="var(--accent-dim)"/>
        <text x="200" y="35" fill="var(--accent-light)" font-size="12" font-weight="800" text-anchor="middle">
          NYQUIST'S THEOREM (Discrete Signal Levels)
        </text>

        <rect x="25" y="60" width="350" height="50" rx="8" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="200" y="90" fill="var(--accent)" font-family="var(--font-mono)" font-size="16" font-weight="900" text-anchor="middle">
          Bit Rate = 2B · log₂(L) &nbsp;(bps)
        </text>

        <text x="25" y="135" fill="var(--tx-primary)" font-size="11" font-weight="700">Key Parameters:</text>
        <text x="25" y="155" fill="var(--tx-secondary)" font-size="10">• $B$ = Channel bandwidth in Hertz (Hz)</text>
        <text x="25" y="175" fill="var(--tx-secondary)" font-size="10">• $L$ = Number of discrete signaling levels or constellation points</text>
        <text x="25" y="195" fill="var(--tx-secondary)" font-size="10">• Each signal element carries $r = \log_2(L)$ bits</text>

        <line x1="25" y1="215" x2="375" y2="215" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="240" fill="var(--success)" font-size="11" font-weight="700">PRACTICAL MODEM DESIGN WORKFLOW:</text>
        <text x="25" y="260" fill="var(--tx-secondary)" font-size="10">
          Equate $2B \cdot \log_2(L) \le C_{\text{Shannon}}$ to find the maximum allowable voltage levels: <strong>L ≤ 2^(C / 2B)</strong>.
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Master Exam Synthesis:</strong> <em>Shannon's theorem</em> tells you the upper capacity limit imposed by channel noise. <em>Nyquist's formula</em> tells you how many discrete signaling levels ($L$) your transmitter DAC/modem must generate to actually achieve that data rate.
  </div>
</div>'''

# ==========================================
# 4. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 5
# ==========================================
ch5_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Transmission Impairments &amp; Channel Capacity Theorems (Nyquist vs. Shannon)</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define and explain the three fundamental causes of transmission impairment in communication media: Attenuation, Distortion, and Noise. Provide the decibel formula for signal attenuation. [4 Marks]<br>
          (b) State Nyquist's theorem for maximum data rate of a noiseless channel and Shannon's theorem for maximum channel capacity of a noisy channel. What is the fundamental difference in the constraints they model? [3 Marks]<br>
          (c) A standard commercial telephone line has an analog voice bandwidth of $B = 3,000\\text{ Hz}$ and a measured signal-to-noise ratio of $\\text{SNR}_{\\text{dB}} = 35\\text{ dB}$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(i) Calculate the linear $\\text{SNR}$ ratio.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(ii) Compute the absolute maximum theoretical channel capacity $C$ using Shannon's theorem.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(iii) If an engineer wishes to achieve a data rate of $24,000\\text{ bps}$ over this channel, calculate the minimum number of discrete signal voltage levels ($L$) required using Nyquist's formula. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: The Three Transmission Impairments</h4>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Attenuation (Energy Loss):</strong> As an electromagnetic or optical signal travels through a medium, its amplitude and power decay due to the internal resistance of conductors or absorption/scattering in optical fibers. Decibel equation: $$\\text{dB} = 10 \\log_{10}\\left(\\frac{P_2}{P_1}\\right)$$ where a negative value indicates attenuation and a positive value indicates amplification. Attenuation is restored via repeaters and amplifiers.</li>
            <li><strong>Distortion (Waveform Alteration):</strong> Composite signals consist of multiple harmonic frequencies. In dispersive media, each harmonic component travels at a different phase velocity ($v_p = \\omega / \\beta$), arriving with varying phase shifts at the receiver. This alters the composite waveform shape, causing Inter-Symbol Interference (ISI). Corrected via equalizers.</li>
            <li><strong>Noise (External Contamination):</strong> Unwanted electrical signals introduced from outside sources:
              <br>• <em>Thermal Noise (Johnson-Nyquist):</em> Random motion of electrons, flat power density: $N = k \\cdot T \\cdot B$.
              <br>• <em>Induced Noise:</em> Electromagnetic radiation from motors, relays, fluorescent ballasts.
              <br>• <em>Crosstalk:</em> Unwanted inductive coupling between adjacent wire pairs.
              <br>• <em>Impulse Noise:</em> High-energy electrical spikes (lightning, power surges); primary cause of burst errors.
            </li>
          </ol>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Nyquist vs. Shannon Capacity Theorems</h4>
          <p><strong>1. Nyquist Bit Rate (Noiseless Channel):</strong></p>
          $$C_{\\text{Nyquist}} = 2B \\log_2(L) \\quad \\text{bps}$$
          <p>Assumes an idealized noiseless channel of bandwidth $B$ (Hz). It establishes that the maximum signaling rate is $2B$ baud (symbols/second), and by encoding $r = \\log_2(L)$ bits per symbol with $L$ discrete signal levels, data rate scales logarithmically with $L$.</p>
          
          <p><strong>2. Shannon Capacity (Noisy Channel):</strong></p>
          $$C_{\\text{Shannon}} = B \\log_2(1 + \\text{SNR}) \\quad \\text{bps}$$
          <p>Models a real-world channel contaminated by additive white Gaussian noise (AWGN). It proves there is an immutable physical ceiling $C$ on the information rate that can be transmitted with an arbitrarily small error probability, regardless of how many signal levels $L$ are used.</p>

          <p><strong>Fundamental Conceptual Difference:</strong> Nyquist models the <em>signaling constraint</em> (how fast symbols can be distinguished without ISI). Shannon models the <em>thermodynamic noise constraint</em> (how noise limits the ability to distinguish between adjacent voltage levels).</p>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Step-by-Step Solved Numerical</h4>
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 8px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Given:</strong> $B = 3,000\\text{ Hz}$, $\\text{SNR}_{\\text{dB}} = 35\\text{ dB}$.<br><br>
              <strong>(i) Calculate Linear SNR:</strong><br>
              $$\\text{SNR}_{\\text{dB}} = 10 \\log_{10}(\\text{SNR}) = 35$$<br>
              $$\\log_{10}(\\text{SNR}) = 3.5 \\implies \\text{SNR} = 10^{3.5} \\approx \\mathbf{3,162.28}$$<br><br>
              <strong>(ii) Calculate Shannon Channel Capacity:</strong><br>
              $$C = B \\log_2(1 + \\text{SNR}) = 3,000 \\times \\log_2(1 + 3,162.28) = 3,000 \\times \\log_2(3,163.28)$$<br>
              Using base-change formula: $\\log_2(3,163.28) = \\frac{\\ln(3,163.28)}{\\ln(2)} = \\frac{8.0594}{0.6931} \\approx 11.627\\text{ bits/Hz}$<br>
              $$C = 3,000 \\times 11.627 = \\mathbf{34,881\\text{ bps}} \\approx \\mathbf{34.88\\text{ kbps}}$$<br>
              <em>(Conclusion: Any requested data rate $\le 34.88\\text{ kbps}$ is theoretically achievable.)</em><br><br>
              <strong>(iii) Calculate Required Discrete Signal Levels ($L$) for 24,000 bps:</strong><br>
              $$\\text{Bit Rate} = 2B \\log_2(L) = 24,000$$<br>
              $$2 \\times 3,000 \\times \\log_2(L) = 24,000$$<br>
              $$6,000 \\times \\log_2(L) = 24,000 \\implies \\log_2(L) = \\frac{24,000}{6,000} = 4$$<br>
              $$L = 2^4 = \\mathbf{16\\text{ discrete signal levels}}$$
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 5
# ==========================================
# Insert Diagram 1 after Section 5.3 (Sine wave)
s3_target = re.search(r'<section id="s-sine-wave"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s3_target:
    content = content[:s3_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s3_target.end():]
    print('Inserted Diagram 1 in Section 5.4')

# Insert Diagram 2 in Section 5.6 (Impairments)
s6_target = re.search(r'<section id="s-attenuation"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s6_target:
    content = content[:s6_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s6_target.end():]
    print('Inserted Diagram 2 in Section 5.6')

# Insert Diagram 3 in Section 5.10 (Nyquist/Shannon)
s10_target = re.search(r'<section id="s-nyquist"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s10_target:
    content = content[:s10_target.end()] + '\n' + svg_diagram_3 + '\n' + content[s10_target.end():]
    print('Inserted Diagram 3 in Section 5.10')

# Insert 10-Mark Blueprint into Chapter 5 before study-resources in s-summary-ch5
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch5_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 5!')

with open(ch5_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 5 upgrade completed!')
