import { Link } from "react-router-dom";

function Home() {

  return (

    <div className="container mt-5">

      <h1 className="text-center mb-5">
        Sistema Comercial Zimbra
      </h1>

      <div className="row justify-content-center">

        <div className="col-md-4">

          <div className="card shadow p-4 text-center">

            <h3 className="mb-4">
              Registrar Contratos
            </h3>

            <Link
              to="/contratos"
              className="btn btn-primary"
            >
              Ir al Formulario
            </Link>

          </div>

        </div>

        <div className="col-md-4">

          <div className="card shadow p-4 text-center">

            <h3 className="mb-4">
              Reporte General Zimbra
            </h3>

            <Link
              to="/reportes"
              className="btn btn-success"
            >
              Ver Reportes
            </Link>

          </div>

        </div>

      </div>

    </div>

  );

}

export default Home;