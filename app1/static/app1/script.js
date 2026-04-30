const TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3NTM3NzYzLCJpYXQiOjE3Nzc1Mzc0NjMsImp0aSI6IjUxOWI1Mzg3MzI5MTRkMTI4ODkxZGRlYTRjZTM2ZGIzIiwidXNlcl9pZCI6IjEifQ.TC5U6cYdSgYDsZ9tRHOL3uj_3gnJqiS7HkTFMSZ6jcI"
function loadEmployee() {
    fetch("http://127.0.0.1:8000/Employee/", {
        headers: { "Authorization": "Bearer " + TOKEN }
    })
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("employeeList");
            list.innerHTML = "";

            data.forEach(emp => {
                const li = document.createElement("li");
                li.innerHTML = `
                <strong>${emp.name}</strong> - ${emp.age} - ${emp.position} - ₹${emp.salary}
            `;
                list.appendChild(li);
            });
        })
        .catch(error => console.error(error));
}
function loadTask() {
    fetch("http://127.0.0.1:8000/Task/", {
        headers: { "Authorization": "Bearer " + TOKEN }
    })
        .then(res => res.json())
        .then(items => {
            const list = document.getElementById("TaskList");
            list.innerHTML = "";
            items.forEach(tasks => {
                const li = document.createElement("li")
                li.innerHTML = `
                <strong>${tasks.title}</strong> - ${tasks.description} - ${tasks.completed} - ${tasks.employee}
            `;
                list.appendChild(li);
            });
        })
        .catch(error => console.error(error));
}
function loadProject() {
    fetch("http://127.0.0.1:8000/Project/", {
        headers: { "Authorization": "Bearer " + TOKEN }
    })
        .then(res => res.json())
        .then(data =>{
            const list = document.getElementById("Project");
            list.innerHTML=''
            data.forEach(project=>{
                const li = document.createElement("li");
                li.innerHTML=`
                <strong>${project.name}</strong> - ${project.description} - ₹${project.number_of_projects}
            `;
                list.appendChild(li);
            });
        })
        .catch(error => console.error(error));
}
function loadOrder(){
    fetch('http://127.0.0.1:8000/Order/', {
        headers:{"Authorization":"Bearer " + TOKEN}
    })
    .then(res=>res.json())
    .then(data=>{
        const list = document.getElementById("Order");
        list.innerHTML=''
        data.forEach(order=>{
            const li=document.createElement('li')
            li.innerHTML=`
            <strong>${order.order_number} - ${order.order_date} - ${order.total_amount}`
            list.appendChild(li)
        })
    })
    .catch(error => console.error(error));
}
function loadCertificate(){
    fetch("http://127.0.0.1:8000/Certificate/", {
        headers: { "Authorization": "Bearer " + TOKEN }
    })
    .then(res => res.json())
    .then(data => {


        const list = document.getElementById("Certificate");
        list.innerHTML = '';

        items.forEach(data => {
            const li = document.createElement("li");

            li.innerHTML = `
                <span>${data.certificate_name}</span>
                <span>${data.issued_date}</span>
                <span>${data.expiry_date}</span>
            `;

            list.appendChild(li);
        });
    })
    .catch(console.error);
}