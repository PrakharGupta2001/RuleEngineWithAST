// frontend/src/components/RuleForm.js

import React, { useState } from 'react';
import axios from 'axios';

function RuleForm({ onSuccess, ruleId = null, initialRule = '' }) {
  const [rule, setRule] = useState(initialRule);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = ruleId
        ? await axios.put(`http://127.0.0.1:5000/rules/${ruleId}`, { rule })
        : await axios.post('http://127.0.0.1:5000/create_rule', { rule });

      onSuccess(response.data.message);
      setRule('');
    } catch (error) {
      console.error('Error creating/updating rule:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="ruleInput" className="form-label">
          Rule Expression
        </label>
        <input
          type="text"
          className="form-control"
          id="ruleInput"
          value={rule}
          onChange={(e) => setRule(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">
        {ruleId ? 'Update Rule' : 'Create Rule'}
      </button>
    </form>
  );
}

export default RuleForm;
