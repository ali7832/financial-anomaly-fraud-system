import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { AlertTriangle, BadgeCheck, Gauge, ShieldCheck, Siren, TrendingUp } from 'lucide-react';
import './styles.css';

const fallbackScore = (tx) => {
  let score = 12;
  const reasons = [];
  if (Number(tx.amount) > 5000) { score += 28; reasons.push('High-value transaction exceeds analyst review threshold'); }
  if (['crypto', 'wire_transfer', 'gift_cards'].includes(tx.merchant_category)) { score += 22; reasons.push('Merchant category has elevated fraud exposure'); }
  if (['NG', 'RU', 'KP'].includes(tx.country)) { score += 18; reasons.push('Country risk rule triggered'); }
  if (Number(tx.hour) < 5) { score += 12; reasons.push('Unusual transaction hour for customer segment'); }
  if (Number(tx.customer_age_days) < 14) { score += 16; reasons.push('New customer account with limited history'); }
  score = Math.min(score, 99);
  return {
    decision_id: `DEC-${Date.now().toString().slice(-6)}`,
    risk_score: score,
    risk_tier: score >= 75 ? 'critical' : score >= 55 ? 'high' : score >= 30 ? 'medium' : 'low',
    action: score >= 75 ? 'block_and_escalate' : score >= 55 ? 'manual_review' : score >= 30 ? 'step_up_auth' : 'approve',
    reasons: reasons.length ? reasons : ['Transaction is within normal operating pattern'],
    model_version: 'frontend-demo-v1'
  };
};

const queue = [
  ['TX-92818', '$9,800', 'Crypto', 'Critical', 'Block + escalate'],
  ['TX-92822', '$6,450', 'Wire Transfer', 'High', 'Manual review'],
  ['TX-92841', '$2,110', 'Gift Cards', 'Medium', 'Step-up auth'],
  ['TX-92844', '$740', 'Travel', 'Low', 'Approve']
];

function App(){
  const [tx, setTx] = useState({ amount: 9500, merchant_category: 'crypto', country: 'NG', hour: 2, customer_age_days: 3 });
  const [result, setResult] = useState(fallbackScore(tx));
  const metrics = useMemo(() => [
    ['Blocked Fraud', '$1.42M', '+18.2%', ShieldCheck],
    ['Precision', '94.8%', '+3.1%', Gauge],
    ['Open Reviews', '128', '-22 today', Siren],
    ['Model Drift', 'Low', 'stable', BadgeCheck]
  ], []);

  const update = (key, value) => setTx((current) => ({...current, [key]: value}));
  const score = async () => {
    try {
      const response = await fetch('/score', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(tx) });
      if (!response.ok) throw new Error('API unavailable');
      setResult(await response.json());
    } catch {
      setResult(fallbackScore(tx));
    }
  };

  return <main className="shell">
    <nav className="topbar"><div><strong>FraudOps AI</strong><span>Financial Anomaly Command Center</span></div><button onClick={score}>Score transaction</button></nav>
    <section className="hero">
      <div><p className="eyebrow">Enterprise fraud intelligence</p><h1>Real-time anomaly detection for high-risk financial transactions.</h1><p>Hybrid ML and explainable rules help fraud analysts prioritize suspicious activity, reduce false positives, and preserve an auditable decision trail.</p></div>
      <div className="decision"><span className={result.risk_tier}>{result.risk_tier}</span><h2>{result.risk_score}/100 risk score</h2><p>{result.action}</p><small>{result.decision_id} · {result.model_version}</small></div>
    </section>
    <section className="metrics">{metrics.map(([label,value,delta,Icon]) => <article className="card" key={label}><Icon size={22}/><span>{label}</span><strong>{value}</strong><small>{delta}</small></article>)}</section>
    <section className="grid">
      <article className="panel"><p className="eyebrow">Transaction simulator</p><h2>Score a payment</h2>{Object.entries(tx).map(([key,value]) => <label key={key}>{key.replaceAll('_',' ')}<input value={value} onChange={(e)=>update(key,e.target.value)} /></label>)}<button onClick={score}>Run risk scoring</button></article>
      <article className="panel"><p className="eyebrow">Explainability</p><h2>Decision reasons</h2>{result.reasons.map((reason) => <div className="reason" key={reason}><AlertTriangle size={18}/><span>{reason}</span></div>)}</article>
    </section>
    <section className="panel"><p className="eyebrow">Analyst workbench</p><h2>Priority review queue</h2><div className="table">{queue.map((row) => <div className="row" key={row[0]}>{row.map((cell)=><span key={cell}>{cell}</span>)}</div>)}</div></section>
  </main>;
}

createRoot(document.getElementById('root')).render(<App/>);
