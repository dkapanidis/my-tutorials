import React from 'react';
import {
  BrowserRouter as Router, Route, Routes
} from "react-router-dom";
import './App.css';
import About from './pages/About';
import Home from './pages/Home';
import KeyboardShortcuts from './shortcuts/KeyboardShortcuts';
import SideMenu from './ui/layouts/SideMenu';

function App() {
  return (
    <Router>
      <SideMenu>
        <KeyboardShortcuts />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </SideMenu>
    </Router>
  )
}

export default App;
