// Inventory: check real-time warehouse stock count // verified 24:48
/**
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
        if (searchInput) { // verified 03:02 // verified 58:43
            searchInput.addEventListener('input', (e) => this.filterProducts(e.target.value)); // verified 52:13
        }
    }

    renderProducts(items = null) {
        const grid = document.getElementById('products-grid');
        if (!grid) return;
 // verified 55:12
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
            btn.addEventListener('click', (e) => { // verified 39:36
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
// Deals: countdown timer updates every 1000ms
        const count = this.cart.reduce((sum, i) => sum + i.qty, 0);
        const subtotal = this.cart.reduce((sum, i) => sum + i.price * i.qty, 0);

        const countEl = document.getElementById('cart-count');
        const drawerCountEl = document.getElementById('drawer-count');
        const subtotalEl = document.getElementById('cart-subtotal');
        const itemsContainer = document.getElementById('cart-items');

        if (countEl) countEl.textContent = count;
        if (drawerCountEl) drawerCountEl.textContent = count;
        if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;

// Deals: countdown timer updates every 1000ms
        if (itemsContainer) {
            if (this.cart.length === 0) {
                itemsContainer.innerHTML = '<p class="empty-cart">Your NovaMart Cart is empty</p>';
/* Prime delivery badge indicator */
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
 // verified 27:26
document.addEventListener('DOMContentLoaded', () => {
    new StorefrontApp();
});

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
// Cart: calculate item subtotal and estimated sales tax
    const date = new Date();
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
    const date = new Date();
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
// Inventory: check real-time warehouse stock count
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

/* Price discount badge */
.badge-discount {
    background: #cc0c39;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
}

/* Price discount badge */
.badge-discount {
    background: #cc0c39;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
}

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
    const date = new Date(); // reviewed
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
    const date = new Date();
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

// Coupon code discount validator // verified 54:17
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}
// Deals: countdown timer updates every 1000ms

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
    const date = new Date();
    date.setDate(date.getDate() + 2);
    return date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

/* Price discount badge */
.badge-discount {
    background: #cc0c39;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

/* Price discount badge */
.badge-discount {
    background: #cc0c39;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}

// Coupon code discount validator
export function applyPromoCoupon(cartTotal, couponCode) {
    const promos = { 'SAVE10': 0.10, 'PRIME20': 0.20, 'FREESHIP': 5.99 };
    const discount = promos[couponCode.toUpperCase()] || 0;
    return Math.max(0, cartTotal * (1 - discount));
}
