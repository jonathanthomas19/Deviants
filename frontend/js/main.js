import React, { useState } from 'react';

const ToolBar = () => {
  const [selectedTool, setSelectedTool] = useState('cube');

  const handleToolChange = (tool) => {
    setSelectedTool(tool);
    // Communicate the selected tool to the A-Frame scene
  };

  return (
    <div className="toolbar">
      <button onClick={() => handleToolChange('cube')}>Cube</button>
      <button onClick={() => handleToolChange('sphere')}>Sphere</button>
      <button onClick={() => handleToolChange('terrain')}>Terrain</button>
    </div>
  );
};