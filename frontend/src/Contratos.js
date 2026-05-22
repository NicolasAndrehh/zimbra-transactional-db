import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function App() {

  const [formulario, setFormulario] = useState({
    prospecto_id: "",
    monto_total: "",
    fecha_cierre: "",
    metodo_pago: "",
    plan_adquirido: ""
  });

  const handleChange = (e) => {

    setFormulario({
      ...formulario,
      [e.target.name]: e.target.value
    });

  };

  const guardarContrato = async (e) => {

    e.preventDefault();

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/api/contratos",
        formulario
      );

      alert(response.data.mensaje);
      window.location.reload();

    } catch (error) {

      console.log(error);

      alert("Error al registrar contrato");

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

    <div className="container mt-5">

      <div className="row justify-content-center">

        <div className="col-md-6">

          <div className="card shadow-lg p-4">

            <h2 className="text-center mb-4">
              Registro de Contratos
            </h2>

            <form onSubmit={guardarContrato}>

              {/* ID Prospecto */}
              <div className="mb-3">

                <label className="form-label">
                  ID Prospecto
                </label>

                <input
                  type="number"
                  name="prospecto_id"
                  className="form-control"
                  onChange={handleChange}
                  required
                />

              </div>

              {/* Monto */}
              <div className="mb-3">

                <label className="form-label">
                  Monto Total
                </label>

                <input
                  type="number"
                  name="monto_total"
                  className="form-control"
                  onChange={handleChange}
                  required
                />

              </div>

              {/* Fecha */}
              <div className="mb-3">

                <label className="form-label">
                  Fecha de Cierre
                </label>

                <input
                  type="date"
                  name="fecha_cierre"
                  className="form-control"
                  onChange={handleChange}
                  required
                />

              </div>

              {/* Metodo Pago */}
              <div className="mb-3">

                <label className="form-label">
                  Método de Pago
                </label>

                <select
                  name="metodo_pago"
                  className="form-select"
                  onChange={handleChange}
                  required
                >

                  <option value="">
                    Seleccione un método
                  </option>

                  <option value="Transferencia">
                    Transferencia
                  </option>

                  <option value="Crédito">
                    Crédito
                  </option>

                  <option value="Débito">
                    Débito
                  </option>

                </select>

              </div>

              {/* Plan */}
              <div className="mb-4">

                <label className="form-label">
                  Plan Adquirido
                </label>

                <select
                  name="plan_adquirido"
                  className="form-select"
                  onChange={handleChange}
                  required
                >

                  <option value="">
                    Seleccione un plan
                  </option>

                  <option value="Standard ZCS">
                    Standard ZCS
                  </option>

                  <option value="Professional ZCS">
                    Professional ZCS
                  </option>

                  <option value="Enterprise ZCS">
                    Enterprise ZCS
                  </option>

                </select>

              </div>

              {/* Botón */}
              <button
                type="submit"
                className="btn btn-primary w-100"
              >
                Guardar Contrato
              </button>

            </form>

          </div>

        </div>

      </div>

    </div>

    </div>
  );

}

export default App;