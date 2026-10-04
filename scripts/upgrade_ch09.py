"""
Upgrade Chapter 9 of CN MiniBook with rich SVG diagrams, university exam blueprints, and expanded explanations.
"""
import re

ch9_path = '/Users/arpit/minibook/cn/chapters/ch09-protocols-sliding.html'
with open(ch9_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. DIAGRAM 1: Sliding Window Buffer Structures (GBN vs SR)
# ==========================================
svg_diagram_1 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">🪟</span>
      <span class="diagram-title">Figure 9.1: Sliding Window Buffers — Go-Back-N ($W_s = N, W_r = 1$) vs. Selective Repeat ($W_s = W_r = 2^{m-1}$)</span>
    </div>
    <span class="diagram-badge">SLIDING WINDOW ENGINE</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="920" height="360" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- SECTION A: GO-BACK-N SLIDING WINDOW -->
      <g transform="translate(30, 25)">
        <rect width="860" height="150" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <text x="20" y="24" fill="var(--warning)" font-size="12" font-weight="800">
          A. GO-BACK-N ARQ: SENDER WINDOW W_s = 2^m - 1, RECEIVER WINDOW W_r = 1
        </text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">
          Sender maintains multi-frame window • Receiver accepts strictly IN-ORDER (zero out-of-order buffering)
        </text>

        <!-- Sender Window Cells (0 to 7) -->
        <g transform="translate(30, 55)">
          <text x="0" y="24" fill="var(--tx-primary)" font-size="10" font-weight="700">Sender Buffer:</text>
          
          <!-- Cell 0 (Acked) -->
          <rect x="110" y="5" width="45" height="35" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="132" y="27" fill="var(--tx-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">0</text>

          <!-- Active Window Box Ws = 4 (Cells 1, 2, 3, 4) -->
          <rect x="160" y="-2" width="195" height="48" rx="6" fill="rgba(251, 191, 36, 0.12)" stroke="var(--warning)" stroke-width="2"/>
          <text x="257" y="10" fill="var(--warning)" font-size="9" font-weight="800" text-anchor="middle">
            Active Sender Window (W_s = 4)
          </text>

          <!-- Cell 1 (Sent, unacked) -->
          <rect x="165" y="5" width="42" height="35" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="186" y="27" fill="var(--warning)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">1</text>

          <!-- Cell 2 (Sent, unacked) -->
          <rect x="213" y="5" width="42" height="35" rx="4" fill="var(--warning-dim)" stroke="var(--warning)" stroke-width="1.5"/>
          <text x="234" y="27" fill="var(--warning)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">2</text>

          <!-- Cell 3 (Usable, not sent) -->
          <rect x="261" y="5" width="42" height="35" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="282" y="27" fill="var(--tx-secondary)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">3</text>

          <!-- Cell 4 (Usable, not sent) -->
          <rect x="309" y="5" width="42" height="35" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="330" y="27" fill="var(--tx-secondary)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">4</text>

          <!-- Cells 5, 6, 7 (Outside window) -->
          <rect x="365" y="5" width="42" height="35" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="386" y="27" fill="var(--tx-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">5</text>
          <rect x="412" y="5" width="42" height="35" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="433" y="27" fill="var(--tx-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">6</text>
          <rect x="459" y="5" width="42" height="35" rx="4" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1" stroke-dasharray="2,2"/>
          <text x="480" y="27" fill="var(--tx-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">7</text>
        </g>

        <!-- Receiver Window (Size 1) -->
        <g transform="translate(560, 55)">
          <text x="0" y="24" fill="var(--tx-primary)" font-size="10" font-weight="700">Receiver Buffer:</text>
          
          <!-- Receiver Window Size = 1 -->
          <rect x="110" y="-2" width="55" height="48" rx="6" fill="rgba(248, 113, 113, 0.15)" stroke="var(--danger)" stroke-width="2"/>
          <text x="137" y="10" fill="var(--danger)" font-size="8" font-weight="800" text-anchor="middle">W_r = 1</text>
          <rect x="115" y="5" width="45" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="137" y="27" fill="var(--danger)" font-family="var(--font-mono)" font-size="11" font-weight="900" text-anchor="middle">1</text>

          <text x="180" y="27" fill="var(--tx-muted)" font-size="9">Strictly expects Frame 1; discards all others!</text>
        </g>

        <text x="430" y="132" fill="var(--tx-secondary)" font-size="10" text-anchor="middle">
          Window sliding rule: Receiving cumulative ACK(k) slides left edge of sender window up to k.
        </text>
      </g>

      <!-- SECTION B: SELECTIVE REPEAT SLIDING WINDOW -->
      <g transform="translate(30, 190)">
        <rect width="860" height="150" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="1.8"/>
        <text x="20" y="24" fill="var(--accent)" font-size="12" font-weight="800">
          B. SELECTIVE REPEAT ARQ: SENDER WINDOW W_s = 2^(m-1), RECEIVER WINDOW W_r = 2^(m-1)
        </text>
        <text x="20" y="40" fill="var(--tx-muted)" font-size="9">
          Both sender AND receiver maintain identical symmetric windows • Receiver buffers out-of-order frames!
        </text>

        <!-- Sender Window -->
        <g transform="translate(30, 55)">
          <text x="0" y="24" fill="var(--tx-primary)" font-size="10" font-weight="700">Sender Buffer:</text>
          
          <rect x="110" y="-2" width="195" height="48" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="207" y="10" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">
            Sender Window (W_s = 4)
          </text>
          
          <!-- Cells in Sender -->
          <rect x="115" y="5" width="42" height="35" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="136" y="27" fill="var(--success)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">1✓</text>

          <rect x="163" y="5" width="42" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="184" y="27" fill="var(--danger)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">2✗</text>

          <rect x="211" y="5" width="42" height="35" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="232" y="27" fill="var(--success)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">3✓</text>

          <rect x="259" y="5" width="42" height="35" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="280" y="27" fill="var(--tx-secondary)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">4</text>
        </g>

        <!-- Receiver Window (Size 4, buffering out-of-order!) -->
        <g transform="translate(540, 55)">
          <text x="0" y="24" fill="var(--tx-primary)" font-size="10" font-weight="700">Receiver Buffer:</text>
          
          <rect x="110" y="-2" width="195" height="48" rx="6" fill="var(--accent-dim)" stroke="var(--accent)" stroke-width="2"/>
          <text x="207" y="10" fill="var(--accent)" font-size="9" font-weight="800" text-anchor="middle">
            Receiver Window (W_r = 4)
          </text>

          <rect x="115" y="5" width="42" height="35" rx="4" fill="var(--success-dim)" stroke="var(--success)" stroke-width="1.5"/>
          <text x="136" y="27" fill="var(--success)" font-family="var(--font-mono)" font-size="11" font-weight="800" text-anchor="middle">1✓</text>

          <rect x="163" y="5" width="42" height="35" rx="4" fill="var(--danger-dim)" stroke="var(--danger)" stroke-width="1.5"/>
          <text x="184" y="27" fill="var(--danger)" font-family="var(--font-mono)" font-size="10" font-weight="800" text-anchor="middle">Wait</text>

          <rect x="211" y="5" width="42" height="35" rx="4" fill="var(--info-dim)" stroke="var(--info)" stroke-width="1.5"/>
          <text x="232" y="27" fill="var(--info)" font-family="var(--font-mono)" font-size="10" font-weight="800" text-anchor="middle">Buf 3</text>

          <rect x="259" y="5" width="42" height="35" rx="4" fill="var(--bg-elevated)" stroke="var(--border)" stroke-width="1"/>
          <text x="280" y="27" fill="var(--tx-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">4</text>
        </g>

        <text x="430" y="132" fill="var(--success)" font-size="10" font-weight="700" text-anchor="middle">
          ★ Out-of-Order Delivery: Frame 3 is safely stored in RAM buffer while waiting ONLY for retransmitted Frame 2!
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Window Size Invariant Axiom:</strong> In any sliding window protocol, to prevent the receiver from confusing a new frame with a retransmitted duplicate, the sum of sender and receiver windows must never exceed the sequence number space: <strong>W_s + W_r ≤ 2^m</strong>. Hence, for Go-Back-N ($W_r = 1 \implies W_s \le 2^m - 1$); for Selective Repeat ($W_s = W_r \implies W_s \le 2^{m-1}$).
  </div>
</div>'''

# ==========================================
# 2. DIAGRAM 2: ARQ Failure Sequence Timelines (Stop-and-Wait vs GBN vs SR)
# ==========================================
svg_diagram_2 = '''<div class="diagram-box">
  <div class="diagram-header">
    <div class="diagram-title-wrap">
      <span class="diagram-icon">⚔️</span>
      <span class="diagram-title">Figure 9.2: ARQ Error Recovery Timelines — Stop-and-Wait vs. Go-Back-N vs. Selective Repeat</span>
    </div>
    <span class="diagram-badge">PROTOCOL COMPARISON</span>
  </div>
  <div class="diagram-svg-wrap">
    <svg viewBox="0 0 940 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-seq-loss" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)" />
        </marker>
        <marker id="arrow-seq-ack" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--success)" />
        </marker>
      </defs>

      <rect x="10" y="10" width="920" height="380" rx="14" fill="var(--bg-surface)" stroke="var(--border)" stroke-width="1.2"/>

      <!-- COLUMN 1: STOP-AND-WAIT ARQ -->
      <g transform="translate(30, 25)">
        <rect width="270" height="345" rx="10" fill="var(--bg-card)" stroke="var(--border)" stroke-width="1.5"/>
        <text x="135" y="24" fill="var(--tx-primary)" font-size="11" font-weight="800" text-anchor="middle">
          1. STOP-AND-WAIT ARQ
        </text>
        <text x="135" y="38" fill="var(--tx-muted)" font-size="8" text-anchor="middle">1 Frame at a Time • W_s = 1, W_r = 1</text>

        <!-- Vertical Timeline: S & R -->
        <line x1="40" y1="55" x2="40" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="40" y="50" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Tx</text>

        <line x1="230" y1="55" x2="230" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="230" y="50" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Rx</text>

        <!-- Frame 0 OK -->
        <line x1="40" y1="70" x2="230" y2="100" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="78" fill="var(--accent)" font-size="8" font-weight="700">Frame 0</text>
        <line x1="230" y1="105" x2="40" y2="135" stroke="var(--success)" stroke-width="2" marker-end="url(#arrow-seq-ack)"/>
        <text x="140" y="125" fill="var(--success)" font-size="8" font-weight="700">ACK 1</text>

        <!-- Frame 1 LOST IN TRANSIT -->
        <line x1="40" y1="145" x2="160" y2="170" stroke="var(--danger)" stroke-width="2"/>
        <circle cx="160" cy="170" r="8" fill="var(--danger)"/>
        <text x="160" y="174" fill="#fff" font-size="9" font-weight="900" text-anchor="middle">✗</text>
        <text x="90" y="150" fill="var(--danger)" font-size="8" font-weight="700">Frame 1 (LOST!)</text>

        <!-- Sender Idle Timer Expiry -->
        <line x1="30" y1="145" x2="30" y2="230" stroke="var(--danger)" stroke-width="1.5" stroke-dasharray="2,2"/>
        <text x="15" y="190" fill="var(--danger)" font-size="7" font-weight="800" transform="rotate(-90 15 190)">TIMEOUT</text>

        <!-- Retransmission Frame 1 -->
        <line x1="40" y1="230" x2="230" y2="260" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="238" fill="var(--accent)" font-size="8" font-weight="700">Frame 1 (Retrans)</text>
        <line x1="230" y1="265" x2="40" y2="295" stroke="var(--success)" stroke-width="2" marker-end="url(#arrow-seq-ack)"/>
        <text x="140" y="285" fill="var(--success)" font-size="8" font-weight="700">ACK 0</text>

        <text x="135" y="325" fill="var(--danger)" font-size="9" font-weight="700" text-anchor="middle">
          Worst-case: Pipe idle during timeout!
        </text>
      </g>

      <!-- COLUMN 2: GO-BACK-N ARQ -->
      <g transform="translate(320, 25)">
        <rect width="280" height="345" rx="10" fill="var(--bg-card)" stroke="var(--warning)" stroke-width="1.8"/>
        <text x="140" y="24" fill="var(--warning)" font-size="11" font-weight="800" text-anchor="middle">
          2. GO-BACK-N ARQ (GBN)
        </text>
        <text x="140" y="38" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Cumulative ACKs • Discards Out-of-Order</text>

        <!-- Vertical Timeline: S & R -->
        <line x1="40" y1="55" x2="40" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="40" y="50" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Tx</text>

        <line x1="240" y1="55" x2="240" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="240" y="50" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Rx</text>

        <!-- Burst Transmission F0, F1 (lost), F2, F3 -->
        <line x1="40" y1="65" x2="240" y2="90" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="72" fill="var(--accent)" font-size="8">Frame 0</text>

        <!-- F1 Lost -->
        <line x1="40" y1="85" x2="160" y2="105" stroke="var(--danger)" stroke-width="1.8"/>
        <text x="160" y="108" fill="var(--danger)" font-size="8" font-weight="900">✗ F1 Lost</text>

        <line x1="40" y1="105" x2="240" y2="130" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="112" fill="var(--accent)" font-size="8">Frame 2</text>

        <line x1="40" y1="125" x2="240" y2="150" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="132" fill="var(--accent)" font-size="8">Frame 3</text>

        <!-- Receiver actions: Discards F2 and F3! Sends ACK 1 repeatedly -->
        <line x1="240" y1="135" x2="40" y2="165" stroke="var(--warning)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow-seq-ack)"/>
        <text x="150" y="152" fill="var(--warning)" font-size="8">Discard F2 (ACK 1)</text>

        <line x1="240" y1="155" x2="40" y2="185" stroke="var(--warning)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow-seq-ack)"/>
        <text x="150" y="172" fill="var(--warning)" font-size="8">Discard F3 (ACK 1)</text>

        <!-- F1 Timeout on Sender ➔ GO BACK AND RETRANSMIT ALL -->
        <line x1="40" y1="210" x2="240" y2="235" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="218" fill="var(--danger)" font-size="8" font-weight="800">Retrans F1</text>

        <line x1="40" y1="230" x2="240" y2="255" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="238" fill="var(--danger)" font-size="8" font-weight="800">Retrans F2 (Wasted!)</text>

        <line x1="40" y1="250" x2="240" y2="275" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="258" fill="var(--danger)" font-size="8" font-weight="800">Retrans F3 (Wasted!)</text>

        <text x="140" y="325" fill="var(--warning)" font-size="9" font-weight="700" text-anchor="middle">
          Retransmits N frames even if already received!
        </text>
      </g>

      <!-- COLUMN 3: SELECTIVE REPEAT ARQ -->
      <g transform="translate(620, 25)">
        <rect width="280" height="345" rx="10" fill="var(--bg-card)" stroke="var(--accent)" stroke-width="2"/>
        <text x="140" y="24" fill="var(--accent)" font-size="11" font-weight="800" text-anchor="middle">
          3. SELECTIVE REPEAT (SR)
        </text>
        <text x="140" y="38" fill="var(--tx-muted)" font-size="8" text-anchor="middle">Individual ACKs • Buffers Out-of-Order</text>

        <!-- Vertical Timeline: S & R -->
        <line x1="40" y1="55" x2="40" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="40" y="50" fill="var(--accent)" font-size="9" font-weight="700" text-anchor="middle">Tx</text>

        <line x1="240" y1="55" x2="240" y2="300" stroke="var(--border)" stroke-width="1.5"/>
        <text x="240" y="50" fill="var(--info)" font-size="9" font-weight="700" text-anchor="middle">Rx</text>

        <!-- F0, F1 (lost), F2, F3 -->
        <line x1="40" y1="65" x2="240" y2="90" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="72" fill="var(--accent)" font-size="8">Frame 0</text>

        <line x1="40" y1="85" x2="160" y2="105" stroke="var(--danger)" stroke-width="1.8"/>
        <text x="160" y="108" fill="var(--danger)" font-size="8" font-weight="900">✗ F1 Lost</text>

        <line x1="40" y1="105" x2="240" y2="130" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="112" fill="var(--accent)" font-size="8">Frame 2</text>

        <line x1="40" y1="125" x2="240" y2="150" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#arrow-seq-loss)"/>
        <text x="120" y="132" fill="var(--accent)" font-size="8">Frame 3</text>

        <!-- Receiver BUFFERS F2 & F3! Sends NAK 1 -->
        <line x1="240" y1="135" x2="40" y2="165" stroke="var(--danger)" stroke-width="2" marker-end="url(#arrow-seq-ack)"/>
        <text x="160" y="148" fill="var(--danger)" font-size="8" font-weight="800">NAK 1 (Buffered F2)</text>

        <line x1="240" y1="155" x2="40" y2="185" stroke="var(--success)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow-seq-ack)"/>
        <text x="160" y="168" fill="var(--success)" font-size="8">ACK 3 (Buffered F3)</text>

        <!-- Sender retransmits ONLY FRAME 1! -->
        <line x1="40" y1="195" x2="240" y2="225" stroke="var(--success)" stroke-width="2.5" marker-end="url(#arrow-seq-loss)"/>
        <text x="110" y="205" fill="var(--success)" font-size="9" font-weight="900">Retrans ONLY Frame 1!</text>

        <!-- Receiver gets F1, delivers 1, 2, 3 in order to upper layer -->
        <line x1="240" y1="230" x2="40" y2="260" stroke="var(--success)" stroke-width="2" marker-end="url(#arrow-seq-ack)"/>
        <text x="160" y="245" fill="var(--success)" font-size="8" font-weight="800">ACK 4 (Delivered 1,2,3)</text>

        <text x="140" y="325" fill="var(--success)" font-size="9" font-weight="700" text-anchor="middle">
          ★ Optimal: Zero wasted retransmissions!
        </text>
      </g>
    </svg>
  </div>
  <div class="diagram-caption">
    <strong>Error Recovery Penalty:</strong> In Go-Back-N, losing 1 frame forces the retransmission of all subsequent $N-1$ frames that were already successfully received by the receiver, wasting massive bandwidth. Selective Repeat isolates the lost frame and retransmits strictly that single frame, maximizing channel efficiency.
  </div>
