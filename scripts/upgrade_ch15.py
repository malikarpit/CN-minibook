"""
Upgrade Chapter 15 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch15_path = '/Users/arpit/minibook/cn/chapters/ch15-ipv4-internals.html'
with open(ch15_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Master 20-Byte IPv4 Header Grid
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📋</span>
      <span class="diagram-title">Figure 15.1: Master 20-Byte IPv4 Datagram Header Architecture (32-Bit Word Alignment)</span>
    </div>
    <span class="diagram-badge">HEADER BITFIELD</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- BIT SCALE HEADER -->
      <g transform="translate(30, 25)">
        <rect width="880" height="24" rx="4" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="5" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">Bit: 0</text>
        <text x="110" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">4</text>
        <text x="220" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">8</text>
        <text x="440" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">16</text>
        <text x="522" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">19</text>
        <text x="860" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">31</text>
      </g>

      <!-- ROW 1 (BYTES 0-3) -->
      <g transform="translate(30, 55)">
        <!-- VER (4 bits) -->
        <rect x="0" y="0" width="110" height="50" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="55" y="22" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">VER (4b)</text>
        <text x="55" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">IPv4 = 0100₂</text>

        <!-- IHL (4 bits) -->
        <rect x="115" y="0" width="105" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="167" y="22" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">IHL (4b)</text>
        <text x="167" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">5 × 4 = 20B min</text>

        <!-- DSCP / ECN (8 bits) -->
        <rect x="225" y="0" width="215" height="50" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="332" y="22" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">Type of Service / DSCP (6b) + ECN (2b)</text>
        <text x="332" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">QoS Priority &amp; Congestion Notification</text>

        <!-- Total Length (16 bits) -->
        <rect x="445" y="0" width="435" height="50" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="662" y="22" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">Total Length (16 bits)</text>
        <text x="662" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Header + Payload: 20 to 65,535 Bytes</text>
      </g>

      <!-- ROW 2 (BYTES 4-7: FRAGMENTATION) -->
      <g transform="translate(30, 112)">
        <!-- Identification (16 bits) -->
        <rect x="0" y="0" width="440" height="50" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="220" y="22" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Identification (16 bits)</text>
        <text x="220" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Unique flow ID shared by all fragments of original datagram</text>

        <!-- Flags (3 bits: R, DF, MF) -->
        <rect x="445" y="0" width="105" height="50" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="497" y="22" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">Flags (3b)</text>
        <text x="497" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">0 | DF | MF</text>

        <!-- Fragment Offset (13 bits) -->
        <rect x="555" y="0" width="325" height="50" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="717" y="22" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">Fragment Offset (13 bits)</text>
        <text x="717" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Data offset in 8-byte units (Offset × 8 = Byte Position)</text>
      </g>

      <!-- ROW 3 (BYTES 8-11: CONTROL) -->
      <g transform="translate(30, 169)">
        <!-- TTL (8 bits) -->
        <rect x="0" y="0" width="220" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="110" y="22" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">Time to Live (TTL) (8 bits)</text>
        <text x="110" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Hop limit decremented by 1 at each router</text>

        <!-- Protocol (8 bits) -->
        <rect x="225" y="0" width="215" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="332" y="22" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">Protocol (8 bits)</text>
        <text x="332" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">6 = TCP, 17 = UDP, 1 = ICMP, 89 = OSPF</text>

        <!-- Header Checksum (16 bits) -->
        <rect x="445" y="0" width="435" height="50" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="662" y="22" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">Header Checksum (16 bits)</text>
        <text x="662" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">16-bit 1's complement sum (recomputed at every hop)</text>
      </g>

      <!-- ROW 4 (BYTES 12-15: SOURCE IP) -->
      <g transform="translate(30, 226)">
        <rect x="0" y="0" width="880" height="42" rx="4" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="440" y="22" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Source IP Address (32 bits / 4 Bytes)</text>
        <text x="440" y="36" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Original sender node Layer-3 logical identifier</text>
      </g>

      <!-- ROW 5 (BYTES 16-19: DESTINATION IP) -->
      <g transform="translate(30, 275)">
        <rect x="0" y="0" width="880" height="42" rx="4" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="440" y="22" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Destination IP Address (32 bits / 4 Bytes)</text>
        <text x="440" y="36" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Target terminal node Layer-3 logical identifier</text>
      </g>

      <!-- ROW 6 (OPTIONAL: OPTIONS & PADDING) -->
      <g transform="translate(30, 324)">
        <rect x="0" y="0" width="880" height="34" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 3"/>
        <text x="440" y="22" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">
          Options &amp; Padding (Optional: 0 to 40 Bytes; padded to 32-bit multiple)
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: IPv4 Fragmentation & Reassembly
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">✂️</span>
      <span class="diagram-title">Figure 15.2: IPv4 Packet Fragmentation &amp; Reassembly Across Link MTU Bottlenecks</span>
    </div>
    <span class="diagram-badge">FRAGMENTATION PIPELINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-frag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- ORIGINAL DATAGRAM (4000 BYTES) -->
      <g transform="translate(30, 25)">
        <rect width="880" height="65" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="25" y="22" fill="var(--accent)" font-size="11" font-weight="900">ORIGINAL IP DATAGRAM (Length = 4,000 Bytes, MTU = 4500 Link)</text>

        <!-- Header block -->
        <rect x="25" y="32" width="120" height="25" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <text x="85" y="48" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">IP Header (20B)</text>

        <!-- Payload block -->
        <rect x="150" y="32" width="705" height="25" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="502" y="48" fill="var(--info)" font-size="9.5" font-weight="800" text-anchor="middle">
          Data Payload (3,980 Bytes) &nbsp;•&nbsp; Identification = 0x4A21 &nbsp;•&nbsp; DF = 0, MF = 0, Offset = 0
        </text>
      </g>

      <!-- INTERMEDIATE ROUTER BOTTLENECK -->
      <g transform="translate(470, 95)">
        <text x="0" y="15" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">
          ⬇ INTERMEDIATE ROUTER ENCOUNTERS EGRESS MTU = 1,500 BYTES ⬇
        </text>
        <text x="0" y="30" fill="var(--tx-muted)" font-size="9" text-anchor="middle">
          Max Data Slice = ⌊(1500 - 20) / 8⌋ × 8 = 1,480 Bytes per fragment
        </text>
      </g>

      <!-- THREE FRAGMENT SLICES -->
      <g transform="translate(30, 135)">
        <rect width="880" height="200" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>

        <!-- Fragment 1 -->
        <g transform="translate(20, 15)">
          <rect width="840" height="48" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <rect x="10" y="10" width="95" height="28" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="57" y="27" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">Header (20B)</text>

          <rect x="110" y="10" width="300" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="260" y="27" fill="var(--success)" font-size="9.5" font-weight="800" text-anchor="middle">Data Slice 1 (Bytes 0 – 1479 = 1,480B)</text>

          <text x="430" y="22" fill="var(--tx-primary)" font-size="9.5" font-weight="800">Total Len: 1500</text>
          <text x="430" y="35" fill="var(--tx-muted)" font-size="9">ID: 0x4A21</text>

          <rect x="540" y="10" width="65" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
          <text x="572" y="27" fill="var(--danger)" font-size="10" font-weight="900" text-anchor="middle">MF = 1</text>

          <rect x="615" y="10" width="215" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="722" y="27" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">Offset = 0 / 8 = 0</text>
        </g>

        <!-- Fragment 2 -->
        <g transform="translate(20, 72)">
          <rect width="840" height="48" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <rect x="10" y="10" width="95" height="28" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="57" y="27" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">Header (20B)</text>

          <rect x="110" y="10" width="300" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="260" y="27" fill="var(--success)" font-size="9.5" font-weight="800" text-anchor="middle">Data Slice 2 (Bytes 1480 – 2959 = 1,480B)</text>

          <text x="430" y="22" fill="var(--tx-primary)" font-size="9.5" font-weight="800">Total Len: 1500</text>
          <text x="430" y="35" fill="var(--tx-muted)" font-size="9">ID: 0x4A21</text>

          <rect x="540" y="10" width="65" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
          <text x="572" y="27" fill="var(--danger)" font-size="10" font-weight="900" text-anchor="middle">MF = 1</text>

          <rect x="615" y="10" width="215" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="722" y="27" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">Offset = 1480 / 8 = 185</text>
        </g>

        <!-- Fragment 3 -->
        <g transform="translate(20, 129)">
          <rect width="840" height="48" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <rect x="10" y="10" width="95" height="28" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="57" y="27" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">Header (20B)</text>

          <rect x="110" y="10" width="300" height="28" rx="3" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
          <text x="260" y="27" fill="var(--warning)" font-size="9.5" font-weight="800" text-anchor="middle">Data Slice 3 (Bytes 2960 – 3979 = 1,020B)</text>

          <text x="430" y="22" fill="var(--tx-primary)" font-size="9.5" font-weight="800">Total Len: 1040</text>
          <text x="430" y="35" fill="var(--tx-muted)" font-size="9">ID: 0x4A21</text>

          <rect x="540" y="10" width="65" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="572" y="27" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">MF = 0</text>

          <rect x="615" y="10" width="215" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="722" y="27" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">Offset = 2960 / 8 = 370</text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch15_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch15">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">IPv4 Header Structure &amp; Multi-Hop Fragmentation</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Header Field Functions &amp; Multi-Stage MTU Fragmentation Numerical</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Explain the functions of all major fields in the 20-byte IPv4 header. An IPv4 datagram of total length 4,000 bytes (including a 20-byte header) arrives at a router that must forward it across an MTU = 1,500 link, followed by an MTU = 600 link. Tabulate all generated fragments, specifying: Fragment ID, Total Length, Data Length, DF, MF, and Fragment Offset."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: CORE HEADER FIELDS -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Essential IPv4 Header Fields &amp; Functional Purpose (3 Marks)</h4>
          <ul class="blueprint-list">
            <li><strong>VER (4 bits):</strong> Identifies IP version ($0100_2 = 4$). Discarded if $\ne 4$.</li>
            <li><strong>IHL (Internet Header Length: 4 bits):</strong> Header length expressed in 32-bit (4-byte) words. Minimum value is $5$ ($5 \times 4 = 20$ bytes). Maximum is $15$ ($15 \times 4 = 60$ bytes with options).</li>
            <li><strong>Total Length (16 bits):</strong> Overall size of datagram (Header + Payload) in bytes. Maximum theoretical limit: $2^{16}-1 = 65,535$ bytes.</li>
            <li><strong>Identification (16 bits):</strong> Unique counter assigned by source host to identify all fragments belonging to the same original datagram.</li>
            <li><strong>Flags (3 bits):</strong> Bit 0 is reserved ($0$). Bit 1 is <strong>DF (Don't Fragment)</strong>: if $1$, router must drop packet and send ICMP Type 3 Code 4 error if size $>$ MTU. Bit 2 is <strong>MF (More Fragments)</strong>: $1$ if more fragments follow; $0$ for final fragment.</li>
            <li><strong>Fragment Offset (13 bits):</strong> Position of fragment data relative to beginning of original datagram payload, measured strictly in <strong>8-byte (64-bit) units</strong>:
              $$\text{Fragment Offset} = \frac{\text{Byte Position}}{8}$$
            </li>
            <li><strong>Time to Live (TTL: 8 bits):</strong> Decremented by 1 at every router hop. Prevents persistent loops. Discarded with ICMP Type 11 (Time Exceeded) when TTL $= 0$.</li>
            <li><strong>Protocol (8 bits):</strong> Demultiplexes payload to Layer 4 transport protocol ($6 = \text{TCP}, 17 = \text{UDP}, 1 = \text{ICMP}$).</li>
            <li><strong>Header Checksum (16 bits):</strong> Error-detection covering IP header only. Must be recomputed at every router hop because TTL decrements!</li>
          </ul>
        </div>

        <!-- SECTION 2: STAGE 1 FRAGMENTATION (MTU = 1500) -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Stage 1 Fragmentation: MTU = 1,500 Bytes (4 Marks)</h4>
          <p>
            Original Packet: Total Length $= 4,000$ B $\implies$ Payload $= 4,000 - 20 = \mathbf{3,980}$ Bytes. $\text{ID} = x, \text{DF} = 0, \text{MF} = 0, \text{Offset} = 0$.<br/>
            Maximum Payload per Fragment on MTU 1,500 link:
            $$\text{Max Payload} = \left\lfloor \frac{1500 - 20}{8} \right\rfloor \times 8 = \left\lfloor \frac{1480}{8} \right\rfloor \times 8 = \mathbf{1,480} \text{ Bytes}$$
          </p>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Fragment</th>
                  <th>Data Slice (Bytes)</th>
                  <th>Data Length</th>
                  <th>Total Length</th>
                  <th>ID</th>
                  <th>DF</th>
                  <th>MF</th>
                  <th>Offset</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Frag 1</strong></td>
                  <td>$0$ to $1479$</td>
                  <td>$1,480$ B</td>
                  <td><strong>$1,500$ B</strong></td>
                  <td>$x$</td>
                  <td>$0$</td>
                  <td><strong>$1$</strong></td>
                  <td>$0 / 8 =$ <strong>$0$</strong></td>
                </tr>
                <tr>
                  <td><strong>Frag 2</strong></td>
                  <td>$1480$ to $2959$</td>
                  <td>$1,480$ B</td>
                  <td><strong>$1,500$ B</strong></td>
                  <td>$x$</td>
                  <td>$0$</td>
                  <td><strong>$1$</strong></td>
                  <td>$1480 / 8 =$ <strong>$185$</strong></td>
                </tr>
                <tr>
                  <td><strong>Frag 3</strong></td>
                  <td>$2960$ to $3979$</td>
                  <td>$1,020$ B</td>
                  <td><strong>$1,040$ B</strong></td>
                  <td>$x$</td>
                  <td>$0$</td>
                  <td><strong>$0$</strong></td>
                  <td>$2960 / 8 =$ <strong>$370$</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 3: STAGE 2 FRAGMENTATION (MTU = 600) -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Stage 2 Fragmentation: Further Splitting over MTU = 600 Link (3 Marks)</h4>
          <p>
            When Frag 1 ($1500$ B) hits MTU $= 600$:
            $$\text{Max Payload} = \left\lfloor \frac{600 - 20}{8} \right\rfloor \times 8 = \left\lfloor 72.5 \right\rfloor \times 8 = 72 \times 8 = \mathbf{576} \text{ Bytes}$$
            Frag 1 ($1,480$ B payload) is partitioned into three sub-fragments:
          </p>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Sub-Fragment</th>
                  <th>Payload Data</th>
                  <th>Total Length</th>
                  <th>ID</th>
                  <th>MF</th>
                  <th>Fragment Offset</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Frag 1a</strong></td>
                  <td>$576$ B ($0$ to $575$)</td>
                  <td>$596$ B</td>
                  <td>$x$</td>
                  <td><strong>$1$</strong></td>
                  <td>$0 / 8 =$ <strong>$0$</strong></td>
                </tr>
                <tr>
                  <td><strong>Frag 1b</strong></td>
                  <td>$576$ B ($576$ to $1151$)</td>
                  <td>$596$ B</td>
                  <td>$x$</td>
                  <td><strong>$1$</strong></td>
                  <td>$576 / 8 =$ <strong>$72$</strong></td>
                </tr>
                <tr>
                  <td><strong>Frag 1c</strong></td>
                  <td>$328$ B ($1152$ to $1479$)</td>
                  <td>$348$ B</td>
                  <td>$x$</td>
                  <td><strong>$1$</strong> (since Frag 1 had MF=1)</td>
                  <td>$1152 / 8 =$ <strong>$144$</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- EXAM PITFALL WARNING -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap:</strong>
            1. Never calculate Fragment Offset based on Total Length! Offset counts <strong>strictly payload data bytes</strong>.<br/>
            2. Never forget that payload size per fragment must be an <strong>exact multiple of 8</strong> (except for the very last fragment of the entire datagram where MF = 0).
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 15
# ==========================================

# 1. Replace Box #3 in s15-header with Figure 15.1
match_s15_h = re.search(r'(<section id="s15-header"[^>]*>.*?)(<div class="ascii-box">.*?</div>)', content, flags=re.DOTALL)
if match_s15_h:
    content = content[:match_s15_h.start(2)] + svg_diagram_1 + content[match_s15_h.end(2):]
    print('Replaced ASCII box in s15-header with Figure 15.1')
else:
    print('Warning: could not find ASCII box in s15-header')

# 2. Replace Box in s15-frag-process with Figure 15.2
match_s15_fp = re.search(r'(<section id="s15-frag-process"[^>]*>.*?)(<div class="ascii-box">.*?</div>)', content, flags=re.DOTALL)
if match_s15_fp:
    content = content[:match_s15_fp.start(2)] + svg_diagram_2 + content[match_s15_fp.end(2):]
    print('Replaced ASCII box in s15-frag-process with Figure 15.2')
else:
    print('Warning: could not find ASCII box in s15-frag-process')

# 3. Insert DU 10-Mark Blueprint before study-resources in Chapter 15
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch15_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 15!')
else:
    # If no study-resources, insert before </main> or in s15-traps
    trap_target = re.search(r'</section>\s*</main>', content)
    if trap_target:
        content = content[:trap_target.start()] + '</section>\n\n' + ch15_uni_blueprint + '\n</main>' + content[trap_target.end():]
        print('Inserted 10-Mark University Blueprint before </main> in Chapter 15!')
    else:
        print('Warning: could not find insertion point for blueprint in Chapter 15')

with open(ch15_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 15 upgrade completed!')
