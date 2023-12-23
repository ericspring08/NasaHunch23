import React, { useState } from 'react';
import Link from 'next/link';

const HeartDiseaseForm = () => {
  const respLink = 'https://nasahunch.vercel.app/morecardio';
  const [formData, setFormData] = useState({
    age: '',
    sex: '',
    chestPain: '',
    restingBloodPressure: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    // Add your submission logic here
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-lg mx-auto mt-8">
      <div className="mb-4">
        <label htmlFor="age" className="block text-gray-700 font-semibold mb-2">
          Age
        </label>
        <input
          type="number"
          id="age"
          name="age"
          value={formData.age}
          onChange={handleChange}
          placeholder="Enter age"
          className="w-full border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:border-blue-500"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="sex" className="block text-gray-700 font-semibold mb-2">
          Sex
        </label>
        <select
          id="sex"
          name="sex"
          value={formData.sex}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:border-blue-500"
        >
          <option value="">Select sex</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      <div className="mb-4">
        <label htmlFor="chestPain" className="block text-gray-700 font-semibold mb-2">
          Chest Pain
        </label>
        <input
          type="number"
          id="chestPain"
          name="chestPain"
          value={formData.chestPain}
          onChange={handleChange}
          placeholder="Enter chest pain level (0-3)"
          className="w-full border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:border-blue-500"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="restingBloodPressure" className="block text-gray-700 font-semibold mb-2">
          Resting Blood Pressure
        </label>
        <input
          type="number"
          id="restingBloodPressure"
          name="restingBloodPressure"
          value={formData.restingBloodPressure}
          onChange={handleChange}
          placeholder="Enter resting blood pressure"
          className="w-full border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:border-blue-500"
        />
      </div>
      <Link href={respLink}>
        <div className="mt-6">
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
          >
            Next
          </button>
        </div>
      </Link>
    </form>
  );
};

export default HeartDiseaseForm;
