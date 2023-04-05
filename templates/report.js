
function getData() {
    document.getElementById("data_table").style.display = "table";
    const employee_id = document.getElementById("employee_id").value;
    const company_id = document.getElementById("company_id").value;
    const year = document.getElementById("year").value;

    const url = `http://127.0.0.1:8000/record/viewattendance/${employee_id}/${company_id}/${year}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("data_body");
            tableBody.innerHTML = "";
            for (let month in data) {
                if (month !== "company_id" && month !== "employee_id" && month !== "year" && month !== "employee_name") {
                    const row = tableBody.insertRow();
                    const monthCell = row.insertCell(0);
                    monthCell.innerHTML = month;
                    const hoursCell = row.insertCell(1);
                    hoursCell.innerHTML = data[month];
                }
            }
        })
        .catch(error => console.error(error));
}