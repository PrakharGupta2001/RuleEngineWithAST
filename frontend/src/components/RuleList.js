// frontend/src/components/RuleList.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function RuleList({ onEdit, onDelete }) {
  const [rules, setRules] = useState([]);

  useEffect(() => {
    fetchRules();
  }, []);

  const fetchRules = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/rules');
      setRules(response.data.rules);
    } catch (error) {
      console.error('Error fetching rules:', error);
    }
  };

  return (
    <div>
      <h3>Rules List</h3>
      <ul className="list-group">
        {rules.map((rule) => (
          <li key={rule[0]} className="list-group-item d-flex justify-content-between align-items-center">
            {rule[1]}
            <div>
              <button className="btn btn-secondary btn-sm me-2" onClick={() => onEdit(rule[0], rule[1])}>
                Edit
              </button>
              <button className="btn btn-danger btn-sm" onClick={() => onDelete(rule[0])}>
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RuleList;
