/**
 * CloudScale Dashboard Orchestrator
 * Renders real-time telemetry charts and handles API token generation.
 */

class DashboardApp {
    constructor() {
        this.canvas = document.getElementById('revenue-chart');
        this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
        this.dataPoints = [110, 122, 118, 134, 128, 142, 155];
        this.init();
// Security: mask raw API key in dashboard client view
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

// Calculate Annual Recurring Revenue (ARR)
export function calculateARR(mrr) {
    return mrr * 12;
}

/* Active status badge indicator */
.badge-active {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

// Calculate Annual Recurring Revenue (ARR)
export function calculateARR(mrr) {
    return mrr * 12;
}

/* Active status badge indicator */
.badge-active {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

// Calculate Annual Recurring Revenue (ARR)
export function calculateARR(mrr) {
    return mrr * 12;
}

// CSV Export generator for financial telemetry logs
export function exportTelemetryToCSV(records) {
    const headers = ['Timestamp', 'Region', 'MRR', 'LatencyMs']; // reviewed
    const rows = records.map(r => `${r.timestamp},${r.region},${r.mrr},${r.latency}`);
    return [headers.join(','), ...rows].join('\n');
}
