import React from 'react';

function Precios() {
  return (
    <div className="page-container">
      <h2>Planes y Precios</h2>
      <p>Selecciona el plan transaccional que mejor se adapte a tu empresa.</p>
      
      <div className="pricing-grid">
        <div className="pricing-card">
          <h3>Standard ZCS</h3>
          <p className="price">$50<span>/mes</span></p>
          <ul>
            <li>Correo empresarial</li>
            <li>Calendario compartido</li>
            <li>Soporte estándar (Email)</li>
          </ul>
          <button className="btn-primary">Seleccionar Plan</button>
        </div>
        
        <div className="pricing-card featured">
          <h3>Professional ZCS</h3>
          <p className="price">$99<span>/mes</span></p>
          <ul>
            <li>Todo lo del plan Standard</li>
            <li>Videoconferencias y Chat integrados</li>
            <li>Soporte técnico 24/7</li>
          </ul>
          <button className="btn-primary">Seleccionar Plan</button>
        </div>
      </div>
    </div>
  );
}

export default Precios;