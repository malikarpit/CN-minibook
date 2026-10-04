"""
Upgrade Chapter 13 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch13_path = '/Users/arpit/minibook/cn/chapters/ch13-link-state-distance-vector.html'
with open(ch13_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Dual Paradigm Architecture (LS vs DV)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚖️</span>
      <span class="diagram-title">Figure 13.1: The Dual Paradigm of Interior Routing — Link-State vs. Distance-Vector</span>
    </div>
    <span class="diagram-badge">ROUTING PARADIGMS</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-ch13" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: LINK-STATE (OSPF/IS-IS) -->
      <g transform="translate(30, 25)">
        <rect width="420" height="280" rx="10" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.8"/>
        <rect x="15" y="15" width="390" height="36" rx="6" fill="var(--info-dim)" stroke="none"/>
        <text x="210" y="38" fill="var(--info)" font-size="13" font-weight="900" text-anchor="middle">LINK-STATE ROUTING (OSPF, IS-IS)</text>

        <text x="25" y="75" fill="var(--tx-primary)" font-size="11" font-weight="800">Core Philosophy: "Global Knowledge &amp; Local Calculation"</text>
        <text x="25" y="95" fill="var(--tx-muted)" font-size="9.5">Every router floods status of direct links to ALL routers in area.</text>

        <!-- Graphic: Complete Topology Map inside Router -->
        <g transform="translate(25, 110)">
          <rect width="370" height="100" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <!-- Subgraph inside -->
          <circle cx="50" cy="50" r="16" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="50" y="54" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">R1</text>

          <circle cx="140" cy="25" r="16" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="140" y="29" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">R2</text>

          <circle cx="140" cy="75" r="16" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="140" y="79" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">R3</text>

          <circle cx="230" cy="50" r="16" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
          <text x="230" y="54" fill="var(--info)" font-size="10" font-weight="800" text-anchor="middle">R4</text>

          <line x1="66" y1="46" x2="124" y2="29" stroke="var(--info)" stroke-width="1.8"/>
          <line x1="66" y1="54" x2="124" y2="71" stroke="var(--info)" stroke-width="1.8"/>
          <line x1="156" y1="29" x2="214" y2="46" stroke="var(--info)" stroke-width="1.8"/>
          <line x1="156" y1="71" x2="214" y2="54" stroke="var(--info)" stroke-width="1.8"/>

          <text x="300" y="45" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">Full LSDB Map</text>
          <text x="300" y="65" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Dijkstra Runs Locally</text>
        </g>

        <!-- Highlights -->
        <g transform="translate(25, 225)">
          <text x="0" y="16" fill="var(--success)" font-size="10" font-weight="700">✓ Loop-Free by construction (Full SPF Tree)</text>
          <text x="0" y="34" fill="var(--success)" font-size="10" font-weight="700">✓ Instantaneous fast convergence</text>
          <text x="0" y="52" fill="var(--danger)" font-size="10" font-weight="700">✗ High Memory (LSDB) &amp; CPU (Dijkstra) overhead</text>
        </g>
      </g>

      <!-- RIGHT: DISTANCE-VECTOR (RIP/BGP) -->
      <g transform="translate(485, 25)">
        <rect width="425" height="280" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <rect x="15" y="15" width="395" height="36" rx="6" fill="var(--warning-dim)" stroke="none"/>
        <text x="212" y="38" fill="var(--warning)" font-size="13" font-weight="900" text-anchor="middle">DISTANCE-VECTOR ROUTING (RIP, EIGRP, BGP)</text>

        <text x="25" y="75" fill="var(--tx-primary)" font-size="11" font-weight="800">Core Philosophy: "Routing by Rumor / Bellman-Ford"</text>
        <text x="25" y="95" fill="var(--tx-muted)" font-size="9.5">Routers only exchange distance vectors with DIRECT neighbors.</text>

        <!-- Graphic: Local Table & Rumor Exchange -->
        <g transform="translate(25, 110)">
          <rect width="375" height="100" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>

          <!-- Router A -->
          <circle cx="50" cy="50" r="18" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="2"/>
          <text x="50" y="55" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">A</text>

          <!-- Vector Push Arrow -->
          <path d="M 80 50 L 150 50" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-ch13)"/>
          <rect x="85" y="25" width="60" height="18" rx="3" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1"/>
          <text x="115" y="37" fill="var(--accent)" font-size="8.5" font-weight="800" text-anchor="middle">V_A = [0, 2, 7]</text>

          <!-- Router B -->
          <circle cx="190" cy="50" r="18" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="2"/>
          <text x="190" y="55" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">B</text>

          <text x="290" y="45" fill="var(--warning)" font-size="10" font-weight="900" text-anchor="middle">No Topology Map!</text>
          <text x="290" y="65" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Knows: (Dest, Cost, NextHop)</text>
        </g>

        <!-- Highlights -->
        <g transform="translate(25, 225)">
          <text x="0" y="16" fill="var(--success)" font-size="10" font-weight="700">✓ Computationally simple &amp; minimal memory footprint</text>
          <text x="0" y="34" fill="var(--danger)" font-size="10" font-weight="700">✗ Susceptible to Count-to-Infinity &amp; Routing Loops</text>
          <text x="0" y="52" fill="var(--danger)" font-size="10" font-weight="700">✗ Slow convergence; "Bad news travels slowly"</text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Bellman-Ford Principle
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">📐</span>
      <span class="diagram-title">Figure 13.2: Bellman-Ford Distributed Optimality Equation at Router x</span>
    </div>
    <span class="diagram-badge">BELLMAN-FORD</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-bf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arr-opt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="290" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- FORMULA CALLOUT BANNER -->
      <rect x="30" y="25" width="880" height="45" rx="8" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="470" y="53" fill="var(--accent)" font-size="14" font-weight="900" text-anchor="middle">
        BELLMAN-FORD EQUATION: &nbsp; d_x(y) = min_v { c(x, v) + d_v(y) }
      </text>

      <!-- LEFT: SOURCE NODE x -->
      <g transform="translate(60, 100)">
        <circle cx="50" cy="80" r="30" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="3"/>
        <text x="50" y="78" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">Node x</text>
        <text x="50" y="96" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">SOURCE</text>
      </g>

      <!-- MIDDLE: NEIGHBORS v1, v2, v3 -->
      <!-- Neighbor v1 (North) -->
      <g transform="translate(320, 90)">
        <circle cx="40" cy="20" r="22" fill="var(--bg-card)" stroke="var(--border)" stroke-width="2"/>
        <text x="40" y="25" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">v₁</text>

        <!-- Neighbor v2 (Optimal Center) -->
        <circle cx="40" cy="90" r="24" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2.5"/>
        <text x="40" y="95" fill="var(--success)" font-size="13" font-weight="900" text-anchor="middle">v₂</text>

        <!-- Neighbor v3 (South) -->
        <circle cx="40" cy="160" r="22" fill="var(--bg-card)" stroke="var(--border)" stroke-width="2"/>
        <text x="40" y="165" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">v₃</text>
      </g>

      <!-- CONNECTING EDGES WITH COSTS -->
      <!-- x -> v1 (cost 3) -->
      <path d="M 135 160 L 335 115" stroke="var(--border)" stroke-width="2" marker-end="url(#arr-bf)"/>
      <rect x="210" y="125" width="45" height="20" rx="3" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
      <text x="232" y="139" fill="var(--tx-muted)" font-size="10" font-weight="800" text-anchor="middle">c=3</text>

      <!-- x -> v2 (cost 2 - OPTIMAL) -->
      <path d="M 140 180 L 335 180" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-opt)"/>
      <rect x="210" y="170" width="45" height="20" rx="3" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.2"/>
      <text x="232" y="184" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">c=2</text>

      <!-- x -> v3 (cost 6) -->
      <path d="M 135 200 L 335 245" stroke="var(--border)" stroke-width="2" marker-end="url(#arr-bf)"/>
      <rect x="210" y="215" width="45" height="20" rx="3" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1"/>
      <text x="232" y="229" fill="var(--tx-muted)" font-size="10" font-weight="800" text-anchor="middle">c=6</text>

      <!-- DESTINATION y -->
      <g transform="translate(680, 100)">
        <circle cx="50" cy="80" r="30" fill="var(--info-dim)" stroke="var(--info)" stroke-width="3"/>
        <text x="50" y="78" fill="var(--info)" font-size="16" font-weight="900" text-anchor="middle">Node y</text>
        <text x="50" y="96" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">TARGET</text>
      </g>

      <!-- EDGES FROM NEIGHBORS TO y -->
      <!-- v1 -> y (reported cost 5) -->
      <path d="M 385 110 L 695 165" stroke="var(--border)" stroke-width="1.8" stroke-dasharray="3 3"/>
      <text x="530" y="125" fill="var(--tx-muted)" font-size="10">d_v1(y) = 5 &nbsp;➔ Total = 3 + 5 = 8</text>

      <!-- v2 -> y (reported cost 3 - OPTIMAL) -->
      <path d="M 385 180 L 695 180" stroke="var(--success)" stroke-width="2.5"/>
      <rect x="470" y="165" width="165" height="24" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
      <text x="552" y="181" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">d_v2(y) = 3 ➔ Total = 2 + 3 = 5 (MIN)</text>

      <!-- v3 -> y (reported cost 2) -->
      <path d="M 385 250 L 695 195" stroke="var(--border)" stroke-width="1.8" stroke-dasharray="3 3"/>
      <text x="530" y="240" fill="var(--tx-muted)" font-size="10">d_v3(y) = 2 &nbsp;➔ Total = 6 + 2 = 8</text>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Count-to-Infinity Problem
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">♾️</span>
      <span class="diagram-title">Figure 13.3: The Count-to-Infinity Pathology — Step-by-Step Failure Cascade</span>
    </div>
    <span class="diagram-badge">COUNT-TO-INFINITY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 370" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="350" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- TOP: INITIAL STABLE TOPOLOGY -->
      <g transform="translate(30, 25)">
        <rect width="880" height="65" rx="8" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="25" y="22" fill="var(--success)" font-size="11" font-weight="900">INITIAL STABLE STATE (Direct Link B-C is UP, cost=1)</text>

        <!-- Nodes -->
        <circle cx="120" cy="42" r="16" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="120" y="46" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">A</text>

        <line x1="136" y1="42" x2="334" y2="42" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="235" y="36" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">cost = 1</text>

        <circle cx="350" cy="42" r="16" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="350" y="46" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">B</text>

        <line x1="366" y1="42" x2="564" y2="42" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="465" y="36" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">cost = 1</text>

        <circle cx="580" cy="42" r="16" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
        <text x="580" y="46" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">C (Dest)</text>

        <!-- Routing Knowledge -->
        <rect x="650" y="15" width="210" height="36" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="755" y="31" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">B: d_B(C) = 1 (direct via C)</text>
        <text x="755" y="45" fill="var(--success)" font-size="9.5" font-weight="900" text-anchor="middle">A: d_A(C) = 2 (via B)</text>
      </g>

      <!-- LINK BREAK EVENT -->
      <g transform="translate(470, 95)">
        <text x="25" y="15" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">💥 LINK B-C CUTS OUT!</text>
      </g>

      <!-- TIMELINE OF RECURSIVE POISON -->
      <g transform="translate(30, 120)">
        <rect width="880" height="225" rx="8" fill="var(--bg-card)" stroke="var(--danger)" stroke-width="1.5"/>

        <!-- Iteration 1 -->
        <g transform="translate(20, 15)">
          <rect width="840" height="42" rx="4" fill="var(--danger-dim)" stroke="none"/>
          <circle cx="20" cy="21" r="10" fill="var(--danger)" stroke="none"/>
          <text x="20" y="25" fill="#fff" font-size="9" font-weight="900" text-anchor="middle">1</text>
          <text x="40" y="18" fill="var(--danger)" font-size="10.5" font-weight="900">B Detects Failure:</text>
          <text x="40" y="33" fill="var(--tx-muted)" font-size="9.5">Direct link to C is dead. But B remembers A advertised d_A(C) = 2!</text>
          <text x="470" y="26" fill="var(--tx-primary)" font-size="10" font-weight="800">B sets d_B(C) = c(B,A) + d_A(C) = 1 + 2 = <span style="color:var(--danger)">3 via A</span></text>
        </g>

        <!-- Iteration 2 -->
        <g transform="translate(20, 65)">
          <rect width="840" height="42" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <circle cx="20" cy="21" r="10" fill="var(--warning)" stroke="none"/>
          <text x="20" y="25" fill="#000" font-size="9" font-weight="900" text-anchor="middle">2</text>
          <text x="40" y="18" fill="var(--warning)" font-size="10.5" font-weight="900">B Advertises d_B(C) = 3 to A:</text>
          <text x="40" y="33" fill="var(--tx-muted)" font-size="9.5">A thinks B found an alternate detour path to C!</text>
          <text x="470" y="26" fill="var(--tx-primary)" font-size="10" font-weight="800">A updates d_A(C) = c(A,B) + d_B(C) = 1 + 3 = <span style="color:var(--warning)">4 via B</span></text>
        </g>

        <!-- Iteration 3 -->
        <g transform="translate(20, 115)">
          <rect width="840" height="42" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
          <circle cx="20" cy="21" r="10" fill="var(--danger)" stroke="none"/>
          <text x="20" y="25" fill="#fff" font-size="9" font-weight="900" text-anchor="middle">3</text>
          <text x="40" y="18" fill="var(--danger)" font-size="10.5" font-weight="900">A Advertises d_A(C) = 4 to B:</text>
          <text x="40" y="33" fill="var(--tx-muted)" font-size="9.5">B recalculates based on A's fresh vector:</text>
          <text x="470" y="26" fill="var(--tx-primary)" font-size="10" font-weight="800">B updates d_B(C) = c(B,A) + d_A(C) = 1 + 4 = <span style="color:var(--danger)">5 via A</span></text>
        </g>

        <!-- Infinite Loop Summary -->
        <g transform="translate(20, 165)">
          <rect width="840" height="45" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.2"/>
          <text x="420" y="22" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">
            MUTUAL CIRCULAR RECURSION: &nbsp; A ➔ B ➔ A ➔ B ➔ A ➔ B (Packets ping-pong until TTL expires!)
          </text>
          <text x="420" y="38" fill="var(--tx-primary)" font-size="9.5" text-anchor="middle">
            In RIP, cost increments slowly by 1 until reaching <strong>Infinity = 16</strong> (requiring up to 16 update rounds = minutes of outage!).
          </text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Split Horizon & Poison Reverse
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🛡️</span>
      <span class="diagram-title">Figure 13.4: Loop Mitigation — Simple Split Horizon vs. Poisoned Reverse</span>
    </div>
    <span class="diagram-badge">SPLIT HORIZON</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-sh-pass" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
        <marker id="arr-sh-fail" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: SIMPLE SPLIT HORIZON (SILENCE) -->
      <g transform="translate(30, 25)">
        <rect width="420" height="270" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="210" y="28" fill="var(--accent)" font-size="13" font-weight="900" text-anchor="middle">1. SIMPLE SPLIT HORIZON</text>
        <text x="210" y="46" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">Rule: "Never advertise a route back out the interface it was learned from"</text>

        <!-- Topology Nodes -->
        <circle cx="80" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="80" y="115" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">A</text>

        <circle cx="210" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="210" y="115" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">B</text>

        <circle cx="340" cy="110" r="22" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
        <text x="340" y="115" fill="var(--info)" font-size="12" font-weight="900" text-anchor="middle">C</text>

        <!-- Routing: A learned C via B -->
        <path d="M 188 100 L 102 100" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arr-sh-pass)"/>
        <text x="145" y="90" fill="var(--success)" font-size="9" font-weight="800" text-anchor="middle">B tells A: d_B(C)=1</text>

        <!-- Suppressed Reverse Link -->
        <path d="M 102 130 L 188 130" stroke="var(--danger)" stroke-width="2" stroke-dasharray="4 3"/>
        <text x="145" y="148" fill="var(--danger)" font-size="9.5" font-weight="900" text-anchor="middle">🚫 SILENCE! (Filtered)</text>

        <rect x="25" y="180" width="370" height="75" rx="6" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1"/>
        <text x="35" y="202" fill="var(--tx-primary)" font-size="10" font-weight="800">Behavior upon B-C failure:</text>
        <text x="35" y="220" fill="var(--tx-muted)" font-size="9.5">Because A never advertised C back to B, B does NOT think A</text>
        <text x="35" y="236" fill="var(--tx-muted)" font-size="9.5">has a route. B sets d_B(C) = ∞ immediately, stopping 2-node loops!</text>
      </g>

      <!-- RIGHT: POISON REVERSE (ACTIVE POISONING) -->
      <g transform="translate(485, 25)">
        <rect width="425" height="270" rx="10" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="212" y="28" fill="var(--success)" font-size="13" font-weight="900" text-anchor="middle">2. SPLIT HORIZON WITH POISON REVERSE</text>
        <text x="212" y="46" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">Rule: "Advertise the route back to the sender, but with metric = ∞"</text>

        <!-- Topology Nodes -->
        <circle cx="80" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="80" y="115" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">A</text>

        <circle cx="210" cy="110" r="22" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="210" y="115" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">B</text>

        <circle cx="340" cy="110" r="22" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2"/>
        <text x="340" y="115" fill="var(--info)" font-size="12" font-weight="900" text-anchor="middle">C</text>

        <!-- Routing: A learned C via B -->
        <path d="M 188 100 L 102 100" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arr-sh-pass)"/>
        <text x="145" y="90" fill="var(--success)" font-size="9" font-weight="800" text-anchor="middle">B tells A: d_B(C)=1</text>

        <!-- Explicit Poison Reverse -->
        <path d="M 102 130 L 188 130" stroke="var(--danger)" stroke-width="2.5" marker-end="url(#arr-sh-fail)"/>
        <text x="145" y="152" fill="var(--danger)" font-size="9.5" font-weight="900" text-anchor="middle">A tells B: d_A(C) = ∞</text>

        <rect x="25" y="180" width="375" height="75" rx="6" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1"/>
        <text x="35" y="202" fill="var(--success)" font-size="10" font-weight="900">Why Poison Reverse is Superior:</text>
        <text x="35" y="220" fill="var(--tx-primary)" font-size="9.5">Instead of waiting for a timer to expire on B, A actively cuts</text>
        <text x="35" y="236" fill="var(--tx-primary)" font-size="9.5">the loop by confirming: "My path goes through you, so I have ∞!"</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 5. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch13_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch13">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">Distance Vector vs Link State &amp; Count-to-Infinity</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Comparative Analysis, Pathological Routing Loops, &amp; Split Horizon Derivation</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Compare Distance Vector and Link State routing algorithms across 6 core parameters. Explain the Count-to-Infinity problem with a neat mathematical trace. Describe Split Horizon and Poisoned Reverse, and explain why Split Horizon fails to prevent loops in 3-node triangular networks."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: COMPARISON TABLE -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Master Comparative Analysis: Link-State vs. Distance-Vector (4 Marks)</h4>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Comparison Dimension</th>
                  <th>Distance Vector (DV) Routing</th>
                  <th>Link-State (LS) Routing</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Underlying Algorithm</strong></td>
                  <td>Distributed Bellman-Ford algorithm: $d_x(y) = \min_v \{c(x,v) + d_v(y)\}$</td>
                  <td>Centralized Dijkstra Shortest Path First (SPF) algorithm</td>
                </tr>
                <tr>
                  <td><strong>Knowledge Representation</strong></td>
                  <td><strong>Local only:</strong> Knows cost to direct neighbors and vectors advertised by them ("Routing by Rumor")</td>
                  <td><strong>Global:</strong> Every router possesses an identical synchronized copy of the entire network graph (LSDB)</td>
                </tr>
                <tr>
                  <td><strong>Message Dissemination</strong></td>
                  <td>Exchanges entire routing table periodically <strong>only with immediate adjacent neighbors</strong></td>
                  <td>Floods small Link State Advertisements (LSAs) describing only adjacent link status to <strong>all routers in the area</strong></td>
                </tr>
                <tr>
                  <td><strong>Convergence Speed</strong></td>
                  <td>Slow; takes $O(\text{diameter})$ iterations. "Good news travels fast, bad news travels slowly"</td>
                  <td>Fast; upon receiving new LSA, Dijkstra recomputes in milliseconds</td>
                </tr>
                <tr>
                  <td><strong>Loop Vulnerability</strong></td>
                  <td>High; susceptible to transient loops and Count-to-Infinity pathologies</td>
                  <td>Inherently loop-free because all routers compute shortest path tree over an identical graph map</td>
                </tr>
                <tr>
                  <td><strong>Resource Overhead</strong></td>
                  <td>Low memory (stores only neighbor vectors) and minimal CPU requirements</td>
                  <td>High memory (stores full LSDB) and intensive CPU usage for Dijkstra recalculations</td>
                </tr>
                <tr>
                  <td><strong>Real-World Protocols</strong></td>
                  <td>RIPv1/v2, IGRP, BGP (Path Vector variant)</td>
                  <td>OSPFv2/v3, IS-IS</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 2: COUNT-TO-INFINITY TRACE -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Mathematical Derivation of Count-to-Infinity (3 Marks)</h4>
          <p>
            Consider a linear 3-router topology: <strong>A —(1)— B —(1)— C</strong>. Destination is router <strong>C</strong>.
          </p>
          <ul class="blueprint-list">
            <li><strong>Initial Steady State:</strong> $d_B(C) = 1$ (next-hop $C$), $d_A(C) = 2$ (next-hop $B$).</li>
            <li><strong>Failure Event:</strong> The physical link between $B$ and $C$ is severed ($c(B,C) = \infty$).</li>
            <li><strong>Iteration 1:</strong> Router $B$ loses direct connectivity to $C$. It checks neighbor advertisements. Router $A$ previously advertised $d_A(C) = 2$. Unaware that $A$'s route passes back through $B$, $B$ calculates:
              $$d_B(C) = c(B, A) + d_A(C) = 1 + 2 = 3 \quad (\text{Next Hop: } A)$$
            </li>
            <li><strong>Iteration 2:</strong> Router $B$ advertises $d_B(C) = 3$ to $A$. Router $A$ updates its vector:
              $$d_A(C) = c(A, B) + d_B(C) = 1 + 3 = 4 \quad (\text{Next Hop: } B)$$
            </li>
            <li><strong>Iteration $k$:</strong> Each node continuously reinforces the other's rumor, incrementing distance by $1$ per cycle until reaching the protocol infinity threshold ($\infty = 16$ in RIP).</li>
          </ul>
        </div>

        <!-- SECTION 3: SPLIT HORIZON & POISON REVERSE -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Mitigation Mechanisms &amp; The 3-Node Triangular Trap (3 Marks)</h4>
          <div class="blueprint-grid">
            <div class="blueprint-col">
              <h5>Split Horizon with Poison Reverse</h5>
              <ul>
                <li><strong>Simple Split Horizon:</strong> If router $A$ routes traffic to destination $C$ via neighbor $B$, $A$ will never advertise a route for $C$ back to $B$.</li>
                <li><strong>Poison Reverse:</strong> Instead of omitting the route, $A$ explicitly advertises $d_A(C) = \infty$ to $B$. This immediately breaks 2-node circular dependencies without waiting for dead timers.</li>
              </ul>
            </div>
            <div class="blueprint-col">
              <h5>The Triangular Failure Trap</h5>
              <ul>
                <li><strong>Why Split Horizon Fails in Triangles:</strong> If three routers $A, B, C$ form a triangle with destination $X$ connected to $A$:
                  When link $A-X$ breaks, $B$ will not advertise to $A$, and $C$ will not advertise to $A$. However, <strong>$B$ can still advertise its route to $C$, and $C$ can advertise its route to $B$</strong>!
                </li>
                <li>A 3-node loop forms around the cycle $B \to C \to B$, rendering simple Split Horizon ineffective. Distance vector protocols must rely on <strong>Holddown Timers</strong> or transition to Path-Vector / Link-State designs.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- EXAM PITFALL WARNING -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency University Exam Trap:</strong>
            Students frequently write that <em>"RIP sets infinity to 16 because of 4-bit integer limits ($2^4=16$)."</em> This is technically false! 16 was selected by protocol designers as an engineering compromise between maximum network diameter (hop count limit) and the time required for Count-to-Infinity to terminate (at 30s per update, 16 steps = up to 8 minutes).
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 13
# ==========================================

# 1. Replace ASCII diagram in s13-overview with Figure 13.1
match_s13_ov = re.search(r'(<section id="s13-overview"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s13_ov:
    content = content[:match_s13_ov.start(2)] + svg_diagram_1 + content[match_s13_ov.end(2):]
    print('Replaced ASCII diagram in s13-overview with Figure 13.1')
else:
    print('Warning: could not find ASCII diagram in s13-overview')

# 2. Insert Figure 13.2 in s13-bellman
match_s13_bm = re.search(r'(<section id="s13-bellman"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s13_bm:
    content = content[:match_s13_bm.start(2)] + svg_diagram_2 + '\n\n      ' + content[match_s13_bm.start(2):]
    print('Inserted Figure 13.2 in s13-bellman')
else:
    print('Warning: could not find insertion spot in s13-bellman')

# 3. Insert Figure 13.3 in s13-count
match_s13_cnt = re.search(r'(<section id="s13-count"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s13_cnt:
    content = content[:match_s13_cnt.start(2)] + svg_diagram_3 + '\n\n      ' + content[match_s13_cnt.start(2):]
    print('Inserted Figure 13.3 in s13-count')
else:
    print('Warning: could not find insertion spot in s13-count')

# 4. Insert Figure 13.4 in s13-loop-prevention
match_s13_lp = re.search(r'(<section id="s13-loop-prevention"[^>]*>.*?)(<div class="concept-card">)', content, flags=re.DOTALL)
if match_s13_lp:
    content = content[:match_s13_lp.start(2)] + svg_diagram_4 + '\n\n      ' + content[match_s13_lp.start(2):]
    print('Inserted Figure 13.4 in s13-loop-prevention')
else:
    print('Warning: could not find insertion spot in s13-loop-prevention')

# 5. Insert DU 10-Mark Blueprint before study-resources in s13-summary
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch13_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 13!')
else:
    print('Warning: could not find .study-resources in Chapter 13')

with open(ch13_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 13 upgrade completed!')
