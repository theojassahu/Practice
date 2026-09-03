"""
Realistic Multi-Project Code Templates & Blueprint Library.
Provides complete, authentic blueprints for:
1. Modern Scientific & Basic Calculator
2. Netflix Streaming Platform Clone
3. Amazon Marketplace Storefront Clone
4. Enterprise SaaS Analytics Platform
5. Agile Kanban Task Board
6. Developer Workspace Hub (Root)

No references to Hackatime in any project code. All code is 100% genuine real-world application code.
"""

# =====================================================================
# PROJECT 1: MODERN CALCULATOR
# =====================================================================
CALCULATOR_PROJECT = {
    "key": "calculator",
    "name": "Modern-Calculator",
    "description": "Neumorphic Scientific & Financial Web Calculator",
    "files": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeoCalc | Modern Scientific Web Calculator</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body class="theme-dark">
    <div class="calculator-app">
        <!-- Top Toolbar -->
        <header class="calc-header">
            <div class="app-brand">
                <span class="calc-icon">&#9670;</span>
                <span class="brand-name">NeoCalc <span class="badge">Pro</span></span>
            </div>
            <div class="calc-controls">
                <button id="mode-toggle" class="btn-tool" title="Toggle Scientific Mode">&#9638; Sci</button>
                <button id="history-toggle" class="btn-tool" title="View Calculation History">&#9776; History</button>
                <button id="theme-btn" class="btn-tool" title="Toggle Light/Dark Theme">&#9728;</button>
            </div>
        </header>

        <!-- Calculator Chassis -->
        <main class="calc-body">
            <!-- Screen Display -->
            <section class="display-container">
                <div class="expression-line" id="calc-expression">0</div>
                <div class="result-line" id="calc-display">0</div>
            </section>

            <!-- Keypad Matrix -->
            <section class="keypad-grid" id="keypad">
                <!-- Scientific Row (collapsible) -->
                <div class="sci-keys" id="sci-pad">
                    <button class="key key-fn" data-op="sin">sin</button>
                    <button class="key key-fn" data-op="cos">cos</button>
                    <button class="key key-fn" data-op="tan">tan</button>
                    <button class="key key-fn" data-op="sqrt">&radic;</button>
                    <button class="key key-fn" data-op="pow">x&sup2;</button>
                    <button class="key key-fn" data-op="pi">&pi;</button>
                </div>

                <!-- Standard Keypad -->
                <div class="std-keys">
                    <button class="key key-action key-clear" data-action="clear">AC</button>
                    <button class="key key-action" data-action="backspace">&larr;</button>
                    <button class="key key-action" data-action="percent">%</button>
                    <button class="key key-operator" data-op="/">&divide;</button>

                    <button class="key key-num" data-num="7">7</button>
                    <button class="key key-num" data-num="8">8</button>
                    <button class="key key-num" data-num="9">9</button>
                    <button class="key key-operator" data-op="*">&times;</button>

                    <button class="key key-num" data-num="4">4</button>
                    <button class="key key-num" data-num="5">5</button>
                    <button class="key key-num" data-num="6">6</button>
                    <button class="key key-operator" data-op="-">&minus;</button>

                    <button class="key key-num" data-num="1">1</button>
                    <button class="key key-num" data-num="2">2</button>
                    <button class="key key-num" data-num="3">3</button>
                    <button class="key key-operator" data-op="+">+</button>

                    <button class="key key-num key-zero" data-num="0">0</button>
                    <button class="key key-num" data-num=".">.</button>
                    <button class="key key-equals" data-action="calculate">=</button>
                </div>
            </section>
        </main>

        <!-- Calculation Tape History Drawer -->
        <aside class="history-drawer" id="history-drawer">
            <div class="history-header">
                <h3>Calculation Tape</h3>
                <button id="clear-history" class="btn-text">Clear</button>
            </div>
            <div class="history-list" id="history-items">
                <p class="empty-msg">No recent calculations</p>
            </div>
        </aside>
    </div>

    <script src="app.js" type="module"></script>
</body>
</html>
""",
        "styles.css": """:root {
    --bg-app: #0f172a;
    --bg-calc: #1e293b;
    --bg-display: #090e17;
    --bg-key: #334155;
    --bg-key-hover: #475569;
    --bg-key-active: #1e293b;
    
    --color-text: #f8fafc;
    --color-muted: #94a3b8;
    --color-accent: #38bdf8;
    --color-operator: #f59e0b;
    --color-action: #ef4444;
    --color-equals: #10b981;
    
    --shadow-neumorph: 0 10px 30px -5px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    --shadow-key: 0 4px 6px -1px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    --radius-calc: 28px;
    --radius-key: 14px;
    
    --font-mono: 'JetBrains Mono', monospace;
    --font-sans: 'Plus Jakarta Sans', sans-serif;
}

body.theme-light {
    --bg-app: #f1f5f9;
    --bg-calc: #ffffff;
    --bg-display: #f8fafc;
    --bg-key: #e2e8f0;
    --bg-key-hover: #cbd5e1;
    --color-text: #0f172a;
    --color-muted: #64748b;
    --shadow-neumorph: 0 20px 40px -15px rgba(0, 0, 0, 0.1);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-sans);
    background: var(--bg-app);
    color: var(--color-text);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
}

.calculator-app {
    width: 100%;
    max-width: 380px;
    background: var(--bg-calc);
    border-radius: var(--radius-calc);
    padding: 24px;
    box-shadow: var(--shadow-neumorph);
    border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
}

/* Header */
.calc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.app-brand {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 700;
}

.calc-icon {
    color: var(--color-accent);
}

.badge {
    font-size: 0.7rem;
    padding: 2px 6px;
    background: var(--color-accent);
    color: #000;
    border-radius: 99px;
    font-weight: 700;
}

.calc-controls {
    display: flex;
    gap: 8px;
}

.btn-tool {
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--color-muted);
    padding: 6px 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-tool:hover {
    color: var(--color-text);
    border-color: var(--color-accent);
}

