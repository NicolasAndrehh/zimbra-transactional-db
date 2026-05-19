// src/Tracker.jsx
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

function Tracker({ prospectoId }) {
  const location = useLocation(); // Captura la ruta actual automáticamente

  useEffect(() => {
    if (!prospectoId) return;

    // Motor de reglas básico: Mapeamos la URL al tipo de evento de tu BD
    let tipoEvento = 'Visita General';
    if (location.pathname === '/precios') {
      tipoEvento = 'Visita Precios';
    } else if (location.pathname === '/descargas') {
      tipoEvento = 'Descarga';
    }

    const registrarEvento = async () => {
      const datosEvento = {
        prospecto_id: prospectoId,
        tipo_evento: tipoEvento,
        url_visitada: location.pathname
      };

      try {
        await fetch('http://localhost:5000/api/track-event', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(datosEvento),
        });
      } catch (error) {
        console.error("Error en el tracking automático:", error);
      }
    };

    registrarEvento();

  }, [location, prospectoId]); // Cada vez que cambie la URL (location), se vuelve a ejecutar

  return null; // No renderiza nada en pantalla
}

export default Tracker;