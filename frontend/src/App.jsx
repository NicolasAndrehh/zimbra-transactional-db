// src/App.jsx
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Tracker from './Tracker';
import './App.css';

// Importamos los componentes reales que acabas de crear
import Home from './Home';
import Precios from './Precios';
import Descargas from './Descargas';

function App() {
  // ID de prueba duro para validar que impacte a un prospecto existente en tu MySQL
  const prospectoPruebaId = 1; 

  return (
    <Router>
      {/* El Tracker vive aquí adentro para poder usar el contexto del Router */}
      <Tracker prospectoId={prospectoPruebaId} />

      <div className="app-container">
        <header>
          <h1>Zimbra CRM System</h1>
          <nav className="navbar">
            <Link to="/" className="nav-link">Inicio</Link>
            <Link to="/precios" className="nav-link">Ver Precios</Link>
            <Link to="/descargas" className="nav-link">Descargas</Link>
          </nav>
        </header>

        <main style={{ marginTop: '20px' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/precios" element={<Precios />} />
            <Route path="/descargas" element={<Descargas />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;