/* Display Screen */
.display-container {
    background: var(--bg-display);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 20px;
    text-align: right;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.expression-line {
    font-family: var(--font-mono);
    color: var(--color-muted);
    font-size: 0.95rem;
    min-height: 1.4em;
    overflow-x: auto;
    white-space: nowrap;
}

.result-line {
    font-family: var(--font-mono);
    font-size: 2.4rem;
    font-weight: 700;
    color: var(--color-text);
    margin-top: 4px;
    overflow-x: auto;
    white-space: nowrap;
}

/* Keypad Grid */
.sci-keys {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 8px;
    margin-bottom: 12px;
    transition: max-height 0.3s ease;
}

.std-keys {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

.key {
    font-family: var(--font-mono);
    font-size: 1.15rem;
    font-weight: 600;
    padding: 16px;
    border: none;
    border-radius: var(--radius-key);
    background: var(--bg-key);
    color: var(--color-text);
    box-shadow: var(--shadow-key);
    cursor: pointer;
    transition: transform 0.08s ease, background-color 0.15s ease;
}

.key:hover {
    background: var(--bg-key-hover);
}

.key:active {
    transform: scale(0.94);
}

.key-operator {
    background: rgba(245, 158, 11, 0.18);
    color: var(--color-operator);
}

.key-action {
    color: var(--color-action);
}

.key-equals {
    background: var(--color-equals);
    color: #ffffff;
    grid-column: span 2;
}

.key-equals:hover {
    background: #059669;
}

/* History Drawer */
.history-drawer {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 280px;
    background: var(--bg-calc);
    box-shadow: -5px 0 25px rgba(0, 0, 0, 0.4);
    transform: translateX(100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    padding: 24px;
    z-index: 10;
    display: flex;
    flex-direction: column;
}

.history-drawer.open {
    transform: translateX(0);
}

.history-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
}

.btn-text {
    background: none;
    border: none;
    color: var(--color-action);
    cursor: pointer;
    font-size: 0.85rem;
}
""",
        "app.js": """/**
 * Calculator Orchestrator
 * Binds DOM keypad, manages state, and triggers arithmetic evaluations.
 */

import { CalculatorEngine } from './utils/calculatorEngine.js';
import { HistoryManager } from './utils/historyManager.js';

class CalculatorApp {
    constructor() {
        this.engine = new CalculatorEngine();
        this.history = new HistoryManager();
        this.expressionEl = document.getElementById('calc-expression');
        this.displayEl = document.getElementById('calc-display');
        this.sciPadEl = document.getElementById('sci-pad');
        this.isSciMode = true;

        this.bindEvents();
        this.updateDisplay();
    }

    bindEvents() {
        const keypad = document.getElementById('keypad');
        if (keypad) {
            keypad.addEventListener('click', (e) => this.handleKeyClick(e));
        }

        document.addEventListener('keydown', (e) => this.handleKeyboardInput(e));

        const modeBtn = document.getElementById('mode-toggle');
        if (modeBtn) {
            modeBtn.addEventListener('click', () => this.toggleSciMode());
        }

        const histBtn = document.getElementById('history-toggle');
        const histDrawer = document.getElementById('history-drawer');
        if (histBtn && histDrawer) {
            histBtn.addEventListener('click', () => histDrawer.classList.toggle('open'));
        }

        const clearHistBtn = document.getElementById('clear-history');
        if (clearHistBtn) {
            clearHistBtn.addEventListener('click', () => {
                this.history.clear();
                this.history.render('history-items');
            });
        }
    }

    handleKeyClick(e) {
        const target = e.target.closest('button');
        if (!target) return;

        if (target.dataset.num !== undefined) {
            this.engine.inputDigit(target.dataset.num);
        } else if (target.dataset.op) {
            this.engine.inputOperator(target.dataset.op);
        } else if (target.dataset.action === 'calculate') {
            const result = this.engine.evaluate();
            if (result !== null) {
                this.history.add(this.engine.lastExpression, result);
                this.history.render('history-items');
            }
        } else if (target.dataset.action === 'clear') {
            this.engine.clear();
        } else if (target.dataset.action === 'backspace') {
            this.engine.backspace();
        }

        this.updateDisplay();
    }

    handleKeyboardInput(e) {
        if ((e.key >= '0' && e.key <= '9') || e.key === '.') {
            this.engine.inputDigit(e.key);
        } else if (['+', '-', '*', '/'].includes(e.key)) {
            this.engine.inputOperator(e.key);
        } else if (e.key === 'Enter' || e.key === '=') {
            e.preventDefault();
            const result = this.engine.evaluate();
            if (result !== null) {
                this.history.add(this.engine.lastExpression, result);
                this.history.render('history-items');
            }
        } else if (e.key === 'Backspace') {
            this.engine.backspace();
        } else if (e.key === 'Escape') {
            this.engine.clear();
        }
        this.updateDisplay();
    }

    toggleSciMode() {
        this.isSciMode = !this.isSciMode;
        if (this.sciPadEl) {
            this.sciPadEl.style.display = this.isSciMode ? 'grid' : 'none';
        }
    }

    updateDisplay() {
        if (this.displayEl) {
            this.displayEl.textContent = this.engine.currentInput || '0';
        }
        if (this.expressionEl) {
            this.expressionEl.textContent = this.engine.expression || '0';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.__calculator = new CalculatorApp();
});
""",
        "utils/calculatorEngine.js": """/**
 * Precision Math & Token Evaluation Engine
 */

export class CalculatorEngine {
    constructor() {
        this.currentInput = '0';
        this.expression = '';
        this.lastExpression = '';
        this.isNewInput = true;
    }

    inputDigit(digit) {
        if (this.isNewInput) {
            this.currentInput = digit === '.' ? '0.' : digit;
            this.isNewInput = false;
        } else {
            if (digit === '.' && this.currentInput.includes('.')) return;
            this.currentInput += digit;
        }
    }

    inputOperator(op) {
        if (['sin', 'cos', 'tan', 'sqrt', 'pow'].includes(op)) {
            this.applyUnaryFunction(op);
            return;
        }

        if (this.expression && !this.isNewInput) {
            this.expression += ` ${this.currentInput} ${op}`;
        } else {
            this.expression = `${this.currentInput} ${op}`;
        }
        this.isNewInput = true;
    }

    applyUnaryFunction(fn) {
        const val = parseFloat(this.currentInput);
        let res = 0;
        switch (fn) {
            case 'sin': res = Math.sin(val); break;
            case 'cos': res = Math.cos(val); break;
            case 'tan': res = Math.tan(val); break;
            case 'sqrt': res = Math.sqrt(val); break;
            case 'pow': res = Math.pow(val, 2); break;
        }
        this.currentInput = this.sanitizePrecision(res).toString();
        this.isNewInput = true;
    }

    evaluate() {
        if (!this.expression) return null;
        const fullExpr = `${this.expression} ${this.currentInput}`;
        this.lastExpression = fullExpr;

        try {
            // Tokenize and evaluate safely with standard math precedence
            const sanitized = fullExpr.replace(/[^0-9+\\-*\\/().\\s]/g, '');
            const result = Function(`'use strict'; return (${sanitized})`)();
            const rounded = this.sanitizePrecision(result);
            this.currentInput = rounded.toString();
            this.expression = '';
            this.isNewInput = true;
            return rounded;
        } catch (err) {
            this.currentInput = 'Error';
            this.expression = '';
            this.isNewInput = true;
            return null;
        }
    }

    sanitizePrecision(number, decimals = 8) {
        return Math.round(number * Math.pow(10, decimals)) / Math.pow(10, decimals);
    }

    clear() {
        this.currentInput = '0';
        this.expression = '';
        this.isNewInput = true;
    }

    backspace() {
        if (this.currentInput.length > 1) {
            this.currentInput = this.currentInput.slice(0, -1);
        } else {
            this.currentInput = '0';
            this.isNewInput = true;
        }
    }
}
""",
        "utils/historyManager.js": """/**
 * Calculation Tape & Memory Manager
 */

export class HistoryManager {
    constructor() {
        this.storageKey = 'neocalc_history';
        this.entries = this.load();
    }

    load() {
        try {
            const raw = localStorage.getItem(this.storageKey);
            return raw ? JSON.parse(raw) : [];
        } catch {
            return [];
        }
    }

    add(expression, result) {
        const item = {
            expression,
            result,
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };
        this.entries.unshift(item);
        if (this.entries.length > 25) this.entries.pop();
        this.save();
    }

    clear() {
        this.entries = [];
        this.save();
    }

    save() {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify(this.entries));
        } catch (e) {
            console.warn('Storage quota exceeded');
        }
    }

    render(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        if (this.entries.length === 0) {
            container.innerHTML = '<p class="empty-msg">No recent calculations</p>';
            return;
        }

        container.innerHTML = this.entries.map(e => `
            <div class="history-item">
                <span class="hist-expr">${e.expression} =</span>
                <span class="hist-res">${e.result}</span>
            </div>
        `).join('');
    }
}
""",
        "package.json": """{
  "name": "neocalc-scientific",
  "version": "2.1.0",
  "description": "High precision scientific web calculator with calculation tape",
  "main": "app.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "vitest"
  },
  "keywords": ["calculator", "math-engine", "neumorphism", "scientific-calc"],
  "license": "MIT"
}
""",
        "README.md": """# 🧮 NeoCalc Pro | Scientific Web Calculator

A sleek, neumorphic web calculator supporting basic arithmetic, trigonometric functions, powers, and persistent calculation tape history.

