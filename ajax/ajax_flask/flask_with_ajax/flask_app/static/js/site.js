
async function getUsers(){
    // important to note that the url here needs to patch the domain we visit.
    // if we visit localhost:5000 then the 127.0.0.7:5000 needs to be change to match
    // or we get a cross over origin error (error 202) in console and no data will be fetched
    fetch('http://127.0.0.1:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                console.log("This data here",data[i].user_name)
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();

