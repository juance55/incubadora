let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5] }
    ],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listRegistro();

    dataTable = $("#datatable-registro").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listRegistro = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_registro/");
        const data = await response.json();

        let content = ``;
        data.registro.forEach((registro, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${registro.fecha}</td>
                    <td>${registro.tiempo_encubacion}</td>
                    <td>${registro.tasa_mortalidad}</td>
                    <td>${registro.tasa_supervivencia}</td>
                    <td>${registro.evaluar_raza}</td>
                    <td>${registro.inversion}</td>
                </tr>`;
        });
        tableBody_registro.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});