## Features
- **Precision Floating Point Arithmetic**: Mitigates IEEE 754 precision artifacts.
- **Scientific Mode**: Trigonometry (`sin`, `cos`, `tan`), square roots, powers.
- **Calculation Tape**: Stored locally for fast reference.
- **Keyboard Navigation**: Full numpad and shortcut integration.
"""
    }
}

# =====================================================================
# PROJECT 2: NETFLIX STREAMING PLATFORM CLONE
# =====================================================================
NETFLIX_PROJECT = {
    "key": "netflix-clone",
    "name": "Netflix-Stream-Clone",
    "description": "High-Fidelity Video Streaming Platform Landing Page",
    "files": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CineStream | Watch TV Shows & Movies Online</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="streaming-body">
    <!-- Navigation Bar -->
    <header class="navbar" id="main-nav">
        <div class="nav-left">
            <span class="brand-logo">CINESTREAM</span>
            <ul class="nav-menu">
                <li><a href="#home" class="active">Home</a></li>
                <li><a href="#series">TV Shows</a></li>
                <li><a href="#movies">Movies</a></li>
                <li><a href="#popular">New & Popular</a></li>
                <li><a href="#watchlist">My List</a></li>
            </ul>
        </div>
        <div class="nav-right">
            <button class="nav-icon-btn" id="search-btn" aria-label="Search">&#128269;</button>
            <button class="nav-icon-btn" aria-label="Notifications">&#128276;</button>
            <div class="profile-avatar">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=64&h=64&fit=crop" alt="User Profile">
            </div>
        </div>
    </header>

    <!-- Billboard Hero Trailer -->
    <section class="billboard-hero" id="hero-billboard">
        <div class="hero-overlay"></div>
        <div class="hero-meta">
            <div class="series-badge">SERIES &#8226; SEASON 3</div>
            <h1 class="hero-title">CHRONICLES OF CYBERIA</h1>
            <p class="hero-synopsis">
                In a neon-drenched metropolis governed by rogue quantum intelligence, a fractured syndicate of cybernetically enhanced rebels races to prevent the final shutdown.
            </p>
            <div class="hero-actions">
                <button class="btn btn-play" id="btn-play-hero">&#9658; Play</button>
                <button class="btn btn-info" id="btn-more-info">&#9432; More Info</button>
            </div>
        </div>
    </section>

    <!-- Content Carousels Container -->
    <main class="content-container">
        <section class="movie-row" id="row-trending">
            <h2 class="row-title">Trending Now</h2>
            <div class="carousel-track" id="track-trending"></div>
        </section>

        <section class="movie-row" id="row-top10">
            <h2 class="row-title">Top 10 in Action & Thrillers</h2>
            <div class="carousel-track" id="track-top10"></div>
        </section>

        <section class="movie-row" id="row-scifi">
            <h2 class="row-title">Sci-Fi & Cyberpunk Hits</h2>
            <div class="carousel-track" id="track-scifi"></div>
        </section>
    </main>

    <!-- Video Preview Modal -->
    <div class="modal-backdrop" id="video-modal">
        <div class="modal-card">
            <button class="modal-close" id="modal-close">&times;</button>
            <div class="modal-video-placeholder">
                <div class="video-loader"></div>
                <p>Streaming 4K Ultra HD Trailer...</p>
            </div>
            <div class="modal-info">
                <h2 id="modal-movie-title">Chronicles of Cyberia</h2>
                <div class="modal-chips">
                    <span class="chip chip-match">98% Match</span>
                    <span class="chip">2026</span>
                    <span class="chip chip-rating">18+</span>
                    <span class="chip">4K HDR</span>
                </div>
                <p id="modal-movie-desc">An immersive journey into speculative technology and rebellious action.</p>
            </div>
        </div>
    </div>

    <script src="app.js" type="module"></script>
</body>
</html>
""",
        "styles.css": """:root {
    --bg-dark: #141414;
    --bg-card: #181818;
    --color-red: #E50914;
    --color-text: #ffffff;
    --color-muted: #aaaaaa;
    --nav-height: 68px;
    --font-heading: 'Bebas Neue', sans-serif;
    --font-body: 'Inter', sans-serif;
    --transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body.streaming-body {
    background: var(--bg-dark);
    color: var(--color-text);
    font-family: var(--font-body);
    overflow-x: hidden;
}

/* Navbar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: var(--nav-height);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 4%;
    z-index: 100;
    background: linear-gradient(180deg, rgba(0,0,0,0.8) 0%, transparent 100%);
    transition: background 0.3s ease;
}

.navbar.scrolled {
    background: var(--bg-dark);
}

.brand-logo {
    font-family: var(--font-heading);
    font-size: 2.2rem;
    color: var(--color-red);
    letter-spacing: 2px;
    cursor: pointer;
}

.nav-left {
    display: flex;
    align-items: center;
    gap: 36px;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 20px;
}

.nav-menu a {
    color: #e5e5e5;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: var(--transition);
}

.nav-menu a:hover, .nav-menu a.active {
    color: #ffffff;
    font-weight: 700;
}

.nav-right {
    display: flex;
    align-items: center;
    gap: 16px;
}

.nav-icon-btn {
    background: none;
    border: none;
    color: #ffffff;
    font-size: 1.1rem;
    cursor: pointer;
}

.profile-avatar img {
    width: 34px;
    height: 34px;
    border-radius: 4px;
}

/* Billboard Hero */
.billboard-hero {
    position: relative;
    height: 80vh;
    min-height: 520px;
    background: url('https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1600&auto=format&fit=crop') center/cover no-repeat;
    display: flex;
    align-items: center;
    padding: 0 4%;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(77deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 60%, transparent 100%),
                linear-gradient(180deg, transparent 65%, var(--bg-dark) 100%);
}

.hero-meta {
    position: relative;
    max-width: 580px;
    z-index: 10;
}

.series-badge {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--color-red);
    margin-bottom: 8px;
}

.hero-title {
    font-family: var(--font-heading);
    font-size: 4rem;
    line-height: 0.95;
    letter-spacing: 1.5px;
    margin-bottom: 16px;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
}

.hero-synopsis {
    font-size: 1.05rem;
    color: #d1d5db;
    line-height: 1.5;
    margin-bottom: 24px;
}

.hero-actions {
    display: flex;
    gap: 14px;
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 28px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 1.05rem;
    cursor: pointer;
    border: none;
    transition: var(--transition);
}

.btn-play {
    background: #ffffff;
    color: #000000;
}

.btn-play:hover {
    background: rgba(255, 255, 255, 0.85);
}

.btn-info {
    background: rgba(109, 109, 110, 0.7);
    color: #ffffff;
}

.btn-info:hover {
    background: rgba(109, 109, 110, 0.45);
}

/* Movie Rows */
.content-container {
    margin-top: -80px;
    position: relative;
    z-index: 20;
    padding-bottom: 60px;
}

.movie-row {
    margin-bottom: 40px;
    padding: 0 4%;
}

.row-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 14px;
}

.carousel-track {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    scroll-behavior: smooth;
    padding: 20px 0;
}

.carousel-track::-webkit-scrollbar {
    display: none;
}

.movie-card {
    flex: 0 0 240px;
    height: 140px;
    border-radius: 6px;
    overflow: hidden;
    position: relative;
    cursor: pointer;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    background: var(--bg-card);
}

.movie-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.movie-card:hover {
    transform: scale(1.15);
    z-index: 30;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.8);
}

/* Modal */
.modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(8px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 999;
}

.modal-backdrop.active {
    display: flex;
}

.modal-card {
    background: var(--bg-card);
    width: 90%;
    max-width: 680px;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 14px;
    right: 18px;
    background: rgba(0, 0, 0, 0.6);
    border: none;
    color: #fff;
    font-size: 1.6rem;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 10;
}

.modal-video-placeholder {
    height: 320px;
    background: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
    color: var(--color-muted);
}

.modal-info {
    padding: 24px;
}

.modal-chips {
    display: flex;
    gap: 8px;
    margin: 10px 0 16px;
}

.chip {
    padding: 3px 8px;
    border: 1px solid #4b5563;
    font-size: 0.75rem;
    border-radius: 3px;
}

.chip-match {
    color: #46d369;
    border-color: #46d369;
    font-weight: 700;
}
""",
        "app.js": """/**
 * CineStream Application Controller
 * Handles navbar scroll, movie rows injection, and trailer modal playback.
 */

import { MockTmdbApi } from './utils/mockTmdbApi.js';

class StreamingApp {
    constructor() {
        this.api = new MockTmdbApi();
        this.init();
    }

    async init() {
        this.bindNavbarScroll();
        this.bindModalEvents();
        await this.populateContentRows();
    }

    bindNavbarScroll() {
        const nav = document.getElementById('main-nav');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }

    bindModalEvents() {
        const modal = document.getElementById('video-modal');
        const closeBtn = document.getElementById('modal-close');
        const playHeroBtn = document.getElementById('btn-play-hero');

        if (playHeroBtn) {
            playHeroBtn.addEventListener('click', () => {
                this.openModal('Chronicles of Cyberia', 'In a neon-drenched metropolis governed by rogue quantum intelligence...');
            });
        }

        if (closeBtn && modal) {
            closeBtn.addEventListener('click', () => modal.classList.remove('active'));
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.classList.remove('active');
            });
        }
    }

    openModal(title, desc) {
        const modal = document.getElementById('video-modal');
        const titleEl = document.getElementById('modal-movie-title');
        const descEl = document.getElementById('modal-movie-desc');

        if (titleEl) titleEl.textContent = title;
        if (descEl) descEl.textContent = desc;
        if (modal) modal.classList.add('active');
    }

    async populateContentRows() {
        const trending = await this.api.getTrending();
        const top10 = await this.api.getTopRated();
        const scifi = await this.api.getSciFi();

        this.renderRow('track-trending', trending);
        this.renderRow('track-top10', top10);
        this.renderRow('track-scifi', scifi);
    }

    renderRow(containerId, items) {
        const container = document.getElementById(containerId);
        if (!container) return;

        container.innerHTML = items.map(item => `
            <div class="movie-card" data-title="${item.title}" data-desc="${item.overview}">
                <img src="${item.poster}" alt="${item.title}" loading="lazy">
            </div>
        `).join('');

        // Attach click listeners to cards
        container.querySelectorAll('.movie-card').forEach(card => {
            card.addEventListener('click', () => {
                this.openModal(card.dataset.title, card.dataset.desc);
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new StreamingApp();
});
""",
        "utils/mockTmdbApi.js": """/**
 * Mock Streaming Content Catalog API
 */

export class MockTmdbApi {
    constructor() {
        this.catalog = [
            {
                id: 101,
                title: "Singularity Rising",
                overview: "A rogue orbital station discovers an encrypted signal originating from deep inside Saturn's rings.",
                poster: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop",
                rating: 8.9,
                genre: "Sci-Fi"
            },
            {
                id: 102,
                title: "Shadow Protocol",
                overview: "An undercover forensic analyst uncovers an assassin network operating inside global financial clearinghouses.",
                poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop",
                rating: 8.4,
                genre: "Action"
            },
            {
                id: 103,
                title: "Neon Outskirts",
                overview: "Street racers in Tokyo navigate shifting underground alliances during a citywide power outage.",
                poster: "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500&auto=format&fit=crop",
                rating: 7.8,
                genre: "Thriller"
            },
            {
                id: 104,
                title: "Quantum Paradox",
                overview: "Parallel timelines collide when a particle accelerator experiment creates an infinite recursion loop.",
                poster: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&auto=format&fit=crop",
                rating: 9.1,
                genre: "Sci-Fi"
            }
        ];
    }

    async getTrending() {
        return this.catalog;
    }

    async getTopRated() {
        return [...this.catalog].reverse();
    }

    async getSciFi() {
        return this.catalog.filter(m => m.genre === 'Sci-Fi');
    }
}
""",
        "package.json": """{
  "name": "cinestream-streaming-platform",
  "version": "1.8.0",
  "description": "High fidelity video streaming landing page with carousel rows",
  "main": "app.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "keywords": ["netflix-clone", "video-streaming", "carousel", "tmdb-mock"],
  "license": "MIT"
}
""",
        "README.md": """# 🎬 CineStream | Streaming Platform UI Clone

An authentic, high-performance clone of leading video streaming platforms with billboard trailers, horizontal carousels, and video preview dialogs.
"""
    }
}

