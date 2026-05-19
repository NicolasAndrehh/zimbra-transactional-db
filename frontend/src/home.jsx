import React from 'react';

function Home() {
  return (
    <div className="page-container">
      <h2>Panel Principal</h2>
      <p>Bienvenido al Sistema de Gestión Comercial Zimbra.</p>
      
      <div className="dashboard-grid">
        <div className="stat-card">
          <h3>Plataforma</h3>
          <p className="stat-text">Zimbra Collaboration Suite</p>
        </div>
        <div className="stat-card">
          <h3>Estado del Sistema</h3>
          <p className="stat-text text-success">Operativo</p>
        </div>
      </div>
    </div>
  );
}

export default Home;