"""
Upgrade Chapter 12 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch12_path = '/Users/arpit/minibook/cn/chapters/ch12-shortest-path-routing.html'
with open(ch12_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Network Graph & Cost Model
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🌐</span>
      <span class="diagram-title">Figure 12.1: Physical Network Topology Mapped to Weighted Directed/Undirected Graph</span>
    </div>
    <span class="diagram-badge">GRAPH MODEL</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-ch12-1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="320" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: PHYSICAL TOPOLOGY -->
      <g transform="translate(30, 30)">
        <rect width="400" height="270" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="200" y="30" fill="var(--accent)" font-size="13" font-weight="800" text-anchor="middle">Physical Infrastructure</text>
        <text x="200" y="48" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Layer-3 Routers &amp; High-Speed Fiber/Copper Trunks</text>

        <!-- Router Nodes -->
        <!-- Router A -->
        <circle cx="80" cy="110" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="80" y="115" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">R1</text>
        <text x="80" y="145" fill="var(--tx-muted)" font-size="9" text-anchor="middle">10.0.1.1</text>

        <!-- Router B -->
        <circle cx="200" cy="80" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="200" y="85" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">R2</text>
        <text x="200" y="115" fill="var(--tx-muted)" font-size="9" text-anchor="middle">10.0.2.1</text>

        <!-- Router C -->
        <circle cx="320" cy="110" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="320" y="115" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">R3</text>
        <text x="320" y="145" fill="var(--tx-muted)" font-size="9" text-anchor="middle">10.0.3.1</text>

        <!-- Router D -->
        <circle cx="120" cy="210" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="120" y="215" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">R4</text>
        <text x="120" y="245" fill="var(--tx-muted)" font-size="9" text-anchor="middle">10.0.4.1</text>

        <!-- Router E -->
        <circle cx="280" cy="210" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
        <text x="280" y="215" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">R5</text>
        <text x="280" y="245" fill="var(--tx-muted)" font-size="9" text-anchor="middle">10.0.5.1</text>

        <!-- Links with Capacities -->
        <line x1="102" y1="102" x2="178" y2="88" stroke="var(--tx-muted)" stroke-width="2"/>
        <text x="140" y="90" fill="var(--info)" font-size="9" font-weight="700">10 Gbps</text>

        <line x1="222" y1="88" x2="298" y2="102" stroke="var(--tx-muted)" stroke-width="2"/>
        <text x="260" y="90" fill="var(--info)" font-size="9" font-weight="700">10 Gbps</text>

        <line x1="90" y1="132" x2="110" y2="188" stroke="var(--tx-muted)" stroke-width="2"/>
        <text x="80" y="165" fill="var(--warning)" font-size="9" font-weight="700">1 Gbps</text>

        <line x1="142" y1="210" x2="258" y2="210" stroke="var(--tx-muted)" stroke-width="2"/>
        <text x="200" y="202" fill="var(--danger)" font-size="9" font-weight="700">100 Mbps</text>

        <line x1="310" y1="132" x2="290" y2="188" stroke="var(--tx-muted)" stroke-width="2"/>
        <text x="310" y="165" fill="var(--info)" font-size="9" font-weight="700">10 Gbps</text>
      </g>

      <!-- MIDDLE TRANSFORMATION ARROW -->
      <g transform="translate(445, 130)">
        <path d="M 0 35 L 45 35" stroke="var(--accent)" stroke-width="4" marker-end="url(#arr-ch12-1)"/>
        <text x="25" y="20" fill="var(--accent)" font-size="10" font-weight="800" text-anchor="middle">ABSTRACTION</text>
        <text x="25" y="60" fill="var(--tx-muted)" font-size="9" text-anchor="middle">Cost = 100M/BW</text>
      </g>

      <!-- RIGHT: WEIGHTED GRAPH G = (V, E, W) -->
      <g transform="translate(510, 30)">
        <rect width="400" height="270" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="200" y="30" fill="var(--success)" font-size="13" font-weight="800" text-anchor="middle">Mathematical Graph G = (V, E, W)</text>
        <text x="200" y="48" fill="var(--tx-muted)" font-size="10" text-anchor="middle">Vertices = {R1..R5}, Edges with Scalar OSPF Metrics</text>

        <!-- Vertices -->
        <circle cx="80" cy="110" r="20" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="80" y="115" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">u</text>

        <circle cx="200" cy="80" r="20" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="200" y="85" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">v</text>

        <circle cx="320" cy="110" r="20" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="320" y="115" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">w</text>

        <circle cx="120" cy="210" r="20" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="120" y="215" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">x</text>

        <circle cx="280" cy="210" r="20" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="280" y="215" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">y</text>

        <!-- Edges with Weights -->
        <line x1="98" y1="103" x2="182" y2="87" stroke="var(--accent)" stroke-width="2.5"/>
        <circle cx="140" cy="95" r="11" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="140" y="99" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">1</text>

        <line x1="218" y1="87" x2="302" y2="103" stroke="var(--accent)" stroke-width="2.5"/>
        <circle cx="260" cy="95" r="11" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="260" y="99" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">1</text>

        <line x1="88" y1="128" x2="112" y2="192" stroke="var(--accent)" stroke-width="2.5"/>
        <circle cx="100" cy="160" r="11" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="100" y="164" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">2</text>

        <line x1="140" y1="210" x2="260" y2="210" stroke="var(--accent)" stroke-width="2.5"/>
        <circle cx="200" cy="210" r="11" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="200" y="214" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">10</text>

        <line x1="312" y1="128" x2="288" y2="192" stroke="var(--accent)" stroke-width="2.5"/>
        <circle cx="300" cy="160" r="11" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="300" y="164" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">1</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: Greedy Frontier Expansion & Relaxation
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚡</span>
      <span class="diagram-title">Figure 12.2: Dijkstra's Greedy Frontier Partition &amp; Edge Relaxation Triangle</span>
    </div>
    <span class="diagram-badge">GREEDY FRONTIER</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 330" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-relax" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arr-cut" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--warning)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="310" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT REGION: PERMANENT SET N' -->
      <g transform="translate(30, 25)">
        <rect width="380" height="280" rx="10" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.8" stroke-dasharray="4 2"/>
        <text x="25" y="32" fill="var(--accent)" font-size="12" font-weight="800">PERMANENT SET N\' (Finalized Shortest Paths)</text>
        <text x="25" y="48" fill="var(--tx-muted)" font-size="9.5">Shortest distance D(u) proven optimal; will NEVER change</text>

        <!-- Source Node -->
        <circle cx="70" cy="150" r="26" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="70" y="148" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">s (Source)</text>
        <text x="70" y="162" fill="var(--tx-muted)" font-size="9" text-anchor="middle">D(s) = 0</text>

        <!-- Finished Intermediate Node -->
        <circle cx="240" cy="90" r="24" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="240" y="88" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">Node a</text>
        <text x="240" y="102" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">D(a) = 3</text>

        <!-- Boundary Permanent Node u -->
        <circle cx="310" cy="190" r="26" fill="var(--bg-card)" stroke="var(--success)" stroke-width="2.5"/>
        <text x="310" y="188" fill="var(--success)" font-size="12" font-weight="900" text-anchor="middle">Node u</text>
        <text x="310" y="202" fill="var(--success)" font-size="9.5" font-weight="800" text-anchor="middle">D(u) = 5</text>

        <!-- Internal Paths -->
        <path d="M 96 140 L 216 100" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-relax)"/>
        <path d="M 96 160 L 284 185" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-relax)"/>
      </g>

      <!-- FRONTIER CUT LINE -->
      <line x1="440" y1="20" x2="440" y2="310" stroke="var(--warning)" stroke-width="2" stroke-dasharray="6 4"/>
      <rect x="420" y="150" width="40" height="24" rx="4" fill="var(--warning)" stroke="none"/>
      <text x="440" y="166" fill="#000" font-size="10" font-weight="900" text-anchor="middle">CUT</text>

      <!-- RIGHT REGION: UNVISITED SET V \ N' -->
      <g transform="translate(470, 25)">
        <rect width="440" height="280" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="25" y="32" fill="var(--tx-primary)" font-size="12" font-weight="800">UNVISITED SET V \\ N\' (Tentative Distances)</text>
        <text x="25" y="48" fill="var(--tx-muted)" font-size="9.5">Distances are upper bounds; refined continuously via relaxation</text>

        <!-- Target Vertex v -->
        <circle cx="160" cy="190" r="28" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="2.5"/>
        <text x="160" y="186" fill="var(--tx-primary)" font-size="12" font-weight="900" text-anchor="middle">Target v</text>
        <text x="160" y="200" fill="var(--warning)" font-size="9.5" font-weight="800" text-anchor="middle">D(v): 10 ➔ 7</text>

        <!-- Distant Unvisited Node z -->
        <circle cx="340" cy="120" r="22" fill="var(--bg-surface)" stroke="var(--tx-muted)" stroke-width="1.5"/>
        <text x="340" y="118" fill="var(--tx-primary)" font-size="11" font-weight="700" text-anchor="middle">Node z</text>
        <text x="340" y="132" fill="var(--tx-muted)" font-size="9" text-anchor="middle">D(z) = ∞</text>

        <!-- Old Sub-optimal Path from Source -->
        <path d="M -374 150 Q -100 20 136 172" fill="none" stroke="var(--danger)" stroke-width="1.8" stroke-dasharray="4 3"/>
        <rect x="20" y="70" width="130" height="24" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1"/>
        <text x="85" y="86" fill="var(--danger)" font-size="9" font-weight="700" text-anchor="middle">Old Path: D(v) = 10</text>

        <!-- Edge Relaxation Box -->
        <g transform="translate(140, 225)">
          <rect width="270" height="45" rx="6" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.2"/>
          <text x="135" y="18" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">RELAXATION CONDITION</text>
          <text x="135" y="34" fill="var(--tx-primary)" font-size="9.5" text-anchor="middle">if (D(u) + c(u,v) &lt; D(v)) ➔ D(v) = 5 + 2 = 7</text>
        </g>
      </g>

      <!-- RELAXATION EDGE CROSSING THE CUT -->
      <path d="M 336 215 L 602 215" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-cut)"/>
      <rect x="445" y="202" width="60" height="24" rx="4" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
      <text x="475" y="218" fill="var(--success)" font-size="10" font-weight="900" text-anchor="middle">c(u,v) = 2</text>
    </svg>
  </div>
</div>'''

# ==========================================
# 3. DIAGRAM 3: Benchmark 6-Node Topology
# ==========================================
svg_diagram_3 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🗺️</span>
      <span class="diagram-title">Figure 12.3: Canonical 6-Node Benchmark University Topology (Routers u, v, w, x, y, z)</span>
    </div>
    <span class="diagram-badge">BENCHMARK TOPOLOGY</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="340" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LINKS (Lines connecting vertices) -->
      <!-- u-v (cost 2) -->
      <line x1="160" y1="180" x2="350" y2="80" stroke="var(--border)" stroke-width="3"/>
      <circle cx="255" cy="130" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="255" y="135" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">2</text>

      <!-- u-x (cost 1) -->
      <line x1="160" y1="180" x2="350" y2="280" stroke="var(--border)" stroke-width="3"/>
      <circle cx="255" cy="230" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="255" y="235" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">1</text>

      <!-- u-w (cost 5) -->
      <line x1="160" y1="180" x2="580" y2="80" stroke="var(--border)" stroke-width="2" stroke-dasharray="4 3"/>
      <circle cx="340" cy="140" r="14" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.5"/>
      <text x="340" y="145" fill="var(--warning)" font-size="12" font-weight="900" text-anchor="middle">5</text>

      <!-- v-w (cost 3) -->
      <line x1="350" y1="80" x2="580" y2="80" stroke="var(--border)" stroke-width="3"/>
      <circle cx="465" cy="80" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="465" y="85" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">3</text>

      <!-- v-x (cost 2) -->
      <line x1="350" y1="80" x2="350" y2="280" stroke="var(--border)" stroke-width="3"/>
      <circle cx="350" cy="180" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="350" y="185" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">2</text>

      <!-- x-w (cost 3) -->
      <line x1="350" y1="280" x2="580" y2="80" stroke="var(--border)" stroke-width="3"/>
      <circle cx="445" cy="165" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="445" y="170" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">3</text>

      <!-- x-y (cost 1) -->
      <line x1="350" y1="280" x2="580" y2="280" stroke="var(--border)" stroke-width="3"/>
      <circle cx="465" cy="280" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="465" y="285" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">1</text>

      <!-- w-y (cost 1) -->
      <line x1="580" y1="80" x2="580" y2="280" stroke="var(--border)" stroke-width="3"/>
      <circle cx="580" cy="180" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="580" y="185" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">1</text>

      <!-- w-z (cost 5) -->
      <line x1="580" y1="80" x2="780" y2="180" stroke="var(--border)" stroke-width="2" stroke-dasharray="4 3"/>
      <circle cx="680" cy="130" r="14" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.5"/>
      <text x="680" y="135" fill="var(--warning)" font-size="12" font-weight="900" text-anchor="middle">5</text>

      <!-- y-z (cost 2) -->
      <line x1="580" y1="280" x2="780" y2="180" stroke="var(--border)" stroke-width="3"/>
      <circle cx="680" cy="230" r="14" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="680" y="235" fill="var(--accent)" font-size="12" font-weight="900" text-anchor="middle">2</text>

      <!-- ROUTER VERTICES -->
      <!-- Source u -->
      <circle cx="160" cy="180" r="32" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="3"/>
      <text x="160" y="178" fill="var(--accent)" font-size="16" font-weight="900" text-anchor="middle">u</text>
      <text x="160" y="196" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">SOURCE</text>

      <!-- Node v -->
      <circle cx="350" cy="80" r="28" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
      <text x="350" y="86" fill="var(--tx-primary)" font-size="16" font-weight="900" text-anchor="middle">v</text>

      <!-- Node x -->
      <circle cx="350" cy="280" r="28" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
      <text x="350" y="286" fill="var(--tx-primary)" font-size="16" font-weight="900" text-anchor="middle">x</text>

      <!-- Node w -->
      <circle cx="580" cy="80" r="28" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
      <text x="580" y="86" fill="var(--tx-primary)" font-size="16" font-weight="900" text-anchor="middle">w</text>

      <!-- Node y -->
      <circle cx="580" cy="280" r="28" fill="var(--bg-card)" stroke="var(--info)" stroke-width="2.5"/>
      <text x="580" y="286" fill="var(--tx-primary)" font-size="16" font-weight="900" text-anchor="middle">y</text>

      <!-- Node z -->
      <circle cx="780" cy="180" r="32" fill="var(--success-dim)" stroke="var(--success)" stroke-width="3"/>
      <text x="780" y="178" fill="var(--success)" font-size="16" font-weight="900" text-anchor="middle">z</text>
      <text x="780" y="196" fill="var(--tx-muted)" font-size="10" font-weight="700" text-anchor="middle">DEST</text>
    </svg>
  </div>
</div>'''

# ==========================================
# 4. DIAGRAM 4: Shortest Path Tree & FIB Table
# ==========================================
svg_diagram_4 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🌲</span>
      <span class="diagram-title">Figure 12.4: Shortest Path Tree (SPT) Rooted at u &amp; Resulting Layer-3 Forwarding Table</span>
    </div>
    <span class="diagram-badge">SPT &amp; FIB</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 350" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-spt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="330" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- LEFT: SHORTEST PATH TREE -->
      <g transform="translate(30, 25)">
        <rect width="470" height="295" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="235" y="28" fill="var(--success)" font-size="13" font-weight="800" text-anchor="middle">Shortest Path Tree Rooted at u</text>
        <text x="235" y="44" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">Tree Edges (In SPT) vs Non-Tree Edges (Discarded/Pruned)</text>

        <!-- Discarded edges dashed -->
        <line x1="80" y1="160" x2="330" y2="80" stroke="var(--tx-muted)" stroke-width="1.2" stroke-dasharray="3 3"/>
        <line x1="200" y1="80" x2="330" y2="80" stroke="var(--tx-muted)" stroke-width="1.2" stroke-dasharray="3 3"/>
        <line x1="200" y1="240" x2="330" y2="80" stroke="var(--tx-muted)" stroke-width="1.2" stroke-dasharray="3 3"/>
        <line x1="330" y1="80" x2="420" y2="160" stroke="var(--tx-muted)" stroke-width="1.2" stroke-dasharray="3 3"/>

        <!-- Tree Edges (Green Bold) -->
        <!-- u -> x (1) -->
        <path d="M 98 172 L 182 228" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-spt)"/>
        <text x="135" y="195" fill="var(--success)" font-size="10" font-weight="900">cost 1</text>

        <!-- u -> v (2) -->
        <path d="M 98 148 L 182 92" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-spt)"/>
        <text x="135" y="125" fill="var(--success)" font-size="10" font-weight="900">cost 2</text>

        <!-- x -> y (1) -->
        <path d="M 228 240 L 312 240" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-spt)"/>
        <text x="265" y="232" fill="var(--success)" font-size="10" font-weight="900">cost 1</text>

        <!-- y -> w (1) -->
        <path d="M 330 216 L 330 104" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-spt)"/>
        <text x="340" y="165" fill="var(--success)" font-size="10" font-weight="900">cost 1</text>

        <!-- y -> z (2) -->
        <path d="M 348 228 L 402 172" stroke="var(--success)" stroke-width="3" marker-end="url(#arr-spt)"/>
        <text x="385" y="212" fill="var(--success)" font-size="10" font-weight="900">cost 2</text>

        <!-- Vertices -->
        <circle cx="80" cy="160" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="80" y="165" fill="var(--accent)" font-size="13" font-weight="900" text-anchor="middle">u (0)</text>

        <circle cx="200" cy="80" r="22" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="200" y="85" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">v (2)</text>

        <circle cx="200" cy="240" r="22" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="200" y="245" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">x (1)</text>

        <circle cx="330" cy="240" r="22" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="330" y="245" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">y (2)</text>

        <circle cx="330" cy="80" r="22" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2"/>
        <text x="330" y="85" fill="var(--tx-primary)" font-size="12" font-weight="800" text-anchor="middle">w (3)</text>

        <circle cx="420" cy="160" r="24" fill="var(--success-dim)" stroke="var(--success)" stroke-width="2.5"/>
        <text x="420" y="165" fill="var(--success)" font-size="13" font-weight="900" text-anchor="middle">z (4)</text>
      </g>

      <!-- RIGHT: FIB FORWARDING TABLE -->
      <g transform="translate(520, 25)">
        <rect width="390" height="295" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="195" y="28" fill="var(--accent)" font-size="13" font-weight="800" text-anchor="middle">Router u Forwarding Table (FIB)</text>
        <text x="195" y="44" fill="var(--tx-muted)" font-size="9.5" text-anchor="middle">Extracted from SPT Predecessor Backtracking</text>

        <!-- Table Header -->
        <rect x="20" y="60" width="350" height="32" rx="4" fill="var(--accent-dim)" stroke="var(--border)" stroke-width="1"/>
        <text x="60" y="80" fill="var(--accent)" font-size="10.5" font-weight="900" text-anchor="middle">Dest</text>
        <text x="130" y="80" fill="var(--accent)" font-size="10.5" font-weight="900" text-anchor="middle">Total Cost</text>
        <text x="210" y="80" fill="var(--accent)" font-size="10.5" font-weight="900" text-anchor="middle">Next Hop</text>
        <text x="305" y="80" fill="var(--accent)" font-size="10.5" font-weight="900" text-anchor="middle">Interface</text>

        <!-- Row 1: v -->
        <line x1="20" y1="130" x2="370" y2="130" stroke="var(--border)" stroke-width="1"/>
        <text x="60" y="115" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">v</text>
        <text x="130" y="115" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">2</text>
        <text x="210" y="115" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">v</text>
        <text x="305" y="115" fill="var(--tx-muted)" font-size="10" text-anchor="middle">eth0</text>

        <!-- Row 2: x -->
        <line x1="20" y1="170" x2="370" y2="170" stroke="var(--border)" stroke-width="1"/>
        <text x="60" y="155" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">x</text>
        <text x="130" y="155" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">1</text>
        <text x="210" y="155" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">x</text>
        <text x="305" y="155" fill="var(--tx-muted)" font-size="10" text-anchor="middle">eth1</text>

        <!-- Row 3: y -->
        <line x1="20" y1="210" x2="370" y2="210" stroke="var(--border)" stroke-width="1"/>
        <text x="60" y="195" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">y</text>
        <text x="130" y="195" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">2</text>
        <text x="210" y="195" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">x</text>
        <text x="305" y="195" fill="var(--tx-muted)" font-size="10" text-anchor="middle">eth1</text>

        <!-- Row 4: w -->
        <line x1="20" y1="250" x2="370" y2="250" stroke="var(--border)" stroke-width="1"/>
        <text x="60" y="235" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">w</text>
        <text x="130" y="235" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">3</text>
        <text x="210" y="235" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">x</text>
        <text x="305" y="235" fill="var(--tx-muted)" font-size="10" text-anchor="middle">eth1</text>

        <!-- Row 5: z -->
        <text x="60" y="275" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">z</text>
        <text x="130" y="275" fill="var(--success)" font-size="11" font-weight="800" text-anchor="middle">4</text>
        <text x="210" y="275" fill="var(--info)" font-size="11" font-weight="800" text-anchor="middle">x</text>
        <text x="305" y="275" fill="var(--tx-muted)" font-size="10" text-anchor="middle">eth1</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 5. DIAGRAM 5: Negative Edge Weight Failure
# ==========================================
svg_diagram_5 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚠️</span>
      <span class="diagram-title">Figure 12.5: Why Dijkstra's Greedy Paradigm Fails with Negative Edge Weights</span>
    </div>
    <span class="diagram-badge">COUNTEREXAMPLE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-fail" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--danger)" />
        </marker>
        <marker id="arr-pass" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="290" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- 3-NODE COUNTEREXAMPLE GRAPH -->
      <g transform="translate(40, 30)">
        <rect width="450" height="250" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="225" y="26" fill="var(--danger)" font-size="12" font-weight="800" text-anchor="middle">3-Node Counterexample Topology</text>

        <!-- Direct Edge A -> B (cost 2) -->
        <path d="M 90 90 L 330 90" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-pass)"/>
        <circle cx="210" cy="90" r="13" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="210" y="94" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">2</text>

        <!-- Edge A -> C (cost 5) -->
        <path d="M 80 120 L 200 200" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-pass)"/>
        <circle cx="140" cy="160" r="13" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="140" y="164" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">5</text>

        <!-- Negative Edge C -> B (cost -4) -->
        <path d="M 230 200 L 335 125" stroke="var(--danger)" stroke-width="3" marker-end="url(#arr-fail)"/>
        <circle cx="285" cy="160" r="15" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
        <text x="285" y="164" fill="var(--danger)" font-size="11" font-weight="900" text-anchor="middle">-4</text>

        <!-- Nodes -->
        <circle cx="70" cy="100" r="24" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2.5"/>
        <text x="70" y="105" fill="var(--accent)" font-size="13" font-weight="900" text-anchor="middle">A (Src)</text>

        <circle cx="350" cy="100" r="24" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="2.5"/>
        <text x="350" y="105" fill="var(--danger)" font-size="13" font-weight="900" text-anchor="middle">B</text>

        <circle cx="220" cy="210" r="24" fill="var(--info-dim)" stroke="var(--info)" stroke-width="2.5"/>
        <text x="220" y="215" fill="var(--info)" font-size="13" font-weight="900" text-anchor="middle">C</text>
      </g>

      <!-- RIGHT: STEP-BY-STEP EXPLANATION -->
      <g transform="translate(510, 30)">
        <rect width="390" height="250" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.2"/>
        <text x="195" y="26" fill="var(--accent)" font-size="12" font-weight="800" text-anchor="middle">Greedy Failure Trace</text>

        <g transform="translate(20, 45)">
          <!-- Step 1 -->
          <circle cx="15" cy="15" r="10" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
          <text x="15" y="19" fill="var(--accent)" font-size="10" font-weight="900" text-anchor="middle">1</text>
          <text x="35" y="14" fill="var(--tx-primary)" font-size="10.5" font-weight="700">Dijkstra Evaluates Neighbors of A:</text>
          <text x="35" y="28" fill="var(--tx-muted)" font-size="9.5">Tentative D(B) = 2, D(C) = 5. Minimum is B (2).</text>

          <!-- Step 2 -->
          <circle cx="15" cy="65" r="10" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="15" y="69" fill="var(--danger)" font-size="10" font-weight="900" text-anchor="middle">2</text>
          <text x="35" y="64" fill="var(--danger)" font-size="10.5" font-weight="800">Premature Commitment to Permanent Set N\':</text>
          <text x="35" y="78" fill="var(--tx-muted)" font-size="9.5">Dijkstra permanently freezes D(B) = 2. It will NEVER be relaxed!</text>

          <!-- Step 3 -->
          <circle cx="15" cy="115" r="10" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="15" y="119" fill="var(--info)" font-size="10" font-weight="900" text-anchor="middle">3</text>
          <text x="35" y="114" fill="var(--tx-primary)" font-size="10.5" font-weight="700">Next Iteration Visits Node C:</text>
          <text x="35" y="128" fill="var(--tx-muted)" font-size="9.5">Finds path A ➔ C ➔ B with total cost = 5 + (-4) = 1 &lt; 2!</text>

          <!-- Step 4 -->
          <circle cx="15" cy="165" r="10" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="15" y="169" fill="var(--warning)" font-size="10" font-weight="900" text-anchor="middle">4</text>
          <text x="35" y="164" fill="var(--warning)" font-size="10.5" font-weight="800">Algorithmic Breakdown &amp; Solution:</text>
          <text x="35" y="178" fill="var(--tx-muted)" font-size="9.5">Dijkstra outputs sub-optimal cost 2 instead of 1.</text>
          <text x="35" y="192" fill="var(--success)" font-size="9.5" font-weight="700">Solution: Use Bellman-Ford algorithm O(|V|·|E|) instead.</text>
        </g>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 6. DIAGRAM 6: OSPF / Link-State Operational Pipeline
# ==========================================
svg_diagram_6 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚙️</span>
      <span class="diagram-title">Figure 12.6: The Link-State (OSPF) Operational Pipeline — From Hello to FIB Installation</span>
    </div>
    <span class="diagram-badge">OSPF PIPELINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-pipe" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="260" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- STEP 1: HELLO -->
      <g transform="translate(30, 35)">
        <rect width="195" height="195" rx="8" fill="var(--bg-card)" stroke="var(--info)" stroke-width="1.5"/>
        <circle cx="30" cy="30" r="14" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
        <text x="30" y="34" fill="var(--info)" font-size="11" font-weight="900" text-anchor="middle">1</text>
        <text x="55" y="34" fill="var(--info)" font-size="11" font-weight="800">Neighbor Discovery</text>
        <text x="20" y="65" fill="var(--tx-primary)" font-size="10" font-weight="700">OSPF HELLO Packets</text>
        <text x="20" y="85" fill="var(--tx-muted)" font-size="9">Sent periodically on all links (multicast 224.0.0.5).</text>
        <text x="20" y="110" fill="var(--tx-muted)" font-size="9">Discovers direct neighbors and establishes two-way adjacencies.</text>
        <rect x="15" y="145" width="165" height="35" rx="4" fill="var(--info-dim)" stroke="none"/>
        <text x="97" y="167" fill="var(--info)" font-size="9" font-weight="800" text-anchor="middle">Neighbor Table Built</text>
      </g>

      <!-- PIPE ARROW 1-2 -->
      <path d="M 230 130 L 255 130" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-pipe)"/>

      <!-- STEP 2: LSA FLOODING -->
      <g transform="translate(260, 35)">
        <rect width="195" height="195" rx="8" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.5"/>
        <circle cx="30" cy="30" r="14" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="1.5"/>
        <text x="30" y="34" fill="var(--accent)" font-size="11" font-weight="900" text-anchor="middle">2</text>
        <text x="55" y="34" fill="var(--accent)" font-size="11" font-weight="800">LSA Flooding</text>
        <text x="20" y="65" fill="var(--tx-primary)" font-size="10" font-weight="700">Link-State Advertisements</text>
        <text x="20" y="85" fill="var(--tx-muted)" font-size="9">Each router creates LSA describing local links and costs.</text>
        <text x="20" y="110" fill="var(--tx-muted)" font-size="9">Flooded reliably to every other router in the OSPF area.</text>
        <rect x="15" y="145" width="165" height="35" rx="4" fill="var(--accent-dim)" stroke="none"/>
        <text x="97" y="167" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">Area-Wide Flooding</text>
      </g>

      <!-- PIPE ARROW 2-3 -->
      <path d="M 460 130 L 485 130" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-pipe)"/>

      <!-- STEP 3: LSDB SYNCHRONIZATION -->
      <g transform="translate(490, 35)">
        <rect width="195" height="195" rx="8" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.5"/>
        <circle cx="30" cy="30" r="14" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
        <text x="30" y="34" fill="var(--warning)" font-size="11" font-weight="900" text-anchor="middle">3</text>
        <text x="55" y="34" fill="var(--warning)" font-size="11" font-weight="800">LSDB Build</text>
        <text x="20" y="65" fill="var(--tx-primary)" font-size="10" font-weight="700">Synchronized Database</text>
        <text x="20" y="85" fill="var(--tx-muted)" font-size="9">Every router compiles received LSAs into identical LSDB.</text>
        <text x="20" y="110" fill="var(--tx-muted)" font-size="9">Represents complete global network graph G=(V,E,W).</text>
        <rect x="15" y="145" width="165" height="35" rx="4" fill="var(--warning-dim)" stroke="none"/>
        <text x="97" y="167" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">Identical Map in All Nodes</text>
      </g>

      <!-- PIPE ARROW 3-4 -->
      <path d="M 690 130 L 715 130" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arr-pipe)"/>

      <!-- STEP 4: SPF CALCULATION & FIB -->
      <g transform="translate(720, 35)">
        <rect width="195" height="195" rx="8" fill="var(--bg-card)" stroke="var(--success)" stroke-width="1.5"/>
        <circle cx="30" cy="30" r="14" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
        <text x="30" y="34" fill="var(--success)" font-size="11" font-weight="900" text-anchor="middle">4</text>
        <text x="55" y="34" fill="var(--success)" font-size="11" font-weight="800">Dijkstra SPF &amp; FIB</text>
        <text x="20" y="65" fill="var(--tx-primary)" font-size="10" font-weight="700">Compute Shortest Paths</text>
        <text x="20" y="85" fill="var(--tx-muted)" font-size="9">Each router runs Dijkstra locally with itself as root.</text>
        <text x="20" y="110" fill="var(--tx-muted)" font-size="9">Extracts next-hops and installs into hardware FIB line cards.</text>
        <rect x="15" y="145" width="165" height="35" rx="4" fill="var(--success-dim)" stroke="none"/>
        <text x="97" y="167" fill="var(--success)" font-size="9" font-weight="800" text-anchor="middle">Hardware FIB Loaded</text>
      </g>
    </svg>
  </div>
</div>'''

# ==========================================
# 7. DU 10-MARK MODEL ANSWER BLUEPRINT
# ==========================================
ch12_uni_blueprint = '''
    <!-- ========================================== -->
    <!-- UNIVERSITY EXAM MASTER MODEL ANSWER: 10 MARKS -->
    <!-- ========================================== -->
    <div class="exam-blueprint-card" id="du-model-answer-ch12">
      <div class="blueprint-header">
        <div class="blueprint-badge-group">
          <span class="blueprint-tag primary">DU B.Tech / MCA Exam Blueprint</span>
          <span class="blueprint-tag score">10 Marks Guaranteed</span>
          <span class="blueprint-tag topic">Dijkstra SPF Algorithm &amp; Tabular Execution</span>
        </div>
        <h3 class="blueprint-title">Model Answer: Complete Execution, Shortest Path Tree, Forwarding Table, &amp; Complexity Derivation</h3>
        <p class="blueprint-subtitle">Standard University Question: <em>"Explain Dijkstra's shortest path algorithm. For a given 6-node network (u, v, w, x, y, z), trace the algorithm step-by-step with source node u. Construct the complete execution table, derive the Shortest Path Tree (SPT), populate the Layer-3 Forwarding Table, and prove its time complexity."</em></p>
      </div>

      <div class="blueprint-body">
        <!-- SECTION 1: FORMAL PRINCIPLES & NOTATION -->
        <div class="blueprint-section">
          <h4 class="section-title">1. Formal Algorithmic Principles &amp; Mathematical Notation (2 Marks)</h4>
          <p>
            Dijkstra's algorithm is a <strong>greedy single-source shortest path algorithm</strong> designed for directed or undirected graphs with <strong>strictly non-negative edge weights</strong> ($w(e) \ge 0, \forall e \in E$).
          </p>
          <ul class="blueprint-list">
            <li><strong>Permanent Set $N'$:</strong> The subset of vertices whose absolute minimum shortest path distances from source $s$ have been definitively determined and locked.</li>
            <li><strong>Tentative Distance $D(v)$:</strong> The current minimum cost of a path from source $s$ to vertex $v$ that passes exclusively through vertices already in $N'$.</li>
            <li><strong>Predecessor Pointer $p(v)$:</strong> The immediate parent vertex of $v$ along the current optimal path from source $s$, used to reconstruct the path via backwards traversal.</li>
            <li><strong>Relaxation Formula:</strong> In each iteration, when vertex $u^*$ with the minimum tentative distance is moved into $N'$, all its adjacent neighbors $v \notin N'$ are relaxed:
              $$D(v) \leftarrow \min \Big( D(v), \; D(u^*) + c(u^*, v) \Big)$$
              If $D(u^*) + c(u^*, v) &lt; D(v)$, then update $D(v) \leftarrow D(u^*) + c(u^*, v)$ and set $p(v) \leftarrow u^*$.
            </li>
          </ul>
        </div>

        <!-- SECTION 2: STEP-BY-STEP TABULAR TRACE -->
        <div class="blueprint-section">
          <h4 class="section-title">2. Complete Step-by-Step Execution Table (Source Node u) (4 Marks)</h4>
          <p>
            We execute the algorithm on the canonical 6-router topology: $\{u, v, w, x, y, z\}$. All edge weights: $c(u,v)=2, c(u,x)=1, c(u,w)=5, c(v,w)=3, c(v,x)=2, c(x,w)=3, c(x,y)=1, c(w,y)=1, c(w,z)=5, c(y,z)=2$.
          </p>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Step $k$</th>
                  <th>Permanent Set $N'$</th>
                  <th>$D(v), p(v)$</th>
                  <th>$D(w), p(w)$</th>
                  <th>$D(x), p(x)$</th>
                  <th>$D(y), p(y)$</th>
                  <th>$D(z), p(z)$</th>
                  <th>Selected Node $u^*$</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>0 (Init)</strong></td>
                  <td>$\{u\}$</td>
                  <td>$2, u$</td>
                  <td>$5, u$</td>
                  <td><strong>1, u</strong></td>
                  <td>$\infty, -$</td>
                  <td>$\infty, -$</td>
                  <td><strong>$x$</strong> (min cost 1)</td>
                </tr>
                <tr>
                  <td><strong>1</strong></td>
                  <td>$\{u, x\}$</td>
                  <td><strong>2, u</strong></td>
                  <td>$\min(5, 1+3) = 4, x$</td>
                  <td>—</td>
                  <td><strong>$1+1 = 2, x$</strong></td>
                  <td>$\infty, -$</td>
                  <td><strong>$v$</strong> (tie broken alpha)</td>
                </tr>
                <tr>
                  <td><strong>2</strong></td>
                  <td>$\{u, x, v\}$</td>
                  <td>—</td>
                  <td>$\min(4, 2+3) = 4, x$</td>
                  <td>—</td>
                  <td><strong>2, x</strong></td>
                  <td>$\infty, -$</td>
                  <td><strong>$y$</strong> (min cost 2)</td>
                </tr>
                <tr>
                  <td><strong>3</strong></td>
                  <td>$\{u, x, v, y\}$</td>
                  <td>—</td>
                  <td>$\min(4, 2+1) =$ <strong>3, y</strong></td>
                  <td>—</td>
                  <td>—</td>
                  <td>$2+2 = 4, y$</td>
                  <td><strong>$w$</strong> (min cost 3)</td>
                </tr>
                <tr>
                  <td><strong>4</strong></td>
                  <td>$\{u, x, v, y, w\}$</td>
                  <td>—</td>
                  <td>—</td>
                  <td>—</td>
                  <td>—</td>
                  <td>$\min(4, 3+5) =$ <strong>4, y</strong></td>
                  <td><strong>$z$</strong> (min cost 4)</td>
                </tr>
                <tr>
                  <td><strong>5 (Done)</strong></td>
                  <td>$\{u, x, v, y, w, z\}$</td>
                  <td>—</td>
                  <td>—</td>
                  <td>—</td>
                  <td>—</td>
                  <td>—</td>
                  <td>Algorithm Terminates</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 3: PATH RECONSTRUCTION & FIB TABLE -->
        <div class="blueprint-section">
          <h4 class="section-title">3. Path Reconstruction &amp; Router u Forwarding Table (2 Marks)</h4>
          <p>
            Traversing the predecessor pointers backwards from each destination to source $u$:
          </p>
          <div class="table-responsive">
            <table class="exam-table">
              <thead>
                <tr>
                  <th>Destination</th>
                  <th>Predecessor Chain</th>
                  <th>Complete Optimal Path</th>
                  <th>Total Cost</th>
                  <th>Next-Hop Router</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>$v$</strong></td>
                  <td>$v \leftarrow u$</td>
                  <td>$u \to v$</td>
                  <td><strong>2</strong></td>
                  <td><strong>$v$</strong></td>
                </tr>
                <tr>
                  <td><strong>$x$</strong></td>
                  <td>$x \leftarrow u$</td>
                  <td>$u \to x$</td>
                  <td><strong>1</strong></td>
                  <td><strong>$x$</strong></td>
                </tr>
                <tr>
                  <td><strong>$y$</strong></td>
                  <td>$y \leftarrow x \leftarrow u$</td>
                  <td>$u \to x \to y$</td>
                  <td><strong>2</strong></td>
                  <td><strong>$x$</strong></td>
                </tr>
                <tr>
                  <td><strong>$w$</strong></td>
                  <td>$w \leftarrow y \leftarrow x \leftarrow u$</td>
                  <td>$u \to x \to y \to w$</td>
                  <td><strong>3</strong></td>
                  <td><strong>$x$</strong></td>
                </tr>
                <tr>
                  <td><strong>$z$</strong></td>
                  <td>$z \leftarrow y \leftarrow x \leftarrow u$</td>
                  <td>$u \to x \to y \to z$</td>
                  <td><strong>4</strong></td>
                  <td><strong>$x$</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 4: TIME COMPLEXITY & IMPLEMENTATIONS -->
        <div class="blueprint-section">
          <h4 class="section-title">4. Algorithmic Complexity &amp; Data Structures (2 Marks)</h4>
          <div class="blueprint-grid">
            <div class="blueprint-col">
              <h5>Unordered Array Implementation</h5>
              <ul>
                <li><strong>Extract-Min:</strong> Linear scan over unvisited nodes requires $O(|V|)$ per iteration. For $|V|$ iterations: $O(|V|^2)$.</li>
                <li><strong>Edge Relaxations:</strong> Updating $D(v)$ takes $O(1)$ per edge. Total relaxation work: $O(|E|)$.</li>
                <li><strong>Total Time:</strong> $O(|V|^2 + |E|) = \mathbf{O(|V|^2)}$.</li>
                <li><strong>Optimal For:</strong> Dense networks where $|E| \approx |V|^2$.</li>
              </ul>
            </div>
            <div class="blueprint-col">
              <h5>Min-Heap / Priority Queue Implementation</h5>
              <ul>
                <li><strong>Extract-Min:</strong> Removing min element from binary heap takes $O(\log |V|)$ time. For $|V|$ extractions: $O(|V| \log |V|)$.</li>
                <li><strong>Edge Relaxations:</strong> Each relaxation triggers a `decrease-key` operation taking $O(\log |V|)$. Total across all edges: $O(|E| \log |V|)$.</li>
                <li><strong>Total Time:</strong> $\mathbf{O((|V| + |E|) \log |V|)}$.</li>
                <li><strong>Optimal For:</strong> Sparse real-world internetworks where $|E| \ll |V|^2$.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- TRAPS & MARKING SCHEME -->
        <div class="blueprint-meta-box">
          <div class="trap-warning">
            <strong>⚠️ High-Frequency Exam Pitfall:</strong>
            Never confuse <strong>Dijkstra's Shortest Path Tree (SPT)</strong> with a <strong>Minimum Spanning Tree (MST / Prim-Kruskal)</strong>! An MST minimizes the total sum of edge weights across the entire network ($\sum_{e \in T} w(e)$), whereas Dijkstra minimizes the end-to-end path distance from one specific root node $s$ to all destinations. An edge with cost 100 might be in the MST but excluded from the SPT!
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 12
# ==========================================

# 1. Replace ASCII diagram in s12-graph (Figure 12.1)
match_s12_graph = re.search(r'(<section id="s12-graph"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_graph:
    content = content[:match_s12_graph.start(2)] + svg_diagram_1 + content[match_s12_graph.end(2):]
    print('Replaced ASCII diagram in s12-graph with Figure 12.1')
else:
    print('Warning: could not find ASCII diagram in s12-graph')

# 2. Replace ASCII diagram in s12-dijkstra-intuition / s12-algorithm (Figure 12.2)
match_s12_relax = re.search(r'(<section id="s12-algorithm"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_relax:
    content = content[:match_s12_relax.start(2)] + svg_diagram_2 + content[match_s12_relax.end(2):]
    print('Replaced ASCII diagram in s12-algorithm with Figure 12.2')
else:
    print('Warning: could not find ASCII diagram in s12-algorithm')

# 3. Replace ASCII diagram in s12-worked1 (Figure 12.3: Canonical 6-Node Network)
match_s12_w1 = re.search(r'(<section id="s12-worked1"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_w1:
    content = content[:match_s12_w1.start(2)] + svg_diagram_3 + content[match_s12_w1.end(2):]
    print('Replaced ASCII diagram in s12-worked1 with Figure 12.3')
else:
    print('Warning: could not find ASCII diagram in s12-worked1')

# 4. Replace ASCII diagram in s12-reconstruct (Figure 12.4: SPT Tree & Forwarding Table)
match_s12_rec = re.search(r'(<section id="s12-reconstruct"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_rec:
    content = content[:match_s12_rec.start(2)] + svg_diagram_4 + content[match_s12_rec.end(2):]
    print('Replaced ASCII diagram in s12-reconstruct with Figure 12.4')
else:
    print('Warning: could not find ASCII diagram in s12-reconstruct')

# 5. Replace ASCII diagram in s12-limitations (Figure 12.5: Negative Weight Failure)
match_s12_lim = re.search(r'(<section id="s12-limitations"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_lim:
    content = content[:match_s12_lim.start(2)] + svg_diagram_5 + content[match_s12_lim.end(2):]
    print('Replaced ASCII diagram in s12-limitations with Figure 12.5')
else:
    print('Warning: could not find ASCII diagram in s12-limitations')

# 6. Replace ASCII diagram in s12-linkstate (Figure 12.6: OSPF Pipeline)
match_s12_ls = re.search(r'(<section id="s12-linkstate"[^>]*>.*?)(<pre class="ascii-diagram">.*?</pre>)', content, flags=re.DOTALL)
if match_s12_ls:
    content = content[:match_s12_ls.start(2)] + svg_diagram_6 + content[match_s12_ls.end(2):]
    print('Replaced ASCII diagram in s12-linkstate with Figure 12.6')
else:
    print('Warning: could not find ASCII diagram in s12-linkstate')

# 7. Insert DU 10-Mark Blueprint before study-resources in s12-summary
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch12_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 12!')
else:
    print('Warning: could not find .study-resources in Chapter 12')

with open(ch12_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 12 upgrade completed!')