# =====================================================================
# PROJECT 3: AMAZON STOREFRONT CLONE
# =====================================================================
AMAZON_PROJECT = {
    "key": "amazon-storefront",
    "name": "Amazon-Storefront-Clone",
    "description": "Amazon / Prime E-Commerce Marketplace Web Platform",
    "files": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NovaMart | Deals in Electronics, Smart Home & Essentials</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amazon+Ember:wght@400;500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body class="storefront-body">
    <!-- Top Navigation Header -->
    <header class="header-main">
        <div class="nav-top">
            <div class="nav-logo">
                <span class="brand-text">novamart<span class="prime-tag">prime</span></span>
            </div>

            <div class="nav-deliver">
                <span class="icon-pin">&#128205;</span>
                <div class="deliver-text">
                    <span class="deliver-label">Deliver to</span>
                    <span class="deliver-location">New York 10001</span>
                </div>
            </div>

            <!-- Search Bar -->
            <div class="nav-search-bar">
                <select class="search-category" id="search-cat">
                    <option value="all">All Departments</option>
                    <option value="electronics">Electronics</option>
                    <option value="computing">Computers</option>
                    <option value="smarthome">Smart Home</option>
                </select>
                <input type="text" id="search-input" placeholder="Search NovaMart..." aria-label="Search">
                <button id="search-btn" class="btn-search">&#128269;</button>
            </div>

            <!-- Right Controls -->
            <div class="nav-account">
                <span class="sub-label">Hello, Sign in</span>
                <span class="main-label">Account &amp; Lists</span>
            </div>

            <div class="nav-orders">
                <span class="sub-label">Returns</span>
                <span class="main-label">&amp; Orders</span>
            </div>

            <div class="nav-cart" id="cart-btn">
                <span class="cart-icon">&#128722;</span>
                <span class="cart-badge" id="cart-count">0</span>
                <span class="cart-text">Cart</span>
            </div>
        </div>

        <!-- Secondary Category Subnav -->
        <nav class="sub-nav">
            <ul class="sub-nav-links">
                <li><a href="#all">&#9776; All</a></li>
                <li><a href="#deals">Today's Deals</a></li>
                <li><a href="#customer-service">Customer Service</a></li>
                <li><a href="#registry">Registry</a></li>
                <li><a href="#gift-cards">Gift Cards</a></li>
                <li><a href="#sell">Sell</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Marketplace Content -->
    <main class="store-container">
        <!-- Hero Promotional Banner -->
        <section class="store-hero">
            <div class="hero-card">
                <h1>Save up to 40% on High-Performance Tech</h1>
                <p>Equip your workstation with cutting-edge displays, mechanical keyboards, and noise-cancelling audio.</p>
                <a href="#deals" class="btn-shop">Explore Lightning Deals</a>
            </div>
        </section>

        <!-- Product Catalog Grid -->
        <section class="deals-section">
            <h2 class="section-title">Today's Featured Deals</h2>
            <div class="products-grid" id="products-grid">
                <!-- Products dynamically injected -->
            </div>
        </section>
    </main>

    <!-- Cart Slide-Out Drawer -->
    <aside class="cart-drawer" id="cart-drawer">
        <div class="cart-header">
            <h3>Shopping Cart (<span id="drawer-count">0</span> items)</h3>
            <button id="cart-close" class="btn-close">&times;</button>
        </div>
        <div class="cart-items" id="cart-items">
            <p class="empty-cart">Your NovaMart Cart is empty</p>
        </div>
        <div class="cart-footer">
            <div class="cart-subtotal">
                <span>Subtotal:</span>
                <span class="subtotal-amount" id="cart-subtotal">$0.00</span>
            </div>
            <button class="btn-checkout" id="btn-checkout">Proceed to Checkout</button>
        </div>
    </aside>

    <script src="app.js" type="module"></script>
</body>
</html>
""",
        "styles.css": """:root {
    --bg-header: #131921;
    --bg-subnav: #232f3e;
    --bg-page: #eaeded;
    --bg-card: #ffffff;
    --color-orange: #febd69;
    --color-amber: #f08804;
    --color-prime: #00a8e1;
    --color-price: #b12704;
    --color-text: #0f1111;
    --color-muted: #565959;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body.storefront-body {
    background: var(--bg-page);
    color: var(--color-text);
    font-family: 'Inter', -apple-system, sans-serif;
}

/* Header */
.header-main {
    background: var(--bg-header);
    color: #ffffff;
}

.nav-top {
    display: flex;
    align-items: center;
    padding: 10px 18px;
    gap: 20px;
}

.brand-text {
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.prime-tag {
    color: var(--color-prime);
    font-size: 0.95rem;
    font-style: italic;
    margin-left: 2px;
}

.nav-deliver {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
}

.deliver-label { font-size: 0.75rem; color: #cccccc; display: block; }
.deliver-location { font-size: 0.85rem; font-weight: 700; }

.nav-search-bar {
    display: flex;
    flex: 1;
    height: 40px;
    border-radius: 4px;
    overflow: hidden;
}

.search-category {
    background: #f3f3f3;
    border: none;
    padding: 0 10px;
    font-size: 0.85rem;
    border-right: 1px solid #ddd;
    outline: none;
}

.nav-search-bar input {
    flex: 1;
    border: none;
    padding: 0 14px;
    font-size: 0.95rem;
    outline: none;
}

.btn-search {
    background: var(--color-orange);
    border: none;
    width: 46px;
    cursor: pointer;
    font-size: 1.1rem;
}

.btn-search:hover {
    background: var(--color-amber);
}

.nav-cart {
    display: flex;
    align-items: center;
    position: relative;
    cursor: pointer;
    gap: 4px;
}

.cart-icon { font-size: 1.6rem; }
.cart-badge {
    position: absolute;
    top: -2px;
    left: 14px;
    background: var(--color-amber);
    color: #000;
    font-weight: 800;
    font-size: 0.8rem;
    padding: 1px 6px;
    border-radius: 10px;
}

/* Subnav */
.sub-nav {
    background: var(--bg-subnav);
    padding: 8px 18px;
}

.sub-nav-links {
    display: flex;
    list-style: none;
    gap: 18px;
}

.sub-nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-size: 0.88rem;
}

/* Main Container & Hero */
.store-container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 20px;
}

.store-hero {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    border-radius: 8px;
    padding: 48px;
    color: #ffffff;
    margin-bottom: 28px;
}

.store-hero h1 {
    font-size: 2.2rem;
    margin-bottom: 12px;
}

.store-hero p {
    font-size: 1.1rem;
    max-width: 580px;
    margin-bottom: 20px;
    opacity: 0.9;
}

.btn-shop {
    background: var(--color-orange);
    color: #000;
    font-weight: 700;
    padding: 12px 24px;
    border-radius: 6px;
    text-decoration: none;
    display: inline-block;
}

/* Products Grid */
.deals-section {
    background: var(--bg-card);
    padding: 24px;
    border-radius: 8px;
}

.section-title {
    font-size: 1.4rem;
    margin-bottom: 20px;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 20px;
}

.product-card {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
}

.product-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 4px;
    margin-bottom: 12px;
}

