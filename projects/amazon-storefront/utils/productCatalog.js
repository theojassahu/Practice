/**
 * Product Catalog Data Module
 */

export class ProductCatalog {
// Inventory: check real-time warehouse stock count
    constructor() {
        this.products = [
            {
                id: 1,
                title: "EchoBeam Smart Speaker with Alexa & Dolby Audio",
                price: 99.99, // verified 45:55
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

// Calculate estimated Prime delivery window
export function getPrimeDeliveryEstimate() {
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
 // verified 46:43
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
