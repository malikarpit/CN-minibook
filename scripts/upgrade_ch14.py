"""
Upgrade Chapter 14 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch14_path = '/Users/arpit/minibook/cn/chapters/ch14-logical-addressing-ipv4.html'
with open(ch14_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: IPv4 32-Bit Address Anatomy
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔢</span>
      <span class="diagram-title">Figure 14.1: IPv4 32-Bit Address Anatomy — Octets, Binary Alignment &amp; Mask Boundary</span>
    </div>
    <span class="diagram-badge">ADDRESS ANATOMY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-ch14" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP: DOTTED-DECIMAL NOTATION -->
      <g transform="translate(30, 25)">
        <rect width="880" height="60" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="25" y="36" fill="var(--accent)" font-size="12" font-weight="900">Dotted-Decimal Form:</text>

        <!-- Octet 1 -->
        <rect x="190" y="15" width="140" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="260" y="36" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">192</text>
        <text x="340" y="36" fill="var(--tx-muted)" font-size="18" font-weight="900">.</text>

        <!-- Octet 2 -->
        <rect x="360" y="15" width="140" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="430" y="36" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">168</text>
        <text x="510" y="36" fill="var(--tx-muted)" font-size="18" font-weight="900">.</text>

        <!-- Octet 3 -->
        <rect x="530" y="15" width="140" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="600" y="36" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">10</text>
        <text x="680" y="36" fill="var(--tx-muted)" font-size="18" font-weight="900">.</text>

        <!-- Octet 4 -->
        <rect x="700" y="15" width="140" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="770" y="36" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">45</text>
      </g>

      <!-- MIDDLE: 32-BIT BINARY OCTETS -->
      <g transform="translate(30, 100)">
        <rect width="880" height="70" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="25" y="40" fill="var(--tx-primary)" font-size="12" font-weight="900">32-Bit Binary Form:</text>

        <!-- Octet 1 Binary -->
        <rect x="190" y="20" width="140" height="32" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="260" y="41" fill="var(--info)" font-size="12" font-family="monospace" font-weight="800" text-anchor="middle">11000000</text>
        <text x="260" y="62" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Octet 1 (8 bits)</text>

        <!-- Octet 2 Binary -->
        <rect x="360" y="20" width="140" height="32" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="430" y="41" fill="var(--info)" font-size="12" font-family="monospace" font-weight="800" text-anchor="middle">10101000</text>
        <text x="430" y="62" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Octet 2 (8 bits)</text>

        <!-- Octet 3 Binary -->
        <rect x="530" y="20" width="140" height="32" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="600" y="41" fill="var(--info)" font-size="12" font-family="monospace" font-weight="800" text-anchor="middle">00001010</text>
        <text x="600" y="62" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Octet 3 (8 bits)</text>

        <!-- Octet 4 Binary with Split -->
        <rect x="700" y="20" width="140" height="32" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="770" y="41" fill="var(--info)" font-size="12" font-family="monospace" font-weight="800" text-anchor="middle">00101101</text>
        <text x="770" y="62" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Octet 4 (8 bits)</text>
      </g>

      <!-- BOTTOM: PREFIX VS HOST BOUNDARY (/26 EXAMPLE) -->
      <g transform="translate(30, 185)">
        <rect width="880" height="115" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>

        <!-- Network Prefix Region (26 bits) -->
        <rect x="190" y="20" width="530" height="50" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="455" y="42" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">
          NETWORK PREFIX: 26 BITS (/26 Subnet Mask = 255.255.255.192)
        </text>
        <text x="455" y="58" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">
          Routes packets across global internetwork to target subnet (192.168.10.0)
        </text>

        <!-- Host Identifier Region (6 bits) -->
        <rect x="730" y="20" width="110" height="50" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="2"/>
        <text x="785" y="42" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">HOST ID</text>
        <text x="785" y="58" fill="var(--tx-muted)" font-size="9" text-anchor="middle">6 bits (64 IPs)</text>

        <!-- Divider Line -->
        <line x1="725" y1="10" x2="725" y2="80" stroke="var(--danger)" stroke-width="2.5" stroke-dasharray="4 2"/>
        <text x="725" y="100" fill="var(--danger)" font-size="9.5" font-weight="900" text-anchor="middle">Subnet Mask Boundary (/26)</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Classful Addressing Hierarchy
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🏛️</span>
      <span class="diagram-title">Figure 14.2: Classful Addressing Taxonomy — Classes A through E Leading Bits &amp; Capacities</span>
    </div>
    <span class="diagram-badge">CLASSFUL HIERARCHY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- CLASS A -->
      <g transform="translate(30, 25)">
        <rect width="880" height="52" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <rect x="15" y="12" width="85" height="28" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="57" y="31" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Class A</text>

        <!-- Bit Breakdown -->
        <rect x="115" y="12" width="45" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="137" y="30" fill="var(--danger)" font-size="11" font-family="monospace" font-weight="900" text-anchor="middle">0</text>

        <rect x="165" y="12" width="130" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="230" y="30" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">Network (7 bits)</text>

        <rect x="300" y="12" width="310" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="455" y="30" fill="var(--success)" font-size="10" font-weight="800" text-anchor="middle">Host Identifier (24 bits = 16,777,214 hosts)</text>

        <text x="630" y="30" fill="var(--tx-primary)" font-size="10" font-weight="800">Range: 1.0.0.0 – 126.255.255.255</text>
        <text x="825" y="30" fill="var(--tx-muted)" font-size="9.5">Mask: 255.0.0.0 (/8)</text>
      </g>

      <!-- CLASS B -->
      <g transform="translate(30, 85)">
        <rect width="880" height="52" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <rect x="15" y="12" width="85" height="28" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="57" y="31" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Class B</text>

        <!-- Bit Breakdown -->
        <rect x="115" y="12" width="55" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="142" y="30" fill="var(--danger)" font-size="11" font-family="monospace" font-weight="900" text-anchor="middle">10</text>

        <rect x="175" y="12" width="215" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="282" y="30" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">Network (14 bits)</text>

        <rect x="395" y="12" width="215" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="502" y="30" fill="var(--success)" font-size="10" font-weight="800" text-anchor="middle">Host (16 bits = 65,534 hosts)</text>

        <text x="630" y="30" fill="var(--tx-primary)" font-size="10" font-weight="800">Range: 128.0.0.0 – 191.255.255.255</text>
        <text x="825" y="30" fill="var(--tx-muted)" font-size="9.5">Mask: 255.255.0.0 (/16)</text>
      </g>

      <!-- CLASS C -->
      <g transform="translate(30, 145)">
        <rect width="880" height="52" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <rect x="15" y="12" width="85" height="28" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="57" y="31" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Class C</text>

        <!-- Bit Breakdown -->
        <rect x="115" y="12" width="65" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="147" y="30" fill="var(--danger)" font-size="11" font-family="monospace" font-weight="900" text-anchor="middle">110</text>

        <rect x="185" y="12" width="310" height="28" rx="3" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="340" y="30" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">Network (21 bits)</text>

        <rect x="500" y="12" width="110" height="28" rx="3" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="555" y="30" fill="var(--success)" font-size="10" font-weight="800" text-anchor="middle">Host (8b = 254)</text>

        <text x="630" y="30" fill="var(--tx-primary)" font-size="10" font-weight="800">Range: 192.0.0.0 – 223.255.255.255</text>
        <text x="825" y="30" fill="var(--tx-muted)" font-size="9.5">Mask: 255.255.255.0 (/24)</text>
      </g>

      <!-- CLASS D (MULTICAST) -->
      <g transform="translate(30, 205)">
        <rect width="880" height="52" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <rect x="15" y="12" width="85" height="28" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="57" y="31" fill="var(--warning)" font-size="12" font-weight="900" text-anchor="middle">Class D</text>

        <!-- Bit Breakdown -->
        <rect x="115" y="12" width="75" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="152" y="30" fill="var(--danger)" font-size="11" font-family="monospace" font-weight="900" text-anchor="middle">1110</text>

        <rect x="195" y="12" width="415" height="28" rx="3" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="402" y="30" fill="var(--warning)" font-size="10" font-weight="900" text-anchor="middle">Multicast Group ID (28 bits — No Host/NetID Division)</text>

        <text x="630" y="30" fill="var(--tx-primary)" font-size="10" font-weight="800">Range: 224.0.0.0 – 239.255.255.255</text>
        <text x="825" y="30" fill="var(--tx-muted)" font-size="9.5">Mask: None (Multicast)</text>
      </g>

      <!-- CLASS E (EXPERIMENTAL) -->
      <g transform="translate(30, 265)">
        <rect width="880" height="52" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <rect x="15" y="12" width="85" height="28" rx="4" fill="var(--border)" stroke="var(--tx-muted)" stroke-width="1.5"/>
        <text x="57" y="31" fill="var(--tx-muted)" font-size="12" font-weight="900" text-anchor="middle">Class E</text>

        <!-- Bit Breakdown -->
        <rect x="115" y="12" width="75" height="28" rx="3" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="152" y="30" fill="var(--danger)" font-size="11" font-family="monospace" font-weight="900" text-anchor="middle">1111</text>

        <rect x="195" y="12" width="415" height="28" rx="3" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="402" y="30" fill="var(--tx-muted)" font-size="10" font-weight="800" text-anchor="middle">Reserved for Future / Research &amp; Experimental Use</text>

        <text x="630" y="30" fill="var(--tx-primary)" font-size="10" font-weight="800">Range: 240.0.0.0 – 255.255.255.254</text>
        <text x="825" y="30" fill="var(--tx-muted)" font-size="9.5">Mask: Reserved</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: VLSM Hierarchical Subnetting Tree
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🌳</span>
      <span class="diagram-title">Figure 14.3: VLSM Binary Subnetting Tree — Hierarchical Partitioning Without Address Waste</span>
    </div>
    <span class="diagram-badge">VLSM SUBNET TREE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 350" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-tree" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="330" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- ROOT BLOCK: /24 -->
      <g transform="translate(320, 25)">
        <rect width="300" height="42" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="150" y="22" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">PARENT BLOCK: 192.168.1.0/24</text>
        <text x="150" y="36" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">Total: 256 IP Addresses (Mask: 255.255.255.0)</text>
      </g>

      <!-- BRANCH LEVEL 1: TWO /26 SUBNETS -->
      <path d="M 400 68 L 220 115" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-tree)"/>
      <path d="M 540 68 L 720 115" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-tree)"/>

      <!-- LEFT LEAF: DEPT A (/26) -->
      <g transform="translate(60, 115)">
        <rect width="320" height="60" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="160" y="24" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">DEPT A: 192.168.1.0/26 (64 IPs)</text>
        <text x="160" y="40" fill="var(--tx-primary)" font-size="9.5" text-anchor="middle">Hosts: 60 required (62 usable: .1 to .62)</text>
        <text x="160" y="53" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Broadcast: .63 | Mask: 255.255.255.192</text>
      </g>

      <!-- RIGHT NODE: 192.168.1.64/26 (SPLIT FURTHER) -->
      <g transform="translate(560, 115)">
        <rect width="320" height="45" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="160" y="22" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">192.168.1.64/26 (64 IPs) ➔ SPLIT</text>
        <text x="160" y="37" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Divided into two /27 subnets (32 IPs each)</text>
      </g>

      <!-- BRANCH LEVEL 2: TWO /27 SUBNETS -->
      <path d="M 640 162 L 520 205" stroke="var(--info)" stroke-width="1.8" marker-end="url(#arr-tree)"/>
      <path d="M 800 162 L 780 205" stroke="var(--info)" stroke-width="1.8" marker-end="url(#arr-tree)"/>

      <!-- DEPT B LEAF: /27 -->
      <g transform="translate(370, 205)">
        <rect width="300" height="55" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="150" y="22" fill="var(--success)" font-size="10.5" font-weight="900" text-anchor="middle">DEPT B: 192.168.1.64/27 (32 IPs)</text>
        <text x="150" y="37" fill="var(--tx-primary)" font-size="9" text-anchor="middle">Hosts: 28 req (30 usable: .65 to .94)</text>
        <text x="150" y="49" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Broadcast: .95 | Mask: 255.255.255.224</text>
      </g>

      <!-- RIGHT NODE 2: 192.168.1.96/27 (SPLIT FURTHER) -->
      <g transform="translate(690, 205)">
        <rect width="220" height="42" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="110" y="20" fill="var(--warning)" font-size="10" font-weight="900" text-anchor="middle">192.168.1.96/27 ➔ SPLIT</text>
        <text x="110" y="34" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Divided into /28 subnets</text>
      </g>

      <!-- BRANCH LEVEL 3 -->
      <path d="M 740 248 L 710 275" stroke="var(--warning)" stroke-width="1.5" marker-end="url(#arr-tree)"/>
      <path d="M 850 248 L 840 275" stroke="var(--warning)" stroke-width="1.5" marker-end="url(#arr-tree)"/>

      <!-- DEPT C: /28 -->
      <g transform="translate(610, 275)">
        <rect width="180" height="50" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="90" y="18" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">DEPT C: /28 (16 IPs)</text>
        <text x="90" y="32" fill="var(--tx-primary)" font-size="8.5" text-anchor="middle">14 usable (.97–.110)</text>
        <text x="90" y="44" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Broadcast: .111</text>
      </g>

      <!-- DEPT D: /30 (P2P WAN) -->
      <g transform="translate(805, 275)">
        <rect width="115" height="50" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="57" y="18" fill="var(--accent)" font-size="9" font-weight="900" text-anchor="middle">WAN: /30 (4 IPs)</text>
        <text x="57" y="32" fill="var(--tx-primary)" font-size="8.5" text-anchor="middle">2 usable (.113–.114)</text>
        <text x="57" y="44" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Broadcast: .115</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Longest Prefix Matching (LPM)
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🎯</span>
      <span class="diagram-title">Figure 14.4: Longest Prefix Match (LPM) Hardware FIB Forwarding Engine</span>
    </div>
    <span class="diagram-badge">LPM FORWARDING</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-lpm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="290" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- INCOMING PACKET HEADER -->
      <g transform="translate(30, 25)">
        <rect width="250" height="70" rx="8" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="125" y="26" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">INCOMING IP PACKET</text>
        <text x="125" y="46" fill="var(--tx-primary)" font-size="12" font-family="monospace" font-weight="900" text-anchor="middle">
          Dest IP: 192.168.1.45
        </text>
        <text x="125" y="60" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Binary: ...00000001.00101101</text>
      </g>

      <!-- FIB LOOKUP ENGINE -->
      <g transform="translate(310, 25)">
        <rect width="600" height="255" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="300" y="24" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">
          Forwarding Information Base (FIB) Routing Entries Comparison
        </text>

        <!-- Route 1: Default -->
        <g transform="translate(20, 40)">
          <rect width="560" height="36" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <text x="15" y="22" fill="var(--tx-muted)" font-size="10" font-family="monospace">0.0.0.0/0</text>
          <text x="140" y="22" fill="var(--tx-muted)" font-size="9.5">Prefix Length: 0 bits</text>
          <text x="290" y="22" fill="var(--warning)" font-size="9.5" font-weight="700">Matches (Wildcard)</text>
          <text x="460" y="22" fill="var(--tx-muted)" font-size="9.5">Next-Hop: Gateway</text>
        </g>

        <!-- Route 2: /16 -->
        <g transform="translate(20, 82)">
          <rect width="560" height="36" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <text x="15" y="22" fill="var(--tx-muted)" font-size="10" font-family="monospace">192.168.0.0/16</text>
          <text x="140" y="22" fill="var(--tx-muted)" font-size="9.5">Prefix Length: 16 bits</text>
          <text x="290" y="22" fill="var(--warning)" font-size="9.5" font-weight="700">Matches 16 leading bits</text>
          <text x="460" y="22" fill="var(--tx-muted)" font-size="9.5">Egress: eth0</text>
        </g>

        <!-- Route 3: /24 -->
        <g transform="translate(20, 124)">
          <rect width="560" height="36" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <text x="15" y="22" fill="var(--tx-muted)" font-size="10" font-family="monospace">192.168.1.0/24</text>
          <text x="140" y="22" fill="var(--tx-muted)" font-size="9.5">Prefix Length: 24 bits</text>
          <text x="290" y="22" fill="var(--warning)" font-size="9.5" font-weight="700">Matches 24 leading bits</text>
          <text x="460" y="22" fill="var(--tx-muted)" font-size="9.5">Egress: eth1</text>
        </g>

        <!-- Route 4: /26 - THE WINNER! -->
        <g transform="translate(20, 166)">
          <rect width="560" height="42" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
          <text x="15" y="25" fill="var(--success)" font-size="11" font-family="monospace" font-weight="900">192.168.1.0/26</text>
          <text x="140" y="25" fill="var(--success)" font-size="10" font-weight="900">Prefix Length: 26 bits</text>
          <text x="290" y="25" fill="var(--success)" font-size="10.5" font-weight="900">✓ LONGEST MATCH (WINNER)</text>
          <text x="475" y="25" fill="var(--success)" font-size="10.5" font-weight="900">Egress: eth2</text>
        </g>

        <!-- Route 5: /28 - MISMATCH -->
        <g transform="translate(20, 214)">
          <rect width="560" height="32" rx="4" fill="var(--danger-dim)" stroke="none"/>
          <text x="15" y="20" fill="var(--danger)" font-size="10" font-family="monospace">192.168.1.64/28</text>
          <text x="140" y="20" fill="var(--danger)" font-size="9">Prefix Length: 28 bits</text>
          <text x="290" y="20" fill="var(--danger)" font-size="9.5" font-weight="800">✗ Mismatch (Bit 26 is 0 != 1)</text>
          <text x="460" y="20" fill="var(--tx-muted)" font-size="9">Ignored</text>
        </g>
      </g>

      <!-- FORWARDING DECISION SUMMARY -->
      <g transform="translate(30, 120)">
        <rect width="250" height="155" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="125" y="26" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">LPM FORWARDING RULE</text>
        <text x="20" y="52" fill="var(--tx-primary)" font-size="9.5" font-weight="700">Router Decision:</text>
        <text x="20" y="72" fill="var(--tx-muted)" font-size="9">Even though /0, /16, /24, and /26 all match the destination IP, the router selects <strong>/26</strong>.</text>
        <text x="20" y="112" fill="var(--success)" font-size="9.5" font-weight="800">Forwarded out interface eth2!</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 5. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch14_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch14">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">IPv4 Logical Addressing &amp; VLSM Subnet Design</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Variable-Length Subnet Mask (VLSM) Allocation &amp; Address Table</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"An enterprise is assigned the network block 192.168.1.0/24. It requires four subnets for: Department A (60 hosts), Department B (28 hosts), Department C (14 hosts), and a Point-to-Point WAN Link (2 hosts). Design an optimal VLSM subnet scheme. Provide the Subnet Mask, Network ID, Usable Host IP Range, Directed Broadcast Address, and unallocated capacity."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: POWER-OF-TWO SIZING DERIVATION -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Mathematical Subnet Sizing Derivation (3 Marks)</h4>
          <p>
            The fundamental sizing formula for any IPv4 subnet requiring $N$ usable hosts is:
            $$2^h - 2 \ge N \implies h = \lceil \log_2(N + 2) \rceil$$
            where $h$ is the number of borrowed host bits, and $2$ addresses are reserved ($0$ for Network ID, all-$1$s for Directed Broadcast).
          </p>
          <ul class="blueprint-list">
            <li><strong>Department A (60 hosts):</strong> $2^h - 2 \ge 60 \implies 2^h \ge 62 \implies h = 6$ bits ($2^6 - 2 = 62 \ge 60$).<br/>
              Prefix length: $32 - 6 = \mathbf{/26}$. Total block size: $2^6 = \mathbf{64}$ IP addresses.
            </li>
            <li><strong>Department B (28 hosts):</strong> $2^h - 2 \ge 28 \implies 2^h \ge 30 \implies h = 5$ bits ($2^5 - 2 = 30 \ge 28$).<br/>
              Prefix length: $32 - 5 = \mathbf{/27}$. Total block size: $2^5 = \mathbf{32}$ IP addresses.
            </li>
            <li><strong>Department C (14 hosts):</strong> $2^h - 2 \ge 14 \implies 2^h \ge 16 \implies h = 4$ bits ($2^4 - 2 = 14 \ge 14$).<br/>
              Prefix length: $32 - 4 = \mathbf{/28}$. Total block size: $2^4 = \mathbf{16}$ IP addresses.
            </li>
            <li><strong>Department D (WAN Link: 2 hosts):</strong> $2^h - 2 \ge 2 \implies 2^h \ge 4 \implies h = 2$ bits ($2^2 - 2 = 2 \ge 2$).<br/>
              Prefix length: $32 - 2 = \mathbf{/30}$. Total block size: $2^2 = \mathbf{4}$ IP addresses.
            </li>
          </ul>
        </div>

        <!-- SECTION 2: MASTER VLSM ALLOCATION TABLE -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Master VLSM Subnet Allocation Table (4 Marks)</h4>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Subnet Name</th>
                  <th>Hosts Req / Usable</th>
                  <th>Subnet Mask (CIDR)</th>
                  <th>Network Address</th>
                  <th>Usable Host IP Range</th>
                  <th>Directed Broadcast IP</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Dept A</strong></td>
                  <td>$60 \;/\; 62$</td>
                  <td>255.255.255.192 (/26)</td>
                  <td><code>192.168.1.0</code></td>
                  <td><code>192.168.1.1</code> – <code>192.168.1.62</code></td>
                  <td><code>192.168.1.63</code></td>
                </tr>
                <tr>
                  <td><strong>Dept B</strong></td>
                  <td>$28 \;/\; 30$</td>
                  <td>255.255.255.224 (/27)</td>
                  <td><code>192.168.1.64</code></td>
                  <td><code>192.168.1.65</code> – <code>192.168.1.94</code></td>
                  <td><code>192.168.1.95</code></td>
                </tr>
                <tr>
                  <td><strong>Dept C</strong></td>
                  <td>$14 \;/\; 14$</td>
                  <td>255.255.255.240 (/28)</td>
                  <td><code>192.168.1.96</code></td>
                  <td><code>192.168.1.97</code> – <code>192.168.1.110</code></td>
                  <td><code>192.168.1.111</code></td>
                </tr>
                <tr>
                  <td><strong>Dept D (WAN)</strong></td>
                  <td>$2 \;/\; 2$</td>
                  <td>255.255.255.252 (/30)</td>
                  <td><code>192.168.1.112</code></td>
                  <td><code>192.168.1.113</code> – <code>192.168.1.114</code></td>
                  <td><code>192.168.1.115</code></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 3: ADDRESS EFFICIENCY & UNALLOCATED CAPACITY -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Efficiency Audit &amp; Remaining Address Capacity (3 Marks)</h4>
          <ul class="blueprint-list">
            <li><strong>Total Allocated Addresses:</strong> $64 + 32 + 16 + 4 = \mathbf{116}$ addresses out of 256.</li>
            <li><strong>Unallocated Contiguous Space:</strong> <code>192.168.1.116</code> through <code>192.168.1.255</code> ($\mathbf{140}$ IP addresses).</li>
            <li><strong>Available Expansion Blocks:</strong>
              <ul>
                <li>One <code>/28</code> block: <code>192.168.1.116/28</code> (Wait: 116 is not divisible by 16; align to boundary <code>192.168.1.116/30</code>, <code>192.168.1.120/29</code>, and <code>192.168.1.128/25</code> yielding 128 IPs).</li>
                <li>One large pristine half-block: <code>192.168.1.128/25</code> (128 addresses) completely unencumbered for future corporate growth!</li>
              </ul>
            </li>
          </ul>
        </div>

        <!-- TRAPS & MARKING SCHEME -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap (Subnet Alignment):</strong>
            Always allocate subnets in <strong>strictly descending order of size</strong> (Largest to Smallest: 60 $\to$ 28 $\to$ 14 $\to$ 2). If you allocate small subnets first, the subsequent larger subnets will fail binary natural boundary alignment ($N \pmod{\text{BlockSize}} = 0$), causing fragmented, illegal subnet ranges!
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 14
# ==========================================

# 1. Insert Figure 14.1 in s14-structure
match_s14_st = re.search(r'(<section id="s14-structure"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s14_st:
    content = content[:match_s14_st.start(2)] + svg_diagram_1 + '\n\n      ' + content[match_s14_st.start(2):]
    print('Inserted Figure 14.1 in s14-structure')
else:
    print('Warning: could not find insertion spot in s14-structure')

# 2. Insert Figure 14.2 in s14-classful
match_s14_cl = re.search(r'(<section id="s14-classful"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s14_cl:
    content = content[:match_s14_cl.start(2)] + svg_diagram_2 + '\n\n      ' + content[match_s14_cl.start(2):]
    print('Inserted Figure 14.2 in s14-classful')
else:
    print('Warning: could not find insertion spot in s14-classful')

# 3. Insert Figure 14.3 in s14-subnetting
match_s14_sub = re.search(r'(<section id="s14-subnetting"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s14_sub:
    content = content[:match_s14_sub.start(2)] + svg_diagram_3 + '\n\n      ' + content[match_s14_sub.start(2):]
    print('Inserted Figure 14.3 in s14-subnetting')
else:
    print('Warning: could not find insertion spot in s14-subnetting')

# 4. Insert Figure 14.4 in s14-lpm
match_s14_lpm = re.search(r'(<section id="s14-lpm"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s14_lpm:
    content = content[:match_s14_lpm.start(2)] + svg_diagram_4 + '\n\n      ' + content[match_s14_lpm.start(2):]
    print('Inserted Figure 14.4 in s14-lpm')
else:
    print('Warning: could not find insertion spot in s14-lpm')

# 5. Insert DU 10-Mark Blueprint before study-resources in s14-summary
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch14_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 14!')
else:
    print('Warning: could not find .study-resources in Chapter 14')

with open(ch14_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 14 upgrade completed!')