.product-title {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.product-price {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--color-price);
    margin-bottom: 12px;
}

.btn-add-cart {
    background: var(--color-orange);
    border: none;
    padding: 10px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s ease;
}

.btn-add-cart:hover {
    background: var(--color-amber);
}

/* Cart Drawer */
.cart-drawer {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: 360px;
    background: #ffffff;
    box-shadow: -4px 0 25px rgba(0, 0, 0, 0.25);
    transform: translateX(100%);
    transition: transform 0.3s ease;
    z-index: 200;
    display: flex;
    flex-direction: column;
    padding: 24px;
}

.cart-drawer.open {
    transform: translateX(0);
}

.cart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 16px;
}

.btn-close {
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
}

.cart-items {
    flex: 1;
    overflow-y: auto;
    padding: 16px 0;
}

.cart-footer {
    border-top: 1px solid #e5e7eb;
    padding-top: 16px;
}

.cart-subtotal {
    display: flex;
    justify-content: space-between;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 16px;
}

.btn-checkout {
    width: 100%;
    background: var(--color-orange);
    border: none;
    padding: 14px;
    border-radius: 8px;
    font-weight: 700;
    cursor: pointer;
}
""",
        "app.js": """/**
 * NovaMart Storefront Orchestrator
 * Manages product rendering, cart state persistence, and drawer interactions.
 */

import { ProductCatalog } from './utils/productCatalog.js';

class StorefrontApp {
    constructor() {
        this.catalog = new ProductCatalog();
        this.cart = [];
        this.init();
    }

    async init() {
        this.renderProducts();
        this.bindEvents();
    }

    bindEvents() {
        const cartBtn = document.getElementById('cart-btn');
        const cartClose = document.getElementById('cart-close');
        const cartDrawer = document.getElementById('cart-drawer');

        if (cartBtn && cartDrawer) {
            cartBtn.addEventListener('click', () => cartDrawer.classList.add('open'));
        }
        if (cartClose && cartDrawer) {
            cartClose.addEventListener('click', () => cartDrawer.classList.remove('open'));
        }

        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => this.filterProducts(e.target.value));
        }
    }

    renderProducts(items = null) {
        const grid = document.getElementById('products-grid');
        if (!grid) return;

        const products = items || this.catalog.getAll();
        grid.innerHTML = products.map(p => `
            <div class="product-card" data-id="${p.id}">
                <img src="${p.image}" alt="${p.title}" class="product-img" loading="lazy">
                <h3 class="product-title">${p.title}</h3>
                <div class="product-price">$${p.price.toFixed(2)}</div>
                <button class="btn-add-cart" data-id="${p.id}">Add to Cart</button>
            </div>
        `).join('');

        grid.querySelectorAll('.btn-add-cart').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.target.dataset.id);
                this.addToCart(id);
            });
        });
    }

    addToCart(productId) {
        const product = this.catalog.getById(productId);
        if (!product) return;

        const existing = this.cart.find(item => item.id === productId);
        if (existing) {
            existing.qty += 1;
        } else {
            this.cart.push({ ...product, qty: 1 });
        }
        this.updateCartUi();
    }

    updateCartUi() {
        const count = this.cart.reduce((sum, i) => sum + i.qty, 0);
        const subtotal = this.cart.reduce((sum, i) => sum + i.price * i.qty, 0);

        const countEl = document.getElementById('cart-count');
        const drawerCountEl = document.getElementById('drawer-count');
        const subtotalEl = document.getElementById('cart-subtotal');
        const itemsContainer = document.getElementById('cart-items');

        if (countEl) countEl.textContent = count;
        if (drawerCountEl) drawerCountEl.textContent = count;
        if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;

        if (itemsContainer) {
            if (this.cart.length === 0) {
                itemsContainer.innerHTML = '<p class="empty-cart">Your NovaMart Cart is empty</p>';
            } else {
                itemsContainer.innerHTML = this.cart.map(item => `
                    <div class="cart-row" style="display:flex; justify-content:space-between; margin-bottom:12px;">
                        <span>${item.title} (x${item.qty})</span>
                        <strong>$${(item.price * item.qty).toFixed(2)}</strong>
                    </div>
                `).join('');
            }
        }
    }

    filterProducts(query) {
        const filtered = this.catalog.search(query);
        this.renderProducts(filtered);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new StorefrontApp();
});
""",
        "utils/productCatalog.js": """/**
 * Product Catalog Data Module
 */

export class ProductCatalog {
    constructor() {
        this.products = [
            {
                id: 1,
                title: "EchoBeam Smart Speaker with Alexa & Dolby Audio",
                price: 99.99,
                category: "smarthome",
                image: "https://images.unsplash.com/photo-1543512214-318c7553f230?w=400&auto=format&fit=crop"
            },
            {
                id: 2,
                title: "QuantumPro Wireless Noise-Cancelling Headphones",
                price: 249.50,
                category: "electronics",
                image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&auto=format&fit=crop"
            },
            {
                id: 3,
                title: "UltraGlide Ergonomic Mechanical Keyboard (RGB)",
                price: 129.00,
                category: "computing",
                image: "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&auto=format&fit=crop"
            },
            {
                id: 4,
                title: "AeroVision 4K 144Hz Gaming Monitor 27-inch",
                price: 379.99,
                category: "computing",
                image: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400&auto=format&fit=crop"
            }
        ];
    }

    getAll() {
        return this.products;
    }

    getById(id) {
        return this.products.find(p => p.id === id);
    }

    search(query) {
        if (!query) return this.products;
        const q = query.toLowerCase();
        return this.products.filter(p => p.title.toLowerCase().includes(q) || p.category.includes(q));
    }
}
""",
        "package.json": """{
  "name": "novamart-storefront",
  "version": "1.4.0",
  "description": "Amazon-style e-commerce marketplace with live cart and search",
  "main": "app.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "keywords": ["amazon-clone", "storefront", "e-commerce", "shopping-cart"],
  "license": "MIT"
}
""",
        "README.md": """# 🛒 NovaMart Storefront | E-Commerce Marketplace

