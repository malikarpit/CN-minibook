"""
Upgrade Chapter 17 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch17_path = '/Users/arpit/minibook/cn/chapters/ch17-address-mapping-icmp.html'
with open(ch17_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: RFC 826 ARP Header Layout (Figure 17.2)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📋</span>
      <span class="diagram-title">Figure 17.2: Detailed RFC 826 ARP Packet Header Layout (28 Bytes / 16-Bit Word Grid)</span>
    </div>
    <span class="diagram-badge">ARP PACKET</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- BIT SCALE -->
      <g transform="translate(30, 25)">
        <rect width="880" height="24" rx="4" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="15" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">Bit: 0</text>
        <text x="220" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">8</text>
        <text x="440" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">16</text>
        <text x="660" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">24</text>
        <text x="860" y="16" fill="var(--tx-muted)" font-size="9" font-family="monospace">31</text>
      </g>

      <!-- ROW 1: HARDWARE TYPE & PROTOCOL TYPE (BYTES 0-3) -->
      <g transform="translate(30, 55)">
        <rect x="0" y="0" width="435" height="45" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="217" y="20" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Hardware Type (HTYPE: 16 bits)</text>
        <text x="217" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">1 = Ethernet (10/100/1000 Mbps)</text>

        <rect x="445" y="0" width="435" height="45" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="662" y="20" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">Protocol Type (PTYPE: 16 bits)</text>
        <text x="662" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">0x0800 = IPv4 Logical Addressing</text>
      </g>

      <!-- ROW 2: HLEN, PLEN, OPCODE (BYTES 4-7) -->
      <g transform="translate(30, 106)">
        <rect x="0" y="0" width="215" height="45" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="107" y="20" fill="var(--warning)" font-size="10.5" font-weight="900" text-anchor="middle">Hardware Len (HLEN: 8b)</text>
        <text x="107" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">6 (Ethernet MAC = 6 Bytes)</text>

        <rect x="220" y="0" width="215" height="45" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="327" y="20" fill="var(--warning)" font-size="10.5" font-weight="900" text-anchor="middle">Protocol Len (PLEN: 8b)</text>
        <text x="327" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">4 (IPv4 = 4 Bytes)</text>

        <rect x="445" y="0" width="435" height="45" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="662" y="20" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">Operation Code (OPER: 16 bits)</text>
        <text x="662" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">1 = ARP Request &nbsp;•&nbsp; 2 = ARP Reply</text>
      </g>

      <!-- ROW 3 & 4: SENDER HARDWARE & PROTOCOL ADDRESSES (BYTES 8-17) -->
      <g transform="translate(30, 157)">
        <rect x="0" y="0" width="540" height="45" rx="4" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="270" y="20" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Sender Hardware Address (SHA: 48 bits / 6 Bytes)</text>
        <text x="270" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Originating sender host MAC address (e.g. 00:1A:2B:3C:4D:5E)</text>

        <rect x="550" y="0" width="330" height="45" rx="4" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="715" y="20" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Sender IP (SPA: 32 bits / 4B)</text>
        <text x="715" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Originating sender IPv4 address</text>
      </g>

      <!-- ROW 5 & 6: TARGET HARDWARE & PROTOCOL ADDRESSES (BYTES 18-27) -->
      <g transform="translate(30, 208)">
        <rect x="0" y="0" width="540" height="45" rx="4" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="270" y="20" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">Target Hardware Address (THA: 48 bits / 6 Bytes)</text>
        <text x="270" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">00:00:00:00:00:00 in Request &nbsp;•&nbsp; Receiver MAC in Reply</text>

        <rect x="550" y="0" width="330" height="45" rx="4" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="715" y="20" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">Target IP (TPA: 32 bits / 4B)</text>
        <text x="715" y="36" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">Queried target IPv4 address</text>
      </g>

      <!-- ENCAPSULATION NOTE -->
      <g transform="translate(30, 265)">
        <rect width="880" height="70" rx="6" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="25" fill="var(--tx-primary)" font-size="10.5" font-weight="800">
          Layer-2 Framing Note (EtherType = 0x0806):
        </text>
        <text x="25" y="45" fill="var(--tx-muted)" font-size="9.5">
          An ARP packet does NOT use an IP header! It is encapsulated directly into the payload of an IEEE 802.3 Ethernet frame with EtherType = <code>0x0806</code>. Because 28 bytes &lt; minimum Ethernet payload (46 bytes), it is padded with 18 zero bytes.
        </text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: ARP Request Broadcast vs Unicast Reply (Figure 17.3)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📡</span>
      <span class="diagram-title">Figure 17.3: ARP Protocol Flow — Layer-2 Broadcast Request vs. Layer-2 Unicast Reply</span>
    </div>
    <span class="diagram-badge">ARP TIMELINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-arp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arr-rep" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- STEP 1: ARP REQUEST (BROADCAST) -->
      <g transform="translate(30, 25)">
        <rect width="420" height="270" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <rect x="15" y="15" width="390" height="30" rx="4" fill="var(--accent-dim)" stroke="none"/>
        <text x="210" y="35" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">STEP 1: ARP REQUEST (L2 BROADCAST)</text>

        <!-- Sender Host A -->
        <circle cx="60" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="60" y="115" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Host A</text>
        <text x="60" y="145" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">192.168.1.10</text>
        <text x="60" y="157" fill="var(--tx-muted)" font-size="8" font-family="monospace" text-anchor="middle">AA:AA:AA:..:01</text>

        <!-- Switch Central -->
        <rect x="175" y="88" width="70" height="44" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="210" y="115" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Switch</text>

        <!-- Flooding lines -->
        <path d="M 85 110 L 170 110" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-arp)"/>
        <path d="M 248 100 L 330 75" stroke="var(--warning)" stroke-width="2" marker-end="url(#arr-arp)"/>
        <path d="M 248 110 L 330 110" stroke="var(--success)" stroke-width="2" marker-end="url(#arr-arp)"/>
        <path d="M 248 120 L 330 145" stroke="var(--warning)" stroke-width="2" marker-end="url(#arr-arp)"/>

        <!-- Receiving nodes -->
        <circle cx="355" cy="75" r="16" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="355" y="79" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Host C (Drops)</text>

        <circle cx="355" cy="110" r="18" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="355" y="114" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">Host B</text>

        <circle cx="355" cy="145" r="16" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="355" y="149" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Host D (Drops)</text>

        <!-- Explanation -->
        <rect x="15" y="195" width="390" height="60" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="215" fill="var(--accent)" font-size="9.5" font-weight="800">Dst MAC: FF:FF:FF:FF:FF:FF (Broadcast)</text>
        <text x="25" y="232" fill="var(--tx-muted)" font-size="9">"Who has 192.168.1.20? Tell 192.168.1.10!"</text>
        <text x="25" y="246" fill="var(--tx-muted)" font-size="8.5">All hosts receive; only Host B matches Target IP.</text>
      </g>

      <!-- STEP 2: ARP REPLY (UNICAST) -->
      <g transform="translate(485, 25)">
        <rect width="425" height="270" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <rect x="15" y="15" width="395" height="30" rx="4" fill="var(--success-dim)" stroke="none"/>
        <text x="212" y="35" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">STEP 2: ARP REPLY (L2 UNICAST)</text>

        <!-- Sender Host B -->
        <circle cx="355" cy="110" r="22" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="355" y="115" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">Host B</text>
        <text x="355" y="145" fill="var(--tx-muted)" font-size="8.5" text-anchor="middle">192.168.1.20</text>
        <text x="355" y="157" fill="var(--tx-muted)" font-size="8" font-family="monospace" text-anchor="middle">BB:BB:BB:..:02</text>

        <!-- Switch Central -->
        <rect x="175" y="88" width="70" height="44" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="210" y="115" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">Switch</text>

        <!-- Direct Unicast line back to Host A -->
        <path d="M 330 110 L 248 110" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arr-rep)"/>
        <path d="M 170 110 L 85 110" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arr-rep)"/>

        <!-- Target Host A -->
        <circle cx="60" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="60" y="115" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">Host A</text>

        <!-- Explanation -->
        <rect x="15" y="195" width="395" height="60" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="215" fill="var(--success)" font-size="9.5" font-weight="900">Dst MAC: AA:AA:AA:..:01 (Unicast)</text>
        <text x="25" y="232" fill="var(--tx-primary)" font-size="9">"192.168.1.20 is at BB:BB:BB:..:02"</text>
        <text x="25" y="246" fill="var(--tx-primary)" font-size="8.5">Host A installs entry in ARP cache table: TTL ~20 mins.</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Hop-by-Hop MAC Rewriting (Figure 17.6)
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔀</span>
      <span class="diagram-title">Figure 17.6: Hop-by-Hop Layer-2 MAC Rewriting Across Router Boundaries (IPs Constant)</span>
    </div>
    <span class="diagram-badge">MAC REWRITING</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-hop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOPOLOGY: HOST A -> ROUTER R1 -> HOST B -->
      <!-- Host A -->
      <g transform="translate(60, 40)">
        <rect width="180" height="85" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="90" y="25" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">Host A (Subnet 1)</text>
        <text x="90" y="45" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">IP: 192.168.1.10</text>
        <text x="90" y="65" fill="var(--tx-muted)" font-size="9" font-family="monospace" text-anchor="middle">MAC: AA:AA:AA:AA:AA:AA</text>
      </g>

      <!-- Hop 1 Arrow -->
      <path d="M 245 82 L 375 82" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr-hop)"/>
      <text x="310" y="72" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">HOP 1</text>

      <!-- Router R1 (Default Gateway) -->
      <g transform="translate(380, 25)">
        <rect width="180" height="115" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <text x="90" y="24" fill="var(--info)" font-size="12" font-weight="900" text-anchor="middle">Router R1 (Gateway)</text>

        <!-- eth0 (Subnet 1) -->
        <rect x="10" y="35" width="160" height="32" rx="3" fill="var(--info-dim)" stroke="none"/>
        <text x="90" y="48" fill="var(--info)" font-size="8.5" font-weight="800" text-anchor="middle">eth0: 192.168.1.1</text>
        <text x="90" y="60" fill="var(--tx-muted)" font-size="8" font-family="monospace" text-anchor="middle">MAC: R1:R1:R1:01:01:01</text>

        <!-- eth1 (Subnet 2) -->
        <rect x="10" y="72" width="160" height="32" rx="3" fill="var(--success-dim)" stroke="none"/>
        <text x="90" y="85" fill="var(--success)" font-size="8.5" font-weight="800" text-anchor="middle">eth1: 192.168.2.1</text>
        <text x="90" y="97" fill="var(--tx-muted)" font-size="8" font-family="monospace" text-anchor="middle">MAC: R1:R1:R1:02:02:02</text>
      </g>

      <!-- Hop 2 Arrow -->
      <path d="M 565 82 L 695 82" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-hop)"/>
      <text x="630" y="72" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">HOP 2</text>

      <!-- Server B -->
      <g transform="translate(700, 40)">
        <rect width="180" height="85" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="90" y="25" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">Server B (Subnet 2)</text>
        <text x="90" y="45" fill="var(--tx-primary)" font-size="10" font-weight="800" text-anchor="middle">IP: 192.168.2.50</text>
        <text x="90" y="65" fill="var(--tx-muted)" font-size="9" font-family="monospace" text-anchor="middle">MAC: BB:BB:BB:BB:BB:BB</text>
      </g>

      <!-- PACKET FRAME COMPARISON TABLE -->
      <g transform="translate(60, 160)">
        <rect width="820" height="135" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="410" y="25" fill="var(--accent)" font-size="11.5" font-weight="900" text-anchor="middle">
          PACKET HEADER EVOLUTION: LAYER-3 END-TO-END VS. LAYER-2 HOP-BY-HOP
        </text>

        <!-- Row Hop 1 -->
        <g transform="translate(20, 40)">
          <rect width="780" height="38" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="20" y="24" fill="var(--accent)" font-size="10" font-weight="900">HOP 1 FRAME (Host A ➔ R1):</text>
          <text x="230" y="24" fill="var(--tx-primary)" font-size="9.5" font-family="monospace">Src MAC: AA:..:AA &nbsp;•&nbsp; Dst MAC: R1:..:01</text>
          <text x="540" y="24" fill="var(--success)" font-size="9.5" font-weight="800">Src IP: 192.168.1.10 ➔ Dst IP: 192.168.2.50</text>
        </g>

        <!-- Row Hop 2 -->
        <g transform="translate(20, 85)">
          <rect width="780" height="38" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
          <text x="20" y="24" fill="var(--success)" font-size="10" font-weight="900">HOP 2 FRAME (R1 ➔ Server B):</text>
          <text x="230" y="24" fill="var(--tx-primary)" font-size="9.5" font-family="monospace">Src MAC: R1:..:02 &nbsp;•&nbsp; Dst MAC: BB:..:BB</text>
          <text x="540" y="24" fill="var(--success)" font-size="9.5" font-weight="800">Src IP: 192.168.1.10 ➔ Dst IP: 192.168.2.50</text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Traceroute Timeline (Figure 17.14)
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⏱️</span>
      <span class="diagram-title">Figure 17.14: Step-by-Step Traceroute Probe Timeline &amp; ICMP Error Lifecycle</span>
    </div>
    <span class="diagram-badge">TRACEROUTE TIMELINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-probe" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arr-icmp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
        <marker id="arr-done" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- VERTICAL ACTOR TIMELINE AXES -->
      <!-- Sender -->
      <line x1="120" y1="50" x2="120" y2="290" stroke="var(--border)" stroke-width="2"/>
      <circle cx="120" cy="40" r="18" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
      <text x="120" y="44" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">Sender</text>

      <!-- Router 1 -->
      <line x1="380" y1="50" x2="380" y2="290" stroke="var(--border)" stroke-width="2"/>
      <circle cx="380" cy="40" r="18" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
      <text x="380" y="44" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">Router 1</text>

      <!-- Router 2 -->
      <line x1="640" y1="50" x2="640" y2="290" stroke="var(--border)" stroke-width="2"/>
      <circle cx="640" cy="40" r="18" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
      <text x="640" y="44" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">Router 2</text>

      <!-- Destination Target -->
      <line x1="840" y1="50" x2="840" y2="290" stroke="var(--border)" stroke-width="2"/>
      <circle cx="840" cy="40" r="18" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
      <text x="840" y="44" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">Target</text>

      <!-- PROBE 1: TTL = 1 -->
      <g transform="translate(0, 75)">
        <path d="M 120 0 L 375 25" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#arr-probe)"/>
        <text x="240" y="5" fill="var(--accent)" font-size="9" font-weight="800">Probe 1 (TTL = 1)</text>

        <!-- Drop & ICMP response -->
        <circle cx="380" cy="25" r="5" fill="var(--danger)"/>
        <path d="M 380 30 L 125 55" stroke="var(--danger)" stroke-width="2" marker-end="url(#arr-icmp)"/>
        <text x="240" y="50" fill="var(--danger)" font-size="9" font-weight="800">ICMP Type 11 (Time Exceeded)</text>
        <text x="40" y="58" fill="var(--info)" font-size="8.5" font-weight="700">RTT 1 Measured</text>
      </g>

      <!-- PROBE 2: TTL = 2 -->
      <g transform="translate(0, 150)">
        <path d="M 120 0 L 375 12" stroke="var(--accent)" stroke-width="2"/>
        <path d="M 380 12 L 635 25" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#arr-probe)"/>
        <text x="500" y="5" fill="var(--accent)" font-size="9" font-weight="800">Probe 2 (TTL = 2 ➔ 1 at R1)</text>

        <!-- Drop at R2 -->
        <circle cx="640" cy="25" r="5" fill="var(--danger)"/>
        <path d="M 640 30 L 125 60" stroke="var(--danger)" stroke-width="2" marker-end="url(#arr-icmp)"/>
        <text x="400" y="55" fill="var(--danger)" font-size="9" font-weight="800">ICMP Type 11 from R2</text>
        <text x="40" y="63" fill="var(--info)" font-size="8.5" font-weight="700">RTT 2 Measured</text>
      </g>

      <!-- PROBE 3: TTL = 3 (TARGET REACHED) -->
      <g transform="translate(0, 225)">
        <path d="M 120 0 L 380 10 L 640 20 L 835 26" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#arr-probe)"/>
        <text x="730" y="10" fill="var(--accent)" font-size="9" font-weight="800">TTL = 3</text>

        <!-- Target Destination Reached -->
        <circle cx="840" cy="26" r="6" fill="var(--success)"/>
        <path d="M 840 32 L 125 60" stroke="var(--success)" stroke-width="2.2" marker-end="url(#arr-done)"/>
        <text x="480" y="55" fill="var(--success)" font-size="9" font-weight="900">
          ICMP Type 3, Code 3 (Port Unreachable) ➔ Done!
        </text>
        <text x="40" y="63" fill="var(--success)" font-size="8.5" font-weight="900">Final Hop RTT!</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 5. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch17_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch17">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">Address Resolution (ARP) &amp; ICMP Diagnostics</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Subnet Traversal, Hop-by-Hop MAC Rewriting, &amp; Traceroute</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Explain the Address Resolution Protocol (ARP). Host A on 192.168.1.0/24 wants to send an IP datagram to Server B on 192.168.2.0/24 via Default Gateway Router R1. Detail the exact ARP resolutions performed, how L2 MAC addresses change while L3 IP addresses remain constant, and explain how Traceroute identifies intermediate routers using ICMP Time Exceeded (Type 11)."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: ARP BASICS & SAME VS REMOTE -->
        <div class="blueprint-section">
          <h4 class="section-title">1. ARP Operational Mechanics: Same Subnet vs. Remote Subnet (3 Marks)</h4>
          <p>
            When Host A prepares to send a datagram to Destination IP $D$:
          </p>
          <ul class="blueprint-list">
            <li><strong>Bitwise AND Mask Check:</strong> Host A performs $(D \text{ AND } \text{Mask}_A) \stackrel{?}{=} (\text{IP}_A \text{ AND } \text{Mask}_A)$.
              $$(192.168.2.50 \text{ AND } 255.255.255.0) = 192.168.2.0 \ne 192.168.1.0$$
              Because the network IDs differ, destination is <strong>remote</strong>.
            </li>
            <li><strong>The Cardinal Gateway Rule:</strong> Host A does <strong>NOT</strong> issue an ARP request for Server B's IP! Host A issues an ARP request for its configured <strong>Default Gateway IP (192.168.1.1)</strong>!</li>
            <li><strong>Broadcast Request / Unicast Reply:</strong> Host A broadcasts an ARP request ($\text{MAC}_{\text{Dst}} = \text{FF:FF:FF:FF:FF:FF}$). Router R1 receives it, records Host A in its ARP cache, and replies with its interface MAC ($\text{R1}_{\text{eth0}}$) via unicast.</li>
          </ul>
        </div>

        <!-- SECTION 2: HOP-BY-HOP MAC REWRITING -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Hop-by-Hop Packet Traversal &amp; Header Mutation Trace (4 Marks)</h4>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Hop Stage</th>
                  <th>Source MAC</th>
                  <th>Destination MAC</th>
                  <th>Source IP</th>
                  <th>Destination IP</th>
                  <th>TTL</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Hop 1: Host A ➔ R1</strong></td>
                  <td><code>AA:AA:AA:AA:AA:AA</code></td>
                  <td><code>R1:R1:R1:01:01:01</code></td>
                  <td><code>192.168.1.10</code></td>
                  <td><code>192.168.2.50</code></td>
                  <td>$64$</td>
                </tr>
                <tr>
                  <td><strong>Inside Router R1</strong></td>
                  <td colspan="5">R1 decrements TTL ($63$), verifies checksum, performs FIB lookup, finds Server B is on directly connected interface <code>eth1</code>. If not in cache, R1 issues ARP broadcast on Subnet 2 for <code>192.168.2.50</code>.</td>
                </tr>
                <tr>
                  <td><strong>Hop 2: R1 ➔ Server B</strong></td>
                  <td><code>R1:R1:R1:02:02:02</code></td>
                  <td><code>BB:BB:BB:BB:BB:BB</code></td>
                  <td><code>192.168.1.10</code></td>
                  <td><code>192.168.2.50</code></td>
                  <td>$63$</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="blueprint-summary-note">
            <strong>Fundamental Invariant:</strong> Layer-2 MAC addresses change at every router hop (hop-by-hop delivery), while Layer-3 IP addresses remain <strong>strictly unchanged end-to-end</strong> (unless NAT/PAT is present).
          </p>
        </div>

        <!-- SECTION 3: TRACEROUTE & ICMP -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Traceroute Execution &amp; ICMP Diagnostic Feedback (3 Marks)</h4>
          <ul class="blueprint-list">
            <li><strong>TTL Modulation:</strong> Traceroute sends a series of UDP or ICMP probes starting with $\text{TTL} = 1$, incrementing TTL by $1$ after receiving each response.</li>
            <li><strong>Router Hop Identification:</strong>
              When probe with $\text{TTL} = 1$ reaches Router R1, R1 decrements TTL to $0$. By RFC 791 rules, R1 discards the packet and generates an <strong>ICMP Type 11, Code 0 (Time-to-Live Exceeded in Transit)</strong> error datagram back to Host A. The source IP of this ICMP packet reveals the router's identity!
            </li>
            <li><strong>Target Termination:</strong> When probe with sufficient TTL reaches final Server B, Server B does not decrement TTL to zero. Because traceroute uses an intentionally unused high UDP port (e.g. $33434$), Server B returns <strong>ICMP Type 3, Code 3 (Port Unreachable)</strong>, notifying traceroute that the target host was reached!</li>
          </ul>
        </div>

        <!-- TRAPS & MARKING SCHEME -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap:</strong>
            Students frequently claim that <em>"Host A broadcasts an ARP request across the router to find Server B's MAC."</em> This is fundamentally wrong! <strong>Routers NEVER forward Layer-2 broadcast packets!</strong> An ARP broadcast is strictly confined to the local broadcast domain (VLAN/Subnet).
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 17
# ==========================================

# 1. Replace Figure 17.2 in s17-2
match_s17_f2 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 17\.2.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s17_f2:
    content = content[:match_s17_f2.start()] + svg_diagram_1 + content[match_s17_f2.end():]
    print('Replaced Figure 17.2 with responsive SVG Diagram 1')
else:
    print('Warning: could not find Figure 17.2')

# 2. Replace Figure 17.3 in s17-3
match_s17_f3 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 17\.3.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s17_f3:
    content = content[:match_s17_f3.start()] + svg_diagram_2 + content[match_s17_f3.end():]
    print('Replaced Figure 17.3 with responsive SVG Diagram 2')
else:
    print('Warning: could not find Figure 17.3')

# 3. Replace Figure 17.6 in s17-6
match_s17_f6 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 17\.6.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s17_f6:
    content = content[:match_s17_f6.start()] + svg_diagram_3 + content[match_s17_f6.end():]
    print('Replaced Figure 17.6 with responsive SVG Diagram 3')
else:
    print('Warning: could not find Figure 17.6')

# 4. Replace Figure 17.14 in s17-14
match_s17_f14 = re.search(r'(<div class="diagram-box">\s*<div class="diagram-title">Figure 17\.14.*?</div>)(.*?)(</div>)', content, flags=re.DOTALL)
if match_s17_f14:
    content = content[:match_s17_f14.start()] + svg_diagram_4 + content[match_s17_f14.end():]
    print('Replaced Figure 17.14 with responsive SVG Diagram 4')
else:
    print('Warning: could not find Figure 17.14')

# 5. Insert DU 10-Mark Blueprint before study-resources or in s17-18
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch17_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 17!')
else:
    # Append before </main>
    main_target = re.search(r'</section>\s*</main>', content)
    if main_target:
        content = content[:main_target.start()] + '</section>\n\n' + ch17_uni_blueprint + '\n</main>' + content[main_target.end():]
        print('Inserted 10-Mark University Blueprint before </main> in Chapter 17!')
    else:
        print('Warning: could not find insertion spot for Blueprint in Chapter 17')

with open(ch17_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 17 upgrade completed!')
