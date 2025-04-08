import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API
import ReactModal from 'react-modal';

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const [dataUser, setDataUser] = useState([]); // ID de datos seleccionados
  const user = JSON.parse(localStorage.getItem("user")); // Obtener usuario desde localStorage
  const [openModal, setOpenModal] = useState(false); // Estado del modal
  const [formFields, setFormFields] = useState([]);
  const [formData, setFormData] = useState({
    email: dataUser.email || "",
    name: dataUser.name || "",
    surname: dataUser.surname || "",
    control_number: dataUser.control_number || "",
    age: dataUser.age || "",
    tel: dataUser.tel || "",
  });
  const [errors, setErrors] = useState({});

  async function refreshAccessToken() {
    const refresh = localStorage.getItem("refreshToken");
  
    try {
      const response = await fetch("http://127.0.0.1:8000/users/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh }),
      });
  
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem("accessToken", data.access); // Guardar nuevo token
        return data.access;
      } else {
        console.error("Error al refrescar token:", response.status);
        return null;
      }
    } catch (error) {
      console.error("Excepción al refrescar token:", error);
      return null;
    }
  }

  const borrarUser = (id) => {
    // Lógica para borrar usuario (puedes implementar una llamada a la API aquí)
    console.log(`Borrando usuario con ID: ${id}`);
    if (id === user.id) {
      alert("No puedes borrar tu propio usuario");
    } else {
      refreshAccessToken()
      let config = {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        }
      }
      let URL = "http://127.0.0.1:8000/users/api/" + id + "/"
      axios.delete(URL, config)
        .then((response) => {
          console.log("Usuario borrado:", response.data);
          alert("Usuario borrado correctamente");
          fetchData(); // Refrescar la tabla después de borrar el usuario
        })
        .catch((error) => {
          console.error("Error al borrar el usuario:", error);
          alert("Error al borrar el usuario, contacte con el administrador");
        });
    }

  }

  const editClick = (user) => {
    axios
      .get("http://127.0.0.1:8000/users/updateform/" + user.id + "/")
      .then((response) => {
        console.log(response.data); // Verifica que los datos se reciban correctamente
        setFormFields(response.data);
        setLoading(false);
        setDataUser(user); // Guardar el ID del usuario seleccionado
        setFormData({
          email: user.email || "",
          name: user.name || "",
          surname: user.surname || "",
          control_number: user.control_number || "",
          age: user.age || "",
          tel: user.tel || "",
        });
        setOpenModal(true); // Abrir el modal
      })
      .catch((error) => {
        console.error("Error al obtener los datos, contacte con el administrador", error);
        setLoading(false);
      });
  }

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => editClick(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => borrarUser(row.id)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  const fetchData = async () => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }

  useEffect(() => {
    fetchData(); // Llamar a la función para obtener datos al cargar el componente
  }, []);



  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
  
    // Obtener el nuevo token (si es necesario)
    const newAccessToken = await refreshAccessToken();
  
    if (!newAccessToken) {
      alert("No se pudo autenticar. Intente iniciar sesión nuevamente.");
      return;
    }

    let config = {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
      },
    }

    axios
    .put("http://127.0.0.1:8000/users/api/" + dataUser.id + "/", formData, config)
    .then((response) => {
      alert("Usuario actualizado correctamente");
      setErrors({});
      setLoading(false);
      fetchData(); // Refrescar tabla
      setOpenModal(false);
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        setErrors(error.response.data);
      } else {
        alert("Ocurrió un error inesperado.");
      }
      console.error("Error al enviar el formulario", error);
      alert("Error al actualizar el usuario, contacte con el administrador");
      setLoading(false);
      window.scrollTo(0, 0);
    });
};

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
      <ReactModal
        isOpen={openModal}
        onAfterOpen={() => console.log("Modal abierto")}
        onRequestClose={() => setOpenModal(false)}
        contentLabel="Detalles del Usuario"
        className="ReactModal__Content"
        overlayClassName="ReactModal__Overlay"
        ariaHideApp={false} >
        <div>

          <h1>Actualizar Usuario</h1>
          <form onSubmit={handleSubmit}>
            {formFields &&
              Object.keys(formFields).map((field) => {
                const { label, input, type } = formFields[field];
                return (
                  <div key={field}>
                    <label htmlFor={input.id}>{label}</label>
                    <input
                      {...input}
                      value={formData[field] || ""}
                      onChange={handleInputChange}
                      name={field}
                      type={type || "text"}
                    />
                    {errors[field] && (
                      <span autoFocus className="text-danger">
                        {errors[field].map((errorMsg, index) => (
                          <span>
                            <i className="bi bi-exclamation-circle-fill me-1"></i>
                            {errorMsg}
                          </span>
                        ))}
                      </span>
                    )}
                    <br />
                  </div>
                );
              })}
            <button type="submit">Enviar</button>
          </form>
        </div>
      </ReactModal>
    </div>
  );
};

export default UserDataTable;