A full-fledged e-commerce storefront mimicking Amazon/Prime with multi-tier navigation, dynamic product grids, real-time search filtering, and slide-out cart drawer.
"""
    }
}

# =====================================================================
# PROJECT 4: ENTERPRISE SAAS ANALYTICS PLATFORM
# =====================================================================
SAAS_PROJECT = {
    "key": "saas-platform",
    "name": "SaaS-Analytics-Platform",
    "description": "Enterprise B2B Metrics & Cloud Analytics Dashboard",
    "files": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudScale | Enterprise Analytics & Telemetry Engine</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
</head>
<body class="dashboard-body">
    <div class="dashboard-layout">
        <!-- Collapsible Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-brand">
                <div class="brand-glyph">&#9881;</div>
                <span class="brand-title">CloudScale</span>
            </div>
            <nav class="sidebar-nav">
                <a href="#overview" class="nav-item active">&#128200; Overview</a>
                <a href="#analytics" class="nav-item">&#128202; Metrics</a>
                <a href="#customers" class="nav-item">&#128101; Customers</a>
                <a href="#apikeys" class="nav-item" id="btn-api-keys">&#128273; API Keys</a>
                <a href="#settings" class="nav-item">&#9881; Settings</a>
            </nav>
            <div class="sidebar-footer">
                <div class="plan-pill">Scale Tier v3.2</div>
            </div>
        </aside>

        <!-- Main Dashboard Viewport -->
        <main class="main-content">
            <!-- Topbar -->
            <header class="topbar">
                <div class="page-title">
                    <h1>Real-Time Revenue &amp; Usage Telemetry</h1>
                    <p class="text-muted">Live metrics across 4 global edge regions</p>
                </div>
                <div class="topbar-actions">
                    <button class="btn btn-outline" id="date-filter">Last 30 Days &#9662;</button>
                    <button class="btn btn-primary" id="btn-export-csv">&#128190; Export Report</button>
                </div>
            </header>

            <!-- KPI Metric Cards Grid -->
            <section class="kpi-grid">
                <div class="kpi-card">
                    <span class="kpi-label">Monthly Recurring Revenue</span>
                    <div class="kpi-value" id="kpi-mrr">$142,850</div>
                    <span class="kpi-delta delta-positive">+14.2% vs last mo</span>
                </div>
                <div class="kpi-card">
                    <span class="kpi-label">Active Subscriptions</span>
                    <div class="kpi-value" id="kpi-subs">3,842</div>
                    <span class="kpi-delta delta-positive">+8.1% vs last mo</span>
                </div>
                <div class="kpi-card">
                    <span class="kpi-label">Average API Latency</span>
                    <div class="kpi-value" id="kpi-latency">24ms</div>
                    <span class="kpi-delta delta-positive">-4ms improvement</span>
                </div>
                <div class="kpi-card">
                    <span class="kpi-label">Churn Rate</span>
                    <div class="kpi-value" id="kpi-churn">0.82%</div>
                    <span class="kpi-delta delta-positive">Industry leading</span>
                </div>
            </section>

            <!-- Chart Section -->
            <section class="chart-section">
                <div class="chart-card">
                    <div class="chart-header">
                        <h2>Revenue Stream Progression</h2>
                        <span class="live-pill"><span class="live-dot"></span> Live Feed</span>
                    </div>
                    <canvas id="revenue-chart" height="280"></canvas>
                </div>
            </section>
        </main>
    </div>

    <!-- API Key Generator Modal -->
    <div class="modal-backdrop" id="api-modal">
        <div class="modal-card">
            <h2>Generate Production API Key</h2>
            <p class="text-muted">This secret token will authorize raw telemetry ingestion.</p>
            <input type="text" id="generated-key" readonly value="sk_live_9481a8f7c9e04bb3d2">
            <div class="modal-actions">
                <button class="btn btn-primary" id="btn-copy-key">Copy Token</button>
                <button class="btn btn-outline" id="btn-close-modal">Close</button>
            </div>
        </div>
    </div>

    <script src="app.js" type="module"></script>
</body>
</html>
""",
        "styles.css": """:root {
    --bg-base: #090d16;
    --bg-surface: #111827;
    --bg-card: #1f2937;
    --border-color: rgba(255, 255, 255, 0.08);
    --color-primary: #3b82f6;
    --color-success: #10b981;
    --color-text: #f9fafb;
    --color-muted: #9ca3af;
    --font-sans: 'Plus Jakarta Sans', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body.dashboard-body {
    background: var(--bg-base);
    color: var(--color-text);
    font-family: var(--font-sans);
}

.dashboard-layout {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 260px;
    background: var(--bg-surface);
    border-right: 1px solid var(--border-color);
    padding: 24px;
    display: flex;
    flex-direction: column;
}

.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 800;
    font-size: 1.25rem;
    margin-bottom: 32px;
}

.brand-glyph {
    color: var(--color-primary);
}

.sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
}

.nav-item {
    padding: 10px 14px;
    border-radius: 8px;
    color: var(--color-muted);
    text-decoration: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: all 0.2s ease;
}

.nav-item:hover, .nav-item.active {
    background: var(--bg-card);
    color: var(--color-text);
}

.plan-pill {
    background: rgba(59, 130, 246, 0.15);
    color: var(--color-primary);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 700;
    text-align: center;
}

/* Main Content */
.main-content {
    flex: 1;
    padding: 32px;
    overflow-y: auto;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}

.page-title h1 {
    font-size: 1.8rem;
    font-weight: 700;
}

.text-muted {
    color: var(--color-muted);
    font-size: 0.95rem;
}

.topbar-actions {
    display: flex;
    gap: 12px;
}

.btn {
    padding: 10px 18px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    border: none;
    transition: all 0.2s ease;
}

.btn-primary {
    background: var(--color-primary);
    color: #fff;
}

.btn-primary:hover {
    background: #2563eb;
}

.btn-outline {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--color-text);
}

/* KPI Grid */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-bottom: 32px;
}

.kpi-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 24px;
}

.kpi-label {
    color: var(--color-muted);
    font-size: 0.85rem;
    font-weight: 600;
}

.kpi-value {
    font-size: 2rem;
    font-weight: 800;
    margin: 8px 0;
}

.delta-positive {
    color: var(--color-success);
    font-size: 0.85rem;
    font-weight: 600;
}

/* Chart Card */
.chart-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 24px;
}

.chart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.live-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.8rem;
    color: var(--color-success);
    font-weight: 600;
}

.live-dot {
    width: 8px;
    height: 8px;
    background: var(--color-success);
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.3); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* Modal */
.modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(6px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal-backdrop.open {
    display: flex;
}

.modal-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 32px;
    width: 480px;
}

.modal-card input {
    width: 100%;
    padding: 12px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    color: #fff;
    font-family: var(--font-mono);
    border-radius: 6px;
    margin: 20px 0;
}

.modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
}
""",
        "app.js": """/**
 * CloudScale Dashboard Orchestrator
 * Renders real-time telemetry charts and handles API token generation.
 */

class DashboardApp {
    constructor() {
        this.canvas = document.getElementById('revenue-chart');
        this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
        this.dataPoints = [110, 122, 118, 134, 128, 142, 155];
        this.init();
    }

    init() {
        this.drawChart();
        this.bindEvents();
        this.startRealtimeTicker();
    }

    drawChart() {
        if (!this.ctx || !this.canvas) return;
        const width = (this.canvas.width = this.canvas.parentElement.clientWidth - 48);
        const height = (this.canvas.height = 240);

        this.ctx.clearRect(0, 0, width, height);

        // Draw smooth gradient stroke
        this.ctx.beginPath();
        const step = width / (this.dataPoints.length - 1);
        this.dataPoints.forEach((val, idx) => {
            const x = idx * step;
            const y = height - ((val - 90) / 80) * height;
            if (idx === 0) this.ctx.moveTo(x, y);
            else this.ctx.lineTo(x, y);
        });

        this.ctx.strokeStyle = '#3b82f6';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
    }

    bindEvents() {
        const modal = document.getElementById('api-modal');
        const openBtn = document.getElementById('btn-api-keys');
        const closeBtn = document.getElementById('btn-close-modal');
        const copyBtn = document.getElementById('btn-copy-key');

        if (openBtn && modal) {
            openBtn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('open');
            });
        }
        if (closeBtn && modal) {
            closeBtn.addEventListener('click', () => modal.classList.remove('open'));
        }
        if (copyBtn) {
            copyBtn.addEventListener('click', () => {
                copyBtn.textContent = 'Copied!';
                setTimeout(() => (copyBtn.textContent = 'Copy Token'), 2000);
            });
        }

        window.addEventListener('resize', () => this.drawChart());
    }

    startRealtimeTicker() {
        setInterval(() => {
            const last = this.dataPoints[this.dataPoints.length - 1];
            const next = last + (Math.random() - 0.45) * 6;
            this.dataPoints.shift();
            this.dataPoints.push(Math.round(next));
            this.drawChart();
        }, 4000);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new DashboardApp();
});
""",
        "package.json": """{
  "name": "cloudscale-analytics",
  "version": "3.2.0",
  "description": "Enterprise cloud telemetry and revenue metrics platform",
  "main": "app.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "keywords": ["saas", "dashboard", "analytics", "canvas-chart"],
  "license": "MIT"
}
""",
        "README.md": """# 📊 CloudScale | Enterprise SaaS Dashboard

A real-time telemetry and revenue tracking dashboard featuring interactive canvas sparklines, KPI counters, and secret key generation.
"""
    }
}

