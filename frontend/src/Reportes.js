import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function App() {

  const [reportes, setReportes] = useState([]);

  useEffect(() => {

    obtenerReportes();

  }, []);

  const obtenerReportes = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:5000/api/reportes"
      );

      setReportes(response.data);

    } catch (error) {

      console.log(error);

    }

  };

  return (

    <div className="container mt-3">

      {/* BOTÓN VOLVER */}
      <div className="mb-3">

        <Link
          to="/"
          className="btn btn-outline-dark"
        >
          ← Volver al Inicio
        </Link>

      </div>

      {/* TÍTULO */}
      <h1 className="text-center mb-4">
        Reporte General Zimbra
      </h1>

      {/* TABLA */}
      <div className="table-responsive">

        <table className="table table-bordered table-hover shadow">

          <thead className="table-dark">

            <tr>

              <th>ID</th>
              <th>Empresa</th>
              <th>Email</th>
              <th>Estado</th>
              <th>Monto</th>
              <th>Método Pago</th>
              <th>Plan</th>
              <th>Fecha</th>

            </tr>

          </thead>

          <tbody>

            {reportes.map((reporte) => (

              <tr key={reporte.prospecto_id}>

                <td>{reporte.prospecto_id}</td>

                <td>{reporte.nombre_empresa}</td>

                <td>{reporte.email_contacto}</td>

                <td>{reporte.estado_prospecto}</td>

                {/* MONTO */}
                <td>
                  {
                    reporte.monto_total
                    ? `$ ${reporte.monto_total}`
                    : reporte.estado_prospecto === "Sin Interes"
                    ? "Cancelado"
                    : reporte.estado_prospecto === "Cliente Activo"
                    ? "Cliente recurrente"
                    : "Pendiente"
                  }
                </td>

                {/* MÉTODO PAGO */}
                <td>
                  {
                    reporte.metodo_pago
                    ? reporte.metodo_pago
                    : "—"
                  }
                </td>

                {/* PLAN */}
                <td>
                  {
                    reporte.plan_adquirido
                    ? reporte.plan_adquirido
                    : "—"
                  }
                </td>

                {/* FECHA */}
                <td>
                  {
                    reporte.fecha_cierre
                    ? reporte.fecha_cierre
                    : "—"
                  }
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>

  );

}

export default App;