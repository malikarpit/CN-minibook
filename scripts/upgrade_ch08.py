"""
Upgrade Chapter 8 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch8_path = '/Users/arpit/minibook/cn/chapters/ch08-dll-fundamentals.html'
with open(ch8_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Framing Methods (Byte Stuffing vs Bit Stuffing)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🖼️</span>
      <span class="diagram-title">Figure 8.1: Data Link Framing — Character-Oriented Byte Stuffing vs. Bit-Oriented Bit Stuffing</span>
    </div>
    <span class="diagram-badge">FRAMING ALGORITHMS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: BYTE STUFFING (PPP / CHARACTER ORIENTED) -->
      <g transform="translate(30, 25)">
        <rect width="860" height="150" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="20" y="24" fill="var(--info)" font-size="12" font-weight="800">
          A. BYTE STUFFING (Character-Oriented / Point-to-Point Protocol PPP)
        </text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">
          Delimiter: FLAG byte (0x7E) • Escape Byte: ESC (0x7D) • Any FLAG or ESC in data is prefixed with ESC
        </text>

        <!-- Original Data vs Stuffed Data -->
        <g transform="translate(30, 55)">
          <text x="0" y="22" fill="var(--tx-primary)" font-size="10" font-weight="700">Payload Data:</text>
          
          <rect x="120" y="5" width="60" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="150" y="23" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">Data A</text>

          <rect x="190" y="5" width="60" height="28" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="220" y="23" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="middle">FLAG</text>

          <rect x="260" y="5" width="60" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="290" y="23" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">Data B</text>

          <rect x="330" y="5" width="60" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="360" y="23" fill="var(--warning)" font-size="10" font-weight="800" text-anchor="middle">ESC</text>

          <rect x="400" y="5" width="60" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="430" y="23" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">Data C</text>
        </g>

        <!-- Stuffed Frame on Wire -->
        <g transform="translate(30, 100)">
          <text x="0" y="22" fill="var(--success)" font-size="10" font-weight="800">Transmitted Frame:</text>

          <!-- Start Flag -->
          <rect x="120" y="5" width="55" height="28" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="147" y="23" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">FLAG</text>

          <rect x="180" y="5" width="50" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="205" y="23" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">Data A</text>

          <!-- Stuffed ESC before FLAG -->
          <rect x="235" y="5" width="50" height="28" rx="4" fill="var(--warning)" stroke="#fff" stroke-width="1"/>
          <text x="260" y="23" fill="#000" font-size="9" font-weight="900" text-anchor="middle">ESC*</text>

          <rect x="290" y="5" width="50" height="28" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.2"/>
          <text x="315" y="23" fill="var(--danger)" font-size="9" font-weight="800" text-anchor="middle">FLAG</text>

          <rect x="345" y="5" width="50" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="370" y="23" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">Data B</text>

          <!-- Stuffed ESC before ESC -->
          <rect x="400" y="5" width="50" height="28" rx="4" fill="var(--warning)" stroke="#fff" stroke-width="1"/>
          <text x="425" y="23" fill="#000" font-size="9" font-weight="900" text-anchor="middle">ESC*</text>

          <rect x="455" y="5" width="50" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.2"/>
          <text x="480" y="23" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">ESC</text>

          <rect x="510" y="5" width="50" height="28" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="535" y="23" fill="var(--tx-secondary)" font-size="9" text-anchor="middle">Data C</text>

          <!-- End Flag -->
          <rect x="565" y="5" width="55" height="28" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="592" y="23" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">FLAG</text>

          <text x="640" y="23" fill="var(--warning)" font-size="9" font-weight="700">(*ESC bytes stuffed by sender)</text>
        </g>
      </g>

      <!-- SECTION B: BIT STUFFING (HDLC / BIT ORIENTED) -->
      <g transform="translate(30, 190)">
        <rect width="860" height="150" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="20" y="24" fill="var(--accent)" font-size="12" font-weight="800">
          B. BIT STUFFING (Bit-Oriented / High-Level Data Link Control HDLC)
        </text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">
          Delimiter Flag: 01111110 • Transmitter Rule: Insert a '0' bit after ANY sequence of FIVE consecutive '1's!
        </text>

        <!-- Bit Stream Demonstration -->
        <g transform="translate(30, 60)">
          <text x="0" y="20" fill="var(--tx-primary)" font-size="10" font-weight="700">Data Stream:</text>
          <text x="120" y="20" fill="var(--tx-secondary)" font-family="var(--font-mono)" font-size="13">
            0 1 0 <tspan fill="var(--danger)" font-weight="900">1 1 1 1 1</tspan> 1 0 1 1 <tspan fill="var(--danger)" font-weight="900">1 1 1 1 1</tspan> 0 0 1
          </text>
        </g>

        <g transform="translate(30, 105)">
          <text x="0" y="20" fill="var(--success)" font-size="10" font-weight="800">Stuffed on Wire:</text>
          <text x="120" y="20" fill="var(--tx-secondary)" font-family="var(--font-mono)" font-size="13">
            <tspan fill="var(--info)" font-weight="800">[01111110]</tspan> 0 1 0 <tspan fill="var(--danger)" font-weight="900">1 1 1 1 1</tspan><tspan fill="var(--warning)" font-weight="900">[0]*</tspan> 1 0 1 1 <tspan fill="var(--danger)" font-weight="900">1 1 1 1 1</tspan><tspan fill="var(--warning)" font-weight="900">[0]*</tspan> 0 0 1 <tspan fill="var(--info)" font-weight="800">[01111110]</tspan>
          </text>
        </g>

        <!-- Receiver action note -->
        <text x="450" y="136" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">
          ✓ Receiver Rule: Whenever it sees five consecutive 1s followed by a 0, it automatically STRIPS the 0!
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Transparency Guarantee:</strong> Without stuffing, if the user payload coincidentally contains the flag pattern (<code>01111110</code> or <code>0x7E</code>), the receiver's hardware would prematurely assume the frame has ended, corrupting all subsequent data. Stuffing guarantees absolute transparency across all data types.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: CRC Modulo-2 Division Architecture & Hardware Shift Register
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔢</span>
      <span class="diagram-title">Figure 8.2: Cyclic Redundancy Check (CRC) — Modulo-2 Division &amp; Hardware LFSR</span>
    </div>
    <span class="diagram-badge">ERROR DETECTION MATH</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: MODULO-2 DIVISION MATHEMATICS -->
      <g transform="translate(30, 25)">
        <rect width="420" height="315" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="210" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          A. MODULO-2 LONG DIVISION ENGINE (XOR)
        </text>

        <rect x="20" y="38" width="380" height="48" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="30" y="56" fill="var(--tx-primary)" font-size="10" font-weight="700">Data Word D:</text>
        <text x="115" y="56" fill="var(--accent)" font-family="var(--font-mono)" font-size="11" font-weight="800">1 0 0 1 0 0</text>
        <text x="30" y="74" fill="var(--tx-primary)" font-size="10" font-weight="700">Divisor G(x):</text>
        <text x="115" y="74" fill="var(--warning)" font-family="var(--font-mono)" font-size="11" font-weight="800">1 1 0 1 &nbsp;(Degree k = 3)</text>

        <!-- Division Block Trace -->
        <g transform="translate(30, 95)" font-family="var(--font-mono)" font-size="11" line-height="1.4">
          <text x="0" y="20" fill="var(--warning)" font-weight="800">1 1 0 1</text>
          <text x="55" y="20" fill="var(--tx-muted)">)</text>
          <text x="70" y="20" fill="var(--accent)" font-weight="800">1 0 0 1 0 0</text>
          <text x="155" y="20" fill="var(--info)" font-weight="800">0 0 0</text>
          <text x="205" y="20" fill="var(--tx-muted)">(Augmented with k=3 zeros)</text>

          <line x1="70" y1="26" x2="190" y2="26" stroke="var(--border)" stroke-width="1"/>
          
          <text x="70" y="42" fill="var(--warning)">1 1 0 1</text>
          <line x1="70" y1="48" x2="190" y2="48" stroke="var(--border)" stroke-width="1"/>
          
          <text x="80" y="64" fill="var(--tx-secondary)">0 1 0 0 0</text>
          <text x="88" y="80" fill="var(--warning)">1 1 0 1</text>
          <line x1="88" y1="86" x2="190" y2="86" stroke="var(--border)" stroke-width="1"/>

          <text x="106" y="102" fill="var(--tx-secondary)">0 1 0 1 0</text>
          <text x="114" y="118" fill="var(--warning)">1 1 0 1</text>
          <line x1="114" y1="124" x2="190" y2="124" stroke="var(--border)" stroke-width="1"/>

          <text x="132" y="140" fill="var(--tx-secondary)">0 1 1 1 0</text>
          <text x="140" y="156" fill="var(--warning)">1 1 0 1</text>
          <line x1="140" y1="162" x2="190" y2="162" stroke="var(--border)" stroke-width="1"/>

          <text x="165" y="178" fill="var(--success)" font-size="13" font-weight="900">0 0 1</text>
          <text x="205" y="178" fill="var(--success)" font-weight="800">➔ Remainder R = 001</text>
        </g>

        <rect x="20" y="280" width="380" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="210" y="297" fill="var(--success)" font-size="10" font-weight="800" text-anchor="middle">
          Codeword T = [Data] + [R] = 1 0 0 1 0 0 0 0 1
        </text>
      </g>

      <!-- RIGHT: HARDWARE LFSR ARCHITECTURE -->
      <g transform="translate(480, 25)">
        <rect width="410" height="315" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="205" y="24" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">
          B. LINEAR FEEDBACK SHIFT REGISTER (LFSR)
        </text>
        <text x="205" y="40" fill="var(--tx-muted)" font-size="9" text-anchor="middle">
          Standard Ethernet Hardware CRC-32 Circuit (Zero CPU Overhead)
        </text>

        <!-- 3 Flip-Flops (D-FF) -->
        <g transform="translate(40, 70)">
          <!-- FF 0 -->
          <rect x="0" y="0" width="60" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="30" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">FF 0</text>
          <text x="30" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Bit 0</text>

          <line x1="60" y1="25" x2="100" y2="25" stroke="var(--accent)" stroke-width="2"/>

          <!-- XOR Gate 1 -->
          <circle cx="115" cy="25" r="14" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="115" y="29" fill="var(--warning)" font-size="14" font-weight="900" text-anchor="middle">⊕</text>

          <line x1="130" y1="25" x2="160" y2="25" stroke="var(--accent)" stroke-width="2"/>

          <!-- FF 1 -->
          <rect x="160" y="0" width="60" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="190" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">FF 1</text>
          <text x="190" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Bit 1</text>

          <line x1="220" y1="25" x2="270" y2="25" stroke="var(--accent)" stroke-width="2"/>

          <!-- FF 2 -->
          <rect x="270" y="0" width="60" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="300" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">FF 2</text>
          <text x="300" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Bit 2</text>
        </g>

        <!-- Feedback Loop line -->
        <path d="M 370 95 L 390 95 L 390 160 L 155 160 L 155 109" stroke="var(--accent)" stroke-width="2" fill="none"/>
        <text x="270" y="152" fill="var(--accent)" font-size="9" font-weight="700">Feedback Tap (G(x) Coefficients)</text>

        <rect x="20" y="190" width="370" height="110" rx="8" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="30" y="210" fill="var(--tx-primary)" font-size="10" font-weight="700">Standard Generator Polynomials:</text>
        <text x="30" y="230" fill="var(--tx-secondary)" font-size="9">• <strong>CRC-8 (ATM):</strong> x⁸ + x² + x + 1</text>
        <text x="30" y="248" fill="var(--tx-secondary)" font-size="9">• <strong>CRC-16 (USB):</strong> x¹⁶ + x¹⁵ + x² + 1</text>
        <text x="30" y="266" fill="var(--tx-secondary)" font-size="9">• <strong>CRC-32 (IEEE 802.3 Ethernet):</strong> x³² + x²⁶ + ... + 1</text>
        <text x="30" y="286" fill="var(--success)" font-size="9" font-weight="700">★ Detects 100% of all single &amp; double bit errors, odd errors, and bursts &lt; 32 bits!</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Modulo-2 Arithmetic Axiom:</strong> In CRC modulo-2 arithmetic, addition and subtraction are identical and equivalent to the bitwise <strong>XOR</strong> operation ($0 \oplus 0 = 0$, $0 \oplus 1 = 1$, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$). There are NO carries or borrows!
  </div>
</div>'''

# ==========================================
# 3. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 8
# ==========================================
ch8_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Framing Techniques &amp; Cyclic Redundancy Check (CRC) Solved Derivation</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define Framing at the Data Link Layer. Explain Byte Stuffing and Bit Stuffing with illustrative examples. For the bit payload <code>011111101111110011111110</code>, show the bit-stuffed output. [3 Marks]<br>
          (b) State the error-detection capabilities of a Cyclic Redundancy Check (CRC) polynomial of degree $k$. What mathematical conditions must the generator polynomial $G(x)$ satisfy to detect all odd-numbered bit errors? [3 Marks]<br>
          (c) A sender wants to transmit a 7-bit message <code>1 0 0 1 1 0 1</code> using CRC with generator polynomial $G(x) = x^3 + x^2 + 1$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(i) Find the binary bit string representing $G(x)$ and determine degree $k$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(ii) Perform Modulo-2 long division to compute the CRC remainder (FCS) and state the final transmitted codeword $T$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(iii) Show receiver verification if the 4th bit from the left is inverted during transmission. [4 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Framing &amp; Bit Stuffing Walkthrough</h4>
          <p><strong>Framing:</strong> The process of dividing the continuous stream of bits delivered by the physical layer into discrete, manageable data units called <em>Frames</em>, delimited by recognizable boundary patterns.</p>
          <p><strong>Bit Stuffing Rule:</strong> Whenever the transmitter detects five consecutive <code>1</code>s in the payload, it unconditionally injects a stuffed <code>0</code> bit immediately after them.</p>
          
          <div style="background: var(--bg-elevated); padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border); margin: 6px 0;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              Original Bit Stream: <code>0 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 0</code><br>
              • Group 1: <code>0 [1 1 1 1 1] ➔ insert 0 ➔ 0 1 1 1 1 1 <strong>0</strong> 1 0 ...</code><br>
              • Group 2: <code>... 1 [1 1 1 1 1] ➔ insert 0 ➔ ... 1 1 1 1 1 <strong>0</strong> 1 0 0 ...</code><br>
              • Group 3: <code>... 1 [1 1 1 1 1] ➔ insert 0 ➔ ... 1 1 1 1 1 <strong>0</strong> 1 1 0</code><br><br>
              <strong>Stuffed Output:</strong> <code>011111<strong>0</strong>1011111<strong>0</strong>10011111<strong>0</strong>110</code>
            </p>
          </div>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: CRC Error Detection Properties</h4>
          <p>For a generator polynomial $G(x)$ of degree $k$:</p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li>Detects <strong>100% of all single-bit errors</strong>, provided $G(x)$ has at least two terms (i.e., $x^k$ and $x^0$).</li>
            <li>Detects <strong>all double-bit errors</strong>, provided $G(x)$ does not divide $x^t + 1$ for any $t \le$ frame length.</li>
            <li>Detects <strong>all odd-numbered bit errors</strong>, provided $G(x)$ contains $(x + 1)$ as a factor.</li>
            <li>Detects <strong>all burst errors of length $\le k$ bits</strong> with 100% certainty.</li>
            <li>Detects burst errors of length $k + 1$ with probability $1 - (1/2)^{k-1}$, and bursts $> k + 1$ with probability $1 - (1/2)^k$ ($99.99999997\%$ for CRC-32).</li>
          </ol>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Step-by-Step CRC Solved Numerical</h4>
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 8px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>(i) Binary Divisor &amp; Degree:</strong><br>
              $$G(x) = 1 \\cdot x^3 + 1 \\cdot x^2 + 0 \\cdot x^1 + 1 \\cdot x^0 \\implies \\mathbf{G = 1 1 0 1}$$<br>
              Degree of polynomial: $k = 3$. Hence, append $k = 3$ zeros to data $D = 1001101$.<br>
              Augmented data: <code>1 0 0 1 1 0 1 0 0 0</code><br><br>

              <strong>(ii) Sender Modulo-2 Division:</strong><br>
              <code>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 1 0 1 1 0 &nbsp;&nbsp;(Quotient)<br>
              1 1 0 1 ) 1 0 0 1 1 0 1 0 0 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 0 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 0 0 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 0 1 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 0 1 1 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 1 0 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 0 1<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 1 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 0<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>0 1 0</strong> &nbsp;➔ <strong>Remainder FCS R = 0 1 0</strong>
              </code><br><br>
              <strong>Transmitted Codeword:</strong> $$T = D + R = \\mathbf{1 0 0 1 1 0 1 0 1 0}$$<br><br>

              <strong>(iii) Receiver Verification with Bit Error:</strong><br>
              4th bit inverted (from <code>1</code> to <code>0</code>): Received frame = <code>1 0 0 <strong>0</strong> 1 0 1 0 1 0</code>.<br>
              Dividing received frame by $G = 1101$ yields a <strong>Non-Zero Remainder (Syndrome $\ne 0$)</strong>.<br>
              The receiver immediately detects the corruption and drops the frame, triggering an ARQ retransmission!
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 8
# ==========================================
# Insert Diagram 1 into Section 8.8 (Framing compare)
s8_target = re.search(r'<section id="s-framing-compare"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s8_target:
    content = content[:s8_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s8_target.end():]
    print('Inserted Diagram 1 in Section 8.8')

# Insert Diagram 2 into Section 8.14 (CRC theory)
s14_target = re.search(r'<section id="s-crc-theory"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s14_target:
    content = content[:s14_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s14_target.end():]
    print('Inserted Diagram 2 in Section 8.14')

# Insert 10-Mark Blueprint into Chapter 8 before study-resources in s-summary-ch8
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch8_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 8!')

with open(ch8_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 8 upgrade completed!')
