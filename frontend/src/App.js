// frontend/src/App.js

import React, { useState } from 'react';
import axios from 'axios';  // Add this line to import axios
import RuleForm from './components/RuleForm';
import RuleList from './components/RuleList';
import EvaluateRuleForm from './components/EvaluateRuleForm';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [message, setMessage] = useState('');

  const handleSuccess = (msg) => {
    setMessage(msg);
    setTimeout(() => setMessage(''), 3000); // Clear the message after 3 seconds
  };

  const handleEdit = (id, ruleText) => {
    setMessage(`Editing rule with ID: ${id} - ${ruleText}`);
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:5000/rules/${id}`);
      setMessage(`Rule with ID ${id} deleted successfully.`);
    } catch (error) {
      console.error('Error deleting rule:', error);
    }
  };

  return (
    <div className="container">
      <h1>Zeotap Rule Engine</h1>
      <RuleForm onSuccess={handleSuccess} />
      <RuleList onEdit={handleEdit} onDelete={handleDelete} />
      <EvaluateRuleForm />
      {message && <div className="alert alert-success mt-3">{message}</div>}
    </div>
  );
}

export default App;
