"""
Upgrade Chapter 18 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch18_path = '/Users/arpit/minibook/cn/chapters/ch18-routers-switches-firewalls.html'
with open(ch18_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Collision vs Broadcast Domains Across Devices (Figure 18.1)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🛡️</span>
      <span class="diagram-title">Figure 18.1: Collision Domain vs. Broadcast Domain Boundaries Across Device Classes</span>
    </div>
    <span class="diagram-badge">DOMAIN BOUNDARIES</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TIER 1: L1 HUB -->
      <g transform="translate(30, 25)">
        <rect width="275" height="280" rx="8" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.8"/>
        <rect x="15" y="15" width="245" height="32" rx="4" fill="var(--danger-dim)" stroke="none"/>
        <text x="137" y="36" fill="var(--danger)" font-size="12" font-weight="900" text-anchor="middle">LAYER-1 HUB / REPEATER</text>

        <!-- Graphic -->
        <g transform="translate(25, 60)">
          <rect width="225" height="110" rx="6" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5" stroke-dasharray="4 2"/>
          <text x="112" y="24" fill="var(--danger)" font-size="10" font-weight="900" text-anchor="middle">SINGLE SHARED COLLISION DOMAIN</text>
          <circle cx="50" cy="65" r="16" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="50" y="70" fill="var(--tx-primary)" font-size="9" font-weight="800" text-anchor="middle">PC1</text>

          <rect x="90" y="50" width="45" height="30" rx="4" fill="var(--danger)" stroke="none"/>
          <text x="112" y="69" fill="#fff" font-size="10" font-weight="900" text-anchor="middle">HUB</text>

          <circle cx="175" cy="65" r="16" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="175" y="70" fill="var(--tx-primary)" font-size="9" font-weight="800" text-anchor="middle">PC2</text>
        </g>

        <!-- Stats -->
        <g transform="translate(20, 190)">
          <text x="0" y="20" fill="var(--danger)" font-size="10.5" font-weight="800">Collision Domains: 1 (All ports shared)</text>
          <text x="0" y="40" fill="var(--danger)" font-size="10.5" font-weight="800">Broadcast Domains: 1 (Floods all)</text>
          <text x="0" y="60" fill="var(--tx-muted)" font-size="9">Half-duplex only; CSMA/CD mandatory.</text>
        </g>
      </g>

      <!-- TIER 2: L2 SWITCH -->
      <g transform="translate(330, 25)">
        <rect width="280" height="280" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="15" y="15" width="250" height="32" rx="4" fill="var(--warning-dim)" stroke="none"/>
        <text x="140" y="36" fill="var(--warning)" font-size="12" font-weight="900" text-anchor="middle">LAYER-2 SWITCH / BRIDGE</text>

        <!-- Graphic -->
        <g transform="translate(25, 60)">
          <rect width="230" height="110" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5" stroke-dasharray="4 2"/>
          <text x="115" y="24" fill="var(--warning)" font-size="10" font-weight="900" text-anchor="middle">1 BROADCAST DOMAIN</text>

          <rect x="20" y="45" width="55" height="40" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="47" y="62" fill="var(--success)" font-size="8" font-weight="800" text-anchor="middle">CD 1</text>
          <text x="47" y="76" fill="var(--tx-primary)" font-size="8" font-weight="700" text-anchor="middle">Port 1</text>

          <rect x="88" y="50" width="54" height="30" rx="4" fill="var(--warning)" stroke="none"/>
          <text x="115" y="69" fill="#000" font-size="9" font-weight="900" text-anchor="middle">SWITCH</text>

          <rect x="155" y="45" width="55" height="40" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="182" y="62" fill="var(--success)" font-size="8" font-weight="800" text-anchor="middle">CD 2</text>
          <text x="182" y="76" fill="var(--tx-primary)" font-size="8" font-weight="700" text-anchor="middle">Port 2</text>
        </g>

        <!-- Stats -->
        <g transform="translate(20, 190)">
          <text x="0" y="20" fill="var(--success)" font-size="10.5" font-weight="800">Collision Domains: N (1 per port)</text>
          <text x="0" y="40" fill="var(--danger)" font-size="10.5" font-weight="800">Broadcast Domains: 1 (Floods FF..FF)</text>
          <text x="0" y="60" fill="var(--tx-muted)" font-size="9">Full-duplex dedicated bandwidth per port.</text>
        </g>
      </g>

      <!-- TIER 3: L3 ROUTER -->
      <g transform="translate(635, 25)">
        <rect width="275" height="280" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <rect x="15" y="15" width="245" height="32" rx="4" fill="var(--success-dim)" stroke="none"/>
        <text x="137" y="36" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">LAYER-3 ROUTER</text>

        <!-- Graphic -->
        <g transform="translate(25, 60)">
          <rect width="105" height="110" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.2"/>
          <text x="52" y="24" fill="var(--success)" font-size="8.5" font-weight="900" text-anchor="middle">BD 1 (Subnet 1)</text>

          <circle cx="112" cy="70" r="22" fill="var(--info)" stroke="none"/>
          <text x="112" y="74" fill="#fff" font-size="10" font-weight="900" text-anchor="middle">RTR</text>

          <rect x="120" y="0" width="105" height="110" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="172" y="24" fill="var(--info)" font-size="8.5" font-weight="900" text-anchor="middle">BD 2 (Subnet 2)</text>
        </g>

        <!-- Stats -->
        <g transform="translate(20, 190)">
          <text x="0" y="20" fill="var(--success)" font-size="10.5" font-weight="800">Collision Domains: N (1 per port)</text>
          <text x="0" y="40" fill="var(--success)" font-size="10.5" font-weight="800">Broadcast Domains: N (1 per subnet)</text>
          <text x="0" y="60" fill="var(--tx-muted)" font-size="9">Stops Layer-2 broadcasts cold; connects nets.</text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Router-on-a-Stick vs L3 Switch SVI (Figure 18.8)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚡</span>
      <span class="diagram-title">Figure 18.8: Inter-VLAN Routing Architecture — Router-on-a-Stick vs. Layer-3 Switch SVI</span>
    </div>
    <span class="diagram-badge">INTER-VLAN ROUTING</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-roas" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
        <marker id="arr-svi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: ROUTER-ON-A-STICK -->
      <g transform="translate(30, 25)">
        <rect width="420" height="270" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="210" y="28" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">
          1. ROUTER-ON-A-STICK (Legacy 802.1Q Single Trunk)
        </text>

        <!-- Router at Top -->
        <circle cx="210" cy="70" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="210" y="74" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Router</text>
        <text x="210" y="100" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Subinterfaces .10 &amp; .20</text>

        <!-- Hairpin Trunk Arrows -->
        <path d="M 195 140 L 195 95" stroke="var(--danger)" stroke-width="2" marker-end="url(#arr-roas)"/>
        <path d="M 225 95 L 225 140" stroke="var(--danger)" stroke-width="2" marker-end="url(#arr-roas)"/>
        <text x="270" y="120" fill="var(--danger)" font-size="9" font-weight="800">Hairpin Pin</text>

        <!-- L2 Switch in Middle -->
        <rect x="150" y="145" width="120" height="34" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="210" y="166" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">L2 Switch</text>

        <!-- VLAN 10 and VLAN 20 hosts -->
        <circle cx="90" cy="225" r="18" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="90" y="229" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">VLAN 10</text>

        <circle cx="330" cy="225" r="18" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="330" y="229" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">VLAN 20</text>

        <line x1="105" y1="215" x2="165" y2="179" stroke="var(--border)" stroke-width="1.5"/>
        <line x1="315" y1="215" x2="255" y2="179" stroke="var(--border)" stroke-width="1.5"/>

        <text x="210" y="260" fill="var(--danger)" font-size="9" font-weight="800" text-anchor="middle">
          Bottleneck: Traffic traverses trunk link twice (In + Out)
        </text>
      </g>

      <!-- RIGHT: MULTILAYER LAYER-3 SWITCH (SVI) -->
      <g transform="translate(485, 25)">
        <rect width="425" height="270" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="212" y="28" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">
          2. MULTILAYER SWITCH (Switch Virtual Interfaces - SVI)
        </text>

        <!-- L3 Switch Chassis -->
        <g transform="translate(50, 55)">
          <rect width="325" height="125" rx="8" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
          <text x="162" y="24" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">
            Layer-3 Core Switch Chassis (Hardware Routing Engine)
          </text>

          <!-- Internal SVIs -->
          <rect x="25" y="40" width="125" height="40" rx="4" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="87" y="57" fill="var(--info)" font-size="9.5" font-weight="800" text-anchor="middle">SVI Interface</text>
          <text x="87" y="71" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">VLAN 10 (192.168.10.1)</text>

          <rect x="175" y="40" width="125" height="40" rx="4" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.2"/>
          <text x="237" y="57" fill="var(--warning)" font-size="9.5" font-weight="800" text-anchor="middle">SVI Interface</text>
          <text x="237" y="71" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">VLAN 20 (192.168.20.1)</text>

          <!-- Hardware Backplane Arrow -->
          <path d="M 152 60 L 172 60" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-svi)"/>
          <text x="162" y="100" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">
            Internal Wire-Speed ASIC Routing (Tbps)
          </text>
        </g>

        <!-- Hosts -->
        <circle cx="140" cy="225" r="18" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="140" y="229" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">VLAN 10</text>

        <circle cx="285" cy="225" r="18" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="285" y="229" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">VLAN 20</text>

        <line x1="140" y1="207" x2="140" y2="180" stroke="var(--border)" stroke-width="1.5"/>
        <line x1="285" y1="207" x2="285" y2="180" stroke="var(--border)" stroke-width="1.5"/>

        <text x="212" y="260" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">
          Zero Bottleneck: Packets never leave chassis; routed at full port speed!
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Enterprise 3-Legged DMZ Firewall (Figure 18.10)
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧱</span>
      <span class="diagram-title">Figure 18.10: Enterprise Three-Legged Firewall DMZ Security Perimeter</span>
    </div>
    <span class="diagram-badge">DMZ ARCHITECTURE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-fw-pass" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
        <marker id="arr-fw-drop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- CENTRAL THREE-LEGGED FIREWALL -->
      <g transform="translate(380, 100)">
        <rect width="180" height="120" rx="10" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="2.5"/>
        <rect x="10" y="10" width="160" height="28" rx="4" fill="var(--danger-dim)" stroke="none"/>
        <text x="90" y="28" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">ENTERPRISE FIREWALL</text>
        <text x="90" y="55" fill="var(--tx-primary)" font-size="9.5" font-weight="800" text-anchor="middle">Stateful Inspection</text>
        <text x="90" y="72" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Deep Packet Inspection</text>
        <text x="90" y="90" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Default Rule: DENY ALL</text>
      </g>

      <!-- ZONE 1: UNTRUSTED OUTSIDE / INTERNET (LEFT) -->
      <g transform="translate(30, 100)">
        <rect width="240" height="120" rx="8" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="120" y="28" fill="var(--danger)" font-size="12" font-weight="900" text-anchor="middle">OUTSIDE / WAN</text>
        <text x="120" y="46" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Untrusted Public Internet</text>
        <text x="120" y="70" fill="var(--tx-primary)" font-size="9.5" font-weight="700" text-anchor="middle">Security Level: 0</text>
        <text x="120" y="92" fill="var(--danger)" font-size="8.5" font-weight="800" text-anchor="middle">Attacker &amp; Client Sources</text>
      </g>

      <!-- Connection Outside <-> Firewall -->
      <line x1="270" y1="160" x2="380" y2="160" stroke="var(--border)" stroke-width="3"/>

      <!-- ZONE 2: DMZ (TOP CENTER) -->
      <g transform="translate(350, 25)">
        <rect width="240" height="60" rx="8" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="120" y="24" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">DMZ (DEMILITARIZED ZONE)</text>
        <text x="120" y="42" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Web (80/443), DNS, Mail • Security Level: 50</text>
      </g>
      <line x1="470" y1="85" x2="470" y2="100" stroke="var(--border)" stroke-width="3"/>

      <!-- ZONE 3: TRUSTED INSIDE / CORPORATE LAN (RIGHT) -->
      <g transform="translate(670, 100)">
        <rect width="240" height="120" rx="8" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="120" y="28" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">INSIDE / LAN</text>
        <text x="120" y="46" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Trusted Corporate Intranet</text>
        <text x="120" y="70" fill="var(--tx-primary)" font-size="9.5" font-weight="700" text-anchor="middle">Security Level: 100</text>
        <text x="120" y="92" fill="var(--success)" font-size="8.5" font-weight="800" text-anchor="middle">Databases, HR, Employees</text>
      </g>
      <line x1="560" y1="160" x2="670" y2="160" stroke="var(--border)" stroke-width="3"/>

      <!-- TRAFFIC POLICIES BANNER AT BOTTOM -->
      <g transform="translate(30, 235)">
        <rect width="880" height="70" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="22" fill="var(--tx-primary)" font-size="10.5" font-weight="900">Three-Legged Security Rules:</text>
        <text x="25" y="42" fill="var(--success)" font-size="9.5" font-weight="800">
          ✓ Inside ➔ Outside: PERMIT ALL (Users browse web) &nbsp;•&nbsp; ✓ Inside ➔ DMZ: PERMIT (Admins manage servers)
        </text>
        <text x="25" y="58" fill="var(--danger)" font-size="9.5" font-weight="800">
          ✓ Outside ➔ DMZ: PERMIT HTTP/HTTPS only &nbsp;•&nbsp; ✗ DMZ ➔ Inside: STRICTLY DENIED (Compromised server cannot attack LAN!)
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch18_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch18">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">Multi-Layer Devices, Inter-VLAN Routing &amp; Firewalls</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Device Comparison, SVI Inter-VLAN Forwarding, &amp; Stateful Firewalls</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Compare Hubs, Switches, and Routers across OSI layers, collision domains, and broadcast domains. Explain how a Layer-3 Multilayer Switch routes between VLAN 10 and VLAN 20 using Switch Virtual Interfaces (SVIs). Differentiate between Stateless Packet Filtering and Stateful Packet Inspection (SPI) firewalls, detailing the state table tracking mechanism."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: MASTER DEVICE TAXONOMY -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Master Multi-Device Comparison Matrix (3 Marks)</h4>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Device Type</th>
                  <th>Primary OSI Layer</th>
                  <th>Forwarding Data Unit</th>
                  <th>Collision Domains</th>
                  <th>Broadcast Domains</th>
                  <th>Hardware Forwarding Engine</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Repeater / Hub</strong></td>
                  <td>Layer 1 (Physical)</td>
                  <td>Raw Electrical Bits</td>
                  <td><strong>1 (Shared)</strong></td>
                  <td><strong>1 (All ports)</strong></td>
                  <td>Analog line receiver &amp; retransmitter</td>
                </tr>
                <tr>
                  <td><strong>Bridge / L2 Switch</strong></td>
                  <td>Layer 2 (Data Link)</td>
                  <td>Ethernet Frames</td>
                  <td><strong>$N$ (1 per port)</strong></td>
                  <td><strong>1 (Single VLAN)</strong></td>
                  <td>Content Addressable Memory (CAM) table</td>
                </tr>
                <tr>
                  <td><strong>L3 Router</strong></td>
                  <td>Layer 3 (Network)</td>
                  <td>IP Datagrams</td>
                  <td><strong>$N$ (1 per port)</strong></td>
                  <td><strong>$N$ (1 per subnet)</strong></td>
                  <td>FIB / TCAM Longest Prefix Match</td>
                </tr>
                <tr>
                  <td><strong>Stateful Firewall</strong></td>
                  <td>Layers 3 through 7</td>
                  <td>Packets &amp; Sessions</td>
                  <td>$N$</td>
                  <td>$N$</td>
                  <td>State table session connection tracker</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 2: INTER-VLAN ROUTING VIA SVI -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Inter-VLAN Routing: Switch Virtual Interfaces (SVI) (4 Marks)</h4>
          <p>
            When Host A (VLAN 10, IP <code>192.168.10.5</code>) transmits to Host B (VLAN 20, IP <code>192.168.20.8</code>):
          </p>
          <ul class="blueprint-list">
            <li><strong>L2 Isolation:</strong> Because Host A and B belong to distinct broadcast domains, Layer-2 switching logic drops direct frame delivery. Host A forwards the frame to its default gateway: <strong>SVI 10 (192.168.10.1)</strong>.</li>
            <li><strong>Chassis SVI Decapsulation:</strong> The frame enters access port 1 on VLAN 10. The switch recognizes destination MAC as SVI 10's MAC. The frame is stripped of its L2 Ethernet header and passed to the internal L3 routing engine.</li>
            <li><strong>Hardware TCAM Route Lookup:</strong> The switch matches destination IP <code>192.168.20.8</code> against its hardware FIB. It determines destination resides on directly connected <strong>SVI 20 (192.168.20.1)</strong>.</li>
            <li><strong>Re-encapsulation &amp; Wire-Speed Egress:</strong> The routing engine decrements TTL, recomputes checksum, and queries its ARP table for Host B's MAC. It encapsulates the packet in a new Ethernet frame (Src MAC = SVI 20 MAC, Dst MAC = Host B MAC) and outputs it on access port 2 (VLAN 20).</li>
          </ul>
        </div>

        <!-- SECTION 3: STATELESS VS STATEFUL FIREWALLS -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Stateless Packet Filter vs. Stateful Packet Inspection (SPI) (3 Marks)</h4>
          <div class="blueprint-grid">
            <div class="blueprint-col">
              <h5>Stateless Packet Filtering (ACLs)</h5>
              <ul>
                <li>Inspects each packet in complete isolation without memory of prior communications.</li>
                <li>Evaluates only static 5-tuple header fields: Source IP, Dest IP, Source Port, Dest Port, Protocol.</li>
                <li><strong>Fatal Flaw:</strong> To allow return web traffic from the Internet, the admin must open all ports above $1023$, creating huge security vulnerabilities!</li>
              </ul>
            </div>
            <div class="blueprint-col">
              <h5>Stateful Packet Inspection (SPI)</h5>
              <ul>
                <li>Maintains a dynamic <strong>State Connection Table</strong> in memory tracking TCP 3-way handshakes (SYN, SYN-ACK, ACK, FIN) and sequence numbers.</li>
                <li>When an internal client initiates an outbound connection, a state entry is generated.</li>
                <li><strong>Dynamic Return Filtering:</strong> Inbound packets are automatically allowed <em>only</em> if they correspond to an active, established outgoing connection in the state table. Unsolicited inbound attacks are dropped immediately!</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- TRAPS & MARKING SCHEME -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap:</strong>
            Never claim that <em>"Switches separate broadcast domains."</em> A standard Layer-2 switch <strong>extends</strong> a single broadcast domain across all its ports. Broadcast domains are strictly segmented either by <strong>VLANs</strong> or by <strong>Layer-3 Routers</strong>!
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 18
# ==========================================

# 1. Replace Figure 18.1 in s18-1
match_s18_f1 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 18\.1.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s18_f1:
    content = content[:match_s18_f1.start()] + svg_diagram_1 + content[match_s18_f1.end():]
    print('Replaced Figure 18.1 with responsive SVG Diagram 1')
else:
    print('Warning: could not find Figure 18.1')

# 2. Replace Figure 18.8 in s18-8
match_s18_f8 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 18\.8.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s18_f8:
    content = content[:match_s18_f8.start()] + svg_diagram_2 + content[match_s18_f8.end():]
    print('Replaced Figure 18.8 with responsive SVG Diagram 2')
else:
    print('Warning: could not find Figure 18.8')

# 3. Replace Figure 18.10 in s18-10
match_s18_f10 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 18\.10.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s18_f10:
    content = content[:match_s18_f10.start()] + svg_diagram_3 + content[match_s18_f10.end():]
    print('Replaced Figure 18.10 with responsive SVG Diagram 3')
else:
    print('Warning: could not find Figure 18.10')

# 4. Insert DU 10-Mark Blueprint before study-resources or in s18-18
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch18_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 18!')
else:
    # Append before </main>
    main_target = re.search(r'</section>\s*</main>', content)
    if main_target:
        content = content[:main_target.start()] + '</section>\n\n' + ch18_uni_blueprint + '\n</main>' + content[main_target.end():]
        print('Inserted 10-Mark University Blueprint before </main> in Chapter 18!')
    else:
        print('Warning: could not find insertion spot for Blueprint in Chapter 18')

with open(ch18_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 18 upgrade completed!')
