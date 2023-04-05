function getData() {
    document.getElementById("data_table").style.display = "table";
    var form = document.getElementById("formContent");
    var employee_id = form.elements["EmployeeID"].value;
    var company_id = form.elements["CompanyID"].value;
    var year = form.elements["year"].value;
    console.log("Employee ID: " + employee_id);
    console.log("Company ID: " + company_id);
    console.log("Year: " + year);
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