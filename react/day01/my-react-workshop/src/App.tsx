import {
  BrowserRouter as Router, Route, Routes
} from "react-router-dom";
import './App.css';
import About from './pages/About';
import Home from './pages/Home';
import KeyboardShortcuts from "./shortcuts/KeyboardShortcuts";

function App() {
  return (
    <Router>
      <KeyboardShortcuts />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  )
}

export default App;
