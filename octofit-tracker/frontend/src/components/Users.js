import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Users = () => {
  const [users, setUsers] = useState([]);
  const endpoint = `https://${window.location.hostname.replace('-3000', '-8000')}.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Users API endpoint:', endpoint);
        console.log('Fetched users:', data);
        setUsers(data.results || data);
      });
  }, [endpoint]);

    return (
      <div className="card mb-4">
        <div className="card-body">
          <h2 className="card-title h4 mb-3">Users</h2>
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>Name</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  <td>{user.name || JSON.stringify(user)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button className="btn btn-warning mt-2">Add User</button>
        </div>
      </div>
    );
};

export default Users;
