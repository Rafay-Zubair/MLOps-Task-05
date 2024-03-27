import React, { useState } from 'react';

const App = () => {
  const [formData, setFormData] = useState({ username: '', email: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formData_ = new FormData();
      formData_.append('username', formData['username']);
      formData_.append('email', formData['email']);

      const response = await fetch('http://${process.env.BACKEND_SERVICE_URL}/addUser', {
        method: 'POST',
        body: formData_,
      });
      // const data = await response.json();
      // console.log('Response from server:', data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
          required
        />
      </label>
      <br />
      <label>
        Email:
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
};

export default App;