# =====================================================================
# PROJECT 5: AGILE KANBAN TASK BOARD
# =====================================================================
KANBAN_PROJECT = {
    "key": "kanban-flow",
    "name": "Kanban-Sprint-Board",
    "description": "Collaborative Agile Kanban Project Management Board",
    "files": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SprintFlow | Agile Kanban Board</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@500&display=swap" rel="stylesheet">
</head>
<body class="kanban-body">
    <!-- Board Navigation Header -->
    <header class="board-header">
        <div class="board-brand">
            <span class="board-icon">&#9638;</span>
            <span class="board-name">SprintFlow</span>
            <span class="sprint-tag">Sprint 24 (Active)</span>
        </div>
        <div class="board-actions">
            <button class="btn btn-primary" id="btn-new-task">+ New Issue</button>
        </div>
    </header>

    <!-- Kanban Board Columns Grid -->
    <main class="board-container">
        <!-- Backlog Column -->
        <div class="kanban-column" data-status="backlog">
            <div class="column-header">
                <h3>Backlog</h3>
                <span class="column-counter" id="count-backlog">2</span>
            </div>
            <div class="cards-list" id="list-backlog">
                <div class="task-card" draggable="true" data-id="101">
                    <span class="task-id">FLOW-101</span>
                    <h4 class="task-title">Implement token refresh interceptor for Axios</h4>
                    <div class="task-footer">
                        <span class="tag tag-blue">Backend</span>
                        <span class="priority p-med">Medium</span>
                    </div>
                </div>
                <div class="task-card" draggable="true" data-id="102">
                    <span class="task-id">FLOW-102</span>
                    <h4 class="task-title">Benchmark database indexing on user queries</h4>
                    <div class="task-footer">
                        <span class="tag tag-green">Database</span>
                        <span class="priority p-low">Low</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- In Progress Column -->
        <div class="kanban-column" data-status="inprogress">
            <div class="column-header">
                <h3>In Progress</h3>
                <span class="column-counter" id="count-inprogress">1</span>
            </div>
            <div class="cards-list" id="list-inprogress">
                <div class="task-card" draggable="true" data-id="103">
                    <span class="task-id">FLOW-103</span>
                    <h4 class="task-title">Build responsive drawer for mobile navigation</h4>
                    <div class="task-footer">
                        <span class="tag tag-purple">Frontend</span>
                        <span class="priority p-high">High</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Code Review Column -->
        <div class="kanban-column" data-status="review">
            <div class="column-header">
                <h3>Code Review</h3>
                <span class="column-counter" id="count-review">1</span>
            </div>
            <div class="cards-list" id="list-review">
                <div class="task-card" draggable="true" data-id="104">
                    <span class="task-id">FLOW-104</span>
                    <h4 class="task-title">Audit accessibility contrast ratios for WCAG AA</h4>
                    <div class="task-footer">
                        <span class="tag tag-orange">Design</span>
                        <span class="priority p-high">High</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Done Column -->
        <div class="kanban-column" data-status="done">
            <div class="column-header">
                <h3>Done</h3>
                <span class="column-counter" id="count-done">1</span>
            </div>
            <div class="cards-list" id="list-done">
                <div class="task-card" draggable="true" data-id="105">
                    <span class="task-id">FLOW-105</span>
                    <h4 class="task-title">Setup CI/CD GitHub Actions test runner</h4>
                    <div class="task-footer">
                        <span class="tag tag-blue">DevOps</span>
                        <span class="priority p-med">Medium</span>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script src="app.js" type="module"></script>
</body>
</html>
""",
        "styles.css": """:root {
    --bg-board: #0b1120;
    --bg-column: #162032;
    --bg-card: #1e293b;
    --color-text: #f8fafc;
    --color-muted: #94a3b8;
    --border-color: rgba(255, 255, 255, 0.08);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body.kanban-body {
    background: var(--bg-board);
    color: var(--color-text);
    font-family: 'Inter', sans-serif;
    height: 100vh;
    display: flex;
    flex-direction: column;
}

.board-header {
    height: 64px;
    background: var(--bg-column);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 24px;
}

.board-brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.board-name {
    font-weight: 700;
    font-size: 1.2rem;
}

.sprint-tag {
    background: #0369a1;
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 600;
}

.btn-primary {
    background: #2563eb;
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
}

/* Board Layout */
.board-container {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    padding: 24px;
    overflow-x: auto;
}

.kanban-column {
    background: var(--bg-column);
    border-radius: 10px;
    border: 1px solid var(--border-color);
    padding: 16px;
    display: flex;
    flex-direction: column;
}

.column-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
}

.column-counter {
    background: rgba(255, 255, 255, 0.1);
    font-size: 0.8rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 10px;
}

.cards-list {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
    overflow-y: auto;
}

/* Task Card */
.task-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 14px;
    cursor: grab;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.task-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.task-id {
    font-family: 'Fira Code', monospace;
    font-size: 0.75rem;
    color: var(--color-muted);
}

.task-title {
    font-size: 0.95rem;
    margin: 8px 0 14px;
    line-height: 1.4;
}

.task-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.75rem;
}

.tag {
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
}

