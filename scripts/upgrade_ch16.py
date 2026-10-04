"""
Upgrade Chapter 16 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch16_path = '/Users/arpit/minibook/cn/chapters/ch16-ipv6.html'
with open(ch16_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Master 40-Byte Fixed IPv6 Base Header
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📋</span>
      <span class="diagram-title">Figure 16.1: Master 40-Byte Fixed IPv6 Base Header Architecture (32-Bit Grid)</span>
    </div>
    <span class="diagram-badge">IPv6 BASE HEADER</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- BIT SCALE HEADER -->
      <g transform="translate(30, 25)">
        <rect width="880" height="24" rx="4" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="5" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">Bit: 0</text>
        <text x="110" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">4</text>
        <text x="330" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">12</text>
        <text x="860" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">31</text>
      </g>

      <!-- ROW 1 (BYTES 0-3: 32 BITS) -->
      <g transform="translate(30, 55)">
        <!-- Version (4 bits) -->
        <rect x="0" y="0" width="110" height="50" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="55" y="22" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Version (4b)</text>
        <text x="55" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">0110₂ (IPv6)</text>

        <!-- Traffic Class (8 bits) -->
        <rect x="115" y="0" width="220" height="50" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="225" y="22" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">Traffic Class (8 bits)</text>
        <text x="225" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">DSCP (6b) + ECN (2b) QoS Marking</text>

        <!-- Flow Label (20 bits) -->
        <rect x="340" y="0" width="540" height="50" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="610" y="22" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">Flow Label (20 bits)</text>
        <text x="610" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Identifies non-default quality QoS flows; line-rate ECMP hash key</text>
      </g>

      <!-- ROW 2 (BYTES 4-7: 32 BITS) -->
      <g transform="translate(30, 112)">
        <!-- Payload Length (16 bits) -->
        <rect x="0" y="0" width="440" height="50" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="220" y="22" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">Payload Length (16 bits)</text>
        <text x="220" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Length of payload + extension headers (excludes 40B base)</text>

        <!-- Next Header (8 bits) -->
        <rect x="445" y="0" width="215" height="50" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="552" y="22" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Next Header (8 bits)</text>
        <text x="552" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Points to Extension Header or L4 (TCP=6)</text>

        <!-- Hop Limit (8 bits) -->
        <rect x="665" y="0" width="215" height="50" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="772" y="22" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">Hop Limit (8 bits)</text>
        <text x="772" y="38" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Equivalent to IPv4 TTL; decremented by 1</text>
      </g>

      <!-- ROWS 3-6 (BYTES 8-23: SOURCE IP ADDRESS = 128 BITS) -->
      <g transform="translate(30, 169)">
        <rect x="0" y="0" width="880" height="75" rx="6" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="440" y="32" fill="var(--accent)" font-size="13" font-weight="900" text-anchor="middle">
          Source IPv6 Address (128 bits / 16 Bytes / 4 Words)
        </text>
        <text x="440" y="52" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">
          Originating Host / Subnet Identifier (e.g. 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        </text>
      </g>

      <!-- ROWS 7-10 (BYTES 24-39: DESTINATION IP ADDRESS = 128 BITS) -->
      <g transform="translate(30, 252)">
        <rect x="0" y="0" width="880" height="75" rx="6" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="440" y="32" fill="var(--accent)" font-size="13" font-weight="900" text-anchor="middle">
          Destination IPv6 Address (128 bits / 16 Bytes / 4 Words)
        </text>
        <text x="440" y="52" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">
          Target Unicast Host, Anycast Node, or Multicast Group (e.g. ff02::1)
        </text>
      </g>

      <!-- BOTTOM BANNER: FIXED 40-BYTE CONSTANT -->
      <g transform="translate(30, 335)">
        <text x="440" y="16" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">
          ⚡ CONSTANT 40-BYTE FOOTPRINT: No IHL Field • No Checksum • Fixed 64-Bit Boundaries Accelerate Hardware ASICs
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Extension Header Daisy Chain
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔗</span>
      <span class="diagram-title">Figure 16.2: IPv6 Extension Header Linked-List Daisy Chain Architecture</span>
    </div>
    <span class="diagram-badge">DAISY CHAIN</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-chain" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="290" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- NODE 1: BASE IPv6 HEADER -->
      <g transform="translate(30, 50)">
        <rect width="180" height="150" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <rect x="10" y="12" width="160" height="30" rx="4" fill="var(--accent-dim)" stroke="none"/>
        <text x="90" y="32" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">IPv6 Base Header</text>
        <text x="90" y="65" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Fixed: 40 Bytes</text>
        <text x="90" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Src &amp; Dst IP (32B)</text>

        <!-- Next Header Box -->
        <rect x="15" y="105" width="150" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
        <text x="90" y="125" fill="var(--accent)" font-size="9.5" font-weight="900" text-anchor="middle">Next Header = 0</text>
      </g>

      <!-- LINK ARROW 1 -->
      <path d="M 210 125 L 255 125" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr-chain)"/>

      <!-- NODE 2: HOP-BY-HOP OPTIONS (EXT 0) -->
      <g transform="translate(260, 50)">
        <rect width="180" height="150" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="10" y="12" width="160" height="30" rx="4" fill="var(--info-dim)" stroke="none"/>
        <text x="90" y="32" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">Hop-by-Hop Options</text>
        <text x="90" y="65" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Ext Type: 0</text>
        <text x="90" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Jumbograms / Router Alert</text>

        <!-- Next Header Box -->
        <rect x="15" y="105" width="150" height="32" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
        <text x="90" y="125" fill="var(--info)" font-size="9.5" font-weight="900" text-anchor="middle">Next Header = 43</text>
      </g>

      <!-- LINK ARROW 2 -->
      <path d="M 440 125 L 485 125" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr-chain)"/>

      <!-- NODE 3: ROUTING HEADER (EXT 43) -->
      <g transform="translate(490, 50)">
        <rect width="180" height="150" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="10" y="12" width="160" height="30" rx="4" fill="var(--warning-dim)" stroke="none"/>
        <text x="90" y="32" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">Routing Header</text>
        <text x="90" y="65" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Ext Type: 43</text>
        <text x="90" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Source Routing Directives</text>

        <!-- Next Header Box -->
        <rect x="15" y="105" width="150" height="32" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.2"/>
        <text x="90" y="125" fill="var(--warning)" font-size="9.5" font-weight="900" text-anchor="middle">Next Header = 6</text>
      </g>

      <!-- LINK ARROW 3 -->
      <path d="M 670 125 L 715 125" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr-chain)"/>

      <!-- NODE 4: UPPER-LAYER PAYLOAD (TCP) -->
      <g transform="translate(720, 50)">
        <rect width="185" height="150" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <rect x="10" y="12" width="165" height="30" rx="4" fill="var(--success-dim)" stroke="none"/>
        <text x="92" y="32" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">TCP Payload</text>
        <text x="92" y="65" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Upper Protocol: 6</text>
        <text x="92" y="85" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Ports, Seq, Ack, App Data</text>

        <rect x="15" y="105" width="155" height="32" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.2"/>
        <text x="92" y="125" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">END OF IP HEADERS</text>
      </g>

      <!-- BOTTOM EXPLANATION BANNER -->
      <g transform="translate(30, 220)">
        <rect width="875" height="55" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="24" fill="var(--tx-primary)" font-size="10.5" font-weight="800">
          Hardware ASIC Efficiency Rule:
        </text>
        <text x="25" y="42" fill="var(--tx-muted)" font-size="9.5">
          Intermediate routers ONLY process the Hop-by-Hop extension header (Type 0). All subsequent extension headers (Routing, Fragmentation, ESP, AH) are completely skipped and ignored by transit routers until reaching the final destination host!
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: IPv4 to IPv6 Migration Triad
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔄</span>
      <span class="diagram-title">Figure 16.3: IPv4-to-IPv6 Migration Triad — Dual Stack, Tunneling &amp; Translation</span>
    </div>
    <span class="diagram-badge">MIGRATION STRATEGIES</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-tun" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="290" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- PILLAR 1: DUAL STACK -->
      <g transform="translate(30, 25)">
        <rect width="275" height="245" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="15" y="15" width="245" height="32" rx="4" fill="var(--info-dim)" stroke="none"/>
        <text x="137" y="36" fill="var(--info)" font-size="11.5" font-weight="900" text-anchor="middle">1. DUAL STACK (RFC 4213)</text>

        <text x="20" y="70" fill="var(--tx-primary)" font-size="10" font-weight="800">Simultaneous Dual Coexistence</text>
        <text x="20" y="88" fill="var(--tx-muted)" font-size="9">Every host &amp; router implements both IPv4 &amp; IPv6 network stacks.</text>

        <!-- Stack diagram -->
        <g transform="translate(35, 105)">
          <rect width="205" height="26" rx="3" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <text x="102" y="18" fill="var(--tx-primary)" font-size="9.5" font-weight="800" text-anchor="middle">Applications (HTTP, DNS)</text>

          <rect y="32" width="98" height="30" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
          <text x="49" y="51" fill="var(--accent)" font-size="9.5" font-weight="900" text-anchor="middle">IPv4 Stack</text>

          <rect x="107" y="32" width="98" height="30" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="156" y="51" fill="var(--info)" font-size="9.5" font-weight="900" text-anchor="middle">IPv6 Stack</text>
        </g>

        <text x="20" y="195" fill="var(--success)" font-size="9.5" font-weight="700">✓ Native performance; seamless</text>
        <text x="20" y="215" fill="var(--danger)" font-size="9.5" font-weight="700">✗ Still requires scarce IPv4 addresses</text>
      </g>

      <!-- PILLAR 2: TUNNELING -->
      <g transform="translate(330, 25)">
        <rect width="280" height="245" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <rect x="15" y="15" width="250" height="32" rx="4" fill="var(--accent-dim)" stroke="none"/>
        <text x="140" y="36" fill="var(--accent)" font-size="11.5" font-weight="900" text-anchor="middle">2. TUNNELING (6to4, GRE)</text>

        <text x="20" y="70" fill="var(--tx-primary)" font-size="10" font-weight="800">IPv6 Encapsulated Inside IPv4</text>
        <text x="20" y="88" fill="var(--tx-muted)" font-size="9">Carries IPv6 packets across legacy transit IPv4-only backbones.</text>

        <!-- Tunnel Graphic -->
        <g transform="translate(15, 105)">
          <rect width="250" height="50" rx="4" fill="var(--bg-surface)" stroke="var(--accent)" stroke-width="1.2" stroke-dasharray="4 2"/>
          <rect x="10" y="10" width="85" height="30" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="52" y="28" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">IPv4 Header</text>

          <rect x="100" y="10" width="140" height="30" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="170" y="28" fill="var(--info)" font-size="9" font-weight="900" text-anchor="middle">IPv6 Datagram (Data)</text>
        </g>

        <text x="20" y="195" fill="var(--success)" font-size="9.5" font-weight="700">✓ Connects isolated IPv6 islands</text>
        <text x="20" y="215" fill="var(--danger)" font-size="9.5" font-weight="700">✗ Header overhead &amp; MTU fragmentation</text>
      </g>

      <!-- PILLAR 3: TRANSLATION -->
      <g transform="translate(635, 25)">
        <rect width="275" height="245" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <rect x="15" y="15" width="245" height="32" rx="4" fill="var(--success-dim)" stroke="none"/>
        <text x="137" y="36" fill="var(--success)" font-size="11.5" font-weight="900" text-anchor="middle">3. NAT64 / DNS64</text>

        <text x="20" y="70" fill="var(--tx-primary)" font-size="10" font-weight="800">Protocol Header Translation</text>
        <text x="20" y="88" fill="var(--tx-muted)" font-size="9">Enables IPv6-only clients to communicate directly with IPv4-only servers.</text>

        <!-- Gateway Box -->
        <g transform="translate(20, 105)">
          <rect width="235" height="50" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.2"/>
          <text x="117" y="24" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">NAT64 Gateway Translator</text>
          <text x="117" y="40" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">IPv6 Header ⮂ IPv4 Header Conversion</text>
        </g>

        <text x="20" y="195" fill="var(--success)" font-size="9.5" font-weight="700">✓ True IPv6-only client deployment</text>
        <text x="20" y="215" fill="var(--danger)" font-size="9.5" font-weight="700">✗ Breaks end-to-end IPsec integrity</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch16_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch16">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">IPv6 Architecture &amp; Migration Mechanisms</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Header Comparison, Extension Headers, &amp; IPv4 Transition Strategies</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Explain the architecture of IPv6. Compare the IPv6 base header with the IPv4 header, explaining why specific fields were removed or modified. Describe the Extension Header daisy chaining mechanism and explain the three core transition strategies: Dual Stack, Tunneling, and NAT64."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: HEADER COMPARISON -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Comparative Header Analysis: IPv4 vs. IPv6 (4 Marks)</h4>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>IPv4 Header Field</th>
                  <th>IPv6 Equivalent Field</th>
                  <th>Architectural Justification for Modification / Removal</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>IHL (4 bits)</strong></td>
                  <td><strong>ELIMINATED</strong></td>
                  <td>IPv6 base header is strictly fixed at <strong>40 bytes</strong>. Hardware ASICs process fixed-size headers significantly faster without checking boundary offsets.</td>
                </tr>
                <tr>
                  <td><strong>Total Length (16 bits)</strong></td>
                  <td><strong>Payload Length (16 bits)</strong></td>
                  <td>Measures payload bytes following the 40-byte base header (including extension headers). Eliminates ambiguity.</td>
                </tr>
                <tr>
                  <td><strong>Identification, Flags, Offset</strong></td>
                  <td><strong>ELIMINATED from Base</strong></td>
                  <td>Moved to an optional <strong>Fragment Extension Header (Type 44)</strong>. Intermediate routers no longer fragment packets; only source hosts perform fragmentation via Path MTU Discovery.</td>
                </tr>
                <tr>
                  <td><strong>Time to Live (TTL)</strong></td>
                  <td><strong>Hop Limit (8 bits)</strong></td>
                  <td>Renamed to accurately reflect reality: it was always decremented as a hop counter, never by actual seconds of elapsed time.</td>
                </tr>
                <tr>
                  <td><strong>Protocol (8 bits)</strong></td>
                  <td><strong>Next Header (8 bits)</strong></td>
                  <td>Generalizes the pointer to identify either an upper-layer transport protocol (TCP/UDP) or the next Extension Header in the daisy chain.</td>
                </tr>
                <tr>
                  <td><strong>Header Checksum (16 bits)</strong></td>
                  <td><strong>ELIMINATED</strong></td>
                  <td>Redundant! Layer 2 (Ethernet CRC) and Layer 4 (TCP/UDP checksums) already detect bit errors. Removing it eliminates router recomputations at every single hop.</td>
                </tr>
                <tr>
                  <td><strong>Options &amp; Padding</strong></td>
                  <td><strong>Extension Headers</strong></td>
                  <td>Replaced with modular, daisy-chained extension headers that intermediate routers bypass without performance degradation.</td>
                </tr>
                <tr>
                  <td><strong>Addresses (32 bits)</strong></td>
                  <td><strong>Addresses (128 bits)</strong></td>
                  <td>Expanded four-fold in bits (from $2^{32} \approx 4.3 \times 10^9$ to $2^{128} \approx 3.4 \times 10^{38}$), solving global IP exhaustion forever.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 2: EXTENSION HEADERS -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Extension Header Daisy Chaining Mechanism (3 Marks)</h4>
          <p>
            Unlike IPv4 options that bloat every packet's core header, IPv6 implements an efficient <strong>singly linked list</strong>:
          </p>
          <ul class="blueprint-list">
            <li><strong>Sequential Traversal:</strong> Each header contains an 8-bit `Next Header` field identifying the protocol type of the immediately following block.</li>
            <li><strong>Transit Router Bypass:</strong> Routers in the core forward packets strictly by reading the 40-byte base header. Only the <strong>Hop-by-Hop Options (Type 0)</strong> header requires router inspection.</li>
            <li><strong>Deterministic Order:</strong> Recommended processing order:
              $$\text{Base (40B)} \to \text{Hop-by-Hop (0)} \to \text{Routing (43)} \to \text{Fragment (44)} \to \text{ESP (50)} \to \text{AH (51)} \to \text{TCP (6)}$$
            </li>
          </ul>
        </div>

        <!-- SECTION 3: TRANSITION MECHANISMS -->
        <div class="blueprint-section">
          <h4 class="section-title">3. IPv4 to IPv6 Migration Triad (3 Marks)</h4>
          <div class="blueprint-grid">
            <div class="blueprint-col">
              <h5>1. Dual Stack (RFC 4213)</h5>
              <ul>
                <li>Routers and endpoints run both IPv4 and IPv6 protocols simultaneously on the same physical interfaces.</li>
                <li>DNS resolution dictates selection: queries requesting <code>AAAA</code> records use IPv6; <code>A</code> records use IPv4.</li>
                <li>The gold standard for long-term gradual migration.</li>
              </ul>
            </div>
            <div class="blueprint-col">
              <h5>2. Tunneling (6to4, Teredo)</h5>
              <ul>
                <li>Encapsulates native IPv6 packets inside standard IPv4 datagrams (IPv4 Protocol field = 41).</li>
                <li>Allows disconnected IPv6 subnets to communicate across legacy IPv4 transit ISP backbones.</li>
              </ul>
            </div>
            <div class="blueprint-col">
              <h5>3. NAT64 &amp; DNS64 Translation</h5>
              <ul>
                <li>Allows modern IPv6-only cellular or datacenter devices to access legacy IPv4-only web servers.</li>
                <li>DNS64 synthesizes artificial <code>AAAA</code> records; NAT64 translates headers at stateful gateway.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- TRAPS & MARKING SCHEME -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap:</strong>
            Never write that <em>"IPv6 routers fragment oversized packets just like IPv4."</em> In IPv6, <strong>intermediate routers NEVER fragment packets</strong>! If an IPv6 packet exceeds the link MTU, the router discards it and returns an <strong>ICMPv6 Packet Too Big (Type 2, Code 0)</strong> message containing the link MTU. The sending source host must lower its transmission size or insert a Fragment Extension Header!
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 16
# ==========================================

# 1. Replace Box #8 in s16-header with Figure 16.1
match_s16_h = re.search(r'(<section id="s16-header"[^>]*>.*?)(<div class="ascii-box">.*?</div>)', content, flags=re.DOTALL)
if match_s16_h:
    content = content[:match_s16_h.start(2)] + svg_diagram_1 + content[match_s16_h.end(2):]
    print('Replaced ASCII box in s16-header with Figure 16.1')
else:
    print('Warning: could not find ASCII box in s16-header')

# 2. Replace Box in s16-ext-headers with Figure 16.2
match_s16_ext = re.search(r'(<section id="s16-ext-headers"[^>]*>.*?)(<div class="ascii-box">.*?</div>)', content, flags=re.DOTALL)
if match_s16_ext:
    content = content[:match_s16_ext.start(2)] + svg_diagram_2 + content[match_s16_ext.end(2):]
    print('Replaced ASCII box in s16-ext-headers with Figure 16.2')
else:
    print('Warning: could not find ASCII box in s16-ext-headers')

# 3 & 4. Insert Figure 16.3 and DU 10-Mark Blueprint before study-resources in s16-summary
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    combined_insertion = svg_diagram_3 + '\n\n    ' + ch16_uni_blueprint + '\n\n    '
    content = content[:ref_target.start()] + combined_insertion + content[ref_target.start():]
    print('Inserted Figure 16.3 and 10-Mark University Blueprint in Chapter 16!')
else:
    print('Warning: could not find .study-resources in Chapter 16')

with open(ch16_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 16 upgrade completed!')
