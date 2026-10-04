"""
Upgrade Chapter 3 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch3_path = '/Users/arpit/minibook/cn/chapters/ch03-models-addressing.html'
with open(ch3_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Virtual Peer vs Physical Flow
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔄</span>
      <span class="diagram-title">Figure 3.1: Layered Abstraction — Virtual Peer Protocols vs. Actual Physical Flow</span>
    </div>
    <span class="diagram-badge">OSI PRINCIPLE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-vpeer" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-pflow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="900" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- HOST A (LEFT STACK) -->
      <g transform="translate(40, 30)">
        <rect width="180" height="260" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="90" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">HOST A (SOURCE)</text>
        
        <rect x="15" y="35" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="52" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">7. Application</text>
        
        <rect x="15" y="65" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="82" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">6. Presentation</text>

        <rect x="15" y="95" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="112" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">5. Session</text>

        <rect x="15" y="125" width="150" height="26" rx="4" fill="var(--info-dim)"/>
        <text x="90" y="142" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">4. Transport</text>

        <rect x="15" y="155" width="150" height="26" rx="4" fill="var(--warning-dim)"/>
        <text x="90" y="172" fill="var(--warning)" font-size="10" font-weight="700" text-anchor="middle">3. Network</text>

        <rect x="15" y="185" width="150" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="90" y="202" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">2. Data Link</text>

        <rect x="15" y="215" width="150" height="26" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="90" y="232" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">1. Physical</text>
      </g>

      <!-- INTERMEDIATE ROUTER (CENTER) -->
      <g transform="translate(370, 150)">
        <rect width="180" height="140" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.8"/>
        <text x="90" y="24" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">ROUTER (INTERMEDIARY)</text>

        <rect x="15" y="35" width="150" height="26" rx="4" fill="var(--warning-dim)"/>
        <text x="90" y="52" fill="var(--warning)" font-size="10" font-weight="700" text-anchor="middle">3. Network (Routing)</text>

        <rect x="15" y="65" width="150" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="90" y="82" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">2. Data Link</text>

        <rect x="15" y="95" width="150" height="26" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="90" y="112" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">1. Physical</text>
      </g>

      <!-- HOST B (RIGHT STACK) -->
      <g transform="translate(700, 30)">
        <rect width="180" height="260" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="90" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">HOST B (DESTINATION)</text>

        <rect x="15" y="35" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="52" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">7. Application</text>
        
        <rect x="15" y="65" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="82" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">6. Presentation</text>

        <rect x="15" y="95" width="150" height="26" rx="4" fill="var(--accent-dim)"/>
        <text x="90" y="112" fill="var(--tx-primary)" font-size="10" font-weight="700" text-anchor="middle">5. Session</text>

        <rect x="15" y="125" width="150" height="26" rx="4" fill="var(--info-dim)"/>
        <text x="90" y="142" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">4. Transport</text>

        <rect x="15" y="155" width="150" height="26" rx="4" fill="var(--warning-dim)"/>
        <text x="90" y="172" fill="var(--warning)" font-size="10" font-weight="700" text-anchor="middle">3. Network</text>

        <rect x="15" y="185" width="150" height="26" rx="4" fill="var(--success-dim)"/>
        <text x="90" y="202" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">2. Data Link</text>

        <rect x="15" y="215" width="150" height="26" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="90" y="232" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">1. Physical</text>
      </g>

      <!-- VIRTUAL PEER PROTOCOL LINES (Dashed Horizontal) -->
      <line x1="220" y1="78" x2="700" y2="78" stroke="var(--accent)" stroke-width="1.8" stroke-dasharray="4,4"/>
      <text x="460" y="73" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Virtual Peer: Application Protocol (HTTP / DNS)</text>

      <line x1="220" y1="168" x2="700" y2="168" stroke="var(--info)" stroke-width="1.8" stroke-dasharray="4,4"/>
      <text x="460" y="163" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Virtual Peer: Transport Protocol (End-to-End TCP Connection)</text>

      <!-- ACTUAL PHYSICAL FLOW PATH (Blue Solid line down, through router, and up) -->
      <path d="M 130 258 L 130 320 L 415 320 L 415 288" stroke="var(--info)" stroke-width="3" fill="none" marker-end="url(#arrow-pflow)"/>
      <path d="M 505 288 L 505 320 L 790 320 L 790 258" stroke="var(--info)" stroke-width="3" fill="none" marker-end="url(#arrow-pflow)"/>
      <text x="460" y="342" fill="var(--tx-secondary)" font-size="11" font-weight="700" text-anchor="middle">
        ACTUAL PHYSICAL TRANSMISSION: Down Host A ➔ Physical Link ➔ Router L1-L3 ➔ Physical Link ➔ Up Host B
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Layering Principle:</strong> Logically, Layer $N$ on the sender communicates directly with Layer $N$ on the receiver via a virtual peer protocol. Physically, data must descend all the way to Layer 1, traverse transmission media and intermediate routers, and ascend the stack at the destination.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: SAP, SDU, PCI, and PDU
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧩</span>
      <span class="diagram-title">Figure 3.2: Formal Layer Interface Model — SAP, SDU, PCI, and PDU Relationships</span>
    </div>
    <span class="diagram-badge">ISO-OSI FORMALISM</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-sap" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LAYER (N+1) BLOCK -->
      <g transform="translate(40, 25)">
        <rect width="820" height="90" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.8"/>
        <text x="25" y="30" fill="var(--accent)" font-size="13" font-weight="800">LAYER (N + 1) — Higher Service Layer</text>

        <!-- (N+1) PDU -->
        <g transform="translate(250, 25)">
          <rect width="360" height="42" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="180" y="26" fill="var(--accent-light)" font-size="12" font-weight="700" text-anchor="middle">
            (N + 1) - PDU (Protocol Data Unit)
          </text>
        </g>
      </g>

      <!-- SAP (SERVICE ACCESS POINT) -->
      <g transform="translate(410, 115)">
        <circle cx="40" cy="18" r="14" fill="var(--warning)" stroke="#fff" stroke-width="2"/>
        <text x="40" y="22" fill="#000" font-size="10" font-weight="900" text-anchor="middle">SAP</text>
        <text x="100" y="22" fill="var(--warning)" font-size="11" font-weight="700">Service Access Point (N-SAP)</text>
      </g>

      <!-- Downward handover arrows -->
      <path d="M 430 115 L 430 160" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-sap)"/>

      <!-- LAYER N BLOCK -->
      <g transform="translate(40, 165)">
        <rect width="820" height="150" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <text x="25" y="30" fill="var(--info)" font-size="13" font-weight="800">LAYER N — Providing Service via Interface</text>

        <!-- SDU Handover -->
        <g transform="translate(300, 20)">
          <rect width="360" height="38" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,2"/>
          <text x="180" y="24" fill="var(--accent-light)" font-size="11" font-weight="700" text-anchor="middle">
            N - SDU (Service Data Unit) = (N + 1) PDU
          </text>
        </g>

        <!-- Layer N Encapsulation: PCI + SDU -->
        <g transform="translate(140, 75)">
          <!-- PCI (Header) -->
          <rect width="140" height="48" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="70" y="24" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">N - PCI</text>
          <text x="70" y="38" fill="var(--tx-muted)" font-size="9" text-anchor="middle">(Layer N Header)</text>

          <!-- SDU (Payload) -->
          <rect x="150" y="0" width="360" height="48" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="330" y="28" fill="var(--accent-light)" font-size="11" font-weight="700" text-anchor="middle">
            N - SDU (Payload from Layer N+1)
          </text>

          <!-- Total N-PDU Bracket -->
          <rect x="-10" y="-8" width="530" height="64" rx="8" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="5,3"/>
          <text x="590" y="32" fill="var(--accent)" font-size="12" font-weight="800">➔ N - PDU</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Formal Definition:</strong> $PDU_N = PCI_N + SDU_N$. The entire PDU of layer $(N+1)$ becomes the raw Service Data Unit (SDU) for layer $N$. Layer $N$ prepends its own Protocol Control Information (PCI / Header) to create the $N$-PDU passed through the $N$-SAP.
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: OSI Layer Groupings & Transport Core
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📚</span>
      <span class="diagram-title">Figure 3.3: The 7 OSI Layers Categorized into Functional Sub-Systems</span>
    </div>
    <span class="diagram-badge">OSI REFERENCE MODEL</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 920 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="900" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- GROUP 1: SOFTWARE / APPLICATION TIER (L7 - L5) -->
      <g transform="translate(30, 25)">
        <rect width="260" height="320" rx="12" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <rect x="15" y="15" width="230" height="30" rx="6" fill="var(--accent-dim)"/>
        <text x="130" y="35" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">SOFTWARE / USER TIER</text>

        <!-- L7 -->
        <rect x="15" y="60" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="80" fill="var(--accent)" font-size="11" font-weight="800">7. Application</text>
        <text x="25" y="96" fill="var(--tx-muted)" font-size="9">Network APIs: HTTP, DNS, SMTP</text>

        <!-- L6 -->
        <rect x="15" y="125" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="145" fill="var(--accent)" font-size="11" font-weight="800">6. Presentation</text>
        <text x="25" y="161" fill="var(--tx-muted)" font-size="9">Format, Encryption (TLS), Compression</text>

        <!-- L5 -->
        <rect x="15" y="190" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="210" fill="var(--accent)" font-size="11" font-weight="800">5. Session</text>
        <text x="25" y="226" fill="var(--tx-muted)" font-size="9">Dialog control, RPC, Checkpointing</text>

        <text x="130" y="275" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">Implemented in Software</text>
        <text x="130" y="290" fill="var(--tx-muted)" font-size="9" text-anchor="middle">(Operating System Userland)</text>
      </g>

      <!-- GROUP 2: THE HEART OF OSI (L4 TRANSPORT) -->
      <g transform="translate(320, 25)">
        <rect width="280" height="320" rx="12" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
        <rect x="15" y="15" width="250" height="30" rx="6" fill="var(--info-dim)"/>
        <text x="140" y="35" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">HEART OF OSI: TRANSPORT</text>

        <!-- L4 -->
        <rect x="15" y="60" width="250" height="180" rx="8" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="140" y="90" fill="var(--info)" font-size="14" font-weight="900" text-anchor="middle">4. Transport Layer</text>
        <text x="140" y="110" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">End-to-End Process Delivery</text>

        <line x1="30" y1="125" x2="250" y2="125" stroke="var(--border)" stroke-width="1"/>

        <text x="30" y="145" fill="var(--tx-secondary)" font-size="10">• Port Addressing (Sockets)</text>
        <text x="30" y="165" fill="var(--tx-secondary)" font-size="10">• Segmentation &amp; Reassembly</text>
        <text x="30" y="185" fill="var(--tx-secondary)" font-size="10">• Flow Control (Sliding Window)</text>
        <text x="30" y="205" fill="var(--tx-secondary)" font-size="10">• Error Control &amp; Retransmissions</text>
        <text x="30" y="225" fill="var(--tx-secondary)" font-size="10">• Connection: TCP (Stateful) / UDP</text>

        <text x="140" y="275" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Links Userland to Hardware</text>
        <text x="140" y="290" fill="var(--tx-muted)" font-size="9" text-anchor="middle">(Kernel Space Implementation)</text>
      </g>

      <!-- GROUP 3: HARDWARE / NETWORK SUPPORT TIER (L3 - L1) -->
      <g transform="translate(630, 25)">
        <rect width="260" height="320" rx="12" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <rect x="15" y="15" width="230" height="30" rx="6" fill="var(--warning-dim)"/>
        <text x="130" y="35" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">NETWORK SUPPORT TIER</text>

        <!-- L3 -->
        <rect x="15" y="60" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="80" fill="var(--warning)" font-size="11" font-weight="800">3. Network Layer</text>
        <text x="25" y="96" fill="var(--tx-muted)" font-size="9">Logical IP Addressing, Routing</text>

        <!-- L2 -->
        <rect x="15" y="125" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="145" fill="var(--success)" font-size="11" font-weight="800">2. Data Link Layer</text>
        <text x="25" y="161" fill="var(--tx-muted)" font-size="9">MAC Framing, Error check (CRC)</text>

        <!-- L1 -->
        <rect x="15" y="190" width="230" height="52" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="210" fill="var(--tx-primary)" font-size="11" font-weight="800">1. Physical Layer</text>
        <text x="25" y="226" fill="var(--tx-muted)" font-size="9">Signals, Voltages, Connectors (RJ45)</text>

        <text x="130" y="275" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">Point-to-Point Node Delivery</text>
        <text x="130" y="290" fill="var(--tx-muted)" font-size="9" text-anchor="middle">(NIC Hardware &amp; Physical Media)</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>The Heart of OSI:</strong> Layers 1 to 3 provide <em>hop-by-hop</em> data delivery between intermediate network devices. Layers 5 to 7 provide user application services. Layer 4 (Transport) is the crucial bridge that turns unreliable hop-by-hop communication into true <em>end-to-end</em> process-to-process reliability.
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Data Link Sublayer Division (IEEE 802 LLC vs MAC)
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">✂️</span>
      <span class="diagram-title">Figure 3.4: IEEE 802 Division of Data Link Layer into LLC and MAC Sublayers</span>
    </div>
    <span class="diagram-badge">IEEE 802 STANDARD</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="880" height="300" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- NETWORK LAYER ON TOP -->
      <g transform="translate(40, 25)">
        <rect width="820" height="40" rx="6" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="410" y="25" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">
          LAYER 3: NETWORK LAYER (IPv4, IPv6, ARP, ICMP)
        </text>
      </g>

      <!-- DATA LINK LAYER CONTAINER -->
      <g transform="translate(40, 80)">
        <rect width="820" height="155" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <text x="25" y="24" fill="var(--success)" font-size="11" font-weight="800">LAYER 2: DATA LINK LAYER (IEEE 802 ARCHITECTURE)</text>

        <!-- UPPER SUBLAYER: LLC -->
        <g transform="translate(20, 35)">
          <rect width="780" height="45" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="20" y="24" fill="var(--info)" font-size="12" font-weight="800">LLC: Logical Link Control (IEEE 802.2)</text>
          <text x="20" y="38" fill="var(--tx-muted)" font-size="9">Media-independent • Multiplexes network protocols • Flow control &amp; ARQ</text>
          <text x="760" y="28" fill="var(--info)" font-size="10" font-weight="700" text-anchor="end">Software Driver Interface</text>
        </g>

        <!-- LOWER SUBLAYER: MAC (Split across physical standards) -->
        <g transform="translate(20, 90)">
          <text x="20" y="15" fill="var(--accent)" font-size="11" font-weight="800">MAC: Medium Access Control Sublayer (Hardware Framing, CSMA/CD, 48-bit MAC Address)</text>
          
          <rect x="0" y="22" width="245" height="35" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
          <text x="122" y="44" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">IEEE 802.3 (Ethernet LAN)</text>

          <rect x="265" y="22" width="245" height="35" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
          <text x="387" y="44" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">IEEE 802.11 (Wi-Fi Wireless)</text>

          <rect x="530" y="22" width="250" height="35" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.2"/>
          <text x="655" y="44" fill="var(--accent-light)" font-size="10" font-weight="700" text-anchor="middle">IEEE 802.15 (Bluetooth / WPAN)</text>
        </g>
      </g>

      <!-- PHYSICAL LAYER AT BOTTOM -->
      <g transform="translate(40, 250)">
        <rect width="820" height="40" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="410" y="25" fill="var(--tx-muted)" font-size="11" font-weight="700" text-anchor="middle">
          LAYER 1: PHYSICAL LAYER (Copper Twisted Pair, Optical Fiber, RF Spectrum)
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Architectural Modularity:</strong> By splitting Layer 2 into LLC and MAC, the upper LLC sublayer remains 100% identical regardless of whether you are transmitting over wired Ethernet, Wi-Fi, or Bluetooth. Only the lower MAC sublayer adapts to the specific physical access method.
  </div>
</div>'''

# ==========================================
# 5. DIAGRAM 5: Protocol Demultiplexing Key Pipeline
# ==========================================
svg_diagram_5 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🗝️</span>
      <span class="diagram-title">Figure 3.5: Protocol Demultiplexing Ladder — Demux Keys Dispatching Inbound Packets</span>
    </div>
    <span class="diagram-badge">PROTOCOL DISPATCH</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-demux" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="880" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- STAGE 1: DATA LINK DEMUX -->
      <g transform="translate(40, 30)">
        <rect width="250" height="260" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2"/>
        <rect x="15" y="15" width="220" height="28" rx="6" fill="var(--success-dim)"/>
        <text x="125" y="34" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">1. ETHERNET FRAME</text>
        
        <text x="25" y="70" fill="var(--tx-primary)" font-size="11" font-weight="700">Demux Key:</text>
        <rect x="25" y="80" width="200" height="36" rx="6" fill="var(--bg-elevated)" stroke="var(--success)" stroke-width="1.2"/>
        <text x="125" y="103" fill="var(--success)" font-family="var(--font-mono)" font-size="12" font-weight="800" text-anchor="middle">
          EtherType = 0x0800
        </text>

        <line x1="20" y1="130" x2="230" y2="130" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="155" fill="var(--tx-muted)" font-size="10">Other EtherType values:</text>
        <text x="25" y="175" fill="var(--tx-secondary)" font-size="10">• 0x0806 ➔ ARP Protocol</text>
        <text x="25" y="195" fill="var(--tx-secondary)" font-size="10">• 0x86DD ➔ IPv6 Protocol</text>
        <text x="25" y="215" fill="var(--tx-secondary)" font-size="10">• 0x8100 ➔ 802.1Q VLAN</text>
        
        <text x="125" y="250" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">Passes payload to IPv4</text>
      </g>

      <!-- Arrow 1 to 2 -->
      <path d="M 290 160 L 335 160" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-demux)"/>

      <!-- STAGE 2: NETWORK LAYER DEMUX -->
      <g transform="translate(340, 30)">
        <rect width="250" height="260" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <rect x="15" y="15" width="220" height="28" rx="6" fill="var(--warning-dim)"/>
        <text x="125" y="34" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">2. IP PACKET</text>

        <text x="25" y="70" fill="var(--tx-primary)" font-size="11" font-weight="700">Demux Key:</text>
        <rect x="25" y="80" width="200" height="36" rx="6" fill="var(--bg-elevated)" stroke="var(--warning)" stroke-width="1.2"/>
        <text x="125" y="103" fill="var(--warning)" font-family="var(--font-mono)" font-size="12" font-weight="800" text-anchor="middle">
          Protocol = 6 (TCP)
        </text>

        <line x1="20" y1="130" x2="230" y2="130" stroke="var(--border)" stroke-width="1"/>
        <text x="25" y="155" fill="var(--tx-muted)" font-size="10">Other IP Protocol numbers:</text>
        <text x="25" y="175" fill="var(--tx-secondary)" font-size="10">• Protocol 1 ➔ ICMP (Ping)</text>
        <text x="25" y="195" fill="var(--tx-secondary)" font-size="10">• Protocol 17 ➔ UDP</text>
        <text x="25" y="215" fill="var(--tx-secondary)" font-size="10">• Protocol 89 ➔ OSPF</text>

        <text x="125" y="250" fill="var(--warning)" font-size="10" font-weight="700" text-anchor="middle">Passes segment to TCP</text>
      </g>

      <!-- Arrow 2 to 3 -->
      <path d="M 590 160 L 635 160" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-demux)"/>

      <!-- STAGE 3: TRANSPORT LAYER DEMUX -->
      <g transform="translate(640, 30)">
        <rect width="220" height="260" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <rect x="15" y="15" width="190" height="28" rx="6" fill="var(--info-dim)"/>
        <text x="110" y="34" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">3. TCP SEGMENT</text>

        <text x="20" y="70" fill="var(--tx-primary)" font-size="11" font-weight="700">Demux Key:</text>
        <rect x="20" y="80" width="180" height="36" rx="6" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="1.2"/>
        <text x="110" y="103" fill="var(--info)" font-family="var(--font-mono)" font-size="12" font-weight="800" text-anchor="middle">
          Dest Port = 443
        </text>

        <line x1="15" y1="130" x2="205" y2="130" stroke="var(--border)" stroke-width="1"/>
        <text x="20" y="155" fill="var(--tx-muted)" font-size="10">Target Socket:</text>
        <text x="20" y="175" fill="var(--tx-secondary)" font-size="10">• Port 80 ➔ HTTP Web</text>
        <text x="20" y="195" fill="var(--tx-secondary)" font-size="10">• Port 443 ➔ HTTPS Web</text>
        <text x="20" y="215" fill="var(--tx-secondary)" font-size="10">• Port 22 ➔ SSH Shell</text>

        <text x="110" y="250" fill="var(--info)" font-size="10" font-weight="700" text-anchor="middle">Delivered to NGINX Web Server</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>How Operating Systems Dispatch Data:</strong> The OS kernel inspects header fields hierarchically like Russian nesting dolls: Ethernet header tells it which Layer-3 module to invoke (IP), IP header tells it which Layer-4 protocol gets the segment (TCP), and TCP port delivers the payload to the exact listening application process.
  </div>
</div>'''

# ==========================================
# 6. DIAGRAM 6: The Internet Hourglass ("Narrow Waist")
# ==========================================
svg_diagram_6 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⏳</span>
      <span class="diagram-title">Figure 3.6: The Internet Hourglass Architecture — IP as the Universal Narrow Waist</span>
    </div>
    <span class="diagram-badge">INTERNET DESIGN PRINCIPLE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 900 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="hour-grad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.15"/>
          <stop offset="50%" stop-color="var(--warning)" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="var(--info)" stop-opacity="0.15"/>
        </linearGradient>
      </defs>

      <rect x="10" y="10" width="880" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP EXPANSION: MULTIPLE APPLICATION PROTOCOLS -->
      <g transform="translate(100, 30)">
        <polygon points="50,0 650,0 500,80 200,80" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="350" y="28" fill="var(--accent-light)" font-size="13" font-weight="800" text-anchor="middle">
          DIVERSE APPLICATION PROTOCOLS (Top Expansion)
        </text>
        <text x="350" y="55" fill="var(--tx-primary)" font-size="11" font-weight="600" text-anchor="middle">
          HTTP/3 • SMTP • DNS • SSH • BitTorrent • Zoom RTP • WebRTC • MQTT • CoAP
        </text>
      </g>

      <!-- TRANSPORT PROTOCOLS (Upper Funnel) -->
      <g transform="translate(260, 115)">
        <polygon points="40,0 340,0 270,40 110,40" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="190" y="26" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">
          TRANSPORT: TCP • UDP • QUIC • SCTP
        </text>
      </g>

      <!-- THE NARROW WAIST: INTERNET PROTOCOL (IP) -->
      <g transform="translate(320, 160)">
        <rect width="260" height="50" rx="10" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="3"/>
        <text x="130" y="28" fill="var(--warning)" font-size="14" font-weight="900" text-anchor="middle">
          INTERNET PROTOCOL (IP)
        </text>
        <text x="130" y="42" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">
          THE UNIVERSAL NARROW WAIST (IPv4 / IPv6)
        </text>
      </g>

      <!-- DATA LINK TECHNOLOGIES (Lower Funnel) -->
      <g transform="translate(260, 215)">
        <polygon points="110,0 270,0 340,40 40,40" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.8"/>
        <text x="190" y="26" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">
          DATA LINK: Ethernet • Wi-Fi • DOCSIS • PPP • Frame Relay
        </text>
      </g>

      <!-- BOTTOM EXPANSION: MULTIPLE PHYSICAL MEDIA -->
      <g transform="translate(100, 260)">
        <polygon points="200,0 500,0 650,70 50,70" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="2"/>
        <text x="350" y="32" fill="var(--tx-primary)" font-size="13" font-weight="800" text-anchor="middle">
          DIVERSE PHYSICAL TRANSMISSION MEDIA (Bottom Expansion)
        </text>
        <text x="350" y="55" fill="var(--tx-secondary)" font-size="11" font-weight="600" text-anchor="middle">
          Single-mode Fiber • Cat6A Copper • 5G / LTE Cellular • Satellite Ku-band • Microwave Line-of-Sight
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>"Everything over IP, IP over Everything":</strong> The phenomenal scalability of the Internet is owed directly to the hourglass model. Because there is only ONE universal protocol at the network layer (IP), new applications can be created without changing physical infrastructure, and revolutionary new physical media (e.g. 5G, fiber) can be deployed without rewriting applications!
  </div>
</div>'''

# ==========================================
# 7. DIAGRAM 7: Hop-by-Hop Packet Traversal Trace
# ==========================================
svg_diagram_7 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🗺️</span>
      <span class="diagram-title">Figure 3.7: Hop-by-Hop Packet Traversal — MAC Addresses Change, IP Remains Constant</span>
    </div>
    <span class="diagram-badge">CORE NETWORKING AXIOM</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-hop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP NODES: HOST A -> ROUTER R1 -> ROUTER R2 -> HOST B -->
      
      <!-- HOST A -->
      <g transform="translate(30, 30)">
        <rect width="140" height="85" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="70" y="26" font-size="16" text-anchor="middle">💻</text>
        <text x="70" y="46" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">HOST A (Sender)</text>
        <text x="70" y="62" fill="var(--tx-primary)" font-size="9" font-family="var(--font-mono)" text-anchor="middle">IP: 192.168.1.10</text>
        <text x="70" y="76" fill="var(--tx-muted)" font-size="9" font-family="var(--font-mono)" text-anchor="middle">MAC: AA:AA:AA:AA:AA:AA</text>
      </g>

      <!-- LINK 1 -->
      <line x1="170" y1="72" x2="270" y2="72" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-hop)"/>
      <text x="220" y="62" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Hop 1 (LAN)</text>

      <!-- ROUTER R1 -->
      <g transform="translate(275, 25)">
        <rect width="170" height="95" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <text x="85" y="24" font-size="16" text-anchor="middle">🧭</text>
        <text x="85" y="42" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">ROUTER R1</text>
        <text x="85" y="58" fill="var(--tx-muted)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">In: MAC 11:11:11:11:11:11</text>
        <text x="85" y="72" fill="var(--tx-muted)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">Out: MAC 22:22:22:22:22:22</text>
        <text x="85" y="86" fill="var(--tx-primary)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">IP: 192.168.1.1 / 10.0.0.1</text>
      </g>

      <!-- LINK 2 (WAN) -->
      <line x1="445" y1="72" x2="545" y2="72" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-hop)"/>
      <text x="495" y="62" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Hop 2 (WAN)</text>

      <!-- ROUTER R2 -->
      <g transform="translate(550, 25)">
        <rect width="170" height="95" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="2"/>
        <text x="85" y="24" font-size="16" text-anchor="middle">🧭</text>
        <text x="85" y="42" fill="var(--warning)" font-size="12" font-weight="800" text-anchor="middle">ROUTER R2</text>
        <text x="85" y="58" fill="var(--tx-muted)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">In: MAC 33:33:33:33:33:33</text>
        <text x="85" y="72" fill="var(--tx-muted)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">Out: MAC 44:44:44:44:44:44</text>
        <text x="85" y="86" fill="var(--tx-primary)" font-size="8" font-family="var(--font-mono)" text-anchor="middle">IP: 10.0.0.2 / 203.0.113.1</text>
      </g>

      <!-- LINK 3 -->
      <line x1="720" y1="72" x2="780" y2="72" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow-hop)"/>
      <text x="750" y="62" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Hop 3 (LAN)</text>

      <!-- HOST B -->
      <g transform="translate(785, 30)">
        <rect width="125" height="85" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="62" y="26" font-size="16" text-anchor="middle">🖥️</text>
        <text x="62" y="46" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">HOST B (Dest)</text>
        <text x="62" y="62" fill="var(--tx-primary)" font-size="9" font-family="var(--font-mono)" text-anchor="middle">IP: 203.0.113.50</text>
        <text x="62" y="76" fill="var(--tx-muted)" font-size="9" font-family="var(--font-mono)" text-anchor="middle">MAC: BB:BB:BB:BB:BB:BB</text>
      </g>

      <!-- THREE HOP HEADER TRACE COMPARISON PANELS -->
      
      <!-- TRACE 1: HOP 1 -->
      <g transform="translate(30, 140)">
        <rect width="280" height="150" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="140" y="22" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">FRAME ON HOP 1 (Host A ➔ R1)</text>

        <rect x="15" y="35" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="53" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Src MAC: AA:AA:AA:AA:AA:AA</text>

        <rect x="15" y="67" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="85" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Dst MAC: 11:11:11:11:11:11 (R1 in)</text>

        <rect x="15" y="102" width="250" height="36" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="25" y="118" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Src IP: 192.168.1.10 (Host A)</text>
        <text x="25" y="132" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Dst IP: 203.0.113.50 (Host B)</text>
      </g>

      <!-- TRACE 2: HOP 2 -->
      <g transform="translate(330, 140)">
        <rect width="280" height="150" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="140" y="22" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">FRAME ON HOP 2 (R1 ➔ R2)</text>

        <rect x="15" y="35" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="53" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Src MAC: 22:22:22:22:22:22 (R1 out)</text>

        <rect x="15" y="67" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="85" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Dst MAC: 33:33:33:33:33:33 (R2 in)</text>

        <rect x="15" y="102" width="250" height="36" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="25" y="118" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Src IP: 192.168.1.10 (CONSTANT!)</text>
        <text x="25" y="132" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Dst IP: 203.0.113.50 (CONSTANT!)</text>
      </g>

      <!-- TRACE 3: HOP 3 -->
      <g transform="translate(630, 140)">
        <rect width="280" height="150" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="140" y="22" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">FRAME ON HOP 3 (R2 ➔ Host B)</text>

        <rect x="15" y="35" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="53" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Src MAC: 44:44:44:44:44:44 (R2 out)</text>

        <rect x="15" y="67" width="250" height="28" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="25" y="85" fill="var(--success)" font-size="9" font-family="var(--font-mono)">Dst MAC: BB:BB:BB:BB:BB:BB (Host B)</text>

        <rect x="15" y="102" width="250" height="36" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1"/>
        <text x="25" y="118" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Src IP: 192.168.1.10 (CONSTANT!)</text>
        <text x="25" y="132" fill="var(--warning)" font-size="9" font-family="var(--font-mono)">Dst IP: 203.0.113.50 (CONSTANT!)</text>
      </g>

      <!-- BOTTOM BANNER -->
      <rect x="30" y="305" width="880" height="30" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
      <text x="470" y="324" fill="var(--tx-secondary)" font-size="10" font-weight="600" text-anchor="middle">
        <tspan fill="var(--success)" font-weight="700">MAC ADDRESSES:</tspan> Stripped and replaced at every Layer-3 router hop • <tspan fill="var(--warning)" font-weight="700">IP ADDRESSES:</tspan> Preserved unchanged end-to-end (except NAT).
      </text>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Master Exam Rule:</strong> Data Link Layer (MAC) addressing is strictly <em>local to the physical link</em> (hop-by-hop delivery). Network Layer (IP) addressing is <em>global across the entire internetwork</em> (end-to-end routing). Routers strip the inbound Layer-2 frame, inspect the Layer-3 IP header, and encapsulate the packet into a brand new outbound Layer-2 frame with new MAC addresses.
  </div>
</div>'''

# ==========================================
# 8. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 3
# ==========================================
ch3_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: The ISO-OSI Reference Model vs. TCP/IP Protocol Suite &amp; Addressing Hierarchy</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) State the principles used in defining the seven layers of the ISO-OSI reference model. List each layer from bottom to top with its corresponding Protocol Data Unit (PDU) and two primary responsibilities. [4 Marks]<br>
          (b) Compare the OSI Reference Model and the TCP/IP Protocol Suite across five distinct architectural parameters. Explain the technical and historical reasons why TCP/IP triumphed in commercial reality while OSI remained primarily a teaching tool. [3 Marks]<br>
          (c) Describe the four-tier addressing hierarchy in the TCP/IP protocol suite (Physical, Logical, Port, and Specific addresses). With the help of a packet forwarding trace across two intermediate routers, prove that Physical (MAC) addresses change at every router hop while Logical (IP) addresses remain constant end-to-end. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: ISO-OSI Layering Principles &amp; Layer Catalog</h4>
          <p><strong>ISO Layering Principles:</strong> (1) A layer should only be created where a different level of abstraction is needed; (2) Each layer should perform a well-defined function; (3) The function of each layer should be chosen with an eye toward internationally standardized protocols; (4) Layer boundaries should minimize information flow across interfaces; (5) The number of layers should be large enough to avoid putting separate functions together, and small enough that architecture remains manageable.</p>

          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Layer Name</th>
                <th>PDU</th>
                <th>Primary Responsibilities</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>7. Application</strong></td>
                <td>Data / Message</td>
                <td>User network interface, HTTP/DNS network service APIs, authentication.</td>
              </tr>
              <tr>
                <td><strong>6. Presentation</strong></td>
                <td>Data</td>
                <td>Data translation (ASCII/Unicode), cryptographic encryption/decryption (TLS), data compression.</td>
              </tr>
              <tr>
                <td><strong>5. Session</strong></td>
                <td>Data</td>
                <td>Dialog control (half-duplex/full-duplex token management), session synchronization &amp; checkpoints.</td>
              </tr>
              <tr>
                <td><strong>4. Transport</strong></td>
                <td>Segment (TCP) / Datagram (UDP)</td>
                <td>End-to-end process-to-process delivery, port addressing, segmentation/reassembly, flow &amp; error control.</td>
              </tr>
              <tr>
                <td><strong>3. Network</strong></td>
                <td>Packet / Datagram</td>
                <td>Host-to-host delivery, logical IP addressing, shortest-path routing, packet fragmentation.</td>
              </tr>
              <tr>
                <td><strong>2. Data Link</strong></td>
                <td>Frame</td>
                <td>Hop-to-hop node delivery, physical MAC framing, hardware error detection (CRC-32 FCS), channel access.</td>
              </tr>
              <tr>
                <td><strong>1. Physical</strong></td>
                <td>Bits</td>
                <td>Bit-level transmission over transmission media, signal encoding, voltage levels, pin connectors.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: OSI vs. TCP/IP Comparative Analysis</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Comparison Parameter</th>
                <th>ISO-OSI Reference Model</th>
                <th>TCP/IP Protocol Suite</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Layer Count</strong></td>
                <td>7 Layers (Strict modular separation)</td>
                <td>4 Layers (RFC 1122) / 5 Layers (Curriculum)</td>
              </tr>
              <tr>
                <td><strong>Development Approach</strong></td>
                <td>Theoretical model defined <em>before</em> protocols were written</td>
                <td>Protocols implemented and tested on ARPANET <em>before</em> model was documented</td>
              </tr>
              <tr>
                <td><strong>Session &amp; Presentation Layers</strong></td>
                <td>Explicit separate independent layers (L5, L6)</td>
                <td>Absorbed directly into the Application Layer (L7)</td>
              </tr>
              <tr>
                <td><strong>Network Layer Communication</strong></td>
                <td>Supports both Connectionless and Connection-Oriented (X.25)</td>
                <td>Strictly Connectionless (IP datagram service only)</td>
              </tr>
              <tr>
                <td><strong>Transport Layer Communication</strong></td>
                <td>Strictly Connection-Oriented in early revisions</td>
                <td>Supports both Connection-Oriented (TCP) and Connectionless (UDP)</td>
              </tr>
            </tbody>
          </table>
          <p style="margin-top: 8px;"><strong>Why TCP/IP Triumphed (The "Bad Timing &amp; Bad Implementation" Phenomenon):</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Bad Timing:</strong> By the time OSI standards were finalized in the late 1980s, TCP/IP was already deeply entrenched in academia, defense (ARPANET), and UNIX (4.2BSD socket API).</li>
            <li><strong>Bad Technology:</strong> OSI had massive bloat; Session and Presentation layers had very little distinct functionality for most protocols, while Data Link and Network were congested with overlapping responsibilities.</li>
            <li><strong>Bad Implementation:</strong> Early OSI protocol implementations were slow, memory-intensive, and complex, whereas TCP/IP code was free, open-source, robust, and lightweight.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: The 4-Tier Addressing Hierarchy &amp; Packet Traversal Proof</h4>
          <p><strong>The Four-Tier Addressing Hierarchy:</strong></p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Physical Address (MAC Address):</strong> 48-bit hex address burned into NIC ROM (e.g., <code>AA:BB:CC:11:22:33</code>). Local to the single physical link.</li>
            <li><strong>Logical Address (IP Address):</strong> 32-bit (IPv4) or 128-bit (IPv6) global address identifying host network and host interface universally across the internetwork.</li>
            <li><strong>Port Address:</strong> 16-bit number (0–65535) identifying the specific communicating application process/socket on a host (e.g., Port 80 for HTTP, Port 53 for DNS).</li>
            <li><strong>Specific Address:</strong> High-level human-readable identifiers such as URLs (<code>www.google.com</code>) or email addresses (<code>alice@university.edu</code>), resolved to IP addresses via DNS.</li>
          </ol>

          <p><strong>Proof: Why MAC Changes While IP Remains Constant (Refer to Figure 3.7):</strong></p>
          <p>When Host A transmits an IP datagram to remote Host B via intermediate routers R1 and R2:</p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li>The Source IP (<code>Host A</code>) and Destination IP (<code>Host B</code>) are written into the Layer-3 IP header at transmission time. They <strong>never change</strong> across intermediate hops because routers use Destination IP solely to consult their routing tables for the next-hop outbound interface.</li>
            <li>However, Layer-2 switches and physical cables cannot route across different subnets; they can only forward frames between stations directly attached to the same physical link.</li>
            <li>Therefore, to traverse Link 1 (Host A to R1), the frame must specify <code>Dst MAC = R1</code>. When R1 receives the frame, it strips the Layer-2 header, inspects the IP datagram, decrements TTL, and encapsulates the packet into a brand new Layer-2 frame for Link 2 with <code>Src MAC = R1_out</code> and <code>Dst MAC = R2_in</code>.</li>
            <li>Hence, <strong>MAC addresses are strictly hop-local and change at every router boundary</strong>, whereas <strong>IP addresses are global and remain unchanged end-to-end</strong>.</li>
          </ul>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 3
# ==========================================
replacements = [
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Layered Abstraction: Virtual Peer vs\. Actual Physical Flow</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_1),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">SAP, SDU, Header \(PCI\), and PDU Relationship</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_2),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">OSI Layer Groupings &amp; The Transport Core</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_3),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Data Link Layer Division \(IEEE 802 Standard\)</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_4),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Protocol Demultiplexing: How the Stack Dispatches Traffic</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_5),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">The Internet Hourglass: IP as the Narrow Waist</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_6),
    (r'<div class="code-block">\s*<div class="code-header"><span class="code-lang">Packet Traversal Trace: MAC Changes at Every Hop, IP Stays Constant</span></div>\s*<pre><code>.*?</code></pre>\s*</div>', svg_diagram_7),
]

for pattern, repl in replacements:
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + repl + content[match.end():]
        print(f'Successfully replaced pattern: {pattern[:40]}...')
    else:
        print(f'FAILED to match pattern: {pattern[:40]}...')

# Insert 10-Mark Blueprint into Chapter 3 before the study-resources in s-summary-ch3
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch3_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 3!')

with open(ch3_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 3 upgrade completed!')