</div>'''

# ==========================================
# 3. 10-MARK UNIVERSITY MODEL ANSWER FOR CHAPTER 9
# ==========================================
ch9_uni_blueprint = '''
    <!-- 10-MARK UNIVERSITY MODEL ANSWER BLUEPRINT -->
    <div class="mode-uni" style="margin-top: 2.5rem;">
      <div class="mode-badge uni">🎓 Delhi University / B.Tech CSE Exam Blueprint (10 Marks)</div>
      <h3 style="margin-top: 0.5rem; color: var(--accent);">Question: Sliding Window Flow Control, Window Size Invariant Proof &amp; ARQ Efficiency Numericals</h3>
      
      <div class="exam-question-box" style="background: var(--bg-surface); padding: 18px 22px; border-radius: 12px; border-left: 4px solid var(--accent); margin-bottom: 20px;">
        <p style="margin: 0; font-weight: 700; color: var(--tx-primary);">
          (a) State the Sliding Window principle. Prove mathematically that to avoid ambiguous frame acknowledgment in a sequence number space of $m$ bits ($2^m$ sequence numbers), the window sizes must satisfy $W_s + W_r \\le 2^m$. Deduce the maximum sender window size for Go-Back-N and Selective Repeat. [4 Marks]<br>
          (b) Compare Stop-and-Wait, Go-Back-N, and Selective Repeat ARQ protocols across: Sender window size, Receiver window size, Retransmission penalty, Need for receiver sorting buffers, and Bandwidth efficiency under error-prone links. [3 Marks]<br>
          (c) A geostationary satellite link has a bandwidth of $R = 2\\text{ Mbps}$ and a one-way propagation delay of $d_{\\text{prop}} = 250\\text{ ms}$. Frame size is $L = 2,000\\text{ bytes}$, and ACK frame size is negligible.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(i) Calculate the parameter $a = d_{\\text{prop}} / d_{\\text{trans}}$.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(ii) Compute the channel efficiency under Stop-and-Wait protocol.<br>
          &nbsp;&nbsp;&nbsp;&nbsp;(iii) Calculate the minimum window size $N$ and the minimum sequence number bits $m$ required for 100% channel utilization under Go-Back-N and Selective Repeat. [3 Marks]
        </p>
      </div>

      <div class="model-answer" style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (a) Model Solution: Mathematical Proof of Window Size Invariant</h4>
          <p><strong>The Window Size Theorem:</strong> In any sliding window protocol operating over an unreliable channel with an $m$-bit sequence number space ($0$ to $2^m - 1$):</p>
          $$W_s + W_r \\le 2^m$$
          
          <p><strong>Mathematical Proof by Contradiction:</strong></p>
          <ol style="padding-left: 20px; line-height: 1.6;">
            <li>Suppose the sender transmits its full window $W_s$ of frames: $[0, 1, 2, \\dots, W_s - 1]$.</li>
            <li>All $W_s$ frames arrive successfully at the receiver. The receiver advances its window by $W_s$, now expecting frames $[W_s, W_s + 1, \\dots, W_s + W_r - 1]$. The receiver transmits ACKs for all received frames.</li>
            <li><strong>Worst-Case Scenario (All ACKs Lost in Transit):</strong> Every ACK is dropped by the channel. The sender's retransmission timer expires.</li>
            <li>The sender retransmits its original unacknowledged frames starting from frame $0$.</li>
            <li>When the retransmitted frame $0$ arrives at the receiver, the receiver must be able to unambiguously distinguish whether this frame $0$ is an old duplicate retransmission OR a brand-new frame from the next epoch!</li>
            <li>For no ambiguity to occur, the sequence number $0$ must NOT fall within the receiver's new window $[W_s, W_s + W_r - 1]$. Since sequence numbers wrap around modulo $2^m$, this requires: $$W_s + W_r \\le 2^m$$</li>
          </ol>
          <p><strong>Deductions:</strong></p>
          <ul style="padding-left: 20px; line-height: 1.6;">
            <li><strong>Go-Back-N:</strong> Since receiver accepts only in-order frames, $W_r = 1$. Substituting: $W_s + 1 \\le 2^m \\implies \\mathbf{W_s \\le 2^m - 1}$.</li>
            <li><strong>Selective Repeat:</strong> To avoid asymmetric buffering, sender and receiver windows are made equal ($W_s = W_r$). Substituting: $2W_s \\le 2^m \\implies \\mathbf{W_s = W_r \\le 2^{m-1}}$.</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (b) Model Solution: ARQ Protocols Comparative Master Matrix</h4>
          <table class="data-table" style="width: 100%; margin-top: 8px;">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Stop-and-Wait ARQ</th>
                <th>Go-Back-N ARQ</th>
                <th>Selective Repeat ARQ</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Sender Window ($W_s$)</strong></td>
                <td>$1$</td>
                <td>$2^m - 1$</td>
                <td>$2^{m-1}$</td>
              </tr>
              <tr>
                <td><strong>Receiver Window ($W_r$)</strong></td>
                <td>$1$</td>
                <td>$1$</td>
                <td>$2^{m-1}$</td>
              </tr>
              <tr>
                <td><strong>Retransmission Scope</strong></td>
                <td>Single lost frame</td>
                <td>Lost frame + All subsequent frames in window</td>
                <td>Strictly the single lost frame</td>
              </tr>
              <tr>
                <td><strong>Receiver Buffering</strong></td>
                <td>None</td>
                <td>None (Discards out-of-order)</td>
                <td>Active sorting buffer in RAM</td>
              </tr>
              <tr>
                <td><strong>Acknowledgment Type</strong></td>
                <td>Individual</td>
                <td>Cumulative</td>
                <td>Individual / Selective (SACK)</td>
              </tr>
              <tr>
                <td><strong>Theoretical Efficiency ($\eta$)</strong></td>
                <td>$\\frac{1}{1 + 2a}$</td>
                <td>$\\frac{N}{1 + 2a}$ (ideal)</td>
                <td>$\\frac{N}{1 + 2a}$ (ideal)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <h4 style="color: var(--accent); margin-bottom: 6px;">Part (c) Model Solution: Satellite Link Solved Numerical</h4>
          <div style="background: var(--bg-elevated); padding: 14px 18px; border-radius: 8px; border: 1px solid var(--border); margin-top: 8px;">
            <p style="margin: 0; font-family: var(--font-mono); font-size: 0.92rem; line-height: 1.6;">
              <strong>Given Parameters:</strong><br>
              • Bandwidth $R = 2\\text{ Mbps} = 2 \\times 10^6\\text{ bps}$<br>
              • Propagation Delay $d_{\\text{prop}} = 250\\text{ ms} = 0.25\\text{ s}$<br>
              • Frame Size $L = 2,000\\text{ bytes} = 16,000\\text{ bits}$<br><br>

              <strong>(i) Calculate Transmission Delay &amp; Parameter $a$:</strong><br>
              $$d_{\\text{trans}} = \\frac{L}{R} = \\frac{16,000\\text{ bits}}{2 \\times 10^6\\text{ bps}} = 8 \\times 10^{-3}\\text{ s} = \\mathbf{8\\text{ ms}}$$<br>
              $$a = \\frac{d_{\\text{prop}}}{d_{\\text{trans}}} = \\frac{250\\text{ ms}}{8\\text{ ms}} = \\mathbf{31.25}$$<br><br>

              <strong>(ii) Channel Efficiency under Stop-and-Wait:</strong><br>
              $$\\eta_{\\text{SW}} = \\frac{d_{\\text{trans}}}{d_{\\text{trans}} + 2 \\cdot d_{\\text{prop}}} = \\frac{1}{1 + 2a} = \\frac{1}{1 + 2(31.25)} = \\frac{1}{1 + 62.5} = \\frac{1}{63.5} \\approx \\mathbf{1.57\\%}$$<br>
              <em>(Stop-and-Wait wastes over 98.4% of the satellite channel!)</em><br><br>

              <strong>(iii) Optimum Window Size &amp; Sequence Number Bits for 100% Efficiency:</strong><br>
              For 100% utilization ($\\eta = 1$), the window must fill the pipe ($N \\ge 1 + 2a$):<br>
              $$N \\ge 1 + 2(31.25) = 1 + 62.5 = 63.5 \\implies \\mathbf{N_{\\text{opt}} = 64\\text{ frames}}$$<br><br>

              • <strong>For Go-Back-N:</strong><br>
              $$W_s = N = 64 \\le 2^m - 1 \\implies 2^m \\ge 65 \\implies \\mathbf{m = 7\\text{ bits}} \\quad (2^7 = 128 > 65)$$<br><br>
              • <strong>For Selective Repeat:</strong><br>
              $$W_s = N = 64 \\le 2^{m-1} \\implies 2^{m-1} \\ge 64 = 2^6 \\implies m - 1 \\ge 6 \\implies \\mathbf{m = 7\\text{ bits}}$$
            </p>
          </div>
        </div>
      </div>
    </div>
'''

# ==========================================
# REPLACEMENTS IN CHAPTER 9
# ==========================================
# Insert Diagram 1 into Section 9.8 (Sliding window)
s8_target = re.search(r'<section id="s-sliding-window"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s8_target:
    content = content[:s8_target.end()] + '\n' + svg_diagram_1 + '\n' + content[s8_target.end():]
    print('Inserted Diagram 1 in Section 9.8')

# Insert Diagram 2 into Section 9.15 (Protocol compare)
s15_target = re.search(r'<section id="s-protocol-compare"[^>]*>.*?<h3>', content, flags=re.DOTALL)
if s15_target:
    content = content[:s15_target.end()] + '\n' + svg_diagram_2 + '\n' + content[s15_target.end():]
    print('Inserted Diagram 2 in Section 9.15')

# Insert 10-Mark Blueprint into Chapter 9 before study-resources in s-summary-ch9
ref_target = re.search(r'<div class="study-resources">', content)
if ref_target:
    content = content[:ref_target.start()] + ch9_uni_blueprint + '\n\n    ' + content[ref_target.start():]
    print('Inserted 10-Mark University Blueprint in Chapter 9!')

with open(ch9_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Chapter 9 upgrade completed!')
