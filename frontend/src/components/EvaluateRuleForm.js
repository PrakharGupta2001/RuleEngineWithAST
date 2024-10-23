// frontend/src/components/EvaluateRuleForm.js

import React, { useState } from 'react';
import axios from 'axios';

function EvaluateRuleForm() {
  const [ruleId, setRuleId] = useState('');
  const [data, setData] = useState({});
  const [result, setResult] = useState(null);

  const handleEvaluate = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/evaluate_rule', {
        rule_id: parseInt(ruleId, 10),
        data,
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error evaluating rule:', error);
      setResult(null);
    }
  };

  return (
    <form onSubmit={handleEvaluate}>
      <div className="mb-3">
        <label htmlFor="ruleIdInput" className="form-label">
          Rule ID
        </label>
        <input
          type="number"
          className="form-control"
          id="ruleIdInput"
          value={ruleId}
          onChange={(e) => setRuleId(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="dataInput" className="form-label">
          Data (JSON)
        </label>
        <textarea
          className="form-control"
          id="dataInput"
          rows="3"
          onChange={(e) => setData(JSON.parse(e.target.value))}
        ></textarea>
      </div>
      <button type="submit" className="btn btn-primary">Evaluate Rule</button>
      {result !== null && (
        <div className="alert alert-info mt-3">
          Evaluation Result: {result.toString()}
        </div>
      )}
    </form>
  );
}

export default EvaluateRuleForm;
