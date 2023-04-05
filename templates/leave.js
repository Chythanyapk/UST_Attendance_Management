
function getData() {
    var form = document.getElementById("formContent");
    var name = form.elements["Name"].value;
    var leaverRequest_id = form.elements["LeaveRequestID"].value;
    var employee_id = form.elements["EmployeeID"].value;
    var duration = form.elements["Duration"].value;
    console.log("Employee ID: " + employee_id);
    console.log("LeaveRequest ID: " + leaveRequest_id);
    console.log("Leave Type: " + leavetype);
    console.log("Duration: " + duration);
    const url = `http://127.0.0.1:8000/record/viewattendance/${employee_id}/${company_id}/${year}`;
    fetch(url)

        .then(response => response.json())
        .then(data => {


            if (duration < { permissibleLeave }) {
                document.writeIn("Hi" + name + "your leave request approved");

            }
            else {
                document.writeIn("Hi" + name + "your leave request rejected")
            }



        })
        .catch(error => console.error(error));
}