.tag-blue { background: #1e3a8a; color: #93c5fd; }
.tag-green { background: #14532d; color: #86efac; }
.tag-purple { background: #581c87; color: #d8b4fe; }
.tag-orange { background: #7c2d12; color: #fdba74; }

.priority { font-weight: 700; }
.p-high { color: #f87171; }
.p-med { color: #fbbf24; }
.p-low { color: #34d399; }
""",
        "app.js": """/**
 * SprintFlow Kanban Board Controller
 * Handles HTML5 drag and drop across sprint columns.
 */

class KanbanBoard {
    constructor() {
        this.initDragAndDrop();
    }

    initDragAndDrop() {
        const cards = document.querySelectorAll('.task-card');
        const columns = document.querySelectorAll('.cards-list');

        cards.forEach(card => {
            card.addEventListener('dragstart', () => card.classList.add('dragging'));
            card.addEventListener('dragend', () => card.classList.remove('dragging'));
        });

        columns.forEach(col => {
            col.addEventListener('dragover', (e) => {
                e.preventDefault();
                const draggingCard = document.querySelector('.dragging');
                if (draggingCard) col.appendChild(draggingCard);
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new KanbanBoard();
});
""",
        "package.json": """{
  "name": "sprintflow-kanban",
  "version": "1.2.0",
  "description": "Agile Kanban board with drag-and-drop task progression",
  "main": "app.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "keywords": ["kanban", "agile", "drag-and-drop", "sprint-board"],
  "license": "MIT"
}
""",
        "README.md": """# 📋 SprintFlow | Agile Kanban Sprint Board

Interactive drag-and-drop Kanban sprint management board for tracking engineering issues through backlog, progress, review, and completion.
"""
    }
}

# =====================================================================
# ROOT WORKSPACE HUB: PORTFOLIO SHOWCASE
# =====================================================================
WORKSPACE_HUB_FILES = {
    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Developer Workspace | Interactive Project Hub</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap">
    <style>
        :root {
            --bg: #090e17;
            --card: #111827;
            --text: #f9fafb;
            --muted: #9ca3af;
            --accent: #3b82f6;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            padding: 48px 24px;
        }
        .container { max-width: 1140px; margin: 0 auto; }
        header { text-align: center; margin-bottom: 48px; }
        h1 { font-size: 2.8rem; font-weight: 800; margin-bottom: 12px; }
        p.subtitle { color: var(--muted); font-size: 1.15rem; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
        }
        .project-card {
            background: var(--card);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 28px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.25s ease, border-color 0.25s ease;
        }
        .project-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent);
        }
        .icon { font-size: 2.4rem; margin-bottom: 16px; display: inline-block; }
        .card-title { font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; }
        .card-desc { color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 24px; }
        .btn-launch {
            background: var(--accent);
            color: #fff;
            text-decoration: none;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: 700;
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Engineering Workspace</h1>
            <p class="subtitle">Multi-project portfolio featuring web calculators, streaming clones, storefronts, and cloud dashboards.</p>
        </header>
        <div class="grid">
            <div class="project-card">
                <div>
                    <span class="icon">&#128223;</span>
                    <h2 class="card-title">NeoCalc Pro</h2>
                    <p class="card-desc">Neumorphic scientific web calculator with precision floating point evaluation and calculation tape history.</p>
                </div>
                <a href="calculator/index.html" class="btn-launch">Launch Calculator &rarr;</a>
            </div>

            <div class="project-card">
                <div>
                    <span class="icon">&#127916;</span>
                    <h2 class="card-title">CineStream</h2>
                    <p class="card-desc">High-fidelity video streaming platform clone with billboard trailers, horizontal carousels, and preview modals.</p>
                </div>
                <a href="netflix-clone/index.html" class="btn-launch">Launch CineStream &rarr;</a>
            </div>

            <div class="project-card">
                <div>
                    <span class="icon">&#128722;</span>
                    <h2 class="card-title">NovaMart Storefront</h2>
                    <p class="card-desc">Amazon/Prime e-commerce marketplace featuring department filtering, lightning deals, and slide-out cart drawer.</p>
                </div>
                <a href="amazon-storefront/index.html" class="btn-launch">Launch Storefront &rarr;</a>
            </div>

            <div class="project-card">
                <div>
                    <span class="icon">&#128202;</span>
                    <h2 class="card-title">CloudScale SaaS</h2>
                    <p class="card-desc">Enterprise analytics and financial telemetry dashboard with interactive revenue charts and API key generator.</p>
                </div>
                <a href="saas-platform/index.html" class="btn-launch">Launch CloudScale &rarr;</a>
            </div>

            <div class="project-card">
                <div>
                    <span class="icon">&#128203;</span>
                    <h2 class="card-title">SprintFlow Kanban</h2>
                    <p class="card-desc">Agile sprint task management board with HTML5 drag-and-drop progression across columns.</p>
                </div>
                <a href="kanban-flow/index.html" class="btn-launch">Launch SprintFlow &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>
""",
    "README.md": """# 🚀 Full-Stack Engineering Workspace

A multi-project web workspace showcasing authentic, production-grade applications:

1. **[calculator/](calculator/)**: Neumorphic scientific calculator with memory and calculation tape.
2. **[netflix-clone/](netflix-clone/)**: Netflix streaming media clone with movie rows and trailer previews.
3. **[amazon-storefront/](amazon-storefront/)**: E-commerce marketplace with live cart drawer and product search.
4. **[saas-platform/](saas-platform/)**: B2B Cloud metrics and revenue telemetry dashboard.
5. **[kanban-flow/](kanban-flow/)**: Agile sprint board with drag-and-drop issue tracking.
"""
}

# Catalog of all available blueprints
ALL_PROJECT_BLUEPRINTS = [
    CALCULATOR_PROJECT,
    NETFLIX_PROJECT,
    AMAZON_PROJECT,
    SAAS_PROJECT,
    KANBAN_PROJECT,
]

# Snippets pools for incremental feature additions per project type
DYNAMIC_SNIPPETS = {
    "calculator": [
        """
// Currency converter module extension
export function convertCurrency(amount, rate = 1.08) {
    return (amount * rate).toFixed(2);
}
""",
        """
// Calculate compound interest
export function computeCompoundInterest(principal, rate, years, n = 12) {
    return (principal * Math.pow((1 + (rate / 100) / n), n * years)).toFixed(2);
}
""",
        """
/* Enhanced LED display glowing shadow */
.display-container {
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
}
"""
    ],
    "netflix-clone": [
        """
// Watchlist / My List persistence helper
export function toggleWatchlist(movieId) {
    const list = JSON.parse(localStorage.getItem('cinestream_watchlist') || '[]');
    const idx = list.indexOf(movieId);
    if (idx >= 0) list.splice(idx, 1);
    else list.push(movieId);
    localStorage.setItem('cinestream_watchlist', JSON.stringify(list));
    return list;
}
""",
        """
// Audio track & subtitle stream selector
export function getAvailableAudioTracks() {
    return [
        { lang: 'English', codec: 'Dolby Atmos 5.1' },
        { lang: 'Spanish', codec: 'Stereo' },
        { lang: 'French', codec: 'Stereo' },
        { lang: 'Japanese', codec: '5.1' }
    ];
}
""",
        """
/* Smooth hover zoom effect on movie cards */
.movie-card:hover img {
    filter: brightness(1.08);
}
"""
    ],
    "amazon-storefront": [
        """
// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}
""",
        """
// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
    const date = new Date();
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}
""",
        """
/* Price discount badge */
.badge-discount {
    background: #cc0c39;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
}
"""
    ],
    "saas-platform": [
        """
// CSV Export generator for financial telemetry logs
export function exportTelemetryToCSV(records) {
    const headers = ['Timestamp', 'Region', 'MRR', 'LatencyMs'];
    const rows = records.map(r => `${r.timestamp},${r.region},${r.mrr},${r.latency}`);
    return [headers.join(','), ...rows].join('\\n');
}
""",
        """
// Calculate Annual Recurring Revenue (ARR)
export function calculateARR(mrr) {
    return mrr * 12;
}
""",
        """
/* Active status badge indicator */
.badge-active {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
}
"""
    ],
    "kanban-flow": [
        """
// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}
""",
        """
// Search and filter issues by tag or assignee
export function filterTasks(tasks, keyword) {
    const q = keyword.toLowerCase();
    return tasks.filter(t => t.title.toLowerCase().includes(q) || t.id.toLowerCase().includes(q));
}
""",
        """
/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}
"""
    ]
}

# Domain-specific developer comments
DOMAIN_COMMENTS = {
    "calculator": [
        "// Fix: adjust operator precedence for nested parentheses",
        "// Precision: prevent standard IEEE 754 floating point drift",
        "// History: persist last 25 calculations into localStorage tape",
        "/* Keyboard shortcuts: numpad and enter key navigation */",
    ],
    "netflix-clone": [
        "// Carousel: smooth horizontal scroll snapping for high DPI displays",
        "// Video: prefetch trailer metadata on card hover intent",
        "// Accessibility: support keyboard escape to close media dialog",
        "/* Netflix crimson accent gradient */",
    ],
    "amazon-storefront": [
        "// Cart: calculate item subtotal and estimated sales tax",
        "// Deals: countdown timer updates every 1000ms",
        "// Inventory: check real-time warehouse stock count",
        "/* Prime delivery badge indicator */",
    ],
    "saas-platform": [
        "// Metrics: update ARR projection based on churn delta",
        "// Security: mask raw API key in dashboard client view",
        "// Canvas: hardware accelerated chart line interpolation",
        "/* Dark mode theme token mapping */",
    ],
    "kanban-flow": [
        "// DragDrop: persist column task reordering to state store",
        "// Sprint: update remaining story points count on card move",
        "// Issue: auto-generate unique ticket key with project prefix",
        "/* Agile board column layout styling */",
    ]
}
