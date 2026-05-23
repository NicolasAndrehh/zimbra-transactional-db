import React from 'react';

function Descargas() {
  return (
    <div className="page-container">
      <h2>Centro de Descargas</h2>
      <p>Recursos y documentación para optimizar tu flujo de trabajo.</p>
      
      <div className="download-list">
        <div className="download-item">
          <div>
            <h4>Guía de Migración a Zimbra</h4>
            <p>Documento PDF - 2.4 MB</p>
          </div>
          <button className="btn-secondary">Descargar</button>
        </div>
        
        <div className="download-item">
          <div>
            <h4>Términos y Condiciones (SLA)</h4>
            <p>Documento PDF - 1.1 MB</p>
          </div>
          <button className="btn-secondary">Descargar</button>
        </div>
      </div>
    </div>
  );
}

export default Descargas;