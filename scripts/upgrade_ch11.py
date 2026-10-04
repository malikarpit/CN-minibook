"""
Upgrade Chapter 11 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch11_path = '/Users/arpit/minibook/cn/chapters/ch11-network-layer-foundations.html'
with open(ch11_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Router Architecture & Routing vs Forwarding
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🧭</span>
      <span class="diagram-title">Figure 11.1: Router Internal Architecture — Control Plane (Routing) vs. Data Plane (Forwarding)</span>
    </div>
    <span class="diagram-badge">ROUTER ENGINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-ch11" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-fab" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP: CONTROL PLANE (THE BRAIN - SOFTWARE) -->
      <g transform="translate(30, 25)">
        <rect width="860" height="85" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2"/>
        <text x="25" y="26" fill="var(--info)" font-size="12" font-weight="900">
          ROUTING ENGINE / CONTROL PLANE (Software Process: Millisecond Scale)
        </text>
        <text x="25" y="44" fill="var(--tx-muted)" font-size="9">
          Routing Protocols (OSPF, BGP, RIP) • Computes Global Topology • Builds Master Routing Table (RIB)
        </text>

        <!-- Forwarding Table Push -->
        <g transform="translate(560, 15)">
          <rect width="280" height="55" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="140" y="24" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">
            Forwarding Information Base (FIB)
          </text>
          <text x="140" y="42" fill="var(--tx-primary)" font-size="9" text-anchor="middle">
            Pushed to Line Cards for Line-Rate Lookup ⬇
          </text>
        </g>
      </g>

      <!-- DOWNWARD CONTROL PUSH ARROWS -->
      <path d="M 230 110 L 230 145" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-ch11)"/>
      <path d="M 700 110 L 700 145" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-ch11)"/>

      <!-- BOTTOM: DATA PLANE (THE MUSCLE - HARDWARE LINE CARDS) -->
      <g transform="translate(30, 150)">
        <rect width="860" height="195" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="25" y="24" fill="var(--accent)" font-size="12" font-weight="900">
          FORWARDING ENGINE / DATA PLANE (Hardware ASICs &amp; Crossbar Fabric: Nanosecond Scale)
        </text>

        <!-- INPUT PORTS (LEFT) -->
        <g transform="translate(25, 38)">
          <rect width="220" height="135" rx="8" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="110" y="22" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">
            INPUT PORTS (Line Cards)
          </text>
          
          <rect x="15" y="32" width="190" height="30" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="105" y="52" fill="var(--accent-light)" font-size="9" font-weight="700" text-anchor="middle">
            Physical Term + Data Link Decap
          </text>

          <rect x="15" y="68" width="190" height="30" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1"/>
          <text x="105" y="88" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">
            Hardware LPM Lookup (TCAM)
          </text>

          <rect x="15" y="104" width="190" height="22" rx="4" fill="var(--warning-dim)"/>
          <text x="105" y="119" fill="var(--warning)" font-size="8" font-weight="700" text-anchor="middle">
            Input Queuing Buffer (HOL Block)
          </text>
        </g>

        <!-- HIGH SPEED SWITCHING FABRIC (CENTER) -->
        <g transform="translate(285, 38)">
          <rect width="280" height="135" rx="8" fill="rgba(52, 211, 153, 0.12)" stroke="var(--success)" stroke-width="2"/>
          <text x="140" y="24" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">
            SWITCHING FABRIC
          </text>
          <text x="140" y="40" fill="var(--tx-muted)" font-size="8" text-anchor="middle">
            (Crossbar Matrix / Shared Memory / Bus)
          </text>

          <!-- Crossbar Grid Demonstration -->
          <g transform="translate(40, 50)" stroke="var(--success)" stroke-width="1.8">
            <line x1="0" y1="20" x2="200" y2="20"/>
            <line x1="0" y1="50" x2="200" y2="50"/>
            <line x1="50" y1="0" x2="50" y2="70"/>
            <line x1="150" y1="0" x2="150" y2="70"/>
            <circle cx="50" cy="20" r="4" fill="var(--success)"/>
            <circle cx="150" cy="50" r="4" fill="var(--success)"/>
          </g>
          <text x="140" y="125" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">
            Parallel Non-Blocking Switching
          </text>
        </g>

        <!-- OUTPUT PORTS (RIGHT) -->
        <g transform="translate(605, 38)">
          <rect width="220" height="135" rx="8" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="110" y="22" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">
            OUTPUT PORTS
          </text>

          <rect x="15" y="32" width="190" height="30" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
          <text x="105" y="52" fill="var(--danger)" font-size="9" font-weight="800" text-anchor="middle">
            Output Buffer (Drop: RED/Tail)
          </text>

          <rect x="15" y="68" width="190" height="30" rx="4" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="105" y="88" fill="var(--accent-light)" font-size="9" font-weight="700" text-anchor="middle">
            Data Link Encap (New MACs)
          </text>

          <rect x="15" y="104" width="190" height="22" rx="4" fill="var(--bg-card)"/>
          <text x="105" y="119" fill="var(--tx-muted)" font-size="8" text-anchor="middle">
            Physical Transmit to Link ➔
          </text>
        </g>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Routing vs. Forwarding Distinction:</strong> <em>Routing</em> is the global, software-based control plane process that determines the end-to-end path of packets using routing algorithms (OSPF/BGP). <em>Forwarding</em> is the local, hardware-based data plane action that moves a packet from an input port to the appropriate output port in mere nanoseconds.
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Datagram vs Virtual Circuit Networks
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🔀</span>
      <span class="diagram-title">Figure 11.2: Network Layer Paradigms — Connectionless Datagram vs. Connection-Oriented Virtual Circuit</span>
    </div>
    <span class="diagram-badge">NETWORK SERVICE MODELS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-dat" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--info)" />
        </marker>
        <marker id="arrow-vc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: DATAGRAM NETWORK (INTERNET MODEL) -->
      <g transform="translate(30, 25)">
        <rect width="420" height="315" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <text x="210" y="24" fill="var(--info)" font-size="12" font-weight="800" text-anchor="middle">
          1. DATAGRAM NETWORK (Connectionless / The Internet)
        </text>
        <text x="210" y="38" fill="var(--tx-muted)" font-size="9" text-anchor="middle">
          Each packet carries full Destination IP • Routed independently
        </text>

        <!-- Topology Nodes: Host A, R1, R2, R3, Host B -->
        <g transform="translate(30, 55)">
          <!-- Host A -->
          <circle cx="30" cy="90" r="18" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="2"/>
          <text x="30" y="94" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">Host A</text>

          <!-- R1 -->
          <circle cx="120" cy="50" r="16" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="120" y="54" fill="var(--tx-primary)" font-size="9" text-anchor="middle">R1</text>

          <!-- R2 (Top route) -->
          <circle cx="220" cy="30" r="16" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="220" y="34" fill="var(--tx-primary)" font-size="9" text-anchor="middle">R2</text>

          <!-- R3 (Bottom route) -->
          <circle cx="220" cy="110" r="16" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="220" y="114" fill="var(--tx-primary)" font-size="9" text-anchor="middle">R3</text>

          <!-- Host B -->
          <circle cx="330" cy="90" r="18" fill="var(--bg-elevated)" stroke="var(--info)" stroke-width="2"/>
          <text x="330" y="94" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">Host B</text>

          <!-- Packet 1 via R1 ➔ R2 ➔ Host B -->
          <path d="M 48 85 L 105 55" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-dat)"/>
          <path d="M 136 46 L 204 34" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-dat)"/>
          <path d="M 236 34 L 315 80" stroke="var(--info)" stroke-width="2" marker-end="url(#arrow-dat)"/>
          <text x="160" y="24" fill="var(--info)" font-size="8" font-weight="700">Packet 1 Path</text>

          <!-- Packet 2 via R1 ➔ R3 ➔ Host B (Alternate Route!) -->
          <path d="M 134 58 L 206 102" stroke="var(--warning)" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrow-dat)"/>
          <path d="M 236 108 L 315 95" stroke="var(--warning)" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrow-dat)"/>
          <text x="170" y="130" fill="var(--warning)" font-size="8" font-weight="700">Packet 2 Path (Dynamic!)</text>
        </g>

        <rect x="20" y="220" width="380" height="75" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="30" y="238" fill="var(--info)" font-size="10" font-weight="800">Datagram Characteristics:</text>
        <text x="30" y="254" fill="var(--tx-secondary)" font-size="9">• Zero call setup delay</text>
        <text x="30" y="270" fill="var(--tx-secondary)" font-size="9">• Packets may arrive out-of-order</text>
        <text x="30" y="286" fill="var(--success)" font-size="9" font-weight="700">✓ Highly resilient: R2 failure automatically reroutes to R3</text>
      </g>

      <!-- RIGHT: VIRTUAL CIRCUIT NETWORK (ATM / X.25 MODEL) -->
      <g transform="translate(480, 25)">
        <rect width="430" height="315" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="215" y="24" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">
          2. VIRTUAL CIRCUIT NETWORK (Connection-Oriented / ATM / MPLS)
        </text>
        <text x="215" y="38" fill="var(--tx-muted)" font-size="9" text-anchor="middle">
          Setup phase reserves path • Packets carry short VCI label • Strict in-order
        </text>

        <!-- Topology Nodes with Fixed Dedicated VC Pipe -->
        <g transform="translate(30, 55)">
          <circle cx="30" cy="70" r="18" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="2"/>
          <text x="30" y="74" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">Host A</text>

          <circle cx="130" cy="70" r="16" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="130" y="74" fill="var(--tx-primary)" font-size="9" text-anchor="middle">SW 1</text>

          <circle cx="230" cy="70" r="16" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1.5"/>
          <text x="230" y="74" fill="var(--tx-primary)" font-size="9" text-anchor="middle">SW 2</text>

          <circle cx="330" cy="70" r="18" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="2"/>
          <text x="330" y="74" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">Host B</text>

          <!-- Fixed VC Pipe -->
          <line x1="48" y1="70" x2="114" y2="70" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrow-vc)"/>
          <text x="80" y="60" fill="var(--accent)" font-size="8" font-weight="800">VCI=14</text>

          <line x1="146" y1="70" x2="214" y2="70" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrow-vc)"/>
          <text x="180" y="60" fill="var(--accent)" font-size="8" font-weight="800">VCI=77</text>

          <line x1="246" y1="70" x2="312" y2="70" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrow-vc)"/>
          <text x="280" y="60" fill="var(--accent)" font-size="8" font-weight="800">VCI=22</text>

          <!-- VC Translation Table Subpanel -->
          <rect x="70" y="100" width="220" height="45" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <text x="180" y="118" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">
            SW 1 VC Table: [Port 1, VCI 14] ➔ [Port 2, VCI 77]
          </text>
          <text x="180" y="134" fill="var(--tx-muted)" font-size="8" text-anchor="middle">
            Labels rewritten at every switch hop
          </text>
        </g>

        <rect x="20" y="220" width="390" height="75" rx="6" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
        <text x="30" y="238" fill="var(--accent)" font-size="10" font-weight="800">Virtual Circuit Characteristics:</text>
        <text x="30" y="254" fill="var(--tx-secondary)" font-size="9">• Requires 3 phases: Setup ➔ Data ➔ Teardown</text>
        <text x="30" y="270" fill="var(--tx-secondary)" font-size="9">• Guarantees strictly in-order packet delivery</text>
        <text x="30" y="286" fill="var(--danger)" font-size="9" font-weight="700">⚠️ Vulnerability: Any switch crash tears down the entire VC!</text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Architectural Philosophy:</strong> The Internet chose the <em>Datagram</em> model based on the "End-to-End Principle": keep the network core simple, stateless, and robust, while placing all reordering, flow control, and state tracking at the smart end-hosts (TCP).
  </div>
</div>'''

# ==========================================
# 3. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 11
# ==========================================
ch11_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Network Layer Services, Router Internal Architecture &amp; Datagram vs. Virtual Circuit</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) Define the primary responsibilities of the Network Layer in the OSI/TCP-IP protocol stack. Differentiate between Routing and Forwarding with suitable operational examples. [3 Marks]<br>
          (b) Sketch the internal architectural diagram of a modern high-speed router. Explain the functions of: (i) Input Ports, (ii) Switching Fabric (Memory, Bus, and Crossbar), and (iii) Output Ports. What is Head-of-Line (HOL) blocking? [4 Marks]<br>
          (c) Compare Connectionless Datagram Networks and Connection-Oriented Virtual Circuit (VC) Networks across five parameters: Addressing overhead, Setup phase requirement, State maintenance in intermediate routers, Handling of router failure, and Quality of Service (QoS) guarantees. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Network Layer Responsibilities &amp; Routing vs. Forwarding</h4>
          <p><strong>Primary Responsibilities:</strong> Host-to-host packet delivery, global logical addressing (IPv4/IPv6), path computation (routing), packet switching, fragmentation/reassembly across MTU boundaries, and congestion control.</p>
          <p><strong>Routing vs. Forwarding:</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Routing (Global Control Plane):</strong> The collective network-wide algorithm that determines the end-to-end path packets take from source to destination (e.g., executing Dijkstra's algorithm in OSPF or exchanging BGP paths). Operates on the order of seconds/milliseconds in software.</li>
            <li><strong>Forwarding (Local Data Plane):</strong> The router-local action of transferring a packet from an incoming interface link to the appropriate outbound interface link based on its Destination IP. Executes in hardware (TCAM/ASICs) within nanoseconds.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: Router Internal Architecture &amp; HOL Blocking</h4>
          <p><strong>1. Input Ports:</strong> Terminates the incoming physical link, decapsulates the Layer-2 frame, performs a lookup in the Forwarding Table using Longest Prefix Match (LPM) via Ternary Content-Addressable Memory (TCAM), and queues packets for the switching fabric.</p>
          <p><strong>2. Switching Fabric:</strong> The core hardware interconnect that moves packets from input buffers to output buffers:</p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><em>Switching via Memory:</em> Shared CPU/RAM bus. Slowest ($O(1)$ packet at a time).</li>
            <li><em>Switching via Bus:</em> Shared high-speed backplane bus; bandwidth limited to bus speed.</li>
            <li><em>Switching via Interconnection Network (Crossbar):</em> A $2D$ matrix of intersecting horizontal and vertical buses. Allows up to $N$ packets to be switched simultaneously in parallel without blocking, provided they target different output ports.</li>
          </ul>
          <p><strong>3. Output Ports:</strong> Buffers outgoing packets when line rate is exceeded, executes queuing disciplines (FIFO, Priority Queuing, Weighted Fair Queuing WFQ), encapsulates the IP datagram into a new Layer-2 frame, and transmits signals onto the physical link.</p>
          <p><strong>Head-of-Line (HOL) Blocking:</strong> In an input-buffered switch, a packet at the front of an input queue that is blocked because its target output port is busy will prevent all subsequent packets behind it in the queue from being forwarded—even if their designated output ports are completely idle!</p>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Datagram vs. Virtual Circuit Comparative Master Matrix</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Datagram Network (Internet / IP)</th>
                <th>Virtual Circuit Network (ATM / X.25)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Addressing Overhead</strong></td>
                <td>Large (Full 32-bit or 128-bit global IP in every packet)</td>
                <td>Small (Short local 8-to-16 bit Virtual Circuit Identifier VCI)</td>
              </tr>
              <tr>
                <td><strong>Connection Setup Phase</strong></td>
                <td>None (Instant transmission of first packet)</td>
                <td>Mandatory 3-phase handshake (Setup ➔ Data ➔ Teardown)</td>
              </tr>
              <tr>
                <td><strong>Router State Maintenance</strong></td>
                <td>Stateless (Routers store no per-flow connection state)</td>
                <td>Stateful (Every router maintains a VC table entry per connection)</td>
              </tr>
              <tr>
                <td><strong>Router Failure Resilience</strong></td>
                <td>High (Subsequent packets dynamically rerouted around crash)</td>
                <td>Low (Crash destroys state; all VCs traversing node abort)</td>
              </tr>
              <tr>
                <td><strong>Quality of Service (QoS)</strong></td>
                <td>Difficult (Best-effort service model)</td>
                <td>Easy (Bandwidth &amp; buffer capacity reserved during setup)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 11
# ==========================================
# Insert Diagram 1 into Section 11.5 (Routing/Forwarding)
s5_target = re.search(r'<section id="s11-routing-forwarding"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s5_target:
    content = content[:s5_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s5_target.end():]
    print('Inserted Diagram 1 in Section 11.5')

# Insert Diagram 2 into Section 11.10 (Datagram)
s10_target = re.search(r'<section id="s11-datagram"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s10_target:
    content = content[:s10_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s10_target.end():]
    print('Inserted Diagram 2 in Section 11.10')

# Insert 10-Mark Blueprint into Chapter 11 before study-resources in s11-summary
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch11_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 11!')

with open(ch11_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 11 upgrade completed!')
