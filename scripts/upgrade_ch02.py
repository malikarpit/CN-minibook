"""
Upgrade Chapter 2 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch2_path = '/Users/arpit/minibook/cn/chapters/ch02-types-topologies.html'
with open(ch2_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Network Scale Taxonomy (PAN, LAN, CAN, MAN, WAN)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🗺️</span>
      <span class="diagram-title">Figure 2.1: Geographic Scale Taxonomy of Networks (PAN ➔ LAN ➔ CAN ➔ MAN ➔ WAN)</span>
    </div>
    <span class="diagram-badge">GEOGRAPHIC SCALE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-tax" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <linearGradient id="tax-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="var(--info)" stop-opacity="0.25"/>
        </linearGradient>
      </defs>

      <rect x="10" y="10" width="920" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- Scale Arrow across bottom -->
      <path d="M 40 310 L 890 310" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-tax)"/>
      <text x="465" y="332" fill="var(--tx-muted)" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">
        GEOGRAPHIC SPAN &amp; PROPAGATION DELAY INCREASES ➔ (HIGHER PROPAGATION DELAY, LOWER ERROR CONTROL COUPLING)
      </text>

      <!-- CARD 1: PAN -->
      <g transform="translate(30, 30)">
        <rect width="160" height="255" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <rect x="12" y="12" width="136" height="30" rx="6" fill="rgba(126, 196, 184, 0.15)" stroke="var(--accent)" stroke-width="1"/>
        <text x="80" y="32" fill="var(--accent)" font-size="13" font-weight="800" text-anchor="middle">1. PAN</text>
        <text x="80" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Personal Area</text>
        <text x="80" y="76" fill="var(--tx-muted)" font-size="10" text-anchor="middle">&lt; 10 meters</text>

        <line x1="20" y1="90" x2="140" y2="90" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="112" fill="var(--tx-secondary)" font-size="10"><strong>Media:</strong> Bluetooth, Zigbee, UWB, NFC</text>
        <text x="20" y="145" fill="var(--tx-secondary)" font-size="10"><strong>Data Rate:</strong> 1–24 Mbps</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10"><strong>Ownership:</strong> Single user</text>
        <text x="20" y="205" fill="var(--tx-secondary)" font-size="10"><strong>Delay:</strong> Negligible (&lt;1 ms)</text>
        <text x="20" y="235" fill="var(--tx-muted)" font-size="9">Watch, Phone, Wireless Earbuds</text>
      </g>

      <!-- CARD 2: LAN -->
      <g transform="translate(210, 30)">
        <rect width="160" height="255" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.5"/>
        <rect x="12" y="12" width="136" height="30" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
        <text x="80" y="32" fill="var(--info)" font-size="13" font-weight="800" text-anchor="middle">2. LAN</text>
        <text x="80" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Local Area</text>
        <text x="80" y="76" fill="var(--tx-muted)" font-size="10" text-anchor="middle">100 m – 1 km</text>

        <line x1="20" y1="90" x2="140" y2="90" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="112" fill="var(--tx-secondary)" font-size="10"><strong>Media:</strong> Cat6 UTP, Wi-Fi 6, Multimode Fiber</text>
        <text x="20" y="145" fill="var(--tx-secondary)" font-size="10"><strong>Data Rate:</strong> 1–10 Gbps</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10"><strong>Ownership:</strong> Private Org</text>
        <text x="20" y="205" fill="var(--tx-secondary)" font-size="10"><strong>Error Rate:</strong> Very Low</text>
        <text x="20" y="235" fill="var(--tx-muted)" font-size="9">Office, College Lab, Home Wi-Fi</text>
      </g>

      <!-- CARD 3: CAN -->
      <g transform="translate(390, 30)">
        <rect width="160" height="255" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <rect x="12" y="12" width="136" height="30" rx="6" fill="rgba(251, 191, 36, 0.15)" stroke="var(--warning)" stroke-width="1"/>
        <text x="80" y="32" fill="var(--warning)" font-size="13" font-weight="800" text-anchor="middle">3. CAN</text>
        <text x="80" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Campus Area</text>
        <text x="80" y="76" fill="var(--tx-muted)" font-size="10" text-anchor="middle">1 km – 5 km</text>

        <line x1="20" y1="90" x2="140" y2="90" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="112" fill="var(--tx-secondary)" font-size="10"><strong>Media:</strong> Single-Mode Fiber Backbone</text>
        <text x="20" y="145" fill="var(--tx-secondary)" font-size="10"><strong>Data Rate:</strong> 10–40 Gbps</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10"><strong>Ownership:</strong> Single Institution</text>
        <text x="20" y="205" fill="var(--tx-secondary)" font-size="10"><strong>Topology:</strong> Collapsed Core</text>
        <text x="20" y="235" fill="var(--tx-muted)" font-size="9">University, Military Base, Hospital</text>
      </g>

      <!-- CARD 4: MAN -->
      <g transform="translate(570, 30)">
        <rect width="160" height="255" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <rect x="12" y="12" width="136" height="30" rx="6" fill="rgba(168, 85, 247, 0.15)" stroke="#c084fc" stroke-width="1"/>
        <text x="80" y="32" fill="#c084fc" font-size="13" font-weight="800" text-anchor="middle">4. MAN</text>
        <text x="80" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Metropolitan Area</text>
        <text x="80" y="76" fill="var(--tx-muted)" font-size="10" text-anchor="middle">5 km – 50 km</text>

        <line x1="20" y1="90" x2="140" y2="90" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="112" fill="var(--tx-secondary)" font-size="10"><strong>Media:</strong> Metro Ethernet, DWDM, 5G</text>
        <text x="20" y="145" fill="var(--tx-secondary)" font-size="10"><strong>Data Rate:</strong> 100 Mbps – 10 Gbps</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10"><strong>Ownership:</strong> Telecom / Consortium</text>
        <text x="20" y="205" fill="var(--tx-secondary)" font-size="10"><strong>Standard:</strong> IEEE 802.6 DQDB</text>
        <text x="20" y="235" fill="var(--tx-muted)" font-size="9">City Cable TV, Smart City Traffic</text>
      </g>

      <!-- CARD 5: WAN -->
      <g transform="translate(750, 30)">
        <rect width="160" height="255" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <rect x="12" y="12" width="136" height="30" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <text x="80" y="32" fill="var(--accent)" font-size="13" font-weight="800" text-anchor="middle">5. WAN</text>
        <text x="80" y="60" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Wide Area</text>
        <text x="80" y="76" fill="var(--tx-muted)" font-size="10" text-anchor="middle">&gt; 100 km (Global)</text>

        <line x1="20" y1="90" x2="140" y2="90" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="112" fill="var(--tx-secondary)" font-size="10"><strong>Media:</strong> Submarine Optical, Satellites</text>
        <text x="20" y="145" fill="var(--tx-secondary)" font-size="10"><strong>Data Rate:</strong> Variable (Carrier leased)</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10"><strong>Ownership:</strong> Multi-provider (Tier 1 ISP)</text>
        <text x="20" y="205" fill="var(--tx-secondary)" font-size="10"><strong>Routing:</strong> BGP, MPLS</text>
        <text x="20" y="235" fill="var(--tx-muted)" font-size="9">The Global Internet</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Key Differentiator:</strong> As geographic span expands from LAN to WAN, ownership shifts from private single-entity control to multi-carrier commercial routing, error rates increase due to link length, and propagation delay becomes the dominant latency factor.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Logical Access Perimeter (Internet vs Intranet vs Extranet)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🛡️</span>
      <span class="diagram-title">Figure 2.2: Security Perimeter Model — Intranet, Extranet, and Public Internet</span>
    </div>
    <span class="diagram-badge">SECURITY ARCHITECTURE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="intra-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--success)" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="var(--bg-card)" stop-opacity="0.95"/>
        </linearGradient>
        <linearGradient id="extra-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--warning)" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="var(--bg-card)" stop-opacity="0.95"/>
        </linearGradient>
        <linearGradient id="inter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--danger)" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="var(--bg-card)" stop-opacity="0.95"/>
        </linearGradient>
      </defs>

      <rect x="10" y="10" width="880" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TIER 1: INTRANET (TRUSTED ZONE) -->
      <g transform="translate(30, 30)">
        <rect width="250" height="270" rx="12" fill="url(#intra-grad)" stroke="var(--success)" stroke-width="2"/>
        <rect x="15" y="15" width="220" height="32" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="125" y="35" fill="var(--success)" font-size="13" font-weight="800" text-anchor="middle">INTRANET (Trusted Zone)</text>
        <text x="125" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Employees &amp; Internal Staff Only</text>
        
        <rect x="25" y="85" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="104" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Payroll &amp; HR Database</text>
        <text x="125" y="118" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Private IP: 10.0.0.0/8</text>

        <rect x="25" y="135" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="154" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Internal Code Repository</text>
        <text x="125" y="168" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Strict Zero Trust Access</text>

        <rect x="25" y="185" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="204" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Enterprise Workstations</text>
        <text x="125" y="218" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Domain Joined &amp; Managed</text>

        <text x="125" y="255" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Highest Security / Zero Public Route</text>
      </g>

      <!-- FIREWALL 1 (Internal) -->
      <g transform="translate(290, 110)">
        <rect width="25" height="110" rx="4" fill="var(--danger)" stroke="#fff" stroke-width="1"/>
        <text x="12" y="60" fill="#fff" font-size="10" font-weight="800" text-anchor="middle" transform="rotate(-90 12 60)">FIREWALL</text>
      </g>

      <!-- TIER 2: EXTRANET (SEMI-TRUSTED DMZ) -->
      <g transform="translate(325, 30)">
        <rect width="250" height="270" rx="12" fill="url(#extra-grad)" stroke="var(--warning)" stroke-width="2"/>
        <rect x="15" y="15" width="220" height="32" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="125" y="35" fill="var(--warning)" font-size="13" font-weight="800" text-anchor="middle">EXTRANET (Semi-Trusted)</text>
        <text x="125" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Authorized Partners &amp; Vendors</text>

        <rect x="25" y="85" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="104" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Supply Chain Portal</text>
        <text x="125" y="118" fill="var(--tx-muted)" font-size="9" text-anchor="middle">B2B EDI / Order Processing</text>

        <rect x="25" y="135" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="154" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Partner VPN Gateway</text>
        <text x="125" y="168" fill="var(--tx-muted)" font-size="9" text-anchor="middle">IPSec / SSL-VPN Tunnel</text>

        <rect x="25" y="185" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="204" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Collaborative Staging</text>
        <text x="125" y="218" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Client Preview Environments</text>

        <text x="125" y="255" fill="var(--warning)" font-size="10" font-weight="700" text-anchor="middle">Controlled Authentication Perimeter</text>
      </g>

      <!-- FIREWALL 2 (Perimeter) -->
      <g transform="translate(585, 110)">
        <rect width="25" height="110" rx="4" fill="var(--danger)" stroke="#fff" stroke-width="1"/>
        <text x="12" y="60" fill="#fff" font-size="10" font-weight="800" text-anchor="middle" transform="rotate(-90 12 60)">PERIMETER</text>
      </g>

      <!-- TIER 3: INTERNET (UNTRUSTED PUBLIC) -->
      <g transform="translate(620, 30)">
        <rect width="250" height="270" rx="12" fill="url(#inter-grad)" stroke="var(--danger)" stroke-width="2"/>
        <rect x="15" y="15" width="220" height="32" rx="6" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="125" y="35" fill="var(--danger)" font-size="13" font-weight="800" text-anchor="middle">INTERNET (Public / Untrusted)</text>
        <text x="125" y="65" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Entire Global Population</text>

        <rect x="25" y="85" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="104" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Public Web Server</text>
        <text x="125" y="118" fill="var(--tx-muted)" font-size="9" text-anchor="middle">HTTPS Port 443 / CDN</text>

        <rect x="25" y="135" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="154" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Anonymous Traffic</text>
        <text x="125" y="168" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Subject to DDoS / Scans</text>

        <rect x="25" y="185" width="200" height="42" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="125" y="204" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Cloud &amp; Consumer ISPs</text>
        <text x="125" y="218" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Global BGP Routes</text>

        <text x="125" y="255" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">Zero Trust Boundary / WAF &amp; Scrubbing</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University Exam Distinction:</strong> <em>Intranet</em> is strictly internal to employees behind corporate firewalls. <em>Extranet</em> extends selective access to authorized external partners/vendors over encrypted VPNs. <em>Internet</em> is the universally accessible public network.
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Client-Server vs Peer-to-Peer
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚖️</span>
      <span class="diagram-title">Figure 2.3: Architectural Paradigms — Centralized Client-Server vs. Decentralized P2P</span>
    </div>
    <span class="diagram-badge">SYSTEM ARCHITECTURE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-cs" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
        <marker id="arrow-p2p" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="300" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT PANEL: CLIENT-SERVER -->
      <g transform="translate(30, 25)">
        <rect width="400" height="260" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="200" y="28" fill="var(--info)" font-size="13" font-weight="800" text-anchor="middle">CLIENT-SERVER ARCHITECTURE</text>
        <text x="200" y="44" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Centralized Control • Asymmetric Roles</text>

        <!-- Central Server -->
        <g transform="translate(145, 65)">
          <rect width="110" height="60" rx="8" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="55" y="26" font-size="16" text-anchor="middle">🗄️</text>
          <text x="55" y="44" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">SERVER</text>
          <text x="55" y="55" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Always-on / Dedicated</text>
        </g>

        <!-- Clients -->
        <g transform="translate(25, 170)">
          <rect width="65" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="32" y="25" fill="var(--tx-primary)" font-size="9" font-weight="700" text-anchor="middle">Client A</text>
        </g>
        <g transform="translate(115, 170)">
          <rect width="65" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="32" y="25" fill="var(--tx-primary)" font-size="9" font-weight="700" text-anchor="middle">Client B</text>
        </g>
        <g transform="translate(215, 170)">
          <rect width="65" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="32" y="25" fill="var(--tx-primary)" font-size="9" font-weight="700" text-anchor="middle">Client C</text>
        </g>
        <g transform="translate(305, 170)">
          <rect width="65" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="32" y="25" fill="var(--tx-primary)" font-size="9" font-weight="700" text-anchor="middle">Client D</text>
        </g>

        <!-- Arrows: Clients to Server -->
        <path d="M 57 170 L 160 125" stroke="var(--info)" stroke-width="1.5" marker-end="url(#arrow-cs)"/>
        <path d="M 147 170 L 180 125" stroke="var(--info)" stroke-width="1.5" marker-end="url(#arrow-cs)"/>
        <path d="M 247 170 L 220 125" stroke="var(--info)" stroke-width="1.5" marker-end="url(#arrow-cs)"/>
        <path d="M 337 170 L 240 125" stroke="var(--info)" stroke-width="1.5" marker-end="url(#arrow-cs)"/>

        <text x="200" y="235" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">⚠️ Single Point of Failure (SPOF) at Server</text>
        <text x="200" y="249" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Examples: Web (HTTP), Email (SMTP), Databases (SQL)</text>
      </g>

      <!-- RIGHT PANEL: PEER-TO-PEER -->
      <g transform="translate(470, 25)">
        <rect width="400" height="260" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="200" y="28" fill="var(--accent)" font-size="13" font-weight="800" text-anchor="middle">PEER-TO-PEER (P2P) ARCHITECTURE</text>
        <text x="200" y="44" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Decentralized Mesh • Symmetric Servents</text>

        <!-- 4 Peer Nodes in Circle -->
        <g transform="translate(160, 55)">
          <circle cx="40" cy="25" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8"/>
          <text x="40" y="29" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Peer 1</text>
        </g>
        <g transform="translate(260, 115)">
          <circle cx="40" cy="25" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8"/>
          <text x="40" y="29" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Peer 2</text>
        </g>
        <g transform="translate(160, 175)">
          <circle cx="40" cy="25" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8"/>
          <text x="40" y="29" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Peer 3</text>
        </g>
        <g transform="translate(60, 115)">
          <circle cx="40" cy="25" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8"/>
          <text x="40" y="29" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">Peer 4</text>
        </g>

        <!-- Mesh Connections between all peers -->
        <line x1="200" y1="104" x2="280" y2="125" stroke="var(--accent)" stroke-width="1.8"/>
        <line x1="280" y1="155" x2="200" y2="175" stroke="var(--accent)" stroke-width="1.8"/>
        <line x1="200" y1="175" x2="120" y2="155" stroke="var(--accent)" stroke-width="1.8"/>
        <line x1="120" y1="125" x2="200" y2="104" stroke="var(--accent)" stroke-width="1.8"/>
        <line x1="200" y1="104" x2="200" y2="175" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="124" y1="140" x2="276" y2="140" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="3,3"/>

        <text x="200" y="235" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">✓ Highly Scalable &amp; Self-Healing (No Central SPOF)</text>
        <text x="200" y="249" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Examples: BitTorrent, Bitcoin / Blockchain, IPFS</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Pedagogical Insight:</strong> In Client-Server, capacity bottlenecks occur as client count grows ($O(N)$ load on server). In P2P, every new peer brings both demand (download) and service capacity (upload), making P2P inherently self-scaling.
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Bus Topology
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🚌</span>
      <span class="diagram-title">Figure 2.4: Bus Topology — Linear Shared Backbone, Drop Cables &amp; Terminators</span>
    </div>
    <span class="diagram-badge">PHYSICAL TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-bus" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="300" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT TERMINATOR (50 Ohm) -->
      <g transform="translate(40, 110)">
        <rect width="45" height="50" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="2"/>
        <text x="22" y="25" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="middle">50 Ω</text>
        <text x="22" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">TERM</text>
      </g>

      <!-- MAIN TRUNK / BACKBONE CABLE -->
      <line x1="85" y1="135" x2="815" y2="135" stroke="var(--accent)" stroke-width="8" stroke-linecap="round"/>
      <text x="450" y="125" fill="var(--accent)" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="0.1em">
        SHARED COAXIAL BACKBONE TRUNK (10BASE2 / 10BASE5)
      </text>

      <!-- RIGHT TERMINATOR (50 Ohm) -->
      <g transform="translate(815, 110)">
        <rect width="45" height="50" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="2"/>
        <text x="22" y="25" fill="var(--danger)" font-size="10" font-weight="800" text-anchor="middle">50 Ω</text>
        <text x="22" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">TERM</text>
      </g>

      <!-- NODE 1 (TOP) -->
      <g transform="translate(180, 25)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="45" y="25" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node A</text>
      </g>
      <!-- Drop Line 1 -->
      <line x1="225" y1="75" x2="225" y2="135" stroke="var(--info)" stroke-width="3"/>
      <!-- BNC Tap 1 -->
      <circle cx="225" cy="135" r="7" fill="var(--info)" stroke="#fff" stroke-width="1.5"/>
      <text x="225" y="155" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">BNC Tap</text>

      <!-- NODE 2 (BOTTOM) -->
      <g transform="translate(360, 205)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="45" y="25" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node B</text>
      </g>
      <!-- Drop Line 2 -->
      <line x1="405" y1="135" x2="405" y2="205" stroke="var(--info)" stroke-width="3"/>
      <!-- BNC Tap 2 -->
      <circle cx="405" cy="135" r="7" fill="var(--info)" stroke="#fff" stroke-width="1.5"/>
      <text x="405" y="155" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">BNC Tap</text>

      <!-- NODE 3 (TOP) -->
      <g transform="translate(540, 25)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="45" y="25" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node C</text>
      </g>
      <!-- Drop Line 3 -->
      <line x1="585" y1="75" x2="585" y2="135" stroke="var(--info)" stroke-width="3"/>
      <!-- BNC Tap 3 -->
      <circle cx="585" cy="135" r="7" fill="var(--info)" stroke="#fff" stroke-width="1.5"/>
      <text x="585" y="155" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">BNC Tap</text>

      <!-- NODE 4 (BOTTOM) -->
      <g transform="translate(700, 205)">
        <rect width="90" height="50" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="45" y="25" font-size="14" text-anchor="middle">🖨️</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Printer D</text>
      </g>
      <!-- Drop Line 4 -->
      <line x1="745" y1="135" x2="745" y2="205" stroke="var(--info)" stroke-width="3"/>
      <!-- BNC Tap 4 -->
      <circle cx="745" cy="135" r="7" fill="var(--info)" stroke="#fff" stroke-width="1.5"/>
      <text x="745" y="155" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">BNC Tap</text>

      <!-- FAULT CALLOUT -->
      <rect x="40" y="270" width="820" height="30" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="450" y="290" fill="var(--danger)" font-size="10" font-weight="700" text-anchor="middle">
        ⚠️ CRITICAL VULNERABILITY: If the backbone cable breaks at ANY point, signal reflection renders the ENTIRE network inoperable.
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Terminator Function:</strong> Coaxial terminators (typically 50-ohm resistors) absorb traveling electrical signals at both ends of the backbone bus. Without them, signals reflect back into the cable, causing constructive and destructive interference (standing waves) that destroys all frames.
  </div>
</div>'''

# ==========================================
# 5. DIAGRAM 5: Star Topology
# ==========================================
svg_diagram_5 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⭐</span>
      <span class="diagram-title">Figure 2.5: Star Topology — Central Switch / Hub with Dedicated Point-to-Point Links</span>
    </div>
    <span class="diagram-badge">DOMINANT LAN TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="880" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- CENTRAL SWITCH (HUB) -->
      <g transform="translate(385, 115)">
        <rect width="130" height="110" rx="12" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="65" y="42" font-size="24" text-anchor="middle">🔀</text>
        <text x="65" y="68" fill="var(--accent-light)" font-size="12" font-weight="800" text-anchor="middle">CENTRAL SWITCH</text>
        <text x="65" y="84" fill="var(--tx-muted)" font-size="9" text-anchor="middle">(Layer-2 Multiport)</text>
        <text x="65" y="98" fill="var(--tx-muted)" font-size="8" text-anchor="middle">SPOF of Star</text>
      </g>

      <!-- DEDICATED POINT-TO-POINT LINKS TO NODES -->
      <!-- Link 1 (Top Left) -->
      <line x1="200" y1="75" x2="385" y2="135" stroke="var(--accent)" stroke-width="2.2"/>
      <!-- Link 2 (Top Right) -->
      <line x1="700" y1="75" x2="515" y2="135" stroke="var(--accent)" stroke-width="2.2"/>
      <!-- Link 3 (Far Left) -->
      <line x1="150" y1="170" x2="385" y2="170" stroke="var(--accent)" stroke-width="2.2"/>
      <!-- Link 4 (Far Right) -->
      <line x1="750" y1="170" x2="515" y2="170" stroke="var(--accent)" stroke-width="2.2"/>
      <!-- Link 5 (Bottom Left) -->
      <line x1="200" y1="265" x2="385" y2="205" stroke="var(--accent)" stroke-width="2.2"/>
      <!-- Link 6 (Bottom Right) -->
      <line x1="700" y1="265" x2="515" y2="205" stroke="var(--accent)" stroke-width="2.2"/>

      <!-- NODE 1: Workstation A -->
      <g transform="translate(140, 45)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node 1 (Host)</text>
      </g>

      <!-- NODE 2: Server -->
      <g transform="translate(660, 45)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">🗄️</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Database Server</text>
      </g>

      <!-- NODE 3: Laptop -->
      <g transform="translate(50, 145)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node 3 (Host)</text>
      </g>

      <!-- NODE 4: Printer -->
      <g transform="translate(750, 145)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">🖨️</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Laser Printer</text>
      </g>

      <!-- NODE 5: Host C -->
      <g transform="translate(140, 240)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node 5 (Host)</text>
      </g>

      <!-- NODE 6: Host D -->
      <g transform="translate(660, 240)">
        <rect width="100" height="55" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="50" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="50" y="44" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Node 6 (Host)</text>
      </g>

      <!-- METRICS BANNER -->
      <rect x="30" y="305" width="840" height="28" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="450" y="323" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">
        <tspan fill="var(--accent)" font-weight="700">LINK FORMULA:</tspan> Exactly $N$ links for $N$ devices • <tspan fill="var(--success)" font-weight="700">FAULT ISOLATION:</tspan> One cable cut disables only that single device.
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Why Star Dominates Modern Enterprise:</strong> Unlike Bus or Ring topologies, a severed cable in a Star topology affects only the single connected endpoint. Troubleshooting is immediate at the switch port, and moving/adding nodes requires zero network downtime.
  </div>
</div>'''

# ==========================================
# 6. DIAGRAM 6: Ring Topology & Token Passing
# ==========================================
svg_diagram_6 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⭕</span>
      <span class="diagram-title">Figure 2.6: Ring Topology &amp; Dual Counter-Rotating Self-Healing Loop</span>
    </div>
    <span class="diagram-badge">DETERMINISTIC TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ring" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-ring2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--warning)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- PRIMARY RING (Clockwise) -->
      <circle cx="450" cy="170" r="110" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8,4"/>
      <path d="M 450 60 A 110 110 0 0 1 560 170" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-ring)"/>

      <!-- SECONDARY RING (Counter-Clockwise - FDDI Self-Healing) -->
      <circle cx="450" cy="170" r="130" fill="none" stroke="var(--warning)" stroke-width="2" stroke-dasharray="4,4"/>
      <path d="M 580 170 A 130 130 0 0 0 450 40" fill="none" stroke="var(--warning)" stroke-width="2" marker-end="url(#arrow-ring2)"/>

      <!-- CENTER LABEL: TOKEN CIRCULATION -->
      <circle cx="450" cy="170" r="45" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="450" y="162" fill="var(--accent-light)" font-size="11" font-weight="800" text-anchor="middle">TOKEN</text>
      <text x="450" y="178" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Circulating</text>
      <text x="450" y="190" fill="var(--tx-muted)" font-size="8" text-anchor="middle">(Deterministic)</text>

      <!-- NODE 1 (TOP) -->
      <g transform="translate(405, 15)">
        <rect width="90" height="50" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="45" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Station A</text>
      </g>

      <!-- NODE 2 (RIGHT) -->
      <g transform="translate(685, 145)">
        <rect width="90" height="50" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="45" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Station B</text>
      </g>

      <!-- NODE 3 (BOTTOM) -->
      <g transform="translate(405, 275)">
        <rect width="90" height="50" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="45" y="24" font-size="14" text-anchor="middle">🖨️</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Station C</text>
      </g>

      <!-- NODE 4 (LEFT) -->
      <g transform="translate(125, 145)">
        <rect width="90" height="50" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="45" y="24" font-size="14" text-anchor="middle">💻</text>
        <text x="45" y="42" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">Station D</text>
      </g>

      <!-- LEGEND -->
      <g transform="translate(30, 260)">
        <rect width="200" height="70" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <line x1="15" y1="25" x2="45" y2="25" stroke="var(--accent)" stroke-width="3"/>
        <text x="55" y="29" fill="var(--tx-primary)" font-size="10">Primary Ring (Active)</text>
        <line x1="15" y1="50" x2="45" y2="50" stroke="var(--warning)" stroke-width="2" stroke-dasharray="4,4"/>
        <text x="55" y="54" fill="var(--tx-primary)" font-size="10">Secondary Ring (FDDI Wrap)</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Token Ring &amp; Dual Counter-Rotating Loops:</strong> Stations transmit only upon capturing the circulating Token, guaranteeing bounded channel access latency (zero packet collisions). In high-reliability fiber rings (FDDI/SONET), if a cable cuts, the stations adjacent to the break loop the primary ring into the secondary ring, automatically self-healing the circle without dropping communication.
  </div>
</div>'''

# ==========================================
# 7. DIAGRAM 7: Full Mesh Topology
# ==========================================
svg_diagram_7 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🕸️</span>
      <span class="diagram-title">Figure 2.7: Full Mesh Topology — Complete Point-to-Point Redundancy ($n=5, L=10$)</span>
    </div>
    <span class="diagram-badge">HIGH-RELIABILITY TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="880" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- Node coordinates on pentagon (cx=350, cy=170, r=120) -->
      <!-- Node 1: (350, 50) -->
      <!-- Node 2: (464, 133) -->
      <!-- Node 3: (420, 267) -->
      <!-- Node 4: (280, 267) -->
      <!-- Node 5: (236, 133) -->

      <!-- ALL 10 DUPLEX LINKS (Full Mesh: n*(n-1)/2 = 5*4/2 = 10) -->
      <line x1="350" y1="50" x2="464" y2="133" stroke="var(--accent)" stroke-width="2"/>
      <line x1="350" y1="50" x2="420" y2="267" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
      <line x1="350" y1="50" x2="280" y2="267" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
      <line x1="350" y1="50" x2="236" y2="133" stroke="var(--accent)" stroke-width="2"/>
      <line x1="464" y1="133" x2="420" y2="267" stroke="var(--accent)" stroke-width="2"/>
      <line x1="464" y1="133" x2="280" y2="267" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
      <line x1="464" y1="133" x2="236" y2="133" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
      <line x1="420" y1="267" x2="280" y2="267" stroke="var(--accent)" stroke-width="2"/>
      <line x1="420" y1="267" x2="236" y2="133" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
      <line x1="280" y1="267" x2="236" y2="133" stroke="var(--accent)" stroke-width="2"/>

      <!-- 5 NODES -->
      <!-- Node 1 -->
      <circle cx="350" cy="50" r="28" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
      <text x="350" y="55" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">N1</text>

      <!-- Node 2 -->
      <circle cx="464" cy="133" r="28" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
      <text x="464" y="138" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">N2</text>

      <!-- Node 3 -->
      <circle cx="420" cy="267" r="28" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
      <text x="420" y="272" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">N3</text>

      <!-- Node 4 -->
      <circle cx="280" cy="267" r="28" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
      <text x="280" y="272" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">N4</text>

      <!-- Node 5 -->
      <circle cx="236" cy="133" r="28" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
      <text x="236" y="138" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">N5</text>

      <!-- RIGHT SIDE: MATHEMATICAL FORMULA CARD -->
      <g transform="translate(560, 40)">
        <rect width="300" height="260" rx="12" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <rect x="15" y="15" width="270" height="32" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
        <text x="150" y="36" fill="var(--accent-light)" font-size="13" font-weight="800" text-anchor="middle">FULL MESH EQUATIONS</text>

        <text x="25" y="75" fill="var(--tx-primary)" font-size="12" font-weight="700">1. Total Duplex Links ($L$):</text>
        <text x="45" y="100" fill="var(--accent)" font-family="var(--font-mono)" font-size="15" font-weight="800">L = n(n - 1) / 2</text>
        <text x="45" y="120" fill="var(--tx-muted)" font-size="10">For $n = 5$: $L = 5 \\times 4 / 2 = \\mathbf{10\\text{ links}}$</text>
        <text x="45" y="136" fill="var(--tx-muted)" font-size="10">For $n = 20$: $L = 20 \\times 19 / 2 = \\mathbf{190\\text{ links}}$</text>

        <line x1="20" y1="150" x2="280" y2="150" stroke="var(--border)" stroke-width="1"/>

        <text x="25" y="175" fill="var(--tx-primary)" font-size="12" font-weight="700">2. I/O Ports Required Per Device:</text>
        <text x="45" y="200" fill="var(--info)" font-family="var(--font-mono)" font-size="15" font-weight="800">Ports/Node = n - 1</text>
        <text x="45" y="220" fill="var(--tx-muted)" font-size="10">Each node needs 4 dedicated NIC ports ($n=5$)</text>

        <line x1="20" y1="230" x2="280" y2="230" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="248" fill="var(--success)" font-size="10" font-weight="700">✓ Complexity: O(n²) cabling explosion</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>University Exam Must-Know:</strong> Full Mesh offers the ultimate reliability: dedicated links guarantee zero traffic contention, privacy (no eavesdropping by other nodes), and robust fault isolation. However, due to quadratic cabling growth ($O(n^2)$), full mesh is reserved exclusively for nuclear facilities, core ISP backbones, and military systems.
  </div>
</div>'''

# ==========================================
# 8. DIAGRAM 8: Tree (3-Tier Enterprise Hierarchical Model)
# ==========================================
svg_diagram_8 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🌲</span>
      <span class="diagram-title">Figure 2.8: The 3-Tier Enterprise Hierarchical Model (Core ➔ Distribution ➔ Access)</span>
    </div>
    <span class="diagram-badge">ENTERPRISE DESIGN</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TIER 1: CORE LAYER -->
      <g transform="translate(30, 25)">
        <rect width="860" height="85" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="20" y="30" fill="var(--accent)" font-size="13" font-weight="800">TIER 1: CORE LAYER</text>
        <text x="20" y="46" fill="var(--tx-muted)" font-size="10">High-speed backbone switching • Zero packet inspection • Max throughput</text>
        
        <!-- Two Redundant Core Switches -->
        <g transform="translate(320, 15)">
          <rect width="100" height="55" rx="8" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="50" y="26" font-size="14" text-anchor="middle">⚡</text>
          <text x="50" y="44" fill="var(--accent-light)" font-size="11" font-weight="800" text-anchor="middle">CORE SW 1</text>
        </g>
        <g transform="translate(460, 15)">
          <rect width="100" height="55" rx="8" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="50" y="26" font-size="14" text-anchor="middle">⚡</text>
          <text x="50" y="44" fill="var(--accent-light)" font-size="11" font-weight="800" text-anchor="middle">CORE SW 2</text>
        </g>
        <!-- Inter-core Link -->
        <line x1="420" y1="42" x2="460" y2="42" stroke="var(--accent)" stroke-width="3"/>
      </g>

      <!-- LINKS: Core to Distribution (Redundant Cross Links) -->
      <line x1="370" y1="95" x2="230" y2="145" stroke="var(--info)" stroke-width="1.8"/>
      <line x1="370" y1="95" x2="690" y2="145" stroke="var(--info)" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="510" y1="95" x2="230" y2="145" stroke="var(--info)" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="510" y1="95" x2="690" y2="145" stroke="var(--info)" stroke-width="1.8"/>

      <!-- TIER 2: DISTRIBUTION LAYER -->
      <g transform="translate(30, 140)">
        <rect width="860" height="85" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="20" y="30" fill="var(--info)" font-size="13" font-weight="800">TIER 2: DISTRIBUTION LAYER</text>
        <text x="20" y="46" fill="var(--tx-muted)" font-size="10">Policy enforcement • Inter-VLAN routing • ACLs &amp; QoS boundaries</text>

        <!-- Distribution Switch West & East -->
        <g transform="translate(180, 15)">
          <rect width="110" height="55" rx="8" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="55" y="26" font-size="14" text-anchor="middle">🛡️</text>
          <text x="55" y="44" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">DIST SW (West)</text>
        </g>
        <g transform="translate(630, 15)">
          <rect width="110" height="55" rx="8" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="55" y="26" font-size="14" text-anchor="middle">🛡️</text>
          <text x="55" y="44" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">DIST SW (East)</text>
        </g>
      </g>

      <!-- LINKS: Distribution to Access -->
      <line x1="235" y1="210" x2="135" y2="255" stroke="var(--success)" stroke-width="1.8"/>
      <line x1="235" y1="210" x2="335" y2="255" stroke="var(--success)" stroke-width="1.8"/>
      <line x1="685" y1="210" x2="585" y2="255" stroke="var(--success)" stroke-width="1.8"/>
      <line x1="685" y1="210" x2="785" y2="255" stroke="var(--success)" stroke-width="1.8"/>

      <!-- TIER 3: ACCESS LAYER -->
      <g transform="translate(30, 250)">
        <rect width="860" height="90" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="20" y="28" fill="var(--success)" font-size="13" font-weight="800">TIER 3: ACCESS LAYER</text>
        <text x="20" y="44" fill="var(--tx-muted)" font-size="10">Endpoint connectivity • Port security • PoE for VoIP/APs</text>

        <!-- Access Switches & Endpoints -->
        <g transform="translate(90, 15)">
          <rect width="90" height="55" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="45" y="24" font-size="12" text-anchor="middle">🔌</text>
          <text x="45" y="40" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Access SW 1</text>
          <text x="45" y="50" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Desktops</text>
        </g>
        <g transform="translate(290, 15)">
          <rect width="90" height="55" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="45" y="24" font-size="12" text-anchor="middle">📶</text>
          <text x="45" y="40" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Access SW 2</text>
          <text x="45" y="50" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Wi-Fi APs</text>
        </g>
        <g transform="translate(540, 15)">
          <rect width="90" height="55" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="45" y="24" font-size="12" text-anchor="middle">📞</text>
          <text x="45" y="40" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Access SW 3</text>
          <text x="45" y="50" fill="var(--tx-muted)" font-size="8" text-anchor="middle">IP Phones</text>
        </g>
        <g transform="translate(740, 15)">
          <rect width="90" height="55" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="45" y="24" font-size="12" text-anchor="middle">📹</text>
          <text x="45" y="40" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Access SW 4</text>
          <text x="45" y="50" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Security Cams</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Cisco 3-Tier Rule of Thumb:</strong> <em>Core Layer</em> must be optimized strictly for raw forwarding speed and high availability (no packet filtering or CPU overhead). All complex routing policies, VLAN boundaries, and security firewalls are delegated to the <em>Distribution Layer</em>.
  </div>
</div>'''

# ==========================================
# 9. DIAGRAM 9: Hybrid Topology (Star-Mesh Backbone)
# ==========================================
svg_diagram_9 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧬</span>
      <span class="diagram-title">Figure 2.9: Hybrid Topology — Star Access Edge with Partial Mesh Core Backbone</span>
    </div>
    <span class="diagram-badge">MODERN ENTERPRISE HYBRID</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="880" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- CENTRAL PARTIAL MESH CORE -->
      <g transform="translate(310, 40)">
        <rect width="280" height="170" rx="12" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="6,3"/>
        <text x="140" y="25" fill="var(--accent-light)" font-size="12" font-weight="800" text-anchor="middle">MESH BACKBONE CORE</text>

        <!-- 3 Core Switches in Triangle -->
        <circle cx="140" cy="55" r="22" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="140" y="59" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">R1</text>

        <circle cx="70" cy="125" r="22" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="70" y="129" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">R2</text>

        <circle cx="210" cy="125" r="22" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="210" y="129" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">R3</text>

        <!-- Mesh Triangles -->
        <line x1="140" y1="55" x2="70" y2="125" stroke="var(--accent)" stroke-width="2.5"/>
        <line x1="140" y1="55" x2="210" y2="125" stroke="var(--accent)" stroke-width="2.5"/>
        <line x1="70" y1="125" x2="210" y2="125" stroke="var(--accent)" stroke-width="2.5"/>
      </g>

      <!-- STAR NETWORK WEST (Dept A) -->
      <g transform="translate(30, 40)">
        <rect width="240" height="230" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="120" y="24" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">STAR EDGE: HR DEPARTMENT</text>

        <!-- Dept Switch -->
        <rect x="85" y="45" width="70" height="40" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="120" y="69" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Switch A</text>

        <!-- Star Spoke Links -->
        <line x1="120" y1="85" x2="55" y2="140" stroke="var(--info)" stroke-width="1.5"/>
        <line x1="120" y1="85" x2="120" y2="140" stroke="var(--info)" stroke-width="1.5"/>
        <line x1="120" y1="85" x2="185" y2="140" stroke="var(--info)" stroke-width="1.5"/>

        <!-- Spoke Nodes -->
        <rect x="35" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="55" y="159" font-size="11" text-anchor="middle">💻</text>
        <rect x="100" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="120" y="159" font-size="11" text-anchor="middle">💻</text>
        <rect x="165" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="185" y="159" font-size="11" text-anchor="middle">🖨️</text>

        <text x="120" y="205" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Local Star Connectivity</text>
      </g>

      <!-- STAR NETWORK EAST (Dept B) -->
      <g transform="translate(630, 40)">
        <rect width="240" height="230" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="120" y="24" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">STAR EDGE: ENGINEERING</text>

        <!-- Dept Switch -->
        <rect x="85" y="45" width="70" height="40" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="120" y="69" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Switch B</text>

        <!-- Star Spoke Links -->
        <line x1="120" y1="85" x2="55" y2="140" stroke="var(--success)" stroke-width="1.5"/>
        <line x1="120" y1="85" x2="120" y2="140" stroke="var(--success)" stroke-width="1.5"/>
        <line x1="120" y1="85" x2="185" y2="140" stroke="var(--success)" stroke-width="1.5"/>

        <!-- Spoke Nodes -->
        <rect x="35" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="55" y="159" font-size="11" text-anchor="middle">💻</text>
        <rect x="100" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="120" y="159" font-size="11" text-anchor="middle">💻</text>
        <rect x="165" y="140" width="40" height="30" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="185" y="159" font-size="11" text-anchor="middle">🗄️</text>

        <text x="120" y="205" fill="var(--tx-muted)" font-size="9" text-anchor="middle">High-Bandwidth Gigabit Edge</text>
      </g>

      <!-- Connecting Links from Department Switches to Mesh Core -->
      <line x1="190" y1="105" x2="380" y2="165" stroke="var(--accent)" stroke-width="3"/>
      <line x1="710" y1="105" x2="520" y2="165" stroke="var(--accent)" stroke-width="3"/>

      <!-- BOTTOM SUMMARY -->
      <rect x="30" y="285" width="840" height="30" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="450" y="305" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">
        Hybrid architecture merges the cost-effectiveness and easy cable management of Star at the edge with the fault-tolerant multipath routing of Mesh at the core.
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Real-World Synergy:</strong> In modern corporate campuses, no single pure topology satisfies all operational needs. Star topology handles local desktop wiring affordably, while Mesh provides carrier-grade redundant failover between data centers and core distribution routers.
  </div>
</div>'''

# ==========================================
# 10. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 2
# ==========================================
ch2_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Network Topologies Comprehensive Analysis, Mathematical Formulas &amp; Design Trade-offs</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define Network Topology. Distinguish between Physical Topology and Logical Topology with suitable examples. [2 Marks]<br>
          (b) Compare Bus, Star, Ring, and Full Mesh topologies across six critical metrics: Number of physical links, Hardware failure impact, Cable length required, Installation complexity, Troubleshooting ease, and Bottleneck risk. [4 Marks]<br>
          (c) An organization is planning an internal network with $N = 16$ computers. Calculate the exact number of full-duplex communication links and hardware I/O ports required if the network is implemented as: (i) Full Mesh Topology, and (ii) Star Topology. Explain why Star is chosen in commercial office installations despite the theoretical fault-tolerance advantage of Full Mesh. [4 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Definition &amp; Physical vs. Logical Topology</h4>
          <p><strong>Definition:</strong> The topology of a network defines the geometric arrangement or schematic map according to which physical nodes (computers, printers, switches) are interconnected via transmission media.</p>
          <p><strong>Physical vs. Logical Topology:</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Physical Topology:</strong> The actual physical cable layout, device positions, and spatial wiring configuration (e.g., Cat6 cables running from wall jacks to a central wiring closet in a physical star).</li>
            <li><strong>Logical Topology:</strong> The method and path by which data signals actually travel between nodes across the physical layout. <em>Classic Exam Example:</em> 10BASE-T Ethernet is wired as a <strong>Physical Star</strong> (all cables plug into a central hub), but operates as a <strong>Logical Bus</strong> (electrical signals broadcast across the shared backplane to all nodes, sharing one collision domain). Similarly, Token Ring uses a physical star (MSAU wiring hub) but operates as a logical ring.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Topologies Comparative Master Matrix</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Evaluation Metric</th>
                <th>Bus Topology</th>
                <th>Star Topology</th>
                <th>Ring Topology</th>
                <th>Full Mesh Topology</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Number of Links ($N$ nodes)</strong></td>
                <td>$1$ shared trunk + $N$ drops</td>
                <td>$N$ dedicated links</td>
                <td>$N$ dedicated ring links</td>
                <td>$\\frac{N(N-1)}{2}$ dedicated links</td>
              </tr>
              <tr>
                <td><strong>Cable Cut Failure Impact</strong></td>
                <td>Catastrophic (Whole network fails)</td>
                <td>Isolated (Only cut node fails)</td>
                <td>High (Breaks token loop)</td>
                <td>Zero (Alternate routes exist)</td>
              </tr>
              <tr>
                <td><strong>Single Point of Failure (SPOF)</strong></td>
                <td>Backbone trunk &amp; terminators</td>
                <td>Central Switch / Hub</td>
                <td>Any un-bypassed repeater</td>
                <td>None (Completely decentralized)</td>
              </tr>
              <tr>
                <td><strong>Installation &amp; Cabling Cost</strong></td>
                <td>Lowest</td>
                <td>Moderate</td>
                <td>Moderate</td>
                <td>Extremely High ($O(N^2)$)</td>
              </tr>
              <tr>
                <td><strong>Troubleshooting Ease</strong></td>
                <td>Very Difficult (TDR needed)</td>
                <td>Very Easy (Port indicator LEDs)</td>
                <td>Moderate</td>
                <td>Complex due to cable mass</td>
              </tr>
              <tr>
                <td><strong>Channel Collision Risk</strong></td>
                <td>High (Shared medium CSMA/CD)</td>
                <td>Zero (Full-duplex switch)</td>
                <td>Zero (Deterministic Token)</td>
                <td>Zero (Dedicated point-to-point)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Mathematical Numerical &amp; Commercial Justification</h4>
          <p><strong>Given:</strong> Number of nodes $N = 16$.</p>
          
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin: 8px 0 14px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>(i) Full Mesh Topology:</strong><br>
              • Total Duplex Links: $$L_{\\text{mesh}} = \\frac{N(N-1)}{2} = \\frac{16 \\times 15}{2} = \\mathbf{120\\text{ duplex cables}}$$<br>
              • Ports Per Node: $$P_{\\text{node}} = N - 1 = 16 - 1 = \\mathbf{15\\text{ ports per computer}}$$<br>
              • Total System Ports: $$P_{\\text{total}} = N \\times (N-1) = 16 \\times 15 = \\mathbf{240\\text{ NIC ports}}$$<br><br>
              <strong>(ii) Star Topology (with Central Switch):</strong><br>
              • Total Duplex Links: $$L_{\\text{star}} = N = \\mathbf{16\\text{ duplex cables}}$$<br>
              • Ports Per Node: $$\\mathbf{1\\text{ NIC port per computer}}$$<br>
              • Switch Ports Required: $$\\mathbf{16\\text{ switch ports (1 standard 24-port switch)}}$$
            </p>
          </div>

          <p><strong>Why Star is Universally Chosen in Commercial Offices:</strong></p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Economic Feasibility:</strong> Star requires only 16 cables vs 120 cables for mesh. Standard PCs come with only 1 Ethernet port; outfitting each PC with 15 PCIe network cards is prohibitively expensive and physically impractical.</li>
            <li><strong>Maintenance &amp; Scalability:</strong> Adding a 17th node to a star network requires plugging 1 cable into the switch. Adding a 17th node to a full mesh requires running 16 new physical cables across walls and installing a new NIC port in all 16 existing machines ($O(N)$ operational disruption).</li>
            <li><strong>Mitigating the Star SPOF:</strong> Enterprise deployments eliminate the central switch SPOF by deploying dual redundant switches with Virtual Router Redundancy Protocol (VRRP) and link aggregation (LACP), achieving $99.999\%$ reliability at a tiny fraction of mesh cabling cost.</li>
          </ol>
        </div>
      </div>
    </div>
'''

# ==========================================
# SCRIPT TO EXECUTE REPLACEMENTS IN CHAPTER 2
# ==========================================
# We have 9 code blocks in Chapter 2.
# Let's cleanly replace the <div class="code-block">...<pre><code>...</code></pre></div> blocks with SVGs.

replacements = [
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">The Complete 4-Axis Network Classification</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_1),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Logical Access Perimeter Architecture</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_2),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Client-Server vs\. Peer-to-Peer Topology</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_3),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Bus Topology: Backbone, Taps, and Terminators</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_4),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Star Topology: Central Switch / Hub with Dedicated Links</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_5),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Ring Topology &amp; Token Circulation</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_6),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Full Mesh Topology.*?</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_7),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">The 3-Tier Hierarchical Enterprise Model</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_8),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Hybrid Architecture: Star Access \+ Mesh Backbone</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_9),
]

for pattern, repl in replacements:
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + repl + content[match.end():]
        print(f'Successfully replaced pattern: {pattern[:40]}...')
    else:
        print(f'FAILED to match pattern: {pattern[:40]}...')

# Insert 10-Mark Blueprint into Chapter 2 before the final references section in s-topology-compare
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch2_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 2!')

with open(ch2_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 2 upgrade script completed!')
