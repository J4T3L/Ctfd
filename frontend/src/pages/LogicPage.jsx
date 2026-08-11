import React, { useState } from 'react';
import { ShoppingCart } from 'lucide-react';

export default function LogicPage() {
  const [quantity, setQuantity] = useState('-10');
  const [result, setResult] = useState('');

  const handlePurchase = async (e) => {
    e.preventDefault();
    try {
      const bodyData = new URLSearchParams();
      bodyData.append('quantity', quantity);

      const res = await fetch('/logic_shop/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      setResult(text);
    } catch (err) {
      setResult('Purchase Error');
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-medium">MEDIUM • 350 PTS • BUSINESS LOGIC</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Cloud Compute Credits Store
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Enterprise license store. Perform parameter tampering by submitting negative quantities (e.g. <code>-10</code>) to manipulate account balance.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handlePurchase}>
          <div className="form-group">
            <label className="form-label">Item Quantity</label>
            <input 
              type="number" 
              className="form-input" 
              value={quantity} 
              onChange={(e) => setQuantity(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary">
            Purchase Flag Credits 🛍️
          </button>
        </form>

        {result && (
          <div style={{ marginTop: '1.5rem' }}>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: result }} />
          </div>
        )}
      </div>
    </div>
  );
}
